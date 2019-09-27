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

features = [
    {
        ID: "near_university",
        LABEL: "Nähe zur Uni",
        PRIORITIES: std_prios,
        DESCRIPTION: 'Lorem Ipsum'
    },
    {
        ID: "shops",
        LABEL: "Einkaufmöglichkeiten",
        PRIORITIES: std_prios,
        DESCRIPTION: 'Lorem Ipsum'
    },
    {
        ID: "nightlife",
        LABEL: "Nightlife",
        PRIORITIES: nightlife_prios,
        DESCRIPTION: 'Lorem Ipsum'
    },
    {
        ID: "public_transport",
        LABEL: "ÖPNV",
        PRIORITIES: std_prios,
        DESCRIPTION: 'Lorem Ipsum'
    },
    {
        ID: "avg_cost",
        LABEL: "Mietspiegel",
        PRIORITIES: std_prios,
        DESCRIPTION: 'Lorem Ipsum'
    }
]
