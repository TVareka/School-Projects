#Author: Ty Vareka
#Date: 1/24/2020
#Description: Program creates a hailstone sequence with positive integers to divide by 2 if even and multiple by 3/add 1 when odd.
def hailstone(n):
    steps = 0
    while n != 1:
        steps += 1
        if n % 2 == 0:
            n = (n/2)
        else:
            n = (n*3+1)
    return steps
#w = int(input())
#print(hailstone(w))
