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
        incoming = []                              # basket for the answers
        for other in self.adjacency:
            if vertex in self.adjacency[other]:    # is vertex written on this?     
                incoming.append(other)

            if vertex not in self.adjacency:            # if vertex is not in the graph
                return []                               # return empty list
        return incoming

    def listOutgoingAdjacentVertex(self, vertex):
        if vertex not in self.adjacency:
            return []
        return self.adjacency[vertex]

    def removeEdge(self, from_vertex, to_vertex):
        if from_vertex in self.adjacency and to_vertex in self.adjacency[from_vertex]:
            self.adjacency[from_vertex].remove(to_vertex)
            return True
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