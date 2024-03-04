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

    def get_size(self):
        total_size = 0
        for item in self.contents:
            if isinstance(item, File):
                total_size += item.size
            elif isinstance(item, Folder):
                total_size += item.get_size()
        return total_size


Folder.model_rebuild

# Initialize root folder and folder stack
root_folder = Folder(name="root", contents={})
current_folder = root_folder
folder_stack = [root_folder]

for line in lines:
    line = line.strip()  # Remove leading and trailing whitespace
    if not line:
        continue
    parts = line.split()
    if parts[0] == "dir":
        folder_name = parts[1]
        new_folder = Folder(name=folder_name, contents={"Folder | File"})
        current_folder.add_item(new_folder)
    elif parts[0] == "cd":
        folder_name = parts[1]
        if folder_name == "..":
            folder_stack.pop()
            current_folder = folder_stack[-1]
        else:
            current_folder = current_folder.contents[folder_name]
            folder_stack.append(current_folder)
    else:
        size, name = parts[0], parts[1]
        file = File(name=name, size=int(size))
        current_folder.add_item(file)
