
def square_val(val):
    """This function will square the variable by rebinding the variable. This will
make it so a different variable
is called upon later on in the program when I am asking it to cube the value."""
val = val**2
return val
num_1 = 5
square_val(num_1)
print(num_1)
def cube_val(val):
    """This function will call upon num_1 to square that value. You will notice it
is going to cube 5 and not 25
because of the fact that val and num_1 no longer refer to the same value. Since
num_1 was not mutated, I cannot
call upon the returned val from square_val this way."""
val = val**3
return val
cube_val(num_1)
print(num_1)


