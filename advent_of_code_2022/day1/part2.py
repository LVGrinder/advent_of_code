import os
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2022", "day1", "input.txt"), "r+") as f:
    lines = f.read()

# print(lines)

elves: list[str] = []
elves = lines.split("\n\n")
# for i in test:
# i.replace("\n", "+")
# print(i)
# print(elves)
# elf: str
items: list[list[int]] = [[]]
for i in range(len(elves)):
    items.append([])
elf_totalCalories: list[int] = []
timesRun: int = 0
for elf in elves:
    # We keep track to know which elf to select
    elf.replace("", "")
    elf = elves[timesRun].split("\n")
    print(elf)
    print(timesRun)
    # We add items for each elf
    # items = items_list
    for item in elf:

        if item == "":
            continue
        print(item)
        items[timesRun].append(int(item))
        print(items[timesRun])
        print(timesRun)

    elf_totalCalories.append(sum(items[timesRun]))
    print(sum(items[timesRun]))
    print(f"Added {items} in {elf_totalCalories}")
    timesRun += 1


# print(elf_totalCalories)
elf_totalCalories.sort(reverse=True)
print("Value is: ")
print(sum(elf_totalCalories[0:3]))
# print(est)
# coneee: list[]
# for i in range(len(est)):
#     est[i] = int(est[i])
# est: list[int]
# print(sum(est))
