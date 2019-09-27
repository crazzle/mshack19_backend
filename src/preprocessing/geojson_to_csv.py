import json

import click
import pandas as pd

@click.command()
@click.argument('jsonfile')
@click.argument('outfile')
def main(jsonfile, outfile):
    with open(jsonfile, "r") as f:
        features = json.load(f)["features"]
    data = pd.DataFrame(None, index=range(len(features)), columns=["Name", "Long", "Lat"])
    for i, f in enumerate(features):
        data.iloc[i] = [
            f["properties"].get("name", "Unbenannt"),
            f["geometry"]["coordinates"][0],
            f["geometry"]["coordinates"][1],
        ]
    with open(outfile, "w") as f:
        data.to_csv(f, index=False)

if __name__ == "__main__":
    main()
