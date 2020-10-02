class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge:
    def __init__(self, edge_val, node_from, node_to):
        self.value = edge_val
        self.node_from = node_from
        self.node_to = node_to

class Graph:
    def __init__(self, edges = [], nodes = []):
        self.edges = edges
        self.nodes = nodes

    def insert_node(self, new_node_val):
        new_node_val = Node(new_node_val)
        self.nodes.append(new_node_val)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None

        for node in self.nodes:
            if node.value == node_from_val:
                from_found = node

            if node.value == node_to_val:
                to_found = node

        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)

        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)

        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def edge_list(self):
        arr = []
        for edge in self.edges:
            arr.append(edge.value)

        return arr

    def get_nodes(self):
        arr = []
        for node in self.nodes:
            arr.append(node.value)

        return arr

    def find_max_node_val(self):
        max_index = -1
        for node in self.nodes:
            if node.value > max_index:
                max_index = node.value

        return max_index

    def adjacency_list(self):
        max_node_val = self.find_max_node_val()
        adjacency_list = [None] * (max_node_val + 1)

        for edge in self.edges:
            if adjacency_list[edge.node_from.value]:
                adjacency_list[edge.node_from.value].append((edge.node_to.value, edge.value))
            else:
                adjacency_list[edge.node_from.value] = [(edge.node_to.value, edge.value)]

        return adjacency_list

    def clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def check_node(self, start_node):
        for node in self.nodes:
            if node.value == start_node:
                start_node = node

        return start_node

    def bfs(self, start_node):
        self.clear_visited()
        start_node = self.check_node(start_node)
        start_node.visited = True

        queue = []
        arr = []
        queue.append(start_node)

        while queue:
            popped = queue.pop(0)
            arr.append(popped.value)

            for neighbour in popped.edges:
                if not neighbour.node_to.visited:
                    neighbour.node_to.visited = True
                    queue.append(neighbour.node_to)

        return arr
        



graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(102, 2, 5)
graph.insert_edge(100, 2, 6)
graph.insert_edge(100, 5, 9)
graph.insert_edge(100, 5, 10)
graph.insert_edge(100, 4, 7)
graph.insert_edge(100, 4, 8)
graph.insert_edge(100, 7, 11)
graph.insert_edge(100, 7, 12)

print(graph.get_nodes())
print(graph.edge_list())
print(graph.adjacency_list())
print(graph.bfs(1))
