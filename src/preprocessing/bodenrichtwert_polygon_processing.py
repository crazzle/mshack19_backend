from shapely.geometry import Point
from shapely import wkt
import pandas as pd
import click
import geopandas as gpd

def polygon_check(pointlong, pointlat):
    point = Point(pointlong, pointlat)

    poly_data = pd.read_csv("../../datasets/bodenrichtwerte_preprocessed.csv")
    poly_data.drop("Unnamed: 0", axis=1, inplace=True)

    poly_data["WKT"] = poly_data["WKT"].apply(wkt.loads)
    geo_poly_data = gpd.GeoDataFrame(poly_data, geometry="WKT")

    match = geo_poly_data[geo_poly_data.contains(point)]
    if len(match) != 1:
        raise ValueError("no single match")

    return match["BRW"], match["ORTST"]

if __name__  == "__main__":
    polygon_check(7.62, 51.9)