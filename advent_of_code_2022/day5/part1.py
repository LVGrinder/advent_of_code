with open("input.txt", "r+") as f:
    lines = f.readlines()

crates = lines[:9]

instructions = lines[9:]

# print(instructions)

cratelist = []
crategroup = 1
for _ in range(9):
    cratelist.append([])
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
