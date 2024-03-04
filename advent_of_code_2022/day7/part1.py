import os
from pathlib import Path
from pydantic import BaseModel

with open(Path(os.getcwd(), "advent_of_code_2022", "day7", "input.txt"), "r+") as f:
    lines = f.readlines()

# print(lines)


class File(BaseModel):
    name: str
    size: int


class Folder(BaseModel):
    contents: dict[str, "Folder | File"]
    name: str

    def add_item(self, item: "Folder | File"):
        self.contents[item.name] = item


for line in lines:
    line = line.replace("$ ", "")
    parts = line.split()
    print(f"this is line: {line}\nthis is parts: {parts}\n")

# folder = Folder().folder
#
# for line in lines:
#     line = line.replace("\n", "")
#     for existingfolder in folder:
#         if line[:4] == existingfolder:
#             break
#     if line[:4] == "$ cd" and line[5] != ".":
#         folder.append(line[5:])
#         print(line)
#     if line[:4] == "dir ":
#         folder.append(line[5:])
#         print(line)
#
# print(folder)
