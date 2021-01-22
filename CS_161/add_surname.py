# Author: Ty Vareka
# Date: 2/5/2020
# Description: Add Kardashian to names that start with K within the list
def add_surname(first_name):
    """Function adds Kardashian to the names that start with K within the list"""
    return [names + " Kardashian" for names in first_name if names[0]== "K"]


