import os
from json import loads


def get_json(filename: str) -> list:
    filepath = f"data/{filename}"

    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            return loads(file.read())

    return []
