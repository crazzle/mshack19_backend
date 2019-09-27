from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from features import features
from roles import preselected_roles

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


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/features")
def features(response_model=List[Feature]):
    # TODO use classes from above
    return features


@app.get("/preselcted_features/{role}")
def preselcted_features(role: str):
    if role in preselected_roles.keys():
        # TODO use classes from above
        print(role)
        return preselected_roles[role]
    else:
        raise HTTPException(status_code=404, detail=f"Role not in '{', '.join(roles)}'")


@app.post("/search")
def read_item(query: str):
    # TODO use classes from above
    # selectedlist(feature: value) -> heatmap
    return {}
