from typing import Dict

from pydantic import BaseModel

from constants import *

role_model = Dict[str, int]


# TODO: for usage of the class add a json formatter which pre-sorts them by importance for the frontend
class Role(BaseModel):
    nightlife: int
    avg_cost: int
    near_university: int
    shops: int
    public_transport: int


if False:
    preselected_roles = {
        STUDENT: Role(nightlife=5, avg_cost=5, near_university=4, shops=4, public_transport=4),
        FAMILY: Role(nightlife=2, avg_cost=4, near_university=1, shops=4, public_transport=4),
        BUSINESS: Role(nightlife=1, avg_cost=3, near_university=1, shops=2, public_transport=3),
    }


preselected_roles = {
    STUDENT: {
        "nightlife": 5,
        "avg_cost": 5,
        "near_university": 4,
        "shops": 4,
        "public_transport": 4,

    },
    FAMILY: {
        "shops": 4,
        "public_transport": 4,
        "avg_cost": 4,
        "nightlife": 2,
        "near_university": 1,
    },
    BUSINESS: {
        "avg_cost": 3,
        "public_transport": 3,
        "shops": 2,
        "near_university": 1,
        "nightlife": 1,

    }
}
