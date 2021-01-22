# Author: Ty Vareka
# Date: 2/5/2020
# Description: Finds the median in a given list
def find_median(numbers):
    """This function sorts the numbers numerically and then determines whether there are an odd or even number
    of numbers.  Depending on whether there are an odd or even number, the function determines the median."""

    numbers.sort()
    total = len(numbers)
    if total % 2 != 0:
        odd_median = int((total-1)/2)
        return numbers[odd_median]
    else:
        even_median_1 = numbers[(int(total/2))-1]
        even_median_2 = numbers[int(total/2)]
        mean_median = ((even_median_1+even_median_2)/2)
        return mean_median

