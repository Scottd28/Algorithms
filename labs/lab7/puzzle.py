
import argparse


import draw



# class of board
# every board is an object of the class Board 
class Board:
    def __init__(self, left, right, bottom, top):
        self.left, self.right, self.bottom, self.top = left, right, bottom, top
    
    # call this method to return four boundaries of the board 
    def get_boundary(self):
        return self.left, self.right, self.bottom, self.top

class Puzzle:
    def __init__(self, size, block):
        # size is the size of board. 
        # block is the position (x,y) of the block 
        
        # fill the initial block as black
        draw.draw_one_square(block, 'k')
        # draw the grid on the board 
        draw.grid(size)

        # create the board at full size 
        board = Board(1, size, 1, size) 
        # call solve to fill the Tromino recursively using divide and conquer 
        self.solve(block, board)
        
        # show and save the result in a picture 
        draw.save_and_show(size, block)

    def solve(self, block, board):
        # block is a position (row, column) and board is an object of Board class 
        # recursively call solve() on four small size boards with only one block on each board
        # stop the recursive call when reaching to the base case, which is board 2*2
        #  
        # call draw.draw_one_tromino(type, board) to draw one type of tromino at the center of the board. The type of the tromino is an integer 1 to 4 as explained in the instruction and the board is an object of Board class where you want to draw the tromino at its center. 

        left, right, bottom, top = board.get_boundary()
        if (right - left + 1) == 2 and (top - bottom + 1) == 2:
            type = self.get_tromino_type(block, board)
            draw.draw_one_tromino(type, board)
            return
        else:

            mid_x = (left + right) // 2
            mid_y = (bottom + top) // 2

            # Quadrant 1 (top-right)
            q1 = Board(mid_x + 1, right, mid_y + 1, top)
            # Quadrant 2 (top-left)
            q2 = Board(left, mid_x, mid_y + 1, top)
            # Quadrant 3 (bottom-left)
            q3 = Board(left, mid_x, bottom, mid_y)
            # Quadrant 4 (bottom-right)
            q4 = Board(mid_x + 1, right, bottom, mid_y)

            # your code goes here:
            typeOriginal = self.get_tromino_type(block, board)
            draw.draw_one_tromino(typeOriginal, board)

            # After determining typeOriginal for the center tromino:

            if typeOriginal == 1:  # original block in Quadrant 1 (top-right)
                b1 = block  # Quadrant 1: original block stays
                b2 = (mid_x, mid_y + 1)  # Quadrant 2: center tromino covers this
                b3 = (mid_x, mid_y)  # Quadrant 3: center tromino covers this
                b4 = (mid_x + 1, mid_y)  # Quadrant 4: center tromino covers this

            elif typeOriginal == 2:  # original block in Quadrant 2 (top-left)
                b1 = (mid_x + 1, mid_y + 1)  # Quadrant 1: center tromino covers
                b2 = block  # Quadrant 2: original block
                b3 = (mid_x, mid_y)  # Quadrant 3: center tromino covers
                b4 = (mid_x + 1, mid_y)  # Quadrant 4: center tromino covers

            elif typeOriginal == 3:  # original block in Quadrant 3 (bottom-left)
                b1 = (mid_x + 1, mid_y + 1)  # Quadrant 1: center tromino covers
                b2 = (mid_x, mid_y + 1)  # Quadrant 2: center tromino covers
                b3 = block  # Quadrant 3: original block
                b4 = (mid_x + 1, mid_y)  # Quadrant 4: center tromino covers

            elif typeOriginal == 4:  # original block in Quadrant 4 (bottom-right)
                b1 = (mid_x + 1, mid_y + 1)  # Quadrant 1: center tromino covers
                b2 = (mid_x, mid_y + 1)  # Quadrant 2: center tromino covers
                b3 = (mid_x, mid_y)  # Quadrant 3: center tromino covers
                b4 = block  # Quadrant 4: original block

            self.solve(b1, q1)
            self.solve(b2, q2)
            self.solve(b3, q3)
            self.solve(b4, q4)

    def get_tromino_type(self, block, board):
        left, right, bottom, top = board.get_boundary()
        mid_x = (left + right) // 2
        mid_y = (bottom + top) // 2

        # Quadrant 1 (top-right)
        if block[0] > mid_x and block[1] > mid_y:
            return 1
        # Quadrant 2 (top-left)
        elif block[0] <= mid_x and block[1] > mid_y:
            return 2
        # Quadrant 3 (bottom-left)
        elif block[0] <= mid_x and block[1] <= mid_y:
            return 3
        # Quadrant 4 (bottom-right)
        elif block[0] > mid_x and block[1] <= mid_y:
            return 4



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='puzzle')

    parser.add_argument('-size', dest='size', required = True, type = int, help='size of the board: 2^n')
    parser.add_argument('-block', dest='block', required = True, nargs='+', type = int, help='position of the initial block')

    args = parser.parse_args()

    # size must be a positive integer 2^n
    # block must be two integers between 1 and size 
    game = Puzzle(args.size, tuple(args.block))

    # game = puzzle(8, (1,1))
    # python puzzle.py -size 8 -block 1 1