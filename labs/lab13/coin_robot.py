import random 
from draw import draw
import argparse

class coin_robot:

    def __init__(self, row, column):
        random.seed(0)
        self.row = row
        self.column = column 
        # Get map
        self.map = [[0 for i in range(column)] for j in range(row)]
        self.generate_map()
        
    def generate_map(self):
        for i in range(self.row):
            for j in range(self.column):
                if random.random() > 0.7:
                    self.map[i][j] = 1 # coin
                else:
                    self.map[i][j] = 0



    def solve(self):
        # Your code goes here:
        parent = {}
        dp = [[0 for _ in range(self.column)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.column):

                #get the directions you can go (ie. up or left) + init
                if i == 0 and j == 0:
                    dp[i][j] = self.map[i][j]
                    continue

                if i > 0:
                    up = dp[i - 1][j]
                else:
                    up = -1

                if j > 0:
                    left = dp[i][j - 1]
                else:
                    left = -1


                #get best direction (left first tho)
                if left >= up:
                    if left != -1:
                        dp[i][j] = self.map[i][j] + left
                    else:
                        dp[i][j] = 0
                    if j > 0:
                        parent[(i, j)] = (i, j - 1)
                else:
                    if up != -1:
                        dp[i][j] = self.map[i][j] + up
                    else:
                        dp[i][j] = 0
                    if i > 0:
                        parent[(i, j)] = (i - 1, j)

        path = []
        current = (self.row - 1, self.column - 1)  # start at bottom-right

        while current in parent:
            path.append(current)
            current = parent[current]

        path.append((0, 0))  # finally add the starting cell
        path.reverse()  # start to end
        f_value = dp[self.row - 1][self.column - 1]
        self.draw(f_value, path)

    # F is the max number of coin
    # path is the route of the robot from top-left to bottom-right
    def draw(self, F, path):
        title = "row_"+str(self.row)+"_column_"+str(self.column)+"_value_"+str(F)
        draw(self.map, path, title)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='coin robot')

    parser.add_argument('-row', dest='row', required = True, type = int, help='number of row')
    parser.add_argument('-column', dest='column', required = True, type = int, help='number of column')

    args = parser.parse_args()

    # Example: 
    # python coin_robot.py -row 20 -column 20
    game = coin_robot(args.row, args.column)
    game.solve()