import numpy as np
import pandas as pd
from math import radians, sin, cos, sqrt, atan2


EARTH_RADIUS_KM = 6371


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    İki koordinat arasındaki kuş uçuşu mesafeyi (km) hesaplar.
    """

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        sin(dlat / 2) ** 2
        + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return EARTH_RADIUS_KM * c


def create_distance_matrix(df: pd.DataFrame):
    """
    Teslimat noktalarından mesafe matrisi oluşturur.
    """

    coordinates = df[["latitude", "longitude"]].values

    size = len(coordinates)

    matrix = np.zeros((size, size))

    for i in range(size):
        for j in range(size):

            if i == j:
                continue

            matrix[i][j] = haversine_distance(
                coordinates[i][0],
                coordinates[i][1],
                coordinates[j][0],
                coordinates[j][1],
            )

    return matrix
