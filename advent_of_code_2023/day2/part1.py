import os
import re
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2023", "day2", "input.txt"), "r+") as f:
    lines = f.readlines()

id: int = 0

for game in lines:
    # print(line)

    id += 1
    color: list[str] = re.findall(r"(\d\s[a-z]+)", game)
    print(color)

    for cube in color:
        print(cube)
        number_of_cubes = cube.split()
        print(number_of_cubes)
