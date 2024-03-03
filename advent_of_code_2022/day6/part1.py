import os
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2022", "day6", "example.txt"), "r+") as f:
    lines = f.readlines()

databuffer: str = lines[0]
print(databuffer)

startofstring: int = 0
endofstring: int = 4

bufferlist: list = []
matchinglist: list = []
constantlist: list = []

times_checked: int = 0

for i in range(len(databuffer)):
    print(i)

    packet = databuffer[i : i + 4]

    print(packet)

    bufferlist = []
    constantlist = []
    for letter in packet:
        print(letter)
        bufferlist.append(letter)
        constantlist.append(letter)

    # print(f"matchlist: {matchlist}")
    # print(f"secondarylist out of loop: {matchinglist}")
    print(f"constantlist out of loop: {constantlist}")

    amount_not_matched = 0
    times_checked = 0
    for letter in constantlist:
        print(f"constantlist inside of loop: {constantlist}")
        matchinglist = list(constantlist)
        print(f"letter being popped: {matchinglist[times_checked]}")
        matchinglist.pop(times_checked)
        print(f"current letter being checked: {letter}")
        print(f"current existing list: {matchinglist}")
        for matchable_letter in matchinglist:
            if letter != matchable_letter:
                print(f"{letter} was not matched with {matchable_letter}")
                amount_not_matched += 1
        times_checked += 1
    if amount_not_matched == 12:
        value = i + 4
        print(f"marked detected at character {value}")
        break

    #     if letter == letter and letter:
    #         print(f"found: {packet}")
    #         break
