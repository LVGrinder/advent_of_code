
# Opening file
file = open("advent_of_code_2022\day4\input.txt", "r+")
output = file.read()
file.close()


pairs = output.split()




#print(pairs)

# Create range with first number with the last number

def format_person(person):
    # Create list of range
    person = person.split("-")

    # Convert to int
    person = list(map(int, person))
    return person


changes_needed = 0

for pair in pairs:
    pair = pair.split(",")
    person1 = format_person(pair[0])
    person2 = format_person(pair[1])

    # 2 - 8
    # 3 - 6


    if (person1[0] <= person2[0] and person1[1] >= person2[1]) or (person2[0] <= person1[0] and person2[1] >= person1[1]):
        print("\n\n", person1, "\n", person2)
        changes_needed += 1

    print(changes_needed)