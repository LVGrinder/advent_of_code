
# Opening file
file = open("advent_of_code_2022\day3\input.txt", "r+")
output = file.read()
file.close()

print(output)

priority = []

alphabet = "0 a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
alphabet = alphabet.split(" ")

for i in range(len(alphabet)):
    priority.append([i, alphabet[i]])

print(priority) 