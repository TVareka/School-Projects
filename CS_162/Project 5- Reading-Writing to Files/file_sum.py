# Author: Ty Vareka
# Date: 4/27/2020
# Description: Make a function that takes the name of a text file then sums the values in the file.

def file_sum(textFile):
    """This function takes as a parameter the name of a text file containing numbers, then sums those numbers.  It
    will then write the sum to a text file named sum.txt"""
    total = 0
    with open(textFile, 'r') as sum:
        for line in sum:
            val = float(line.strip())
            total += val
    with open('sum.txt', 'w') as result:
        result.write(str(total))


