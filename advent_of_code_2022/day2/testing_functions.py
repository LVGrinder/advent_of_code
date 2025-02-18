import os
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2022", "day2", "input.txt"), "r+") as f:
    lines = f.read()

line = lines.split("\n")

point = 0


def func(point):
    point += 5
    print(f"point is currently {point}")
    return point


for i in range(5):
    point = func(point)
    print(point)
