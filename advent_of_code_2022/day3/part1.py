
# Opening file
file = open("advent_of_code_2022\day3\input.txt", "r+")
output = file.read()
file.close()

supplies = output.split("\n")

alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
alphabet = alphabet.split(" ")

priorities = []
for i in range(len(alphabet)):
    priorities.append([i + 1, alphabet[i]])

list_value = []
list_rucksack = []
for rucksack in supplies:
    list_rucksack.append(rucksack)


    half_len = int(len(rucksack) / 2)

    #compartment_first = rucksack[:int(sum([len(rucksack) / 2]))]
    #compartment_last = rucksack[int(sum([len(rucksack) / 2])):]
    compartment_first = rucksack[:half_len]
    compartment_last = rucksack[half_len:]

    #print(compartment_first)
    #print(compartment_last)
    
    for f_item in compartment_first:
        #print("Now checking if", f_item, "is in", compartment_last)
        if compartment_last.__contains__(f_item):
            for kvp in priorities:
                priority = kvp[0]
                letter = kvp[1]
                if letter == f_item:
                    print(priority, f_item)
                    list_value.append(priority)
                    print(compartment_first, "", compartment_last)
                    break
            else:
                continue
            break
                

print(sum(list_value))