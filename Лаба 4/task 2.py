import json


def task() -> float:

    data = [
        {"score": 0.0009456152645028281, "weight": 1},
        {"score": 0.003, "weight": 2},
        {"score": 0.005, "weight": 3},
        {"score": 2.274, "weight": 1}
    ]

    total_sum = 0.0
    for entry in data:
        total_sum += entry["score"] * entry["weight"]

    return round(total_sum, 3)


print(task())