# Author: Ty Vareka
# Date: 2/5/2020
# Description: Creates a class [person] with name and age, then uses a function to calculate std.dev for a list of person
class Person:
    """Represents an individual's name and age"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
def std_dev(people):
    """Determines the standard deviation from a list of people.  The people are given names and age which are determined
    in the class Person and used for the standard deviation"""
    total_age_sq = 0
    average_age = 0
    for n in people:
        average_age += n.age
    average_age /= len(people)
    for n in people:
        total_age_sq += (n.age-average_age)**2
    final_age = (total_age_sq/len(people)) ** 0.5
    return final_age
