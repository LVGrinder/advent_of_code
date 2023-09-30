
# Opening file
file = open("advent_of_code_2022\day3\input.txt", "r+")
output = file.read()
file.close()

supplies = output.split("\n")

list_rucksack = []

priority = []

alphabet = "0 a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
alphabet = alphabet.split(" ")

for i in range(len(alphabet)):
    priority.append([i, alphabet[i]])


for rucksack in supplies:


    list_rucksack.append(rucksack)


    # This with list slicing
    # (len(rucksack) / 2)
    length_rucksack = [len(rucksack) / 2]
    #compartment_first = ([len(rucksack) / 2])
    #compartment_first = int(sum(compartment_first))
    #compartment_last = rucksack[:[sum(length_rucksack)]]
    compartment_last = rucksack[:int(sum([len(rucksack) / 2]))]

    print(list_rucksack)
    #print(compartment_first)
    print(compartment_last)

    break

