
with open("input.txt", "r+") as f:
    lines = f.readlines()

crates = lines[:9]

instructions = lines[9:]

print(instructions)

