import pathlib
from typing import List

import numpy as np
from fastapi import FastAPI, HTTPException

from features import features, Feature
from roles import preselected_roles

app = FastAPI()
# TODO sqlite database with anbindung an fastapi


@app.get("/features/", response_model=List[Feature])
def features_route():
    # TODO use classes from above
    return features


@app.get("/preselected_features/{role}", responses={404: {}})  # responses={404: {"model": Message}}
def preselected_features(role: str):
    if role in preselected_roles.keys():
        # TODO use classes from above
        return preselected_roles[role]
    else:
        raise HTTPException(status_code=404, detail=f"Role not in '{', '.join(preselected_roles.keys())}'")


@app.get("/search")
def search(query=[]):
    """
    Search based on preferences (e.g. features) returning the heatmap.

    :param query: [{feature: prio}], empty means, all to default.
    :return: heatmap
    """
    """
    Magic happens here
    """
    long_lat_file = pathlib.Path.cwd().parent.joinpath('datasets', 'longlatgrid.csv')
    raw = np.genfromtxt(long_lat_file, delimiter=',')
    weighted = np.zeros((900, 3))
    weighted[:, :-1] = raw
    for w in range(900):
        weighted[w, 2] = w / 900

    return weighted.tolist()
