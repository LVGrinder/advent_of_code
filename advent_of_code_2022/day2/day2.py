# Points
win = 6
draw = 3
loss = 0

# Choices
rock_points = 1
paper_points = 2
scissor_points = 3

rock = "A"
paper = "B"
scissors = "C"

my_points = []

me = "Z"
opponent = "C"

# Opening file
file = open("advent_of_code_2022\day2\input.txt", "r+")
output = file.read()
file.close()

def map_xyz_input(input):
    if input == "X":
        return rock
    if input == "Y":
        return paper
    if input == "Z":
        return scissors
    return input

# Returning values from round
def do_round(player1, player2):
    player1 = map_xyz_input(player1)
    player2 = map_xyz_input(player2)

    points = 0

    # Apply Choice points
    if player1 == rock:
        points += rock_points

    if player1 == paper:
        points += paper_points

    if player1 == scissors:
        points += scissor_points

    # Check for draw
    if player1 == player2:
        points += draw
        
    # Check for win
    if player1 == rock and player2 == scissors:
        points += win
    if player1 == paper and player2 == rock:
        points += win
    if player1 == scissors and player2 == paper:
        points += win

    # Check for loss
    if player1 == rock and player2 == paper:
        points += loss
    if player1 == paper and player2 == scissors:
        points += loss
    if player1 == scissors and player2 == rock:
        points += loss
    
    return points

for round in output.split("\n"):
    if (round == ""):
        print("Warning: empty line")
        continue

    my_move = round[2]
    opponent_move = round[0]

    my_points.append(do_round(my_move, opponent_move)) 

print("According to this strategy I would have", sum(my_points))