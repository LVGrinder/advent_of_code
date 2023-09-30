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

def calculate_move(outcome, opponents_move):
    if outcome == "X":
        if opponents_move == rock:
            return scissors
        if opponents_move == paper:
            return rock
        if opponents_move == scissors:
            return paper
    if outcome == "Y":
        return opponents_move
    if outcome == "Z":
        if opponents_move == rock:
            return paper
        if opponents_move == paper:
            return scissors
        if opponents_move == scissors:
            return rock

    raise ValueError("Whops?")

# Returning values from round
def do_round(outcome, opponents_move):
    my_move = calculate_move(outcome, opponents_move)

    points = 0

    # Apply Choice points
    if my_move == rock:
        points += rock_points

    if my_move == paper:
        points += paper_points

    if my_move == scissors:
        points += scissor_points

    # Check for draw
    if my_move == opponents_move:
        points += draw
        
    # Check for win
    if my_move == rock and opponents_move == scissors:
        points += win
    if my_move == paper and opponents_move == rock:
        points += win
    if my_move == scissors and opponents_move == paper:
        points += win

    # Check for loss
    if my_move == rock and opponents_move == paper:
        points += loss
    if my_move == paper and opponents_move == scissors:
        points += loss
    if my_move == scissors and opponents_move == rock:
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