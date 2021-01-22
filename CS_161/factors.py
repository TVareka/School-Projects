# Author: Ty Vareka
# Date: 1/21/2020
# Description: Allows you to input a positive integer and then determines factors of that integer
integer = int(input("Please enter a positive integer: "))
print("The factors of", integer, "are:")
for val in range(1, integer+1):
    if val == 1:
        continue
    elif val == integer:
        continue
    elif integer % val == 0:
        print(val)
