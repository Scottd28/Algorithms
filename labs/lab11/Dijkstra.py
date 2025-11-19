
from bridges.graph_adj_list import *
import heapq

class Dijkstra():
    def __init__(self, inputFile, startingVertex, goalVertex):
        # an initially empty dictionary containing mapping: vertex: [child, weight]
        self.adjacency = {}
        # collection of vertices
        self.vertices = []
        # each dictionary entry contains mapping of vertex:parent
        self.parent = {}
        # startingVertex, goalVertex
        self.startingVertex, self.goalVertex = startingVertex, goalVertex

        # The following reads in the input file and constructs an adjacency list of the graph.
        graph = open(inputFile)
        for line in graph:
            entry = line.split()

            # get the vertices
            self.vertices.append(entry[0])
            self.vertices.append(entry[1])

            if entry[0] not in self.adjacency:
                self.adjacency[entry[0]] = []

            # construct an edge for the adjacency list
            edge = (entry[1], int(entry[2]))
            self.adjacency[entry[0]].append(edge)

        # remove duplication in vertices
        self.vertices = list(set(self.vertices))

        # checking if start and goal are in vertices
        if startingVertex not in self.vertices:
            print('Starting vertex', startingVertex, 'not present in graph')
            quit()
        elif goalVertex not in self.vertices:
            print('Goal vertex', goalVertex, 'not present in graph')
            quit()

        # create Bridges graph
        self.g = GraphAdjList()
        for vertex in self.vertices:
            self.g.add_vertex(vertex, str(vertex))
            self.g.get_visualizer(vertex).color = "red"

        for vertex in self.adjacency:
            for edge in self.adjacency[vertex]:
                self.g.add_edge(vertex, edge[0], edge[1])













    # solve it using Dijkstra algorithm
    def solve(self):
       # your code goes here:

       '''
       Initialize a heap using the start vertex

        while heap:
            remove a vertex from the heap
            if vertex not in visited:
                do something
            if vertex is the goal:
                return True
            do something else
       '''
       minDistances = {}
       for vertex in self.vertices:
           minDistances[vertex] = float('inf')
       visitedVertices = []
       pq = []
       heapq.heappush(pq, (0, self.startingVertex, None))
       minDistances[self.startingVertex] = 0
       while pq:
           dist, vertex, directparent = heapq.heappop(pq) #remove a vertex from the heap
           if(dist > minDistances[vertex]):
               continue   #TODO: REMEBER WHAT CONTINUE DOES
           print(f"adjacency list of [{vertex}]: {self.adjacency.get(vertex, [])}\n")
           if vertex not in visitedVertices:
               #update priority and add to visited vertices
               visitedVertices.append(vertex)
               adjacencyListOfVertex = self.adjacency.get(vertex, [])
               for edge in adjacencyListOfVertex:
                   print(f"{edge[0]} -> {edge[1]}")
                   child = edge[0]
                   weight = edge[1]

                   if minDistances[child] > minDistances[vertex] + weight:
                       self.parent[child] = vertex
                       minDistances[child] = minDistances[vertex]+weight
                       heapq.heappush(pq, (minDistances[child], child, vertex))

                   print("dist : ", weight + dist)
                   # heapq.heappush(pq, ( weight + dist, child, vertex))
           if vertex == self.goalVertex:
                print("minDistance DICTIONARY: " , minDistances)
                return True






    # retrieve the path from start to the goal
    def find_path(self):
        path= [self.goalVertex]
        # your code goes here:
        while self.parent[path[0]] is not self.startingVertex:
            print(self.parent[path[0]])
            path.insert (0, self.parent[path[0]])

        path.insert(0, self.startingVertex)
        return path







    # draw the path as red
    def draw_path(self):

        path = self.find_path()
        print(path)
        for i in range(len(path)-1):
            self.g.get_link_visualizer(path[i], path[i+1]).color = "red"

    # return the Bridges object
    def get_graph(self):
        return self.g
