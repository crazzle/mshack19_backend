from constants import *

# pre-sort them by importance for the frontend

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
