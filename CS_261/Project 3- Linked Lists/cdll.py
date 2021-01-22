# Course: CS261 - Data Structures
# Student Name: Ty Vareka
# Assignment: 3: cdll
# Description: This program creates a class for circular doubly linked lists.  It has many methods that allow the user
# to add values, remove values, reverse the list, etc.


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        This method takes a value as a parameter.  The method will then add this value to the front of the list.  The
        method makes sure that all pointers are facing the correct nodes within the list.
        """
        node = DLNode(value)
        if self.is_empty():
            node.next = self.sentinel
            node.prev = self.sentinel
            self.sentinel.next = node
            self.sentinel.prev = node
        else:
            node.next = self.sentinel.next
            node.prev = self.sentinel
            self.sentinel.next.prev = node
            self.sentinel.next = node

    def add_back(self, value: object) -> None:
        """
        This method takes a value as a parameter.  It checks to see if the list is empty, because this will slightly
        change how the node is added to the list (exact same as 'add_front).  If the list is not empty, though, the
        method efficiently adds in the node to the back of the list while making sure that all of the pointers are
        pointing at the correct nodes.
        """
        node = DLNode(value)
        if self.is_empty():
            node.next = self.sentinel
            node.prev = self.sentinel
            self.sentinel.next = node
            self.sentinel.prev = node
        else:
            node.prev = self.sentinel.prev
            node.next = self.sentinel
            self.sentinel.prev.next = node
            self.sentinel.prev = node


    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method takes an index and a value as parameters.  The method checks to makes sure that the index is valid
        and will raise an exception if it is not.  Following this, the method walks through the list to determine where
        this value should be placed, and efficiently adds it into the list.
        """
        prev = self.sentinel
        cur = self.sentinel.next
        cur_index = 0
        node = DLNode(value)
        if index < 0 or index > self.length():
            raise CDLLException
        if index == 0:
            self.add_front(value)
        else:
            while cur_index != index:
                prev = prev.next
                cur = cur.next
                cur_index += 1
            node.next = cur
            node.prev = prev
            cur.prev = node
            prev.next = node

    def remove_front(self) -> None:
        """
        This method does not take any parameters.  It first checks to see if the list is empty and raises an exception
        if the list is empty.  As long as the list is not empty, the method will remove the first element in the list.
        """
        if self.is_empty():
            raise CDLLException
        else:
            cur = self.sentinel.next
            self.sentinel.next = cur.next
            cur.next.prev = self.sentinel

    def remove_back(self) -> None:
        """
        This method does not take any parameters.  It first checks to see if the list is empty and raises an exception
        if the list is empty.  As long as the list is not empty, the method will remove the last element in the list.
        """
        if self.is_empty():
            raise CDLLException
        else:
            cur = self.sentinel.prev
            self.sentinel.prev = cur.prev
            cur.prev.next = self.sentinel

    def remove_at_index(self, index: int) -> None:
        """
        This method takes an index as a parameter.  The method first checks to make sure that the index is valid and
        will raise an exception if the index is not.  After this, the method will walk through the list to determine
        the element at the passed-in index.  The method will remove the element corresponding to the passed in index.
        """
        prev = self.sentinel
        cur = self.sentinel.next
        cur_index = 0
        if index < 0 or index > self.length()-1:
            raise CDLLException
        if index == 0:
            self.remove_front()
        else:
            while cur_index != index:
                prev = prev.next
                cur = cur.next
                cur_index += 1
            prev.next = cur.next
            cur.next.prev = prev


    def get_front(self) -> object:
        """
        This method does not take any parameters.  The method will first check to see if the list is empty and will
        raise an exception if this is true.  As long as the list is not empty, the method will return the first value
        in the list without altering it.
        """
        if self.is_empty():
            raise CDLLException
        else:
            return self.sentinel.next.value

    def get_back(self) -> object:
        """
        This method does not take any parameters.  The method will first check to see if the list is empty and will
        raise an exception if this is true.  As long as the list is not empty, the method will return the last value
        in the list without altering it.
        """
        if self.is_empty():
            raise CDLLException
        else:
            return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        This method takes a value as a parameter.  The method walks through the link and compares each value with the
        value that was passed in.  If the current value in the list and the value that was passed in match, the method
        will remove that element and return True.  If the passed in value does not match any value in the list, the
        method will return False.
        """
        cur = self.sentinel.next
        prev = self.sentinel
        while cur.value != value and cur.next != self.sentinel:
            cur = cur.next
            prev = prev.next
        if cur.value == value:
            prev.next = cur.next
            cur.next.prev = prev
            return True
        else:
            return False

    def count(self, value: object) -> int:
        """
        This method takes a value as a parameter and walks through the list, keeping track of any values that match
        both the passed in value, and the current value in the list.  Once the entire list has been walked through, the
        method returns the count.
        """
        count = 0
        cur = self.sentinel.next
        while cur != self.sentinel:
            if cur.value == value:
                count += 1
            cur = cur.next

        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        This method takes two indexes as parameters.  The method checks to make sure that both of the indexes are valid.
        Once both indexes are determined valid, the method checks to see if index1 and index2 are the same.  If they
        are, it just returns because nothing will change within the list.  After this, the method will begin walking
        through the list to determine where both indexes end up.  The method will then swap nodes of index1 and index2
        by changing the nodes that are pointing to them/away from them.
        """
        # Make sure that you don't delete something before you need it
        if index1 < 0 or index2 < 0 or index1 > self.length()-1 or index2 > self.length()-1:
            raise CDLLException
        if index1 == index2:
            return
        cur1 = self.sentinel.next
        prev1 = self.sentinel
        cur2 = self.sentinel.next
        prev2 = self.sentinel
        cur_index = 0
        while cur_index != index1:
            cur1 = cur1.next
            prev1 = prev1.next
            cur_index += 1
        cur_index = 0
        while cur_index != index2:
            cur2 = cur2.next
            prev2 = prev2.next
            cur_index += 1
        if index1 == index2-1:
            temp = DLNode(0)
            prev1.next = cur2
            cur2.next.prev = cur1
            temp.next = cur1.next
            temp.prev = cur1.prev
            cur1.next = cur2.next
            cur2.prev = temp.prev
            cur2.next = cur1
            cur1.prev = cur2
        elif index1 == index2+1:
            temp = DLNode(0)
            prev2.next = cur1
            cur1.next.prev = cur2
            temp.next = cur2.next
            temp.prev = cur2.prev
            cur2.next = cur1.next
            cur1.prev = temp.prev
            cur1.next = cur2
            cur2.prev = cur1
        else:
            temp = DLNode(0)
            prev1.next = cur2
            prev2.next = cur1
            cur1.next.prev = cur2
            cur2.next.prev = cur1
            temp.next = cur1.next
            temp.prev = cur1.prev
            cur1.next = cur2.next
            cur1.prev = cur2.prev
            cur2.next = temp.next
            cur2.prev = temp.prev



    def reverse(self) -> None:
        """
        This method does not take any parameters.  The method creates a left index/right index which start from the
        beginning and end of the list.  The method will walk through half of the list and swap values
        corresponding to the right and left side of the list.
        """
        left_in = 0
        right_in = self.length()-1
        while left_in < (self.length()/2):
            self.swap_pairs(left_in, right_in)
            left_in += 1
            right_in -= 1


    def sort(self) -> None:
        """
        This method does not take any parameters.  The method uses a bubble sort to sort out the list (also using
        the previously made swap_pairs method).
        """
        for pass_num in range(self.length() - 1):
            left = self.sentinel.next
            for index in range(self.length() - 1 - pass_num):
                if left.value > left.next.value:
                    self.swap_pairs(index, index+1)
                else:
                    left = left.next


    def rotate(self, steps: int) -> None:
        """
        This method takes 'steps' as a parameter.  The method first checks to see if the list is empty and will just
        return if it is.  Following this, the method determines how many times it must 'rotate' itself to match the
        passed in parameter.  If the 'stp' is 0, that means that the list will not have to rotate at all so it can just
        return.  After this, the method determines left rotation vs right rotation and moves the sentinel to the correct
        position so parameters (rotation steps) are met.
        """
        if self.length() == 0:
            return
        stp = abs(steps) % self.length()
        if stp == 0:
            return
        if steps > 0:
            stp -= 1
            temp1 = self.sentinel.prev
            while stp > 0:
                stp -= 1
                temp1 = temp1.prev
            self.sentinel.next.prev = self.sentinel.prev
            self.sentinel.prev.next = self.sentinel.next
            temp1.prev.next = self.sentinel
            self.sentinel.prev = temp1.prev
            self.sentinel.next = temp1
            temp1.prev = self.sentinel
        else:
            temp1 = self.sentinel.next
            while stp > 0:
                stp -= 1
                temp1 = temp1.next
            self.sentinel.next.prev = self.sentinel.prev
            self.sentinel.prev.next = self.sentinel.next
            temp1.prev.next = self.sentinel
            self.sentinel.prev = temp1.prev
            self.sentinel.next = temp1
            temp1.prev = self.sentinel




    def remove_duplicates(self) -> None:
        """
        This method does not take any parameters.  The method walks through the list and determines if there are any
        duplicate values (assumed that the list is sorted).  If duplicate values are found, all traces of those values
        are removed from the list using the 'remove' method.
        """
        cur = self.sentinel.next
        while cur.next != self.sentinel:
            if cur.value == cur.next.value:
                val = cur.value
                while cur.value == cur.next.value:
                    cur = cur.next
                while self.count(val) != 0:
                    self.remove(val)
            else:
                cur = cur.next

    def odd_even(self) -> None:
        """
        This method does not take any parameters.  The method first determines if the list is empty or of length <2.
        If either of these are true, the method will just return because nothing needs to be changed.  If the list is
        larger than this, though, the method will move all odd indices to the front of the list, and all even indices
        to the back of the list.
        """
        cur = self.sentinel.next
        counter = int((self.length()/2))
        if self.is_empty() or (self.length() <= 2):
            return
        while counter > 0:
            odd = cur.next
            self.sentinel.prev.next = odd
            cur.next = odd.next
            odd.next.prev = cur
            odd.prev = self.sentinel.prev
            self.sentinel.prev = odd
            odd.next = self.sentinel
            cur = cur.next
            counter -= 1




if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    lst = CircularList()
    print(lst)
    lst.add_front('A')
    lst.add_front('B')
    lst.add_front('C')
    print(lst)
    #
    print('\n# add_back example 1')
    lst = CircularList()
    print(lst)
    lst.add_back('C')
    lst.add_back('B')
    lst.add_back('A')
    print(lst)
    #
    print('\n# insert_at_index example 1')
    lst = CircularList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))
    #
    print('\n# remove_front example 1')
    lst = CircularList([1, 2])
    print(lst)
    for i in range(3):
        try:
            lst.remove_front()
            print('Successful removal', lst)
        except Exception as e:
            print(type(e))
    #
    print('\n# remove_back example 1')
    lst = CircularList()
    try:
        lst.remove_back()
    except Exception as e:
        print(type(e))
    lst.add_front('Z')
    lst.remove_back()
    print(lst)
    lst.add_front('Y')
    lst.add_back('Z')
    lst.add_front('X')
    print(lst)
    lst.remove_back()
    print(lst)
    #
    print('\n# remove_at_index example 1')
    lst = CircularList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)
    #
    print('\n# get_front example 1')
    lst = CircularList(['A', 'B'])
    print(lst.get_front())
    print(lst.get_front())
    lst.remove_front()
    print(lst.get_front())
    lst.remove_back()
    try:
        print(lst.get_front())
    except Exception as e:
        print(type(e))
    #
    print('\n# get_back example 1')
    lst = CircularList([1, 2, 3])
    lst.add_back(4)
    print(lst.get_back())
    lst.remove_back()
    print(lst)
    print(lst.get_back())
    #
    print('\n# remove example 1')
    lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)
    #
    print('\n# count example 1')
    lst = CircularList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
    #
    print('\n# swap_pairs example 1')
    lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
                  (4, 2), (3, 3), (1, 2), (2, 1))
    #
    for i, j in test_cases:
        print('Swap nodes ', i, j, ' ', end='')
        try:
            lst.swap_pairs(i, j)
            print(lst)
        except Exception as e:
            print(type(e))
    #
    print('\n# reverse example 1')
    test_cases = (
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D']
    )
    for case in test_cases:
        lst = CircularList(case)
        lst.reverse()
        print(lst)
    #
    print('\n# reverse example 2')
    lst = CircularList()
    print(lst)
    lst.reverse()
    print(lst)
    lst.add_back(2)
    lst.add_back(3)
    lst.add_front(1)
    lst.reverse()
    print(lst)
    #
    print('\n# reverse example 3')

    #
    class Student:
        def __init__(self, name, age):
            self.name, self.age = name, age
    #
        def __eq__(self, other):
            return self.age == other.age
    #
        def __str__(self):
            return str(self.name) + ' ' + str(self.age)
    #
    #
    s1, s2 = Student('John', 20), Student('Andy', 20)
    lst = CircularList([s1, s2])
    print(lst)
    lst.reverse()
    print(lst)
    print(s1 == s2)
    #
    print('\n# reverse example 4')
    lst = CircularList([1, 'A'])
    lst.reverse()
    print(lst)
    #
    print('\n# sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        lst = CircularList(case)
        print(lst)
        lst.sort()
        print(lst)
    #
    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        lst = CircularList(source)
        lst.rotate(steps)
        print(lst, steps)
    #
    print('\n# rotate example 2')
    lst = CircularList([10, 20, 30, 40])
    for j in range(-1, 2, 2):
        for _ in range(3):
            lst.rotate(j)
            print(lst)
    #
    print('\n# rotate example 3')
    lst = CircularList()
    lst.rotate(10)
    print(lst)
    #
    print('\n# remove_duplicates example 1')
    test_cases = (
    [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
    [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
    [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],list("abccd"),list("005BCDDEEFI")
    )

    print(list("032hfsha"))
    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.remove_duplicates()
        print('OUTPUT:', lst)
    #
    print('\n# odd_even example 1')
    test_cases = (
    [1, 2, 3, 4, 5], list('ABCDE'),
    [], [100], [100, 200], [100, 200, 300],
    [100, 200, 300, 400],
    [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E'] )
    #
    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.odd_even()
        print('OUTPUT:', lst)
