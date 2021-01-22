# Course: CS261 - Data Structures
# Student Name: Tyler Vareka
# Assignment: #2: Bag
# Description: This program creates a 'bag' of elements using the previous dynamic array program we wrote.  This 'bag'
# has the ability to add, remove, count, size, clear, and determine if is the same as another 'bag'.
# Last revised: 10/23/2020

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    def add(self, value: object) -> None:
        """
        This method uses the previously written 'append' method from dynamic array to add elements into the bag.
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        This method takes a value as a parameter and checks the bag to see if that element is in it.  If the value
        matches an element from the bag, it will remove that element and return True.  If no such element is found in
        the bag, it will only return False.
        """
        check = 0
        for i in range(self.da.length()):
            if value == self.da.get_at_index(i):
                self.da.remove_at_index(i)
                check += 1
                break
        if check > 0:
            return True
        else:
            return False

    def count(self, value: object) -> int:
        """
        This method takes a value as a parameter and then walks through the elements of the bag to see if any match
        the current value.  If the element/value match, the method adds one to the variable 'count'.  Once all elements
        of the bag have been compared with 'value', the method returns the count.
        """
        count = 0
        for i in range(self.da.length()):
            if value == self.da.get_at_index(i):
                count += 1

        return count

    def clear(self) -> None:
        """
        This method 'clears' out the bag by creating a new empty dynamic array, which it then sets equal to self.da.
        """
        new_da = DynamicArray()
        self.da = new_da

    def equal(self, second_bag: object) -> bool:
        """
        This method takes a second bag as a parameter.  The method determines if the two bags are identical by comparing
        lengths and count values of each element in the bag.  If the bags are identical, the method returns True, if not
        the method returns False
        """
        if self.da.length() == second_bag.da.length():
            for i in range(self.da.length()):
                value = self.da.get_at_index(i)
                if self.count(value) != second_bag.count(value):
                    return False
            return True
        else:
            return False




# BASIC TESTING
if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
