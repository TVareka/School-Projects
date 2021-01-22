# Author: Ty Vareka
# Date: 1/21/2020
# Description: Min/Max Program that determines highest/lowest integer from numbers input
smallest = 0
largest = 0
print("How many integers would you like to enter?")
num_integers = int(input()) #number of integers wanted
print("Please enter", num_integers, "integers.")
for val in range(1,num_integers+1):
    integer = int(input())
    if val == 1:
        smallest = integer
        largest = integer
    elif (integer < smallest):
        smallest = integer
    elif (integer > largest):
        largest = integer
print("min:", smallest)
print("max:", largest)


