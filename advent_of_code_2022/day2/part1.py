import os
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2022", "day2", "input.txt"), "r+") as f:
    lines = f.read()

line = lines.split("\n")
print(line)

# Me
# A = Rock
# B = Paper
# C = Scissors
# Opponent
# X = Rock
# Y = Paper
# Z = Scissors


def score(outcome: str, player: str, points: int) -> int:
    if outcome == "Win":
        print("Win iiii")
        print(player)
        if player == "A":
            print("YAYAYAYY")
            print(points)
            return points + 3
        if player == "B":
            print("YAYAYAYY")
            print(points)
            return points + 5
        if player == "C":
            print("YAYAYAYY")
            print(points)
            return points + 7
    return points


def who_win(player1: str, player2: str, points: int) -> int:
    if player1 == "A":
        if player2 == "X":
            points = score("Draw", player1, points)
        if player2 == "Y":
            points = score("Lose", player1, points)
        if player2 == "Z":
            points = score("Win", player1, points)
            # points += 1
            return points

    if player1 == "B":
        if player2 == "X":
            points = score("Win", player1, points)
            # points += 1
            return points
        if player2 == "Y":
            points = score("Draw", player1, points)
        if player2 == "Z":
            points = score("Lose", player1, points)
    if player1 == "C":
        if player2 == "X":
            points = score("Lose", player1, points)
        if player2 == "Y":
            points = score("Win", player1, points)

            return points
        if player2 == "Z":
            points = score("Draw", player1, points)
    return points


points: int = 0
for game in line:

    # To avoid empty lines
    if game == "":
        continue

    game = game.split(" ")
    print(game)
    player1: str = game[0]
    player2: str = game[1]
    print(f"This is player1 choice: {player1}")
    print(f"This is player2 choice: {player2}")
    points = who_win(player1, player2, points)
    print(who_win(player1, player2, points))
    print(points)

    print(f"Score is {points}")
