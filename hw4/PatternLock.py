from itertools import permutations
import math
import argparse
from draw import draw_path
from test import test_path



class password():
    def __init__(self, rule):
        self.rule = rule
        # Longest distance
        self.longest_length = 0.0
        # List of longest path. The longest path is not unique. 
        self.longest_path = []
        # Your code goes here:


        #adjacency list for rule 1

    midpointList = {
        # rows
        ("1", "3"): "2",
        ("4", "6"): "5",
        ("7", "9"): "8",

        # colums
        ("7", "1"): "4",
        ("8", "2"): "5",
        ("9", "3"): "6",

        # diagonals
        ("7", "3"): "5",
        ("9", "1"): "5",

        # inverse
        # rows
        ("3", "1"): "2",
        ("6", "4"): "5",
        ("9", "7"): "8",

        # colums
        ("1", "7"): "4",
        ("2", "8"): "5",
        ("3", "9"): "6",

        # diagonals
        ("3", "7"): "5",
        ("1", "9"): "5"}

    positions = {
        "1": (0, 0), "2": (1, 0), "3": (2, 0),
        "4": (0, 1), "5": (1, 1), "6": (2, 1),
        "7": (0, 2), "8": (1, 2), "9": (2, 2)
    }

    # Find the longest path
    def find_longest_path(self):
        # Your code goes here:
        password = "123456789"
        coordinate = permutations(password)
        valid = True
        validPath = []

        if self.rule == 1: # first way to find the result

            for i in coordinate: # for each possibility
                valid = True #flush
                for j in range(len(i)-1): # for each path
                    a,b, = i[j], i[j+1]
                    if (a,b) in self.midpointList: #if it breaks the rules
                        valid = False
                        break

                if valid:
                    validPath.append(i)

            length = dict.fromkeys(validPath, 0)
            for path in validPath:
                for i in range(len(path)-1):
                    length[path]+= self.distance(self.positions[path[i]], self.positions[path[i+1]])

            self.longest_length = max(length.values())
            for path in validPath:
                if length[path] == self.longest_length:
                    self.longest_path.append(path)



        if self.rule == 2:  # second way to find the result


            for i in coordinate:  # for each possibility
                valid = True  # flush
                visited = set()
                for j in range(len(i)-1):  # for each path
                    a, b = i[j], i[j + 1]
                    if (a,b) in self.midpointList and self.midpointList[(a,b)] not in visited:
                        valid = False
                    visited.add(a)

                if valid:
                    validPath.append(i)

            length = dict.fromkeys(validPath, 0)
            for path in validPath:
                for i in range(len(path) - 1):
                    length[path] += self.distance(self.positions[path[i]], self.positions[path[i + 1]])

            self.longest_length = max(length.values())
            for path in validPath:
                if length[path] == self.longest_length:
                    self.longest_path.append(path)





















            # Calculate distance between two vertices
    # Format of a coordinate is a tuple (x_value, y_value), for example, (1,2), (0,1)
    def distance(self, vertex1, vertex2):
        return math.sqrt((vertex1[0]-vertex2[0])**2 + (vertex1[1]-vertex2[1])**2)

    # Print and save the result
    def print_result(self):
        print("The longest length using rule " + str(self.rule) + " is:")
        print(self.longest_length)
        print()
        print("All paths with longest length using rule " + str(self.rule) + " are:") 
        print(self.longest_path)
        print()
        with open('results_rule'+str(self.rule)+'.txt', 'w') as file_handler:
            file_handler.write("{}\n".format(self.longest_length)) 
            for path in self.longest_path:
                file_handler.write("{}\n".format(path)) 

    # test the result 
    def test(self):
        test_path(self.longest_length, self.longest_path, self.rule)

    # draw first result
    def draw(self):
        if len(self.longest_path) > 0:
            draw_path(self.longest_path[0], self.rule)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='PatternLock')
    parser.add_argument('-rule', dest='rule', required = True, type = int, help='Index of the rule')
    args = parser.parse_args()

    # usage
    # python PatternLock.py -rule 1
    # python PatternLock.py -rule 2
    
    # Initialize the object using rule 1 or rule 2
    run = password(args.rule)
    # Find the longest path
    run.find_longest_path()
    # Print and save the result
    run.print_result()
    # Draw the first longest path
    run.draw()
    # Verify the result 
    run.test()