import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry import Point
from shapely import wkt

from math import radians, cos, sin, asin, sqrt

poly_data = pd.read_csv("../datasets/bodenrichtwerte_preprocessed.csv")
poly_data.drop("Unnamed: 0", axis=1, inplace=True)

poly_data["WKT"] = poly_data["WKT"].apply(wkt.loads)
geo_poly_data = GeoDataFrame(poly_data, geometry="WKT")


def polygon_check(pointlong, pointlat):
    point = Point(pointlong, pointlat)

    match = geo_poly_data[geo_poly_data.contains(point)]
    # should contain only one element
    if len(match) == 0:
        return 0, "Unbekannt"

    match = match.iloc[0]
    return match["BRW"], match["ORTST"]


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



longlatfile = "longlatgrid2.csv"

BUS = "bus_stop_preprocessed.csv"
NIGHTLIFE = "nightlife_preprocessed.csv"
SUPERMARKT = "supermarkt_preprocessed.csv"
UNIVERSITY = "university_preprocessed.csv"

preprocessedfiles = [BUS,
                    NIGHTLIFE,
                    SUPERMARKT,
                    UNIVERSITY]

feature_range = {BUS: 0.2,
                  NIGHTLIFE: 0.5,
                  SUPERMARKT: 1,
                  UNIVERSITY: 1}

db_name_mapping = {
    BUS : "public_transport",
    NIGHTLIFE : "nightlife",
    SUPERMARKT : "shops",
    UNIVERSITY : "university",
}
crs = {'init': 'epsg:5243'}


def create_act_gdf(preprocfile):
    data = pd.read_csv("../datasets/" + preprocfile)
    geom = [Point(xy) for xy in zip(data.Long, data.Lat)]
    return GeoDataFrame(data.Name, crs=crs, geometry=geom)


def attractivity_matrix():
    pois = pd.read_csv("../datasets/" + longlatfile)
    pois_geom = [Point(xy) for xy in zip(pois.iloc[:,0], pois.iloc[:,1])]
    pois_gdf = GeoDataFrame(None, crs=crs, geometry=pois_geom)

    bus_gdf = create_act_gdf(BUS)
    nightlife_gdf = create_act_gdf(NIGHTLIFE)
    supermarkt_gdf = create_act_gdf(SUPERMARKT)
    university_gdf = create_act_gdf(UNIVERSITY)

    data = pd.DataFrame(None, index=range(len(pois)), columns=[
        "Lat", "Long", "public_transport", "nightlife", "shops", "near_university"
    ])
    #data = pd.DataFrame(None, index=range(len(pois)), columns=["avg_cost", "district"])
    for (i, poi) in pois_gdf.itertuples():
        #bwr, ortst = polygon_check(poi.x, poi.y)

        data.iloc[i] = [
            poi.y,
            poi.x,
            len(bus_gdf[bus_gdf["geometry"].apply(lambda x: haversine(x, poi)) < feature_range[BUS]]),
            len(nightlife_gdf[nightlife_gdf["geometry"].apply(lambda x: haversine(x, poi)) < feature_range[NIGHTLIFE]]),
            len(supermarkt_gdf[supermarkt_gdf["geometry"].apply(lambda x: haversine(x, poi)) < feature_range[SUPERMARKT]]),
            len(university_gdf[university_gdf["geometry"].apply(lambda x: haversine(x, poi)) < feature_range[UNIVERSITY]]),
        ]
        print(i)

    with open("../datasets/" + "final.csv", "w") as f:
        data.to_csv(f, index=False)


if __name__ == "__main__":
    attractivity_matrix()


