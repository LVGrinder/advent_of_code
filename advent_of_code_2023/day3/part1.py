import os
import re
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2023", "day3", "example.txt"), "r+") as f:
    lines = f.readlines()


for row in lines:
    print(row)
