# TODO решите задачу
import json


def task() -> float:
    file_path = "input.json"
    with open(file_path, "r") as file:
        data = json.load(file)

    result = 0.0
    for entry in data:
        result += entry["score"] * entry["weight"]

    return round(result, 3)


print(task())
