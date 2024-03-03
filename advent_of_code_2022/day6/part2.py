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

amount: int = 14
amount_list: int = amount - 1
databuffer_character_to_match: int = amount * amount_list

for i in range(len(databuffer)):
    print(i)

    packet = databuffer[i : i + amount]

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
        # making sure its same list
        matchinglist = list(constantlist)
        print(f"constantlist inside of loop: {constantlist}")
        print(f"letter being popped: {matchinglist[times_checked]}")
        # popping up character to be matched
        matchinglist.pop(times_checked)
        # printing
        print(f"current letter being checked: {letter}")
        print(f"current existing list: {matchinglist}")
        # matching letters to see if they don't match
        for matchable_letter in matchinglist:
            if letter != matchable_letter:
                # printing info
                print(f"{letter} was not matched with {matchable_letter}")
                # variable increased if its not matched
                amount_not_matched += 1
                # if amount is equal stop script
        times_checked += 1
    print(amount_not_matched)
    if amount_not_matched >= databuffer_character_to_match:
        value = i + amount
        print(f"marked detected at character {value}")
        break

    #     if letter == letter and letter:
    #         print(f"found: {packet}")
    #         break
