# Course: CS261 - Data Structures
# Student Name: Ty Vareka
# Assignment: 3: Queue from Stacks
# Description: This program uses resources from the max_stack_sll program that was previously written.  The program
# creates a queue, though, rather than a stack.  This means that instead of 'first on last off' like a stack, the
# queue uses 'first on first off' much like a line of people.  The class creates a main storage and temp storage.
# The two methods that were created for this class are enqueue and dequeue.  Greater details for both methods can be
# found below.


from max_stack_sll import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new Queue based on two stacks
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.s1 = MaxStack()  # use as main storage
        self.s2 = MaxStack()  # use as temp storage

    def __str__(self) -> str:
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def is_empty(self) -> bool:
        """
        Return True if queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.size()

    # ------------------------------------------------------------------ #

    def enqueue(self, value: object) -> None:
        """
        This method takes a value as a parameter.  The method then uses the .push method from the 'max stack' program
        to add a value to the list.
        """
        self.s1.push(value)

    def dequeue(self) -> object:
        """
        This method does not take any parameters.  The method first checks to see if the queue is empty and raises an
        exception if it is.  As long as the queue is not empty, the method will try walking through the entire queue
        and push those values onto the temp queue that was created at the beginning of the class. Once an exception is
        raised, we know that original list is depleted.  The method keeps track of the value that is on top of the
        temp queue by popping it off.  The rest of the original queue is placed back into the main queue and the saved
        popped value is returned. 
        """
        if self.is_empty():
            raise QueueException
        else:
            try:
                while 1:
                    temp = self.s1.pop()
                    self.s2.push(temp)
            except Exception as e:
                temp = temp
            rtn = self.s2.pop()
            try:
                while 1:
                    temp = self.s2.pop()
                    self.s1.push(temp)
            except Exception as e:
                temp = temp
            return rtn



# BASIC TESTING
if __name__ == "__main__":
    pass

    print('\n# enqueue example 1')
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    #
    print('\n# dequeue example 1')
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue(), q)
        except Exception as e:
            print("No elements in queue", type(e))



