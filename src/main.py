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
def features(response_model=List[Feature]):
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
def preselcted_features(role: str):
    if role in roles:
        # TODO use classes from above
        print(role)
        return preselected_roles
    else:
        raise HTTPException(status_code=404, detail=f"Role not in '{', '.join(roles)}'")


@app.post("/search")
def read_item(query: str):
    # TODO use classes from above
    # selectedlist(feature: value) -> heatmap
    return {}
