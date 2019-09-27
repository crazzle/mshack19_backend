import pandas as pd
from geopy.distance import distance
longlatfile = "longlatgrid.csv"

BUS = "bus_stop_preprocessed.csv"
NIGHTLIFE = "nightlife_preprocessed.csv"
SUPERMARKT = "supermarkt_preprocessed.csv"
UNIVERSITY = "university_preprocessed.csv"

preprocessedfiles = [BUS,
                    NIGHTLIFE,
                    SUPERMARKT,
                    UNIVERSITY]

feature_range = {BUS: 0.5,
                  NIGHTLIFE: 1,
                  SUPERMARKT: 2,
                  UNIVERSITY: 3}


def attractiviy_matrix():
    position_data = pd.read_csv("../datasets/" + longlatfile)
    position_data = position_data[:1000]

    for preprocfile in preprocessedfiles:
        activity_data = pd.read_csv("../datasets/" + preprocfile)
        # Construct DataFrame
        data = pd.DataFrame(None, index=range(len(position_data)), columns=["Value", "Long", "Lat"])
        for position in position_data.itertuples():
            distances = []

            for activity_position in activity_data.itertuples(index=False):
                distances.append(distance((position[1], position[2]), (activity_position[1], activity_position[2])).km)
            value = len(list(filter(lambda x: x < feature_range[preprocfile], distances)))
            # Assign Value
            data.iloc[position[0]] = [
                value,
                position[1],
                position[2],
            ]
        with open("../datasets/" + "final_" + preprocfile, "w") as f:
            data.to_csv(f, index=False)


if __name__ == "__main__":
    attractiviy_matrix()


