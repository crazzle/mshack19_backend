import pathlib
from typing import List

import numpy as np
from fastapi import FastAPI, HTTPException, Body
from starlette.middleware.cors import CORSMiddleware

from models.database import DatabaseConnection
from models.features import features, Feature
from models.roles import preselected_roles, role_model

app = FastAPI()


origins = [
    "http:localhost",
    "http:localhost:8080",
    "http:localhost:8000",
    "http:127.0.0.1",
    "http:127.0.0.1:8080",
    "http:127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TODO sqlite database with anbindung an fastapi


@app.get("/features/", response_model=List[Feature])
def features_route():
    """
    List of all features available with possible settings.
    :return: List[Feature]
    """
    return features


@app.get("/preselected_features/{role}", response_model=role_model, responses={404: {}})  # "model": role
def preselected_features(role: str):
    """
    The preset of features for a specific role.
    :param role: The role
    :return: [feature, prio]
    """
    if role in preselected_roles.keys():
        # TODO use formatter for specific order of features
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

    db_file = pathlib.Path.cwd().parent.joinpath('database', 'features.db')
    db = DatabaseConnection(db_file)
    heatmap = []
    query = {
        "public_transport": 3,
        "nightlife": 4,
        "shops": 3,
        "near_university": 4,
        "avg_cost": 5
    }

    with db:
        db.cursor.execute("""
            SELECT long,
                    lat,
                    public_transport,
                    nightlife,
                    shops,
                    near_university,
                    avg_cost
            FROM main.standard_heat
        """)
        std_heat = db.cursor.fetchall()

    # TODO map via sqlalchemy
    table_map = {
        "public_transport": 2,
        "nightlife": 3,
        "shops": 4,
        "near_university": 5,
        "avg_cost": 6
    }

    for table_data in std_heat:
        weight = 0
        for feature_name, feature_weight in query.items():
            # TODO map table index to query param -> pydantic
            """
            Magic happens here
            """
            weight += feature_weight * table_data[table_map[feature_name]]
        heatmap.append([table_data[0], table_data[1], weight])

    if False:
        long_lat_file = pathlib.Path.cwd().parent.joinpath('datasets', 'longlatgrid.csv')
        raw = np.genfromtxt(long_lat_file, delimiter=',')
        weighted = np.zeros((3600, 3))
        weighted[:, :-1] = raw
        for w in range(3600):
            weighted[w, 2] = w / 900

        return weighted.tolist()

    return heatmap
