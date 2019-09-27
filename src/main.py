from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from features import features

app = FastAPI()


# TODO sqlite database with anbindung an fastapi


class Prio(BaseModel):
    VALUE: str
    LABEL: str


class Feature(BaseModel):
    ID: str
    LABEL: str
    PRIORITIES: Prio
    DESCRIPTION: str


roles = ["student", "family", "business"]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/features")
def read_item(response_model=List[Feature]):
    # TODO use classes from above
    return features


preselected_roles = {
    "near_university": 3,
    "shops": 3,
    "nightlife": 3,
    "public_transport": 3,
    "avg_cost": 3
}


@app.get("/preselcted_features/{role}")
def read_item(role: str):
    if role in roles:
        # TODO use classes from above
        print(role)
        return preselected_roles
    else:
        raise HTTPException(status_code=404, detail=f"Role not in '{', '.join(roles)}'")


@app.get("/search")
def search(features):
    import numpy as np
    import json

    """
    Magic happens here
    """
    raw = np.genfromtxt('datasets/latlonggrid.csv', delimiter=',')
    weighted = np.zeros((900,3))  
    weighted[:,:-1] = raw
    for w in range(900):
        weighted[w,2] = w/900

    return json.dumps(weighted.tolist())
