# Points
win = 6
draw = 3
loss = 1

# Choices
rock = 1
paper = 2
scissor = 3

my_points = 0

me = "Z"
opponent = "C"

# Opening file
file = open("advent_of_code_2022\day2\input.txt", "r+")
output = file.read()
file.close()

# Returning values from round
def do_round(player1, player2):
    if player1 == "Y" and player2 == "A":
        return draw + rock
    if player1 == "Y" and player2 == "B":
        return loss + rock
    if player1 == "Y" and player2 == "C":
        return win + rock
    if player1 == "X" and player2 == "A":
        return win + paper
    if player1 == "X" and player2 == "B":
        return draw + paper
    if player1 == "X" and player2 == "C":
        return loss + paper
    if player1 == "Z" and player2 == "A":
        return loss + scissor
    if player1 == "Z" and player2 == "B":
        return win + scissor
    if player1 == "Z" and player2 == "C":
        return draw + scissor
    
    raise ValueError("Invalid choice")
    

for round in output.split("\n"):
    if (round == ""):
        print("Warning: emptly line")
        continue

    print(do_round(round[2], round[0]))
    my_points += do_round(me, opponent)
    
    
