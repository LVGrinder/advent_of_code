import os
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2022", "day6", "input.txt"), "r+") as f:
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

    amount_not_matched: int = 0
    for letter in bufferlist:
        print(f"constantlist inside of loop: {constantlist}")
        matchinglist = list(constantlist)
        matchinglist.pop(times_checked)
        # print(f"matchlist: {matchinglist}")
        print(f"current letter being checked: {letter}")
        print(f"current existing list: {matchinglist}")
        for matchable_letter in matchinglist:
            if letter != matchable_letter:
                print("was not matched with any")
                amount_not_matched = +1
        times_checked = +1
    if times_checked == 3:
        times_checked: int = 0
    if amount_not_matched == 12:
        print(f"we got it bois {i}")
        break

    #     if letter == letter and letter:
    #         print(f"found: {packet}")
    #         break
