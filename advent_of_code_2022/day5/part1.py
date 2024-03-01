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
        amount=int(-1 + inputInstruct[0]),
        crate=int(-1 + inputInstruct[1]),
        move_to=int(inputInstruct[2]),
    )


for row in instructions:

    instruct: Instruct | None = parseRowToInstruct(row)

    if instruct is not None:
        print("row: " + row)
        print("amount: " + str(Instruct.amount))
        print("crate: " + str(Instruct.crate))
        for i in range(Instruct.amount):
            item_to_move = cratelist[Instruct.crate].pop()
            cratelist[Instruct.move_to].insert(0, item_to_move)

    print(cratelist)


# print(cratelist[0][0])
