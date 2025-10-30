import numpy as np
from animation import draw
import argparse

class Node():
    """
    cost_from_start - the cost of reaching this node from the starting node
    state - the state (row,col)
    parent - the parent node of this node, default as None
    """
    def __init__(self, state, cost_from_start, parent = None):
        self.state = state
        self.parent = parent
        self.cost_from_start = cost_from_start


class EightPuzzle():
    
    def __init__(self, start_state, goal_state, algorithm, array_index):
        self.start_state = start_state
        self.goal_state = goal_state
        self.visited = [] # state
        self.algorithm = algorithm
        self.m, self.n = start_state.shape 
        self.array_index = array_index

    # goal test(ie. does our current state match the end goal)
    def goal_test(self, current_state):
        if current_state == self.goal_state:
            return True
        else:
            return False





    # get cost function (ie. find next available states of current state)
    def get_cost(self, current_state, next_state):
        return 1





    # get successor function (ie. find next available states of current state)
    def get_successors(self, state):
        successors = []
        # your code goes here:
        current_state = state.copy()
        zeroRow, zeroCol = np.where(current_state == 0)
        pos_after_row = zeroRow+1
        pos_before_row = zeroRow-1
        pos_after_column = zeroCol+1
        pos_before_column = zeroCol-1
        available_pos = [0,1,2]
        if pos_after_row in available_pos:
            original_position = current_state[zeroRow][zeroCol]
            current_state[zeroRow][zeroCol] = current_state[pos_after_row][zeroCol]
            current_state[pos_after_row][zeroCol] = original_position
            successors.append(current_state)
            current_state = state.copy()

        if pos_before_row in available_pos:
            original_position = current_state[zeroRow][zeroCol]
            current_state[zeroRow][zeroCol] = current_state[pos_before_row][zeroCol]
            current_state[pos_before_row][zeroCol] = original_position
            successors.append(current_state)
            current_state = state.copy()
        if pos_after_column in available_pos:
            original_position = current_state[zeroRow][zeroCol]
            current_state[zeroRow][zeroCol] = current_state[zeroRow][pos_after_column]
            current_state[zeroRow][pos_after_column] = original_position
            successors.append(current_state)
            current_state = state.copy()

        if pos_before_column in available_pos:
            original_position = current_state[zeroRow][zeroCol]
            current_state[zeroRow][zeroCol] = current_state[zeroRow][pos_before_column]
            current_state[zeroRow][pos_before_column] = original_position
            successors.append(current_state)

        return successors
    
    # draw 
    def draw(self, node):
        path=[]
        while node.parent:
            path.append(node.state)
            node = node.parent
        path.append(self.start_state)
        draw(path[::-1], self.array_index, self.algorithm)

    # solve it
    def solve(self):
        fringe = [] # node
        state = self.start_state.copy() # use copy() to copy value instead of reference 
        node = Node(state, 0, None)
        self.visited.append(state)
        if self.algorithm == 'Depth-Limited-DFS': 
            pass
            # your code goes here:

        elif self.algorithm == 'BFS': 
            pass
            # your code goes here:

        while fringe:
            pass 
            # your code goes here:
            # if one solution is found, call self.draw(current_node) to show and save the animation.      
            
    
if __name__ == "__main__":
    
    goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
    start_arrays = [np.array([[0,1,3],[4,2,5],[7,8,6]]), # easy one. use this in lab
                    np.array([[0,2,3],[1,4,6],[7,5,8]])] # medium one.

    algorithms = ['Depth-Limited-DFS', 'BFS']
    
    parser = argparse.ArgumentParser(description='eight puzzle')

    parser.add_argument('-array', dest='array_index', required = True, type = int, help='index of array')
    parser.add_argument('-algorithm', dest='algorithm_index', required = True, type = int, help='index of algorithm')

    args = parser.parse_args()

    # run this in the terminal using array 0, algorithm BFS
    # python eight_puzzle_uninform.py -array 0 -algorithm 1
    game = EightPuzzle(start_arrays[args.array_index], goal, algorithms[args.algorithm_index], args.array_index)
    game.solve()