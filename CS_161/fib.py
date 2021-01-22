#Author: Ty Vareka
#Date: 1/24/2020
#Description:Program takes a positive integer and returns the number at that position of the Fibonacci sequence
def fib(n):
    a = 0
    b = 1
    if n==1:
        return a+b
    else:
        for val in range (2,n+1):
            c = a + b
            a = b
            b = c
        return c

