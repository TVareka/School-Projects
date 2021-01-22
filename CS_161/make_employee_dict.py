# Author: Ty Vareka
# Date: 2/19/2020
# Description: Create a dictionary of employees, keyed on ID number from lists of names, IDs, salaries, and email addresses

class Employee:
    """Represent employee's name, ID, salary and email address"""
    def __init__(self, name, ID_number, salary, email_address):
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email_address
def make_employee_dict(names, ID_numbers, salaries, email_addresses):
    """Creates a dictionary where the keys are the employee ID and the values associate with it
    are the employees name, salary, and email address"""
    d = dict()
    for i in range(len(names)):
        d[ID_numbers[i]] = Employee(names[i], ID_numbers[i], salaries[i], email_addresses[i])
    return d


