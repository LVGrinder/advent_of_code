import os
import re
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2023", "day1", "example.txt"), "r+") as f:
    lines = f.readlines()

calibration_sum: list[int] = []
for line in lines:
    print(line)

    if line == "":
        break
    two_digit: list[str] = re.findall(r"(\d).*(\d)", line)

    if not two_digit:
        two_digit: list[str] = re.findall(r"(\d)", line)
        string = str("".join(two_digit[0])) + str("".join(two_digit[0]))
        number: int = int(string)
        print(number)
        calibration_sum.append(number)
        break

    # value: list[str] = two_digit
    # calibration_value: int = int(value)
    if two_digit:
        number = int("".join(two_digit[0]))
        print(number)
        calibration_sum.append(number)
print(sum(calibration_sum))
