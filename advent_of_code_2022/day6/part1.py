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
    amount_not_matched: int = 0
    for letter in matchlist:
        secondarylist = matchlist
        secondarylist.pop(times_checked)
        print(f"current letter being checked: {letter}")
        print(f"current existing list: {secondarylist}")
        for matchable_letter in secondarylist:
            if letter != matchable_letter:
                print("was not matched with any")
                amount_not_matched = +1
        times_checked = +1
    if amount_not_matched == 12:
        print(f"we got it bois {i}")
        break

    #     if letter == letter and letter:
    #         print(f"found: {packet}")
    #         break
