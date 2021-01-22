# Course: CS261 - Data Structures
# Assignment: 5
# Student: Tyler Vareka
# Description: This program creates a Hash Map with various methods that the user may use.  Some of these methods
# include putting values into the Hash Map, clearing, removing values, etc.  All of the methods are clearly defined
# below.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        This method takes no parameters and clears the current buckets within the hash map.  This method also resets
        the size of the hash map back to zero.
        """
        self.buckets = DynamicArray()
        for _ in range(self.capacity):
            self.buckets.append(LinkedList())
        self.size = 0



    def get(self, key: str) -> object:
        """
        This method takes a key as a parameter.  It first determines the hash value by plugging key into the
        hash function and then using % to fit the capacity.  A variable node is then created which searches for
        that hash index and contains that key.  If there is a value that contains that key, it will return it,
        otherwise it returns None.
        """
        hash_index = self.hash_function(key) % self.capacity
        node = self.buckets.get_at_index(hash_index).contains(key)
        if node is None:
            return None
        else:
            return node.value


    def put(self, key: str, value: object) -> None:
        """
        This method takes a key and a value as parameters.  First the hash index is determined so that we can search
        the Dynamic Array.  If there is not a key/value pair, the method inserts the key value pair and increases the
        self.size by 1.  If there is already a key/value pair, the method changes the node.value to value.
        """
        hash_index = self.hash_function(key) % self.capacity
        node = self.buckets.get_at_index(hash_index).contains(key)
        if node is None:
            self.buckets.get_at_index(hash_index).insert(key, value)
            self.size += 1
        else:
            node.value = value


    def remove(self, key: str) -> None:
        """
        This method takes a key as a parameter.  First we determine the hash index and create the variable is_there.
        Since .remove will return a boolean value, we then figure out if remove actually got rid of anything and if it
        did, the size is decremented by 1.
        """
        hash_index = self.hash_function(key) % self.capacity
        is_there = self.buckets.get_at_index(hash_index).remove(key)
        if is_there is True:
            self.size -= 1


    def contains_key(self, key: str) -> bool:
        """
        This method takes a key as a parameter.  First, the hash index is determined.  That index is then used along
        with the .contains function to determine if the Linked List contains that key.  If it does, the method returns
        True, but if it does not, the method returns false.
        """
        hash_index = self.hash_function(key) % self.capacity
        node = self.buckets.get_at_index(hash_index).contains(key)
        if node is not None:
            return True
        else:
            return False

    def empty_buckets(self) -> int:
        """
        This method walks through the capacity of the Dynamic Array counting any bucket that has a length of 0.  Once
        it has walked through the entire array, it returns total back to the user, which will tell them how many empty
        buckets are currently present.
        """
        total = 0
        for i in range(self.capacity):
            if self.buckets.get_at_index(i).length() == 0:
                total += 1
        return total

    def table_load(self) -> float:
        """
        This method does not take any parameters.  It takes the size of the dynamic array divided by the capacity to
        return the table load back to the user.
        """
        return (self.size/self.capacity)

    def resize_table(self, new_capacity: int) -> None:
        """
        This method takes a new capacity as a parameter.  If the new capacity is less than 1, the method immediately
        returns.  Holder variables are initially saved using old_array and old_capacity.  The capacity is set to the
        passed in value and the array is cleared.  The method then walks through the range of the old capacity and gets
        values at the index, while also keeping the key/value pairs of the Linked Lists.
        """
        if new_capacity < 1:
            return
        old_array = self.buckets
        old_capacity = self.capacity
        self.capacity = new_capacity
        self.clear()

        for i in range(old_capacity):
            lst = old_array.get_at_index(i)
            for node in lst:
                self.put(node.key, node.value)


    def get_keys(self) -> DynamicArray:
        """
        This method does not take any parameters.  This method creates a fresh dynamic array and walks through the
        entire current dynamic array.  At each bucket, the method then walks through Linked List and appends each key
        to the fresh dynamic array.  Once the method has walked through the entire dynamic array, it returns the
        key array.
        """
        key_array = DynamicArray()
        for i in range(self.capacity):
            lst = self.buckets.get_at_index(i)
            for node in lst:
                key_array.append(node.key)
        return key_array


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
