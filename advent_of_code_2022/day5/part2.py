import re
import os
from queue import LifoQueue
from pydantic import BaseModel
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2022", "day5", "input.txt"), "r+") as f:
    lines = f.readlines()

crates = lines[:8]
print(crates)

instructions = lines[9:]

# print(instructions)

stackamount: int = 9

stacks: list[list[str]] = [[] for _ in range(stackamount)]

movement = -1

for row in crates:
    # print(row)
    # row = row.split()
    # print(row)
    for i in range(0, len(row), 4):
        # print(row[i + 1])
        if row[i + 1] == " ":
            print("skipping as empty")
        else:
            print(row)
            print("putting to stack" + str(stacks))
            stacks[i // 4].append(row[i + 1])
    # print(cratelist)
print("Here is cratelist:")
print(stacks)


class Instruct(BaseModel):
    amount: int
    crate: int
    move_to: int


def parseRowToInstruct(row: str) -> Instruct | None:
    inputInstruct: list[str] = re.findall(r"\d+", row)
    print("inputInstruct" + str(inputInstruct))
    if not inputInstruct:
        return None

    return Instruct(
        amount=int(inputInstruct[0]),
        crate=-1 + int(inputInstruct[1]),
        move_to=-1 + int(inputInstruct[2]),
    )


queue = LifoQueue()

for row in instructions:
    instruct: Instruct | None = parseRowToInstruct(row)

    if instruct is not None:
        for stack in stacks:
            print(f"Stack: {stack}")
        print("row: " + row)
        print("amount: " + str(instruct.amount))
        print("crate: " + str(instruct.crate))
        print("move_to: " + str(instruct.move_to))
        print("which crate: " + str(stacks[instruct.crate][0]))
        print("crate to move: " + str(stacks[instruct.move_to]))
        for i in range(instruct.amount):
            if stacks[instruct.crate]:
                item_to_move = stacks[instruct.crate].pop(0)
                # cratelist[instruct.move_to].insert(1, item_to_move)
                queue.put(item_to_move)
                print(stacks[instruct.move_to])
            else:
                print(f"Not enough items in crate {instruct.crate} to move.")
                break
        for i in range(instruct.amount):
            stacks[instruct.move_to].insert(0, queue.get())

        print("crates remaining: " + str(stacks[instruct.crate]))
    # print(cratelist)

print(stacks)

output: list[list[str]] = [[] for _ in range(stackamount)]

for i in range(stackamount):
    if stacks[i]:
        item_to_move = stacks[i].pop(0)
        output[i].append(item_to_move)
    else:
        print("Not enough items in crate to move.")

# print(cratelist)
print("Here is the cool list:")
print(output)
