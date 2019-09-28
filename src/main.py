import json
import pathlib
from typing import List

from fastapi import FastAPI, HTTPException, Body
from starlette.middleware.cors import CORSMiddleware

from models.database import DatabaseConnection
from models.features import features, Feature, Features
from models.roles import preselected_roles, role_model
from constants import *

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:4200",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
def search(
        query
        # query: Features = Body(
        #     default={},
        #     example={
        #         "public_transport": 3,
        #         "nightlife": 4,
        #         "shops": 3,
        #         "near_university": 4,
        #         "avg_cost": 5
        #     }
        # )
):
    """
    Search based on preferences (e.g. features) returning the heatmap.

    :param query: {feature: prio}, empty means, all to default.
    :return: heatmap
    """

    db_file = pathlib.Path.cwd().parent.joinpath('database', 'features.db')
    db = DatabaseConnection(db_file)
    heatmap = []

    with db:
        db.cursor.execute("""
            SELECT long,
                    lat,
                    public_transport,
                    nightlife,
                    shops,
                    near_university,
                    avg_cost,
                    district
            FROM main.standard_heat
        """)
        std_heat = db.cursor.fetchall()

    # TODO sqlite database with anbindung an fastapi
    table_map = {
        PUBLIC_TRANSPORT: 2,
        NIGHTLIFE: 3,
        SHOPS: 4,
        NEAR_UNIVERSITY: 5,
        AVG_COST: 6,
        DISTRICT: 7
    }

    filter_norm = [PUBLIC_TRANSPORT, NIGHTLIFE, SHOPS, NEAR_UNIVERSITY, AVG_COST]

    query: dict = json.loads(query)
    for table_data in std_heat:
        weight = 0
        for feature_name, feature_weight in query.items():
            if feature_name == NIGHTLIFE:
                feature_weight = feature_weight / 3
            else:
                feature_weight = feature_weight / 5
            """
            Magic happens here
            """
            if feature_name in table_map.keys():
                table_weight = table_data[table_map[feature_name]]
                if type(table_weight) == float or type(table_weight) == int:
                    if feature_name == AVG_COST:
                        #weight += 1 / (feature_weight * table_data[table_map[feature_name]])
                        avg_norm = feature_weight * table_data[table_map[feature_name]]
                        if weight > avg_norm:
                            weight -= avg_norm
                    elif feature_name == NEAR_UNIVERSITY:
                        weight += feature_weight * table_data[table_map[feature_name]] * 0.7
                    else:
                        weight += feature_weight * table_data[table_map[feature_name]]
        weight = weight / len(filter_norm)
        heatmap.append([table_data[0], table_data[1], weight, table_data[table_map[DISTRICT]]])

    return heatmap
