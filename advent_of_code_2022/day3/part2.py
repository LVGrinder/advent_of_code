
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
list_item = []
list_rucksack = []
check_group = 0
amount = 0
for rucksack in supplies:
    list_rucksack.append(rucksack)

    check_group += 1 

    
    if check_group == 3:
        #print("checking")
        check_group = 0
        amount += 1
        for f_item in list(list_rucksack[0]):
            #print(list(list_rucksack[0]))
            if f_item in list(list_rucksack[1]):
                #print(list(list_rucksack[1]))
                if f_item in list(list_rucksack[2]):
                    #print(list(list_rucksack[2]))
                    for kvp in priorities:
                        priority = kvp[0]
                        letter = kvp[1]
                        if letter == f_item:
                            print(priority, f_item, amount)
                            list_item.append(f_item)
                            list_value.append(priority)
                            #print()
                            list_rucksack = []
                            #print(find_group)
                            break
                else: 
                    continue
            
            else: 
                continue
            break
                
    
                
print(sum(list_value))