import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry import Point

from math import radians, cos, sin, asin, sqrt


def haversine(p1, p2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    lon1, lat1 = p1.x, p1.y
    lon2, lat2 = p2.x, p2.y
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r



longlatfile = "longlatgrid.csv"

BUS = "bus_stop_preprocessed.csv"
NIGHTLIFE = "nightlife_preprocessed.csv"
SUPERMARKT = "supermarkt_preprocessed.csv"
UNIVERSITY = "university_preprocessed.csv"

preprocessedfiles = [BUS,
                    NIGHTLIFE,
                    SUPERMARKT,
                    UNIVERSITY]

feature_range = {BUS: 0.5,
                  NIGHTLIFE: 1,
                  SUPERMARKT: 2,
                  UNIVERSITY: 3}
crs = {'init': 'epsg:5243'}


def attractivity_matrix():
    pois = pd.read_csv("../datasets/" + longlatfile)
    pois_geom = [Point(xy) for xy in zip(pois.iloc[:,0], pois.iloc[:,1])]
    pois_gdf = GeoDataFrame(None, crs=crs, geometry=pois_geom)

    for preprocfile in preprocessedfiles:
        activity_data = pd.read_csv("../datasets/" + preprocfile)
        act_geom = [Point(xy) for xy in zip(activity_data.Long, activity_data.Lat)]
        act_gdf = GeoDataFrame(activity_data.Name, crs=crs, geometry=act_geom)

        data = pd.DataFrame(None, index=range(len(pois)), columns=["Value", "Lat", "Long"])
        for (i, poi) in pois_gdf.itertuples():
            data.iloc[i] = [
                len(act_gdf[act_gdf["geometry"].apply(lambda x: haversine(x, poi)) < feature_range[preprocfile]]),
                poi.x,
                poi.y,
            ]
            print(data.iloc[i])

        with open("../datasets/" + "final_" + preprocfile, "w") as f:
            data.to_csv(f, index=False)


if __name__ == "__main__":
    attractivity_matrix()


