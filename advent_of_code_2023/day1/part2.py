import os
import re
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2023", "day1", "input.txt"), "r+") as f:
    lines = f.readlines()


def convert_to_number(number):
    convert_to_number_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        # Add other mappings as necessary
    }
    word = number.group(0)
    return convert_to_number_dict.get(word, word)


calibration_sum: list[int] = []
for line in lines:
    print(line)

    if line == "":
        break
    two_digit: list[str] = re.findall(
        r"(one|two|three|four|five|six|seven|eight|nine|\d).*(one|two|three|four|five|six|seven|eight|nine|\d)",
        line,
    )

    if not two_digit:
        two_digit: list[str] = re.findall(
            r"(one|two|three|four|five|six|seven|eight|nine|\d)", line
        )
        string = str("".join(two_digit[0])) + str("".join(two_digit[0]))
        numbered_string = re.sub(
            r"one|two|three|four|five|six|seven|eight|nine", convert_to_number, string
        )
        number: int = int(numbered_string)
        print(number)
        calibration_sum.append(number)
        continue

    # value: list[str] = two_digit
    # calibration_value: int = int(value)
    if two_digit:
        string = str("".join(two_digit[0]))
        numbered_string = re.sub(
            r"one|two|three|four|five|six|seven|eight|nine", convert_to_number, string
        )
        number: int = int(numbered_string)
        print(number)
        calibration_sum.append(number)
print(sum(calibration_sum))
