# Author: Ty Vareka
# Date: 5/11/2020
# Description: Created the class Node and the class LinkedList.  This program allows the user to create a list by
# adding, removing, reversing, inserting, etc. different elements to the list.

class Node:
    '''Class for node that takes a val as a parameter'''

    def __init__(self, data):
        '''Initializes the class Node'''
        self.data = data
        self.next = None


class LinkedList:
    '''Class for LinkedList'''

    def __init__(self):
        '''Initializes the LinkedList class'''
        self._head = None

    def add(self, val):
        '''Method that takes a val as a parameter and calls on another recursive add method to add that val into the
         LinkedList'''
        if self._head is None:
            self._head = Node(val)
        else:
            self.rec_add(self._head, val)

    def rec_add(self, current, val):
        '''Recursive add method that adds a val to the end of the list.  If it's not the end of a list, it
        recursively calls itself again'''
        if current.next is not None:
            self.rec_add(current.next, val)
        else:
            current.next = Node(val)

    def remove(self, val):
        '''Method that will remove a val from a LinkedList'''
        if self._head is None:
            return
        if self._head.data == val:
            self._head = self._head.next
        else:
            self.rec_remove(self._head.next, val, self._head)

    def rec_remove(self, current, val, prev):
        '''Recursive remove method that checks to see if the val is in the list and removes it if it is'''
        if current is not None and current.data != val:
            self.rec_remove(current.next, val, current)
        else:
            if current is not None:
                prev.next = current.next

    def contains(self, key):
        '''Method that takes a key as a parameter and checks to see if the key is in the LinkedList'''
        if self._head is None:
            return False
        return self.rec_contains(self._head, key)

    def rec_contains(self, current, key):
        '''Recursive contains method that recursively calls itself to check to see if the key is in the LinkedList'''
        if current is not None:
            if current.data == key:
                return True
            return self.rec_contains(current.next, key)
        return False

    def insert(self, val, pos):
        '''Method that will take a val and position as a parameter.  It then plugs in the val at the designated
        position if possible'''
        if pos == 0:
            temp = self._head
            self._head = Node(val)
            self._head.next = temp
        else:
            self.rec_insert(self._head, pos - 1, val)

    def rec_insert(self, current, pos, val):
        '''Recursive insert method that recursively checks the LinkedList to find out where the position is within
        the list.  It then will plug in that val to the list at that position.  If the position is larger than the
        length of the list, it will plug in that val at the end of the list'''
        if current.next is None:
            current.next = Node(val)
            return
        if pos != 0:
            self.rec_insert(current.next, pos - 1, val)
        else:
            temp = current.next
            current.next = Node(val)
            current.next.next = temp

    def reverse(self):
        '''Method that takes no parameters and reverses the list by calling the recursive reverse function'''
        if self._head is None or self._head.next is None:
            return
        following = self._head.next
        self._head.next = None
        self.rec_reverse(following, self._head)

    def rec_reverse(self, current, prev):
        '''Recursive reverse function that recursively calls itself and helps reverse the order of the LinkedList'''
        if current is not None:
            following = current.next
            current.next = prev
            prev = current
            current = following
            self.rec_reverse(current, prev)
        else:
            self._head = prev

    def to_regular_list(self):
        '''Method that creates a list and the calls the recursive version of itself to add elements from the LinkedList
        to the list that was created.  It then returns that list once finished'''
        result = []
        return self.rec_to_regular_list(self._head, result)

    def rec_to_regular_list(self, current, result):
        '''Recursive method that recursively calls itself and adds all elements of the list.  Once it is finished it
        returns that finished list all the way back through the recursive calls'''

        if current is not None:
            newResult = result + [current.data]
            return self.rec_to_regular_list(current.next, newResult)
        else:
            return result

    def display(self):
        '''Simple display function that displays elements of the LinkedList'''
        self.rec_display(self._head)

    def rec_display(self, a_node):
        '''Recursive display function that recursively calls itself to display all elements of the LinkedList'''
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)


def main():
    '''testing the program with simple parameters'''
    list = LinkedList()
    list.add(5)
    list.add(10)
    list.add(30)
    list.remove(10)
    list.display()
    print('\n')
    list.insert(11, 1)
    list.display()
    print('\n')
    list.insert(54, 0)
    list.display()
    print('\n')
    list.insert(65, 493)
    list.display()
    print('\n')
    list.remove(8)
    list.display()
    print('\n')
    list.remove(54)
    list.remove(65)
    list.display()
    print('\n')
    list.reverse()
    list.display()
    print('\n')
    print(list.contains(11))
    print('\n')
    print(list.contains(52))
    print(list.to_regular_list())


if __name__ == "__main__":
    main()
