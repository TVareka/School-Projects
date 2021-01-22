# Course: CS261 - Data Structures
# Student Name: Tyler Vareka
# Assignment: #2: Dynamic Array
# Description: This program will be used to create a dynamic array.  The various methods of this program allow
# for a lot of customization when creating a dynamic array.  The various methods will be used in later programs
# in order to append values, resize the array, get elements at a specific index, etc.
# Last revised: 10/23/2020


from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    def resize(self, new_capacity: int) -> None:
        """
        This method will be called anytime an array is full, so that the current array can be given a new capacity.
        In most situations, the new capacity that will be passed to this method will be double the current capacity.
        If the new capacity is less than zero or smaller than the amount of elements already in the array, the method
        will return without changing anything.
        """
        if new_capacity <= 0 or new_capacity < self.size:
            return
        new_array = StaticArray(new_capacity)
        for val in range(self.size):
            new_array[val] = self.data[val]
        self.data = new_array
        self.capacity = new_capacity

    def append(self, value: object) -> None:
        """
        This method is used append a value to the end of the array.  It also checks, first, to see if the array is
        at capacity.  If it is, it calls the resize method with double its current capacity before adding the next
        element.
        """
        if self.size == self.capacity:
            cap = self.capacity * 2
            self.resize(cap)
        self.data[self.size] = value
        self.size += 1


    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method will first check to see if the index passed to it is valid.  If it is not valid, it will raise the
        Dynamic Array Exception.  If it is valid, though, it will check to see if it needs to be resized, then add
        in the element at the passed in index.  The method works by moving all elements at the index, to the end of the
        array, back one space before entering the passed in value.
        """
        if index < 0 or index > self.size:
            raise DynamicArrayException
        if self.size == self.capacity:
            cap = self.capacity * 2
            self.resize(cap)
        for val in range(self.size-1, index-1, -1):
            self.data[val+1] = self.data[val]
        self.data[index] = value
        self.size += 1

    def get_at_index(self, index: int) -> object:
        """
        This method takes an index as a parameter, checks that index for its validity, then returns the element at
        that index.  If the index is not valid, it will raise a Dynamic Array Exception
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def remove_at_index(self, index: int) -> None:
        """
        This method takes an index as a parameter, checks for the validity of that index, then determines the current
        size of the array.  If the amount of elements in the array is less than capacity/4 AND the capacity is greater
        than 10, the method will change the capacity to 2*current size.  Once it has made this change, the method will
        move all elements over one space after the intended index.  It will then delete the final element in the
        array/decrease size by one.
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        if self.size < (self.capacity/4) and self.capacity > 10:
            if (self.size * 2) < 10:
                self.capacity = 10
            else:
                self.capacity = self.size * 2

        for val in range(index, self.size-1):
            self.data[val] = self.data[val+1]

        self.data[self.size-1] = None
        self.size -= 1


    def slice(self, start_index: int, quantity: int) -> object:
        """
        This method takes an index and quantity as parameters.  The index and quantity must be greater than 0 and
        the 'slice' must not be larger than the size of the current array.  The method will create a new Dynamic Array
        and copy the elements from the index until it has reached the intended quantity.  It will then return the new
        Dynamic Array.  This method ensures that the original Dynamic Array is not tampered with.
        """
        if start_index < 0 or quantity < 0 or (start_index + quantity) > self.size:
            raise DynamicArrayException
        new_da = DynamicArray()
        for val in range(start_index, (start_index+quantity)):
            new_da.append(self.data[val])
        return new_da

    def merge(self, second_da: object) -> None:
        """
        This method takes another dynamic array as its parameter and appends the new array onto the end of the original
        Dynamic Array.
        """
        for val in range(second_da.length()):
            self.append(second_da.data[val])

    def map(self, map_func) -> object:
        """
        This method allows the user to pass in a function, which is applied to a copy of the original dynamic array.
        The original dynamic array will not be tampered with.
        """
        new_da = DynamicArray()
        for val in range(self.size):
            new_da.append(map_func(self.data[val]))
        return new_da

    def filter(self, filter_func) -> object:
        """
        This method takes a filter function as a parameter and creates a new dynamic array.  The filter function
        is applied to the dynamic array and if the filter function returns True, it will append that value into the
        new array.  Once it has gone through the entire array, it returns the new dynamic array.  Once again, the
        original Dynamic Array is not tampered with in this method.
        """
        new_da = DynamicArray()
        for val in range(self.size):
            if filter_func(self.data[val]):
                new_da.append(self.data[val])
        return new_da

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        TThis method takes a reduce function and an initializer as parameters.  If the current dynamic array is 0, only
        the initializer is returned.  If there is no initializer passed into this method, the first element of the
        array becomes the initializer.  The function is applied to all other elements of the array (including the
        first element if an initializer is passed in) and the sum is returned.
        """
        if self.size == 0:
            return initializer

        if initializer is None:
            initializer = self.data[0]
            sum = initializer
            for val in range(1, self.size):
                sum += reduce_func(0, self.data[val])
            return sum
        else:
            sum = initializer
            for val in range(self.size):
                sum += reduce_func(0, self.data[val])
            return sum



# BASIC TESTING
if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Can not insert value", value, "at index", index)
    print(da)

    print("\n# get_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50])
    print(da)
    for i in range(4, -1, -1):
        print(da.get_at_index(i))

    print("\n# get_at_index example 2")
    da = DynamicArray([100, 200, 300, 400, 500])
    print(da)
    for i in range(-1, 7):
        try:
            print("Index", i, ": value", da.get_at_index(i))
        except Exception as e:
            print("Index", i, ": exception occurred")

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOUCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))


    print("\n# map example 2")
    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

