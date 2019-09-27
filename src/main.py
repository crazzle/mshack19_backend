from fastapi import FastAPI
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


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/features")
def read_item(response_model=Feature):
    # TODO use classes from above
    return features
