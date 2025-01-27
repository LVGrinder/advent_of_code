
# Get input so we can use it in the task later
file = open("advent_of_code_2022\day4\input.txt", "r+")
input = file.read()
file.close()

pairs = input.split()

def format_person(person):
    person = person.split("-")

    # Map list to ints since they are strings
    person = list(map(int, person))
    return person


changes_needed = 0

for pair in pairs:
    # We're splitting it since the people are seperated by a comma like "24-26,80-42"
    pair = pair.split(",")

    person1 = format_person(pair[0])
    person2 = format_person(pair[1])


    person1_overlap_person2 = max(person1) >= min(person2) and min(person1) <= min(person2)
    person2_overlap_person1 = max(person2) >= min(person1) and min(person2) <= min(person1)

    if person1_overlap_person2 or person2_overlap_person1:
        changes_needed += 1
    else:
        print("Does not overlap")
    print(pair)
    print(changes_needed)