
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

        mid_x = right//2
        mid_y = top//2
        # Quadrant 1 (top-right)
        q1 = Board(mid_x + 1, right, mid_y + 1, top)

        # Quadrant 2 (top-left)
        q2 = Board(left, mid_x, mid_y + 1, top)

        # Quadrant 3 (bottom-left)
        q3 = Board(left, mid_x, bottom, mid_y)

        # Quadrant 4 (bottom-right)
        q4 = Board(mid_x + 1, right, bottom, mid_y)

        if block in q1:

            draw.draw_one_tromino(1, board)

            #recursion for type 1 problem
            if board.get_boundary() == (1, 2, 1, 2):  # if we have 2x2
                draw.draw_one_tromino(2, board)
                return
            else:
                 self.solve(block, q1) #recursive call
        elif block in q2:
            draw.draw_one_tromino(2, board)
            if board.get_boundary() == (1, 2, 1, 2):  # if we have 2x2
                draw.draw_one_tromino(2, board)
                return
            else:
                self.solve(block, q1)  # recursive call

        elif block in q3:
            draw.draw_one_tromino(3, board)
        elif block in q4:
            draw.draw_one_tromino(4, board)
        # your code goes here:






    def get_tromino_type(self, block, board):
        # return the type of the tromino you should draw based on the position of the block and the board.
        left, right, bottom, top = board.get_boundary() 
        # your code goes here:




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