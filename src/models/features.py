from typing import List

from pydantic import BaseModel


class Prio(BaseModel):
    value: int
    label: str


class Feature(BaseModel):
    id: str
    label: str
    priorities: List[Prio]
    description: str


class Features(BaseModel):
    public_transport: int
    nightlife: int
    shops: int
    near_university: int
    avg_cost: int


std_prios = [
    Prio(value=1, label="sehr niedrig"),
    Prio(value=2, label="niedrig"),
    Prio(value=3, label="mittel"),
    Prio(value=4, label="hoch"),
    Prio(value=5, label="sehr hoch"),
]

nightlife_prios = [
    Prio(value=1, label="kein"),
    Prio(value=2, label="wenige Bars"),
    Prio(value=3, label="Altstadt"),
]

features = [
    Feature(id="near_university", label="Nähe zur Uni", priorities=std_prios, description='Lorem Ipsum'),
    Feature(id="shops", label="Einkaufmöglichkeiten", priorities=std_prios, description='Lorem Ipsum'),
    Feature(id="nightlife", label="Nightlife", priorities=nightlife_prios, description='Lorem Ipsum'),
    Feature(id="public_transport", label="ÖPNV", priorities=std_prios, description='Lorem Ipsum'),
    Feature(id="avg_cost", label="Mietspiegel", priorities=std_prios, description='Lorem Ipsum'),
]
