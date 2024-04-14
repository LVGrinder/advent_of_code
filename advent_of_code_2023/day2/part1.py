import os
import re
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2023", "day2", "input.txt"), "r+") as f:
    lines = f.readlines()

id: int = 0
invalid_amount: int = 0
sum_id: int = 0

for game in lines:
    # print(line)

    id += 1
    sum_id += id
    color: list[str] = re.findall(r"(\d+\s[a-z]+)", game)
    print(color)

    for cube in color:
        print(cube)
        # We convert to list to access the number_of_cubes
        cube = cube.split()
        number_of_cubes = cube[0]
        number_of_cubes = int(number_of_cubes)
        print(number_of_cubes)
        if cube[1] == "red":
            print("red")
            if number_of_cubes > 12:
                print(f"invalid: {number_of_cubes}")
                invalid_amount += 1
        if cube[1] == "green":
            print("green")
            if number_of_cubes > 13:
                print(f"invalid: {number_of_cubes}")
                invalid_amount += 1
        if cube[1] == "blue":
            print("blue")
            if number_of_cubes > 14:
                print(f"invalid: {number_of_cubes}")
                invalid_amount += 1
        if invalid_amount >= 1:
            sum_id -= id
            invalid_amount = 0
            break


print(invalid_amount)
print(f"Sum of ID is: {sum_id}")
