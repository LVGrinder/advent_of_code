import re
import pydantic

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


class Instruct:
    def __init__(self) -> None:
        self.amount: int = 0
        self.crate: int = 0
        self.move_to: int = 0

    def process(self, row):
        inputInstruct = re.findall(r"\d+", row)
        if inputInstruct:
            # using i for instruction because these are python preserved words
            self.amount = int(inputInstruct[0])
            self.crate = int(inputInstruct[1])
            self.move_to = int(inputInstruct[2])


for row in instructions:
    print("row: " + row)
    instruct = Instruct()
    instruct.process(row)
    amount = int(-1 + instruct.amount)
    crate = int(-1 + instruct.crate)

    print("amount: " + str(amount))

    print("crate: " + str(crate))
    for i in range(amount):
        item_to_move = cratelist[crate].pop()
        cratelist[instruct.move_to].insert(0, item_to_move)

    print(cratelist)


# print(cratelist[0][0])
