# Course: CS261 - Data Structures
# Student Name: Tyler Vareka
# Assignment: Singly Linked Lists
# Description: This program creates a class for singly linked lists that have a variety of different corresponding
# methods.  When the program is complete, the user should be able to add values to the front of the list, the back
# of the list, insert at a specific index, etc.



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        This method takes a value as a parameter and adds that value to the front of the list.  This method makes
        sure that all of the corresponding pointers are in the right direction as well.
        """
        node = SLNode(value)
        if self.is_empty():
            node.next = self.tail
            self.head.next = node
        else:
            node.next = self.head.next
            self.head.next = node


    def add_back(self, value: object) -> None:
        """
        This method takes a value as a parameter and adds that value to the back of the list.  This method also makes
        sure that all of the corresponding pointers are in the correct direction.
        """
        # traverse the list to find last node
        node = SLNode(value)
        if self.is_empty():
            node.next = self.tail
            self.head.next = node
        else:
            node.next = self.tail
            cur = self.head.next
            while cur.next != self.tail:
                cur = cur.next
            cur.next = node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method takes an index and a value as parameters.  The method will then walk through the list and place
        that value at the correct index.  Once again, all of the pointers within the linked list will be pointed
        correctly.
        """
        prev = self.head
        cur = self.head.next
        cur_index = 0
        node = SLNode(value)
        if index < 0 or index > self.length():
            raise SLLException
        if index == 0:
            self.add_front(value)
        else:
            while cur_index != index:
                prev = prev.next
                cur = cur.next
                cur_index += 1
            node.next = cur
            prev.next = node


    def remove_front(self) -> None:
        """
        This method does not take any parameters.  This method will simply check to see if the list is empty and raise
        an exception if this is true.  If not, the method will remove the front value from the list.
        """
        if self.is_empty():
            raise SLLException
        else:
            cur = self.head.next
            prev = self.head
            prev.next = cur.next


    def remove_back(self) -> None:
        """
        This method does not take any parameters.  It will check to see if the list is empty and raise an exception
        if that is true.  If the list is not empty, it will walk through the list and remove the final element within
        that list.
        """
        if self.is_empty():
            raise SLLException
        else:
            cur = self.head.next
            prev = self.head
            while cur.next != self.tail:
                cur = cur.next
                prev = prev.next
            prev.next = cur.next

    def remove_at_index(self, index: int) -> None:
        """
        This method takes an index only as a parameter.  The method will make sure that the index is valid and if it is
        not, it will raise an exception.  As long as the index is valid, the method will walk through the list and
        remove the element at that index.
        """
        prev = self.head
        cur = self.head.next
        cur_index = 0
        if index < 0 or index > self.length()-1:
            raise SLLException
        if index == 0:
            self.remove_front()
        else:
            while cur_index != index:
                prev = prev.next
                cur = cur.next
                cur_index += 1
            prev.next = cur.next


    def get_front(self) -> object:
        """
        This method does not take any parameters.  This method checks to see if the list is empty and raises an
        exception if it is empty.  If the list is not empty, it will return the value that is at the front of the list.
        """
        if self.is_empty():
            raise SLLException
        else:
            return self.head.next.value

    def get_back(self) -> object:
        """
        This method does not take any parameters.  This method checks to see if the list is empty and raises an
        exception if it is empty.  If the list is not empty, it will return the value that is at the back of the list.
        """
        if self.is_empty():
            raise SLLException
        else:
            cur = self.head.next
            while cur.next != self.tail:
                cur = cur.next
            return cur.value


    def remove(self, value: object) -> bool:
        """
        This method takes a value as a parameter.  It then walks through the entire list to see if the value that was
        passed in matches any of the values in the list.  If it does match a value in the list, it will remove that
        value and return True.  If the value does not match any values in the list, it will simply return false.
        """
        cur = self.head.next
        prev = self.head
        if self.is_empty():
            return False
        while cur.value != value and cur.next != self.tail:
            cur = cur.next
            prev = prev.next
        if cur.value == value:
            prev.next = cur.next
            return True
        else:
            return False

    def count(self, value: object) -> int:
        """
        This method takes a value as a parameter.  It will then walk through the entire list and keep a count of how
        many times that value occurs in the list.  The method then returns the total count.
        """
        count = 0
        cur = self.head.next
        while cur != self.tail:
            if cur.value == value:
                count += 1
            cur = cur.next

        return count

    def slice(self, start_index: int, size: int) -> object:
        """
        This method takes a starting index and a size as parameters.  The method checks to see if the starting index
        and size are valid.  If not, it will raise an exception.  If they are valid, the method will make a copy of the
        values starting at the starting index and extending the length of size.  The method will then return the new
        linked list that these values were copied to.
        """
        new_ll = LinkedList()
        cur = self.head.next
        cur_index = 0
        if start_index < 0 or size < 0 or start_index > (self.length()-1) or (start_index + size) > self.length():
            raise SLLException
        while cur_index != start_index:
            cur = cur.next
            cur_index += 1
        if size == 0:
            return new_ll
        else:
            comparison = 0
            while size != comparison:
                new_ll.add_back(cur.value)
                cur = cur.next
                comparison += 1
            return new_ll




if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)
    #
    #
    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)
    #
    #
    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))
    #
    #
    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))
    #
    #
    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)
    #
    #
    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)
    #
    #
    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))
    #
    #
    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())
    #
    #
    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)

    #
    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))
    #
    #
    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")
    #
    #
    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

