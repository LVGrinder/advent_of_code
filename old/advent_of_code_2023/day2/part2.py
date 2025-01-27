import os
import re
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2023", "day2", "input.txt"), "r+") as f:
    lines = f.readlines()

power: int = 0
sum_power: int = 0

red_list: list[int] = []
green_list: list[int] = []
blue_list: list[int] = []

red_power: int
green_power: int
blue_power: int

for game in lines:
    # print(line)

    color: list[str] = re.findall(r"(\d+\s[a-z]+)", game)
    print(color)

    red_list = []
    green_list = []
    blue_list = []

    for cube in color:
        print(cube)
        # We convert to list to access the number_of_cubes
        cube = cube.split()
        number_of_cubes = cube[0]
        number_of_cubes = int(number_of_cubes)
        print(number_of_cubes)
        if cube[1] == "red":
            print("red")
            red_list.append(number_of_cubes)
        if cube[1] == "green":
            print("green")
            green_list.append(number_of_cubes)
        if cube[1] == "blue":
            print("blue")
            blue_list.append(number_of_cubes)
    red_power = max(red_list)
    green_power = max(green_list)
    blue_power = max(blue_list)
    print("red power: ", red_power)
    print("red_list: ", red_list)

    power = red_power * green_power * blue_power
    sum_power += power


print(f"Sum of ID is: {sum_power}")
