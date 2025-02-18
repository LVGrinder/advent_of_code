import os
from pathlib import Path

with open(Path(os.getcwd(), "advent_of_code_2022", "day2", "input.txt"), "r+") as f:
    lines = f.read()

line = lines.split("\n")
points = 0
print(line)

# Me
# A = Rock
# B = Paper
# C = Scissors
# Opponent
# X = Rock
# Y = Paper
# Z = Scissors


def score(outcome, player, points):
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


def who_win(player1, player2, points):
    if player1 == "A":
        if player2 == "X":
            score("Draw", player1, points)
        if player2 == "Y":
            score("Lose", player1, points)
        if player2 == "Z":
            score("Win", player1, points)
            points += 1
            return points

    if player1 == "B":
        if player2 == "X":
            score("Win", player1, points)
            points += 1
            return points
        if player2 == "Y":
            score("Draw", player1, points)
        if player2 == "Z":
            score("Lose", player1, points)
    if player1 == "C":
        if player2 == "X":
            score("Lose", player1, points)
        if player2 == "Y":
            score("Win", player1, points)

            return points
        if player2 == "Z":
            score("Draw", player1, points)


def return_42():
    return 42 + 5


for game in line:

    # To avoid empty lines
    if game == "":
        continue

    game = game.split(" ")
    print(game)
    player1 = game[0]
    player2 = game[1]
    print(f"This is player1 choice: {player1}")
    print(f"This is player2 choice: {player2}")
    who_win(player1, player2, points)
    print(who_win(player1, player2, points))
    print(points)
    print(return_42())

    print(f"Score is {points}")
