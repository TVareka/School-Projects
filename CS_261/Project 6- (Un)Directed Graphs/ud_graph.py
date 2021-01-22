# Course: CS 261: Data Structures
# Author: Ty Vareka
# Assignment: 6
# Description: This program implements an undirected graph for the user.  The user will be allowed to add vertices,
# edges, get all vertices/edges, etc.  All methods for this program are described in detail below.


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        This method takes a string as a parameter.  It checks to see if the string that was passed in already exists.
        If it does exist, the method does nothing, or else it adds the vertices to the graph.
        """
        for key in self.adj_list:
            if key == v:
                return
        self.adj_list[v] = []

    def add_edge(self, u: str, v: str) -> None:
        """
        This method takes two strings as parameters.  The method first checks to make sure the two strings are not
        identical and returns if they are.  The method then adds the two vertices to the graph and adds their edges
        to each other.
        """
        if u == v:
            return
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def remove_edge(self, v: str, u: str) -> None:
        """
        This method takes two strings as parameters.  The method checks to see if the edges exist and removes them if
        they do exist.
        """
        if v in self.adj_list.keys() and u in self.adj_list[v]:
            self.adj_list[v].remove(u)
        if u in self.adj_list.keys() and v in self.adj_list[u]:
            self.adj_list[u].remove(v)

    def remove_vertex(self, v: str) -> None:
        """
        This method takes a string vertex as a parameter.  The method first deletes that vertex from the graph and then
        walks through each vertex and deletes any edge that previously pointed to that vertex.
        """
        if v in self.adj_list.keys():
            del self.adj_list[v]
            for key, i in self.adj_list.items():
                if v in i:
                    self.adj_list[key].remove(v)

    def get_vertices(self) -> []:
        """
        This method returns a list of vertices in the graph.
        """
        key_list = []
        for key in self.adj_list:
            key_list.append(key)
        return key_list

    def get_edges(self) -> []:
        """
        This method does not take any parameters.  It creates a list of tuples that consist of a vertex and an edge so
        all edges are accounted for.  The method also checks existing edge list to see if that tuple pair exists already,
        and if it does, it does not add it again to the list.  The method then returns this list to the user.
        """
        edge_list = []
        for key in self.adj_list:
            for i in self.adj_list[key]:
                t_list = tuple([key, i])
                if not edge_list:
                    edge_list.append(t_list)
                else:
                    flag = False
                    for t in edge_list:
                        if sorted(t_list) == sorted(t):
                            flag = True
                    if flag is False:
                        edge_list.append(t_list)
        return edge_list

    def is_valid_path(self, path: []) -> bool:
        """
        This method takes a path list as a parameter.  The method first checks to see if the list is empty and returns
        true if it is empty.  The method then walks through the list and compares it to the get_edges list.  If the
        method walks through the list and those values match up with the tuples created in the get_edge list, the method
        will return true.  Otherwise, the method will return false because the path does not exist within the graph.
        """
        if not path:
            return True
        index = 0
        length = 0
        for i in path:
            length += 1
        vertices = self.get_vertices()
        v_edge = self.get_edges()
        for i in path:
            flag = False
            if i not in vertices:
                return False
            if index == (length - 1):
                return True
            step = tuple([path[index], path[index + 1]])
            for tup in v_edge:
                if sorted(step) == sorted(tup):
                    flag = True
            if flag is False:
                return False
            index += 1

    def dfs(self, v_start, v_end=None) -> []:
        """
        This method takes a start vertex and an end vertex as parameters. The method first checks to make sure the
        start vertex and end vertex are valid.  The method then utilizes a depth-first search to walk from the starting
        vertex to the ending vertex.  If the ending vertex does not exist, the method walks as far as it can throughout
        the graph.  The method creates a list of the path it takes and returns it to the user.
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
            for i in self.adj_list[vertex]:
                successors.append(i)
            successors.sort(reverse=True)
            if vertex not in reachable:
                reachable.append(vertex)
                for i in successors:
                    stack.append(i)
        return reachable

    def bfs(self, v_start, v_end=None) -> []:
        """
        This method takes a start vertex and an end vertex as parameters. The method first checks to make sure the
        start vertex and end vertex are valid.  The method then utilizes a breadth-first search to walk from the starting
        vertex to the ending vertex.  If the ending vertex does not exist, the method walks as far as it can throughout
        the graph.  The method creates a list of the path it takes and returns it to the user.  This uses very similar
        implementation to dfs, except it uses a queue instead of a stack to pop things off.
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
            for i in self.adj_list[vertex]:
                successors.append(i)
            successors.sort()
            if vertex not in reachable:
                reachable.append(vertex)
                for i in successors:
                    stack.append(i)
        return reachable

    def count_connected_components(self):
        """
        This method creates a list of the vertices and then uses a dfs to walk the graph from position vertices[0].  The
        list of vertices and the dfs are compared, removing any values that match.  The process is then repeated,
        incrementing count, so the user knows how many connected components make up the graph.  That count is returned
        to the user.
        """
        vertices = self.get_vertices()
        count = 0
        while len(vertices) != 0:
            count += 1
            reachable = self.dfs(vertices[0])
            for i in reachable:
                if i in vertices:
                    vertices.remove(i)
        return count

    def cyclic(self, start):
        """
        This method takes a starting vertex as a parameter and walks the graph utilizing a similar method as the bfs.
        This method, though, checks to see if the vertex is already in reachable, thus meaning the graph is cyclic.  The
        method returns true if the graph is cyclic and false if it is not cyclic.
        """
        reachable = []
        stack = [start]
        while len(stack) != 0:
            successors = []
            vertex = stack.pop(0)
            for i in self.adj_list[vertex]:
                successors.append(i)
            if vertex not in reachable:
                reachable.append(vertex)
                for i in successors:
                    if i not in reachable:
                        stack.append(i)
            else:
                return True
        return False

    def has_cycle(self):
        """
        This method creates a list of vertices and uses the cyclic method to see if a cycle can be found starting from
        vertices[0].  If it cannot, it removes any common vertices between the vertices list and a dfs.  The method
        then repeats, once again calling the cyclic function.  If a cycle is found, the method returns True and returns
        False if not.
        """
        vertices = self.get_vertices()
        while len(vertices) != 0:
            start = vertices[0]
            if self.cyclic(start):
                return True
            reachable = self.dfs(vertices[0])
            for i in reachable:
                if i in vertices:
                    vertices.remove(i)
        return False


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)

    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'B')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)

    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')

    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))

    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')

    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()

    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
