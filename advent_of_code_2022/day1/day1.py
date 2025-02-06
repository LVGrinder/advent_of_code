import os
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2022", "day1", "input.txt"), "r+") as f:
    lines = f.read()

# print(lines)

test: list[str] = []
test = lines.split("\n\n")
# for i in test:
# i.replace("\n", "+")
# print(i)
print(test[0])
est = test[0].split("\n")
print(est)
# coneee: list[]
for i in range(len(est)):
    est[i] = int(est[i])
est: list[int]
print(sum(est))
