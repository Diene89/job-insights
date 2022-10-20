import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(f"{path}") as file:
        data_file = csv.DictReader(file)
        new_data = []
        for data in data_file:
            new_data.append(data)
        return new_data
