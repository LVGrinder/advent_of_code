# Write a program which loops through n numbers.
# if number is a multiple of 3 write Fizz
# if number is a multiple of 5 write Buzz
# if number is a multiple of both 3 and 5. Print "FizzBuzz" instead.

# Create a list containing numbers 0 thorough n.
# loop through the list running your fizz buzz thingy

# Input:
n = 100

# Your Code:
for i in range(n):
    y = i % 3
    z = i % 5

    if y == 0 and z == 0:
        print("FizzBuzz")
        continue

    if y == 0:
        print("fizz")

    if z == 0:
        print("buzz")