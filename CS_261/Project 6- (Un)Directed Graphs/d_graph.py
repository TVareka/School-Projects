# Course: CS 261: Data Structures
# Author: Ty Vareka
# Assignment: 6
# Description: This program implements a directed weighted graph for the user.  The directed graph utilizes a matrix
# instead of a adj_list like the undirected graph program.  This program has all of the functionality of the previous
# undirected graph except it also adds the dijkstra's method as well.


class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        This method helps create the matrix this graph relies on to be accurate.  The method also increments the
        self.v_count each time adds a new vertex.
        """
        if self.v_count == 0:
            self.v_count += 1
            self.adj_matrix = [[0]]
            return self.v_count
        else:
            lst = [0 for i in range(self.v_count)]
            self.adj_matrix.append(lst)
            for i in self.adj_matrix:
                i.append(0)
            self.v_count += 1
            return self.v_count


        

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        This method takes a source, a destination and a weight as parameters.  The method first checks to see if the
        src and dst are the sam and if the weight is less than 1.  If either of those are true, the method returns
        immediately.  The method then makes sure that the src and dst passed in are valid and returns if they are not.
        The method finally adds that edge to the matrix once it has passed the previous tests.
        """
        if src == dst or weight < 1:
            return
        if src >= self.v_count or dst >= self.v_count or src < 0 or dst < 0:
            return
        self.adj_matrix[src][dst] = weight
        
    def remove_edge(self, src: int, dst: int) -> None:
        """
        This method checks the validity of src and dst as well as making sure they are not equal and returns if any
        of those are not true. The method then changes the edge at that position to 0 to essentially remove the edge
        from the graph.
        """
        if src >= self.v_count or dst >= self.v_count or src < 0 or dst < 0 or src == dst:
            return
        self.adj_matrix[src][dst] = 0
        

    def get_vertices(self) -> []:
        """
        This method returns a list of the vertices from the graph.  These vertices, though, are essentially a list of
        numbers that increment up to self.v_count.
        """
        lst = [i for i in range(self.v_count)]
        return lst

    def get_edges(self) -> []:
        """
        This method creates a list of tuples that consist of two vertices and the weight between them  The method does
        this by walking through the matrix and checking to see if the value is greater than 0.  If it is, it means that
        there is a weight, meaning there is a connection between those two vertices.
        """
        lst = []
        for i in range(self.v_count):
            for j in range(self.v_count):
                if self.adj_matrix[i][j] > 0:
                    tup = (i, j, self.adj_matrix[i][j])
                    lst.append(tup)
        return lst


    def is_valid_path(self, path: []) -> bool:
        """
        This method takes a path list as a parameter.  The method returns true if the list is empty or if the list
        has one value that is less than self.v_count.  The method then walks through the path list, checking to see
        if the values are valid and then making sure the edges at that position are not 0.  If the method can walk
        through the path list successfully, it will return True, or else it will return False.
        """
        index = 0
        if len(path) == 0:
            return True
        if len(path) == 1:
            if 0 <= path[index] < self.v_count:
                return True
            else:
                return False
        while index < len(path)-1:
            if 0 <= path[index] < self.v_count and 0 <= path[index+1] < self.v_count:
                if self.adj_matrix[path[index]][path[index+1]] == 0:
                    return False
                index += 1
            else:
                return False
        return True



    def dfs(self, v_start, v_end=None) -> []:
        """
        This method takes a start vertex and an end vertex as parameters.  The method checks to see if the start and
        end vertex are valid.  If the start is not valid, it will return immediately.  The method then utilizes a dfs
        implementation to walk through the graph and create a list as it walks.  The method then returns that list
        to the user.
        """
        reachable = []
        vertices = self.get_vertices()
        if v_start not in vertices:
            return reachable
        if v_end not in vertices:
            v_end = None
        stack = [v_start]
        while len(stack) != 0:
            successors = []
            vertex = stack.pop()
            if v_end is not None and vertex == v_end:
                reachable.append(vertex)
                return reachable
            count = 0
            for i in self.adj_matrix[vertex]:
                if i > 0:
                    successors.append(count)
                count += 1
            successors.sort(reverse=True)
            if vertex not in reachable:
                reachable.append(vertex)
                for i in successors:
                    stack.append(i)
        return reachable

    def bfs(self, v_start, v_end=None) -> []:
        """
        This method takes a start vertex and an end vertex as parameters.  The method checks to see if the start and
        end vertex are valid.  If the start is not valid, it will return immediately.  The method then utilizes a bfs
        implementation to walk through the graph and create a list as it walks.  The method then returns that list
        to the user.
        """
        reachable = []
        vertices = self.get_vertices()
        if v_start not in vertices:
            return reachable
        if v_end not in vertices:
            v_end = None
        stack = [v_start]
        while len(stack) != 0:
            successors = []
            vertex = stack.pop(0)
            if v_end is not None and vertex == v_end:
                reachable.append(vertex)
                return reachable
            count = 0
            for i in self.adj_matrix[vertex]:
                if i > 0:
                    successors.append(count)
                count += 1
            successors.sort()
            if vertex not in reachable:
                reachable.append(vertex)
                for i in successors:
                    stack.append(i)
        return reachable

    def cyclic(self, node, visited, explored):
        """
        This method takes a node, a visted list and a explored list as parameters.  This method recursively calls itself
        to essentially walk as far as it can on the initial path.  The method keeps track of its current path by marking
        explored[node] true while it is walking a path.  It then marks visited[node] true if that path has exhausted
        all of its options without finding a cyclic path.  If the method runs into a situation where explored[node] is
        true, it returns true because that path must be cyclic.  If it walks through everything without that happening,
        it returns false.
        """
        if visited[node]:
            return False
        if explored[node]:
            return True
        explored[node] = True
        neighbors = []
        count = 0
        for i in self.adj_matrix[node]:
            if i > 0:
                neighbors.append(count)
            count += 1
        for i in neighbors:
            if not visited[i]:
                rtn = self.cyclic(i, visited, explored)
                if rtn is True:
                    return True
        explored[node] = False
        visited[node] = True
        return False

    def has_cycle(self):
        """
        This method creates a list of vertices and two lists of false values (visited/explored).  The method then
        walks through the vertices and calls the cyclic function to see if the path is cyclic.  If visited[i] is true,
        it means the cyclic function has already walked that path, thus it can ignore it.  If cyclic returns true, the
        method can return true because it found a cycle.  If not, it moves onto the next value that is not true for
        visited[i].  If it walks through all the vertices, it returns false.
        """
        vertices = self.get_vertices()
        visited = [False for i in vertices]
        explored = [False for i in vertices]
        for i in vertices:
            if not visited[i]:
                rtn = self.cyclic(i, visited, explored)
                if rtn is True:
                    return True
        return False


    def dijkstra(self, src: int) -> []:
        """
        This method takes a source as its parameter.  The method first creates a list of values initialized to 'inf'
        and a list of False values.  The method sets the distance[src] to 0 since it is the value we will start with.
        The method then starts an infinite while loop where it essentially checks the distances from one value to the
        next.  It keeps track of the shortest distances as it walks through the graph and keeps them in the distance
        list.  The method then returns the distance list back to the user.
        """
        distance = [float('inf') for i in range(self.v_count)]
        visited = [False for i in range(self.v_count)]
        distance[src] = 0
        while True:
            short = float('inf')
            short_i = -1
            for i in range(self.v_count):
                if distance[i] < short and not visited[i]:
                    short = distance[i]
                    short_i = i
            if short_i == -1:
                return distance
            for i in range(self.v_count):
                if self.adj_matrix[short_i][i] != 0 and distance[i] > distance[short_i] + self.adj_matrix[short_i][i]:
                    distance[i] = distance[short_i] + self.adj_matrix[short_i][i]
            visited[short_i] = True




if __name__ == '__main__':
    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
