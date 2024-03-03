import os
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2022", "day6", "input.txt"), "r+") as f:
    lines = f.readlines()

databuffer: str = lines[0]
print(databuffer)

startofstring: int = 0
endofstring: int = 4

matchlist: list = []
secondarylist: list = []

for i in range(len(databuffer)):
    print(i)

    packet = databuffer[i : i + 4]

    print(packet)

    matchlist = []
    for letter in packet:
        print(letter)
        matchlist.append(letter)

    print(matchlist)
    times_checked: int = 0
    for letter in matchlist:
        secondarylist = matchlist
        secondarylist.pop(times_checked)
        print(f"current letter being checked: {letter}")
        print(f"current existing list: {secondarylist}")
        times_checked = +1

    #     if letter == letter and letter:
    #         print(f"found: {packet}")
    #         break
