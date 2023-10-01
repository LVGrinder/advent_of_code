
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

    person1_contains_person2 = person1[0] <= person2[0] and person1[1] >= person2[1]
    person2_contains_person1 = person2[0] <= person1[0] and person2[1] >= person1[1]

    if person1_contains_person2 or person2_contains_person1:
        print("\n\n", person1, "\n", person2)
        changes_needed += 1

    print(changes_needed)