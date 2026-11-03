class Graph:
    def __init__(self):
        self.adjacency = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    def addEdge(self, from_vertex, to_vertex):
        if from_vertex not in self.adjacency or to_vertex not in self.adjacency:
            return False
        if to_vertex not in self.adjacency[from_vertex]:
            self.adjacency[from_vertex].append(to_vertex)
        return True

    def listIncomingAdjacentVertex(self, vertex):
        if vertex not in self.adjacency:            # if vertex is not in the graph
            return []                               # return empty list
        
        incoming = []                              # vertices with an edge into 'vertex'
        for other in self.adjacency:
            if vertex in self.adjacency[other]:    # does 'other' point to 'vertex'? 
                incoming.append(other)

        return incoming

    def listOutgoingAdjacentVertex(self, vertex):
        if vertex not in self.adjacency:
            return []
        return list(self.adjacency[vertex])     # a copy, so callers can't change the graph by accident

    def removeEdge(self, from_vertex, to_vertex):
        if from_vertex in self.adjacency and to_vertex in self.adjacency[from_vertex]:
            self.adjacency[from_vertex].remove(to_vertex)
            return True
        return False

    def hasPath(self, start, end):
        if start not in self.adjacency or end not in self.adjacency:
            return False

        stack = [start]
        visited = set()

        while stack:
            current = stack.pop()
            if current == end:
                return True
            if current not in visited:
                visited.add(current)
                stack.extend(self.adjacency[current])

        return False
    
if __name__ == "__main__":
    graph = Graph()
    graph.addVertex("MTH110")
    graph.addVertex("PRG210")
    graph.addVertex("AIN310")
    graph.addVertex("DSC320")

    print(graph.addEdge("MTH110", "PRG210"))
    print(graph.addEdge("PRG210", "AIN310"))
    print(graph.addEdge("PRG210", "DSC320"))
    print(graph.addEdge("MTH110", "XYZ999"))   # XYZ999 doesn't exist

    print("Into AIN310:", graph.listIncomingAdjacentVertex("AIN310"))
    print("Into MTH110:", graph.listIncomingAdjacentVertex("MTH110"))
    print("Out of PRG210:", graph.listOutgoingAdjacentVertex("PRG210"))

    graph.addVertex("MTH110")                  # added again: is PRG210 still there?
    print(graph.adjacency)