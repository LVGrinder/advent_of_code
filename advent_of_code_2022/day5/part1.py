with open("input.txt", "r+") as f:
    lines = f.readlines()

crates = lines[:9]

instructions = lines[9:]

# print(instructions)

amount = 1
for row in crates:
    amount += 1
    print(row)
    # row = row.split()
    # print(row)
    for i in range(0, len(row), 4):
        print(row[i + 1])
