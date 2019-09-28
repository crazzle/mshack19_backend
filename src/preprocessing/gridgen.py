import math
import csv
import numpy as np
import os.path


def km_to_long(lat, km):
    return km / (111.320*math.cos(math.radians(lat)))


def km_to_lat(km):
    return km/110.574


def long_to_km(lat, long):
    return 111.320*math.cos(math.radians(lat)) * long


def lat_to_km(lat):
    return lat*110.574


def gengrid(x, y, stepsize):
    center_deg = (51.960, 7.626)
    # lat: 1 deg = 110.574 km
    # long: 1 deg =  111.320*cos(lat) km

    grid_size = (x, y)
    # 30 km north south
    # 30 km east west
    list = []

    center_km = (lat_to_km(center_deg[0]), long_to_km(center_deg[0], center_deg[1]))
    bottom_left = (center_km[0] - grid_size[0] / 2, center_km[1] - grid_size[1] / 2)
    top_right = (center_km[0] + grid_size[0] / 2, center_km[1] + grid_size[1] / 2)

    for latkm in np.arange(int(bottom_left[0]), int(top_right[0]), stepsize):
        for longkm in np.arange(int(bottom_left[1]), int(top_right[1]), stepsize):
            currentlatdg = km_to_lat(latkm)
            currentlongdg = km_to_long(currentlatdg, longkm)

            list.append([currentlongdg, currentlatdg])
    path = os.path.join("..", "..", "datasets/longlatgrid2.csv")
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(list)


if __name__ == "__main__":
    gengrid(12, 12, 0.1)