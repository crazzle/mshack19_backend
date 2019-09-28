import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry import Point
import csv
import click

from math import radians, cos, sin, asin, sqrt

@click.command()
@click.argument('csvfile')
@click.argument('outfile')
def main(csvfile, outfile):
    raw = pd.read_csv(csvfile, encoding = 'utf-8', decimal=",")
    data = raw[["WKT", "BRW", "ORTST"]]
    data.fillna(0, inplace=True)
    data["BRW"] = pd.to_numeric(data["BRW"])
    data["BRW"] = (data["BRW"]-data["BRW"].min())/(data["BRW"].max()-data["BRW"].min())
    print(data.max())
    data.to_csv(outfile)

if __name__ == "__main__":
    main()