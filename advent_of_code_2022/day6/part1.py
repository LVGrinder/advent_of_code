import os
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2022", "day6", "input.txt"), "r+") as f:
    lines = f.readlines()

databuffer: str = lines[0]
print(databuffer)

startofstring: int = 0
endofstring: int = 4

for i in range(len(databuffer)):
    print(i)
    startofstring = +1
    endofstring = +1

    packet = databuffer[i : i + 4]

    print(packet)
