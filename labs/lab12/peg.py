from copy import deepcopy as copy
import argparse
from turtledemo.chaos import jumpto

from astropy.cosmology import available

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
        pegs = 0
        for row in self.board:
            for col in row:
                if col == 1:
                    pegs += 1

        if self.rule == 0:
            return pegs == 1
        elif self.rule == 1:
            return pegs == 1 and self.board[self.start_row][self.start_col] == 1
        else:
            return False

    def solve(self):
        # Base case
        if self.success():
            return True

        # one available move
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # Found a peg
                if self.board[i][j] == 1:

                    # Jump right (col 110)
                    if j + 2 < len(self.board[i]):  # check if its within bounds
                        if self.board[i][j + 1] == 1 and self.board[i][j + 2] == 0:
                            self.board[i][j] = 0  # jumpfrom
                            self.board[i][j + 1] = 0  # jump over
                            self.board[i][j + 2] = 1  # jumpto

                            # add to path
                            self.path.append(Node(copy(self.board), (i, j), (i, j + 1), (i, j + 2)))

                            if self.solve():
                                return True

                            # backtracking, return the board to original state
                            self.board[i][j] = 1
                            self.board[i][j + 1] = 1
                            self.board[i][j + 2] = 0
                            self.path.pop()

                    # Jump left (col 011)
                    if j - 2 >= 0:  # check if its within bounds
                        if self.board[i][j - 1] == 1 and self.board[i][j - 2] == 0:
                            self.board[i][j] = 0  # jumpfrom
                            self.board[i][j - 1] = 0  # jump over
                            self.board[i][j - 2] = 1  # jumpto

                            # add to path
                            self.path.append(Node(copy(self.board), (i, j), (i, j - 1), (i, j - 2)))

                            if self.solve():
                                return True

                            # backtracking, return the board to original state
                            self.board[i][j] = 1
                            self.board[i][j - 1] = 1
                            self.board[i][j - 2] = 0
                            self.path.pop()

                    # Jump down-right diagonal
                    if i + 2 < len(self.board) and j + 2 < len(self.board[i + 2]):  # check if its within bounds
                        if self.board[i + 1][j + 1] == 1 and self.board[i + 2][j + 2] == 0:
                            self.board[i][j] = 0  # jumpfrom
                            self.board[i + 1][j + 1] = 0  # jump over
                            self.board[i + 2][j + 2] = 1  # jumpto

                            # add to path
                            self.path.append(Node(copy(self.board), (i, j), (i + 1, j + 1), (i + 2, j + 2)))

                            if self.solve():
                                return True

                            # backtracking, return the board to original state
                            self.board[i][j] = 1
                            self.board[i + 1][j + 1] = 1
                            self.board[i + 2][j + 2] = 0
                            self.path.pop()

                    # Jump up-left diagonal
                    if i - 2 >= 0 and j - 2 >= 0:  # check if its within bounds
                        if self.board[i - 1][j - 1] == 1 and self.board[i - 2][j - 2] == 0:
                            self.board[i][j] = 0  # jumpfrom
                            self.board[i - 1][j - 1] = 0  # jump over
                            self.board[i - 2][j - 2] = 1  # jumpto

                            # add to path
                            self.path.append(Node(copy(self.board), (i, j), (i - 1, j - 1), (i - 2, j - 2)))

                            if self.solve():
                                return True

                            # backtracking, return the board to original state
                            self.board[i][j] = 1
                            self.board[i - 1][j - 1] = 1
                            self.board[i - 2][j - 2] = 0
                            self.path.pop()

                    # Jump down (vertical)
                    if i + 2 < len(self.board) and j < len(self.board[i + 2]):  # check if its within bounds
                        if self.board[i + 1][j] == 1 and self.board[i + 2][j] == 0:
                            self.board[i][j] = 0  # jumpfrom
                            self.board[i + 1][j] = 0  # jump over
                            self.board[i + 2][j] = 1  # jumpto

                            # add to path
                            self.path.append(Node(copy(self.board), (i, j), (i + 1, j), (i + 2, j)))

                            if self.solve():
                                return True

                            # backtracking, return the board to original state
                            self.board[i][j] = 1
                            self.board[i + 1][j] = 1
                            self.board[i + 2][j] = 0
                            self.path.pop()

                    # Jump up (vertical)
                    if i - 2 >= 0 and j < len(self.board[i - 2]):  # check if its within bounds
                        if self.board[i - 1][j] == 1 and self.board[i - 2][j] == 0:
                            self.board[i][j] = 0  # jumpfrom
                            self.board[i - 1][j] = 0  # jump over
                            self.board[i - 2][j] = 1  # jumpto

                            # add to path
                            self.path.append(Node(copy(self.board), (i, j), (i - 1, j), (i - 2, j)))

                            if self.solve():
                                return True

                            # backtracking, return the board to original state
                            self.board[i][j] = 1
                            self.board[i - 1][j] = 1
                            self.board[i - 2][j] = 0
                            self.path.pop()

        return False


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
