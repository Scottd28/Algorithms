

class TopologicalSorting:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a directed graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
        # file name
        self.name = fileName
        
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

        # sorted list
        self.sortedList = []

    def print_and_save(self):
        #print(self.vertices)
        #print(self.adjacencyList)
        self.sort()
        print(self.sortedList)
        with open('result_'+str(self.name), 'w') as file_handler:
            for node in self.sortedList:
                file_handler.write("{}\n".format(node)) 
        

    # Topological sorting using decrease-by-one-and-conquer. 
    def sort(self):
        # Your code goes here:
        while len(self.vertices) > 0:
            endpoints = self.adjacencyList.values()
            for vertex in self.vertices:
                no_parent = True
                for e in endpoints:
                    if vertex in e:
                        no_parent = False
                if no_parent:
                    self.sortedList.append(vertex)
                    if vertex in self.adjacencyList:
                        del[self.adjacencyList[vertex]]
                    self.vertices.remove(vertex)
                    break
                

    # How many different ways can the spider reach the fly by moving along the web’s lines in the directions indicated by the arrow?
    def spider(self,start,end):
        # Your code goes here:
        if start == end:
            return 1
        if start not in self.adjacencyList:
            return 0
        total = 0
        for vertex in self.adjacencyList[start]:
            total += self.spider(vertex, end)
        return total


if __name__ == "__main__":

    s = TopologicalSorting("graph_example.txt")
    s.print_and_save()

    # Be careful! graph-courses.txt is incomplete. Please finish this txt file at first. 
    s = TopologicalSorting("graph_courses.txt")
    s.print_and_save()

    s = TopologicalSorting("graph_spider.txt")
    s.print_and_save()

    s = TopologicalSorting("graph_spider.txt")
    count = s.spider("A", "F")
    with open("result_spider_count.txt", 'w') as f:
        f.write("{}\n".format(count))