
'''
Demonstration of some simple graph algorithms.
    
@author: Jingsai Liang
'''

import sys

class GraphAlgorithms:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
    
        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }
    
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]
        self.path = ""

        for line in graphFile:
            '''
            Get the two vertices
        
            Python lets us assign two variables with one
            assignment statement.
            '''
            (firstVertex, secondVertex) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            '''
            Check if the first vertex is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if firstVertex not in self.adjacencyList:
                self.adjacencyList[firstVertex] = [ ]

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacencyList[firstVertex].append(secondVertex)
        
        # creates and sort a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        # sort adjacency list for each vertex
        for vertex in self.adjacencyList:
            self.adjacencyList[vertex].sort()

    '''
    Begins the DFS algorithm.
    '''
    def DFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        self.unVisitedVertices.sort()
        # initialize path as an empty string
        self.path = ""

    '''
    depth-first traversal of specified graph
    '''
    def DFS(self, method):
        self.DFSInit()
        if method == 'recursive':
            # Your code goes here:
            while len(self.unVisitedVertices) > 0:
                self.DFS_recur(self.unVisitedVertices[0])

            return self.path
        elif method == 'stack':
            # Your code goes here:
            while len(self.unVisitedVertices) > 0:
                self.DFS_stack(self.unVisitedVertices[0])
            
            return self.path
        else:
            return None
            

    def DFS_recur(self,vertex):
        # Your code goes here:
        self.unVisitedVertices.remove(vertex)
        self.path = self.path + vertex

        for v in self.adjacencyList[vertex]:
            if v in self.unVisitedVertices:
                self.DFS_recur(v)

            
                
    def DFS_stack(self, vertex):
        stack=[]
        # Your code goes here:
        stack.append(vertex)
        while len(stack) > 0:
            v = stack.pop()
            if v in self.unVisitedVertices:
                self.unVisitedVertices.remove(v)
                self.path = self.path + v
                for w in self.adjacencyList[v]:
                    if w in self.unVisitedVertices:
                        stack.append(w)



    def BFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        self.unVisitedVertices.sort()
        # initialize path as an empty string
        self.path = ""
        

    def BFS(self):
        self.BFSInit()
        queue = []
        # Your code goes here:
        while len(self.unVisitedVertices) > 0:
            vertex = self.unVisitedVertices.pop(0)
            self.path = self.path + vertex
            queue.append(vertex)
            while len(queue) > 0:
                v = queue.pop(0)
                for w in self.adjacencyList[v]:
                    if w in self.unVisitedVertices:
                        self.path = self.path + w
                        self.unVisitedVertices.remove(w)
                        queue.append(w)

 
        return self.path


    def hasCycle(self):
        # Your code goes here:
        ImmediateParent = {}


        self.unVisitedVertices = list(set(self.vertices))
        self.unVisitedVertices.sort()
        self.path = "" # initialize path as an empty string
        queue = []
        # we do BFS
        while len(self.unVisitedVertices) > 0:
            start = self.unVisitedVertices.pop(0)
            queue.append(start)
            ImmediateParent[start] = None  # root has no parent
            self.path = self.path + start


            while len(queue) > 0:
                v = queue.pop(0)
                for w in self.adjacencyList[v]:
                    if w in self.unVisitedVertices:
                        self.path = self.path + w
                        ImmediateParent[w] = v # we add the parent to the child
                        self.unVisitedVertices.remove(w)
                        queue.append(w)
                    elif w in ImmediateParent and ImmediateParent[v] != w: #the child's parent is not w
                        return True  # cycle detected
        return False
       
                    
    # Work on this function for at most 10 extra points
    def shortestpath(self, p, q):
        # Your code goes here:
        #In shortestpath, you can label each vertex using a level when searching a BFS path starting from p.
        # The level of starting vertex p is 0, the level of all children of p is 1, and so on. The algorithm stops when reaching to end vertex q.
        # Then the shortest path between p and q is level[q] - level[p].

        level= {}
        queue = []
        level[p] = 0
        queue.append(p)
        while len(queue) > 0:
            v = queue.pop(0)
            if v == q:
                return level[q] - level[p]
            for w in self.adjacencyList[v]: # go to the child of v
                if not w in level: # we haven't assigned a value to it yet (ie unvisited)
                    level[w] = level[v] + 1
                    queue.append(w) # dont stop the loop till there are no children left









  
                
        

        

