# Course: CS261 - Data Structures
# Assignment: 5
# Student: Tyler Vareka
# Description: This program allows the user to create and manipulate Min Heaps.  This program allows the user
# to add values to the heap, get the minimum value, remove the minimum value, etc.  All of the methods are defined
# below.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def find_parent(self, index):
        """
        This method takes an index as a parameter.  This method uses that index to do the calculations needed to find
        the parent's index.  The method then returns that parent index.
        """
        if index == 0:
            return None
        parent_index = int((index-1)/2)
        return parent_index

    def find_Lchild(self, index):
        """
        This method takes an index as a parameter.  This method uses that index to do the calculations needed to find
        the left child's index.  It then returns that child's index.
        """
        leftC_index = 2*index + 1
        return leftC_index

    def find_Rchild(self, index):
        """
        This method takes an index as a parameter.  This method uses that index to do the calculations needed to find
        the right child's index.  It then returns that child's index.
        """
        rightC_index = 2*index + 2
        return rightC_index

    def find_sNode(self, index):
        """
        This method takes an index as a parameter.  It finds that node's left and right child.  If there aren't any
        children, the method sets the variable 'smaller_child' to None.  If there are children, it determines which of
        the two is smaller, sets smaller_child equal to that child's index. It then returns 'smaller_child'.
        """
        smaller_child = None
        leftC = self.find_Lchild(index)
        rightC = self.find_Rchild(index)
        if leftC + 1 > self.heap.length() and rightC + 1 > self.heap.length():
            smaller_child = None
        elif rightC + 1 > self.heap.length():
            smaller_child = leftC
        elif self.heap.get_at_index(leftC) > self.heap.get_at_index(rightC):
            smaller_child = rightC
        elif self.heap.get_at_index(leftC) <= self.heap.get_at_index(rightC):
            smaller_child = leftC
        return smaller_child

    def perc_down(self, leaf_node):
        """
        This method takes a node index as a parameter.  It uses the previously defined methods to determine the smaller
        child.  If the variable smaller is None, then the method immediately returns.  This method then allows the node
        to percolate down the tree (as long as it is bigger than its smaller child) as far as it needs to go, by
        calling itself recursively.
        """
        smaller = self.find_sNode(leaf_node)
        if smaller is None:
            return
        elif self.heap.get_at_index(leaf_node) > self.heap.get_at_index(smaller):
            self.heap.swap(leaf_node, smaller)
            self.perc_down(smaller)

    def add(self, node: object) -> None:
        """
        This method takes a node as a parameter.  It first checks to see if the heap is empty and if it is, immediately
        appends that node to the heap.  If the heap is not empty, it determines index at which the node will be placed
        by using the heap's length.  It also determines the parent of the node that will be added.  The node is then
        added and allowed to percolate up the tree to its correct position.
        """
        if self.is_empty():
            self.heap.append(node)
        else:
            next_pos = self.heap.length()
            parent_index = self.find_parent(next_pos)
            self.heap.append(node)
            while parent_index is not None and node < self.heap.get_at_index(parent_index):
                self.heap.swap(next_pos, parent_index)
                next_pos = parent_index
                parent_index = self.find_parent(next_pos)


    def get_min(self) -> object:
        """
        This method does not take any parameters.  The method first checks to see if the heap is empty.  If it is
        it raises the MinHeapException.  If the heap is not empty, though, it returns the node at index 0, because this
        will always be the smallest value.
        """
        if self.is_empty():
            raise MinHeapException
        else:
            return self.heap.get_at_index(0)


    def remove_min(self) -> object:
        """
        This method does not take any parameters.  The method first checks to see if the heap is empty and raises an
        exception if it is.  The method determines the last position filled, saves the minimum value to the variable
        'rtn' and then swaps the first value with the last value that was added.  The last value is then popped off and
        the perc_down function is called to allow the heap to correct itself and reposition everything correctly.
        """
        if self.is_empty():
            raise MinHeapException
        else:
            last_pos = self.heap.length()-1
            rtn = self.get_min()
            if self.heap.length() == 1:
                self.heap.pop()
            else:
                self.heap.swap(last_pos, 0)
                self.heap.pop()
                node_index = 0
                self.perc_down(node_index)

            return rtn

    def build_heap(self, da: DynamicArray) -> None:
        """
        This method takes a dynamic array as a parameter.  The heap is then cleared and the values from the passed in
        dynamic array are appending to the current heap.  If the length is less than two, the method returns.  If the
        array length is longer, the method determines the leaf node which is the parent of the last filled position. The
        method calls the perc_down function.  Following that, the leaf node is decremented by one and the perc_down
        function is called continuously until leaf node is not greater than 0.
        """
        self.heap = DynamicArray()
        for node in da:
            self.heap.append(node)
        if self.heap.length() < 2:
            return

        leaf_node = self.find_parent(self.heap.length()-1)
        self.perc_down(leaf_node)
        while leaf_node > 0:
            leaf_node = leaf_node-1
            self.perc_down(leaf_node)


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
