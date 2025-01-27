file = open("advent_of_code_2022\day1\input.txt", "r+")
output = file.read()
file.close()

elves = output.split("\n\n")

carb_sums = []

for elf in elves:
    #print(i, spliitedOutput[i])

    elf = elf.split("\n")

    elf = list(map(int, elf))

    output = sum(elf)

    carb_sums.append(output)


carb_sums.sort(reverse=True)



print(sum(carb_sums[:3]))