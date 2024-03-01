import re
from pydantic import BaseModel

with open("input.txt", "r+") as f:
    lines = f.readlines()

crates = lines[:8]

instructions = lines[9:]

# print(instructions)

cratelist: list[list[str]] = []
crategroup = int(1)

for _ in range(9):
    cratelist.append([])

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
        print("crate to move: " + str(cratelist[instruct.move_to][0]))
        print("crates remaining: " + str(cratelist[instruct.crate]))
        for i in range(instruct.amount):
            if cratelist[instruct.crate]:
                item_to_move = cratelist[instruct.crate].pop()
                cratelist[instruct.move_to].insert(0, item_to_move)
            else:
                print(f"Not enough items in crate {instruct.crate} to move.")
                break
    # print(cratelist)

coolList: list = []
for i in range(8):
    item_to_move = cratelist[i].pop()
    coolList[i].insert(0, item_to_move)

print(coolList)
