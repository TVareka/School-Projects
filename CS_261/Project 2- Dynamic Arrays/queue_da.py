# Course: CS261 - Data Structures
# Student Name: Tyler Vareka
# Assignment: #2: Queue
# Description: This program uses the previously made dynamic array program to create a Queue.  This queue has the
# ability to determine if it is empty, add elements, and remove the first element in the queue.
# Last revised: 10/23/2020

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self):
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    def enqueue(self, value: object) -> None:
        """
        This method uses the append method from dynamic array to add 'value' to the queue.
        """
        self.da.append(value)

    def dequeue(self) -> object:
        """
        This method first checks to see if the queue is empty.  If it is, it raises the Queue Exception.  If it is not
        empty, though, it will make a copy of the very first element of the queue (save it to the variable 'value').
        After this, it uses the dynamic array's method 'remove_at_index' to remove the first element of the queue.  Then
        the method returns 'value'.
        """
        if self.is_empty():
            raise QueueException
        value = self.da.get_at_index(0)
        self.da.remove_at_index(0)
        return value





# BASIC TESTING
if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
