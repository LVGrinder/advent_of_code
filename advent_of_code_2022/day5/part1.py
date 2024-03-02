import re
from pydantic import BaseModel

with open("input.txt", "r+") as f:
    lines = f.readlines()

crates = lines[:8]

instructions = lines[9:]

# print(instructions)

cratelist: list[list[str]] = []
coollist: list[list[str]] = []
crategroup = int(1)

for _ in range(9):
    cratelist.append([])
    coollist.append([])

movement = int(-1)

for row in crates:
    # print(row)
    # row = row.split()
    # print(row)
    for i in range(0, len(row), 4):
        # print(row[i + 1])
        if row[i + 1] == " ":
            break
        else:
            cratelist[i // 4].append(row[i + 1])
    # print(cratelist)
print(cratelist)


class Instruct(BaseModel):
    amount: int
    crate: int
    move_to: int


def parseRowToInstruct(row: str) -> Instruct | None:
    inputInstruct = re.findall(r"\d+", row)
    if not inputInstruct:
        return None

    return Instruct(
        amount=int(inputInstruct[0]),
        crate=int(-1 + int(inputInstruct[1])),
        move_to=int(-1 + int(inputInstruct[2])),
    )


for row in instructions:
    instruct: Instruct | None = parseRowToInstruct(row)

    if instruct is not None:
        print("row: " + row)
        print("amount: " + str(instruct.amount))
        print("crate: " + str(instruct.crate))
        print("move_to: " + str(instruct.move_to))
        print("which crate: " + str(cratelist[instruct.crate]))
        print("crate to move: " + str(cratelist[instruct.move_to]))
        for i in range(instruct.amount):
            if cratelist[instruct.crate]:
                item_to_move = cratelist[instruct.crate].pop()
                # cratelist[instruct.move_to].insert(1, item_to_move)
                cratelist[instruct.move_to].append(item_to_move)
                print(cratelist[instruct.move_to])
            else:
                print(f"Not enough items in crate {instruct.crate} to move.")
                break
        print("crates remaining: " + str(cratelist[instruct.crate]))
    # print(cratelist)

print(cratelist)
for i in range(8):
    if cratelist[i]:
        item_to_move = cratelist[i].pop()
        coollist[i].append(item_to_move)
    else:
        print("Not enough items in crate to move.")

# print(cratelist)
print("Here is the cool list:")
print(coollist)
