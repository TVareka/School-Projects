# Course: CS261 - Data Structures
# Student Name: Ty Vareka
# Assignment: Assignment #4
# Description: This program creates a Stack class, a Queue class, a TreeNode class, and a BST class.  This program
# allows the user to create binary trees by using various methods.  It also has the ability to walk through the trees
# and provide the user with a Pre-Order, In-Order, and Post-Order traversal of those trees.  Specifications on what
# all of the individual methods can do are provided below.


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        This method takes a value as a parameter and adds that value to the tree.
        """
        if self.root is None:  # if the tree is empty, value becomes the root of the tree
            self.root = TreeNode(value)
        else:
            parent = None
            node = self.root
            while node is not None:  # Walks down the tree until node is None, making parent the node value attaches to
                parent = node
                if value < node.value:  # By definition of BST, if value is less than the current node value, will take
                    # the left path (.left)
                    node = node.left
                else:
                    node = node.right
            if value < parent.value:
                parent.left = TreeNode(value)
            else:
                parent.right = TreeNode(value)

    def contains(self, value: object) -> bool:
        """
        This method takes a value as a parameter and returns the bool value True if that value is within the tree and
        returns False if it is not within the tree.
        """
        if self.root is None:  # Important to first check to see if the tree is completely empty
            return False
        else:
            node = self.root
            while node is not None:  # Walks all the way down the tree and checking if value is equal to node.value
                if value == node.value:
                    return True
                elif value < node.value:
                    node = node.left
                else:
                    node = node.right
            return False  # If we haven't found the value by this point, the value is not within the tree, thus we must
        # return false

    def get_first(self) -> object:
        """
        This method does not take any parameters and tells the user what the first value in the tree is (root value)
        """
        if self.root is None:  # If the tree is empty, the first value will be None
            return None
        else:
            return self.root.value

    def remove_first(self) -> bool:
        """
        This method does not take any parameters.  It will return False only if the tree is empty, but will replace the
        first value (root) in the tree with its successor, then return True
        """
        if self.root is None:  # Checks to see if the tree is empty, so that it can return False
            return False
        elif self.root.right is None:  # If the root does not have a right node, we must use the .left node
            if self.root.left is not None:
                self.root = self.root.left
                return True
            else:  # If there is only the root in the tree, that root is removed and now the tree is empty
                self.root = None
                return True
        else:
            successor = None
            node = self.root.right
            count = 0
            parent = self.root.right
            while node is not None:  # Important to find the successor and how far it is from the root.right node
                successor = node
                node = node.left
                count += 1
            if count == 1:
                successor.left = self.root.left
                self.root = successor
                return True
            else:
                count -= 1
                while count != 1:  # Must find the parent of the successor so no nodes are lost, especially if
                    # successor.right is not None
                    parent = parent.left
                    count -= 1
                parent.left = successor.right
                successor.right = self.root.right
                successor.left = self.root.left
                self.root = successor
                return True

    def remove(self, value) -> bool:
        """
        This method takes a value as a parameter.  It then searches through the tree to see if that value is within the
        tree.  If it is, it replaces that value with its successor and removes itself.  If the value is found, the
        method will return True or else it will return False.
        """
        if self.root is None:  # Must check to see if the tree is empty
            return False
        elif self.root.value == value:  # If the value is equal to the root value, we can use the remove_first() function
            self.remove_first()
            return True
        else:
            node = self.root
            parent = None
            while node is not None and node.value != value:
                if value > node.value:
                    if node.right is not None:
                        if node.right.value == value:
                            parent = node
                    node = node.right
                else:
                    if node.left is not None:
                        if node.left.value == value:
                            parent = node
                    node = node.left
                if node is None:
                    return False
            # Now we are on the node that needs to be removed and we have the parent node
            if node.right is None:
                if node.value < parent.value:
                    parent.left = node.left
                else:
                    parent.right = node.left
                return True
            else:
                if node.value >= parent.value:
                    node_bigger = True
                else:
                    node_bigger = False
                successor = None
                node_two = node.right
                count = 0
                ps = node.right
                while node_two is not None:  # Using a very similar method to remove_first() function to replace the
                    # node with its successor
                    successor = node_two
                    node_two = node_two.left
                    count += 1
                if count == 1 and node_bigger:
                    parent.right = successor
                    successor.left = node.left
                    return True
                elif count == 1 and not node_bigger:
                    parent.left = successor
                    successor.left = node.left
                    return True
                else:
                    count -= 1
                    while count != 1:
                        ps = ps.left
                        count -= 1
                    ps.left = successor.right
                    successor.right = node.right
                    successor.left = node.left
                    if node_bigger:
                        parent.right = successor
                    else:
                        parent.left = successor
                    return True

    def pre_order_traversal(self, node=None, queue=None) -> Queue:
        """
        This is a recursive method that does not need to take any parameters.  The only time this function takes
        parameters is when it is recursively calling itself so that it can create a queue to return to the user.  This
        function will create a queue that starts at the root node and walks down the tree starting with the left
        subtree, then traversing through to the right subtree.
        """
        if queue is None:
            temp = Queue()
            self.pre_order_traversal(self.root, temp)
            return temp
        else:
            if node is not None:
                queue.enqueue(node.value)
                self.pre_order_traversal(node.left, queue)
                self.pre_order_traversal(node.right, queue)
        return queue

    def in_order_traversal(self, node=None, queue=None) -> Queue:
        """
        This is a recursive method that does not need to take any parameters.  The only time this function takes
        parameters is when it is recursively calling itself so that it can create a queu to return to the user.  This
        function will create a queue that traverses the left subtree, visits the root node, then traverses the right
        subtree.
        """
        if queue is None:
            temp = Queue()
            self.in_order_traversal(self.root, temp)
            return temp
        else:
            if node is not None:
                self.in_order_traversal(node.left, queue)
                queue.enqueue(node.value)
                self.in_order_traversal(node.right, queue)
        return queue

    def post_order_traversal(self, node=None, queue=None) -> Queue:
        """
        This is a recursive method that does not need to take any parameters.  The only time this function takes
        parameters is when it is recursively calling itself so that it can create a queu to return to the user.  This
        function will create a queue that traverses the left subtree, then the right subtree, and then finally the
        root node.
        """
        if queue is None:
            temp = Queue()
            self.post_order_traversal(self.root, temp)
            return temp
        else:
            if node is not None:
                self.post_order_traversal(node.left, queue)
                self.post_order_traversal(node.right, queue)
                queue.enqueue(node.value)
        return queue

    def by_level_traversal(self) -> Queue:
        """
        This method does not take any parameters.  This method creates a queue and a temporary queue that it uses to
        traverse through the tree by level.  When complete, the method will return a queue to the user that has the
        tree in order by level.
        """
        queue = Queue()
        temp = Queue()
        temp.enqueue(self.root)
        while not temp.is_empty():
            node = temp.dequeue()
            if node is not None:
                queue.enqueue(node.value)
                temp.enqueue(node.left)
                temp.enqueue(node.right)
        return queue

    def is_full(self, node=None, first=True) -> bool:
        """
        This method will not take any parameters when called by the user.  It will use a node and a variable that
        determines if it is the first time this method is being called, though, that is used for its recursive calls.
        This method will walk all the way down the tree and determine if the tree is full, meaning that all nodes have
        a left/right node except for the leaves of the tree.
        """
        if first is True:
            node = self.root
        if node is None or (node.right is None and node.left is None):  # Will return true if the tree is empty or if
            # the tree only consists of a root node.
            return True
        elif node.left is not None and node.right is not None:
            temp_one = self.is_full(node.left, False)
            temp_two = self.is_full(node.right, False)
            return temp_one and temp_two
        return False

    def is_complete(self) -> bool:
        """
        This method does not take any parameters, but returns True if the tree is 'complete' and False if the tree is
        not complete.  A complete tree is defined as a binary tree where all of the levels are filled except for
        possibly the lowest level.  This level is filled in the left subtree.
        """
        if self.root is None:
            return True
        queue = Queue()
        flag = False  # This is a check variable to make sure False is returned to the user if this flag is raise.
        #  This flag will only raise if the tree is not complete
        queue.enqueue(self.root)
        while not queue.is_empty():
            node = queue.dequeue()
            if node.left is not None:
                if flag == True:
                    return False
                queue.enqueue(node.left)
            else:
                flag = True

            if node.right is not None:
                if flag == True:
                    return False
                queue.enqueue(node.right)
            else:
                flag = True
        return True

    def count_node_leaves(self, node, count):
        """
        This method takes a node and a count as parameters.  It is used multiple times throughout this program to
        determine node count of the tree (count[0]) and the leaf count of the tree (count[1])
        """
        count[0] += 1
        if node.left is None and node.right is None:
            count[1] += 1
        if node.left is not None:
            self.count_node_leaves(node.left, count)
        if node.right is not None:
            self.count_node_leaves(node.right, count)

    def is_perfect(self) -> bool:
        """
        This method does not take any parameters.  This method works by determining the tree's node count, leaf count,
        and height.  It then uses the equation that was provided in the lecture to determine if the tree is perfect.
        If the tree is perfect, it will return True or else it will return False
        """
        if self.root is None or (self.root.left is None and self.root.right is None):
            # If the tree is empty or only consists of a root node, then the method returns a True value
            return True
        count = [0, 0]
        node = self.root
        self.count_node_leaves(node, count)
        height = self.height()
        if (2 ** height == count[1]) and ((2 ** (height + 1) - 1) == count[0]):
            return True
        else:
            return False

    def size(self) -> int:
        """
        This method does not take any parameters.  It uses the previously made count_node_leaves method to determine
        the total node count.  It then returns that node count to the user.
        """
        if self.root is None:
            return 0
        node = self.root
        count = [0, 0]
        self.count_node_leaves(node, count)
        return count[0]

    def check_height(self, node, count):
        """
        This method takes a node and count as parameters. This method essentially walks down the tree keeping track
        of how 'deep' into the tree it is (with count[0]), and recursively calling itself. It also checks to see if the
        current depth is larger than the largest depth (count[1]).  If it is larger, it sets the current depth equal to
        the largest depth.
        """
        if node.left is not None:
            count[0] += 1
            if count[0] > count[1]:
                count[1] = count[0]
            self.check_height(node.left, count)

        if node.right is not None:
            count[0] += 1
            if count[0] > count[1]:
                count[1] = count[0]
            self.check_height(node.right, count)

        count[0] -= 1

    def height(self) -> int:
        """
        This method does not take any parameters.  It uses the check_height method to determine the total height of the
        tree and returns that value to the user.
        """
        if self.root is None:  # If the tree is empty it returns a value of -1
            return -1
        if self.root.right is None and self.root.left is None:  # If the tree only consists of a root node, it will
            # return a value of 0
            return 0
        count = [0, 0]
        node = self.root
        self.check_height(node, count)
        return count[1]

    def count_leaves(self) -> int:
        """
        This method does not take any parameters.  This method also uses the count_node_leaves method to determine
        how many leaves are in the tree.  It then returns that value.
        """
        if self.root is None:  # If the tree is empty, the overall leaves are 0 and thus, returns that value
            return 0

        count = [0, 0]
        node = self.root
        self.count_node_leaves(node, count)
        return count[1]

    def count_unique(self) -> int:
        """
        This method does not take any parameters.  It uses two separate queues to determine the amount of unique values
        within the tree.  Each time the outside 'while' function runs, the count increases.  Once queue_one (which
        keeps track of all the values in the original tree) is empty, it returns the count variable.
        """
        if self.root is None:
            return 0

        queue_one = self.post_order_traversal()
        queue_two = Queue()
        count = 0
        while not queue_one.is_empty():
            count += 1
            value = queue_one.dequeue()
            while not queue_one.is_empty():
                value_two = queue_one.dequeue()
                if value_two != value:
                    queue_two.enqueue(value_two)
            while not queue_two.is_empty():
                queue_one.enqueue(queue_two.dequeue())
        return count

    # BASIC TESTING - PDF EXAMPLES


if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

    """remove_first() ty example 1"""
    print("\nPDF - method remove_first() TY example 1")
    print("-------------------------------------")
    tree = BST([10, 5])
    print(tree.remove_first())
    print(tree)
    # Success

    """remove_first() ty example 1"""
    print("\nPDF - method remove_first() TY example 2")
    print("-------------------------------------")
    tree = BST([10])
    print(tree.remove_first())
    print(tree)
    # Success

    """remove_first() ty example 3"""
    print("\nPDF - method remove_first() TY example 3")
    print("-------------------------------------")
    tree = BST([10])
    tree.add(5)
    tree.add(7)
    print(tree.remove_first())
    print(tree)
    print(tree.remove_first())
    print(tree)
    # Success

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)
    print(tree.root.value)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)
    print(tree.root.value)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree, tree.root.value)
    print(tree.remove_first(), tree, tree.root.value)
    print(tree.remove_first(), tree, tree.root.value)
    print(tree.remove_first(), tree, tree.root.value)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')
