from constants import *

std_prios = [
    {
        VALUE: 1,
        LABEL: "sehr niedrig"
    },
    {
        VALUE: 2,
        LABEL: "niedrig"
    },
    {
        VALUE: 3,
        LABEL: "mittel"
    },
    {
        VALUE: 4,
        LABEL: "hoch"
    },
    {
        VALUE: 5,
        LABEL: "sehr hoch"
    }
]
nightlife_prios = [
    {
        VALUE: 1,
        LABEL: "kein"
    },
    {
        VALUE: 2,
        LABEL: "wenige Bars"
    },
    {
        VALUE: 3,
        LABEL: "Altstadt"
    }
]

features = {
    "near_university": {
        LABEL: "Nähe zur Uni",
        PRIORITIES: std_prios,
        DESCRIPTION: 'Lorem Ipsum'
    },
    "shops": {
        LABEL: "Einkaufmöglichkeiten",
        PRIORITIES: std_prios,
        DESCRIPTION: 'Lorem Ipsum'
    },
    "nightlife": {
        LABEL: "Nightlife",
        PRIORITIES: nightlife_prios,
        DESCRIPTION: 'Lorem Ipsum'
    },
    "public_transport": {
        LABEL: "ÖPNV",
        PRIORITIES: std_prios,
        DESCRIPTION: 'Lorem Ipsum'
    },
    "avg_cost": {
        LABEL: "Mietspiegel",
        PRIORITIES: std_prios,
        DESCRIPTION: 'Lorem Ipsum'
    }
}
