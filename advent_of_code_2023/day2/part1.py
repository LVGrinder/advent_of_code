import os
import re
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2023", "day2", "input.txt"), "r+") as f:
    lines = f.readlines()


for line in lines:
    print(line)
