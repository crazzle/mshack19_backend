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
        NIGHTLIFE: 5,
        AVG_COST: 5,
        NEAR_UNIVERSITY: 4,
        SHOPS: 4,
        PUBLIC_TRANSPORT: 4,

    },
    FAMILY: {
        SHOPS: 4,
        PUBLIC_TRANSPORT: 4,
        AVG_COST: 4,
        NIGHTLIFE: 2,
        NEAR_UNIVERSITY: 1,
    },
    BUSINESS: {
        AVG_COST: 3,
        PUBLIC_TRANSPORT: 3,
        SHOPS: 2,
        NEAR_UNIVERSITY: 1,
        NIGHTLIFE: 1,

    }
}
