import os
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2022", "day2", "input.txt"), "r+") as f:
    lines = f.read()

line = lines.split("\n")
print(line)

# X = Rock
# Y = Paper
# Z = Scissors


def who_win(player1, player2):
    if player1 == "X":
        if player2 == "X":
            print("draw")
        if player2 == "Y":
            print("lose")
        if player2 == "Z":
            print("win")


for game in line:
    # To avoid empty lines
    if game == "":
        continue

    print(game)
    game = game.split(" ")
    print(game)
