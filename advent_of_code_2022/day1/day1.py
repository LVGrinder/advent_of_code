file = open("input.txt", "r+")
output = file.read()
file.close()

#"print(output)

elves = output.split("\n\n")

#"2468\n2468\n2468\n\n2468\n2468" -->  ["2468\n2468\n2468", "2468\n2468"]

carb_sums = []

for i in range(len(elves)):
    #print(i, spliitedOutput[i])

    elf = elves[i].split("\n")

    elf = list(map(int, elf))

    output = sum(elf)

    carb_sums.append(output)



    #print(i, elf)
    
    # ["2468", "2468", "2468"] --> [2468, 2468, 2468]
    #if spliitedOutput[i] == "\n":
    #    spliitedOutput[i] = "+"

#print(carb_sums)

carb_sums.sort(reverse=True)



print(sum(carb_sums[:3]))