import numpy as np
from heapq import heappush, heappop
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


class Maze():
    
    def __init__(self, map, start_state, goal_state, map_index):
        self.start_state = start_state
        self.goal_state = goal_state
        self.map = map
        self.visited = [] # state
        self.m, self.n = map.shape 
        self.map_index = map_index


    def draw(self, node):
        path=[]
        while node.parent:
            path.append(node.state)
            node = node.parent
        path.append(self.start_state)
    
        draw(self.map, path[::-1], self.map_index)


    def goal_test(self, current_state):
        # your code goes here:
        return current_state == self.goal_state


    def get_cost(self, current_state, next_state):
        # your code goes here:
        return 1

    def get_successors(self, state):
        successors = []

        # your code goes here:
        red_row, red_column = state
        nrows = len(self.map)
        ncols = len(self.map[0])

        # move up
        if red_row - 1 >= 0 and self.map[red_row - 1][red_column] != 0: #check that is within bounds of the map
            successors.append((red_row - 1, red_column))
        # move down
        if red_row + 1 < nrows and self.map[red_row + 1][red_column] != 0:
            successors.append((red_row + 1, red_column))
        # move right
        if red_column + 1 < ncols and self.map[red_row][red_column + 1] != 0:
            successors.append((red_row, red_column + 1))
        # move left
        if red_column - 1 >= 0 and self.map[red_row][red_column - 1] != 0:
            successors.append((red_row, red_column - 1))

        return successors
    # heuristics function
    def heuristics(self, state):
        # your code goes here:
        red_row, red_column = state
        goal_row, goal_column = self.goal_state
        distance = abs(red_row - goal_row) + abs(red_column - goal_column)
        return distance



    # priority of node 
    def priority(self, node):
        # your code goes here:
        return node.cost_from_start + self.heuristics(node.state)

    
    # solve it
    def solve(self):
        # !!! In A* algorithm, you only need to return the first solution.
        #     The first solution is in general possibly not the best solution, however, in this eight puzzle,
        #     we can prove that the first solution is the best solution.
        # your code goes here:
        if self.goal_test(self.start_state): return
        fringe = []  # node
        state = self.start_state  # use copy() to copy value instead of reference
        node = Node(state, 0, None)
        self.visited.append(state)
        count = 1
        heappush(fringe, (self.priority(node), count, node))


        while fringe:


            priority, _, current_node = heappop(fringe)

            moves = self.get_successors(current_node.state)
            for move in moves:
                visit = False
                for visited in self.visited:
                    if move == visited:
                        visit = True
                        break
                if not visit:
                    if self.goal_test(move):
                        next_cost = current_node.cost_from_start + self.get_cost(current_node.state, move)
                        next_node = Node(move, next_cost, current_node)
                        self.draw(next_node)
                        return
                    next_cost = current_node.cost_from_start + self.get_cost(current_node.state, move)
                    next_node = Node(move, next_cost, current_node)
                    self.visited.append(move)
                    count += 1
                    heappush(fringe, (self.priority(next_node), count, next_node))
        pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='maze')
    parser.add_argument('-index', dest='index', required = True, type = int)
    index = parser.parse_args().index

    # Example:
    # Run this in the terminal solving map 1
    #     python maze_astar.py -index 1
    
    data = np.load('map_'+str(index)+'.npz')
    map, start_state, goal_state = data['map'], tuple(data['start']), tuple(data['goal'])

    game = Maze(map, start_state, goal_state, index)
    game.solve()
    