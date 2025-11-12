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

    def __init__(self, state, cost_from_start, parent=None):
        self.state = state
        self.parent = parent
        self.cost_from_start = cost_from_start


class EightPuzzle():

    def __init__(self, start_state, goal_state, method, algorithm, array_index):
        self.start_state = start_state
        self.goal_state = goal_state
        self.visited = []  # state
        self.method = method
        self.algorithm = algorithm
        self.m, self.n = start_state.shape
        self.array_index = array_index

    def goal_test(self, current_state):
        # your code goes here:
        return np.array_equal(current_state, self.goal_state)

    def get_cost(self, current_state, next_state):
        # your code goes here:
        return 1

    def get_successors(self, state):
        # your code goes here:
        successors = []
        # your code goes here:
        current_state = state.copy()
        zeroRow, zeroCol = np.where(current_state == 0)
        zeroRow, zeroCol = int(zeroRow[0]), int(zeroCol[0])
        pos_after_row = zeroRow + 1
        pos_before_row = zeroRow - 1
        pos_after_column = zeroCol + 1
        pos_before_column = zeroCol - 1
        available_pos = [0, 1, 2]
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

    # heuristics function
    def heuristics(self, state):

        # your code goes here:
        if self.method == "Hamming":
            current_state = state.copy()

            notInPosition = 0
            for r in range(len(current_state)):
                for c in range(len(current_state[r])):
                    if current_state[r][c] != self.goal_state[r][c] and current_state[r][c] != 0:
                        notInPosition += 1
            return notInPosition

        elif self.method == "Manhattan":
            current_state = state.copy()
            distance = 0
            for r in range(len(current_state)):
                for c in range(len(current_state[r])):
                    if current_state[r][c] != self.goal_state[r][c] and current_state[r][c] != 0: #if its a number we need to add to sum
                        location_in_goal = np.where(self.goal_state == current_state[r][c]) #get an array of the row and col in goal
                        goalrow, goalcol = location_in_goal[0][0], location_in_goal[1][0]
                        currentrow, currentcol = r, c
                        h = abs(goalrow - currentrow)
                        w = abs(goalcol - currentcol)
                        distance += h + w
            return distance




    # priority of node
    def priority(self, node):
        # use if-else here to take care of different type of algorithms
        # your code goes here:
        if self.algorithm == "Greedy":
            return  self.heuristics(node.state)
        elif self.algorithm == "AStar":
            return node.cost_from_start + self.heuristics(node.state)

    # draw
    def draw(self, node):
        path = []
        while node.parent:
            path.append(node.state)
            node = node.parent
        path.append(self.start_state)

        draw(path[::-1], self.array_index, self.algorithm, self.method)

    # solve it
    def solve(self):
        # use one framework to merge all five algorithms.
        # !!! In A* algorithm, you only need to return the first solution.
        #     The first solution is in general possibly not the best solution, however, in this eight puzzle,
        #     we can prove that the first solution is the best solution.
        # your code goes here:
        if self.goal_test(self.start_state): return
        fringe = []  # node
        state = self.start_state.copy()  # use copy() to copy value instead of reference
        node = Node(state, 0, None)
        self.visited.append(state)
        depth = 15
        count = 0

        if self.algorithm in ["AStar", "Greedy"]:
            count +=1
            heappush(fringe, (self.priority(node),count, node))
        else:
            fringe.append(node)

        while fringe:
            if self.algorithm == 'Depth-Limited-DFS':
                current_node = fringe.pop()
                if current_node.cost_from_start >= depth:
                    continue
            elif self.algorithm == 'BFS':
                current_node = fringe.pop(0)
            elif self.algorithm in ["AStar", "Greedy"]:
                priority, _, current_node = heappop(fringe)



            moves = self.get_successors(current_node.state)
            for move in moves:
                visit = False
                for visited in self.visited:
                    if np.array_equal(move, visited):
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
                    if self.algorithm == 'Depth-Limited-DFS':
                        fringe.insert(0, next_node)
                    elif self.algorithm == 'BFS':
                        fringe.append(next_node)
                    elif self.algorithm == "AStar" or self.algorithm == "Greedy":
                        count+=1
                        heappush(fringe, (self.priority(next_node),count ,next_node))
        pass


if __name__ == "__main__":
    goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    start_arrays = [np.array([[1, 2, 0], [3, 4, 6], [7, 5, 8]]),
                    np.array([[8, 1, 3], [4, 0, 2], [7, 6, 5]])]
    methods = ["Hamming", "Manhattan"]
    algorithms = ['Depth-Limited-DFS', 'BFS', 'Greedy', 'AStar']

    parser = argparse.ArgumentParser(description='eight puzzle')

    parser.add_argument('-array', dest='array_index', required=True, type=int, help='index of array')
    parser.add_argument('-method', dest='method_index', required=True, type=int, help='index of method')
    parser.add_argument('-algorithm', dest='algorithm_index', required=True, type=int, help='index of algorithm')

    args = parser.parse_args()

    # Example:
    # Run this in the terminal using array 0, method Hamming, algorithm AStar:
    #     python eight_puzzle.py -array 0 -method 0 -algorithm 3
    game = EightPuzzle(start_arrays[args.array_index], goal, methods[args.method_index],
                       algorithms[args.algorithm_index], args.array_index)
    game.solve()