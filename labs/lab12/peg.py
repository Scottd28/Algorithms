from copy import deepcopy as copy
import argparse
from animation import draw

class Node():
    def __init__(self, board, jumpfrom = None, jumpover = None, jumpto = None):
        self.board = board
        self.jumpfrom = jumpfrom
        self.jumpover = jumpover
        self.jumpto = jumpto

class peg:
    def __init__(self, start_row, start_col, rule):
        self.size = 5
        self.start_row, self.start_col, self.rule = start_row, start_col, rule
        # board
        self.board = [[1 for j in range(i+1)] for i in range(self.size)]
        self.board[start_row][start_col] = 0
        self.start = Node(copy(self.board))
        # path
        self.path = []

        # self.path is a list of Node. You need to create a new Node for each jump and then append this Node to the path.
        self.path.append(Node(copy(self.board)))

    def draw(self):
        if self.success():
            draw(self.path, self.start_row, self.start_col, self.rule)
        else:
            print("No solution were found!")


    def success(self):
        # your code goes here:
        pass 



        
    def solve(self):
        # your code goes here:
        ''''
        if board is solution:
            return True

        for one available jump:

            process
            board and path

            if solve():
                return True

            backtrack
            board and path

        return False
        '''
        if self.success():
            return True
        #calculate the available jumps
        for i in range(len(self.board)): # row
            for j in range(len(self.board[i])):







        
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='peg game')

    parser.add_argument('-hole', dest='position', required = True, nargs = '+', type = int, help='initial position of the hole')
    parser.add_argument('-rule', dest='rule', required = True, type = int, help='index of rule')

    args = parser.parse_args()

    start_row, start_col = args.position
    if start_row > 4:
        print("row must be less or equal than 4")
        exit()
    if start_col > start_row:
        print("column must be less or equal than row")
        exit()

    # Example: 
    # python peg.py -hole 0 0 -rule 0
    game = peg(start_row, start_col, args.rule)
    game.solve()
    game.draw()
    