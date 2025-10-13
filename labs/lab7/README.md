<div class="crossnote markdown-preview">

### CMPT 306 Algorithms

#### Fall 2025

------------------------------------------------------------------------

#### Lab 7 - Tromino Puzzle

##### How Labs are Managed and Grade

1.  Select a partner on your own. The rules are you must pair with a new
    partner each week.

2.  Work as a pair to complete the lab. At the end of the lab period,
    make sure to share all files with each partner.

3.  Each partner will submit the lab separately. (Submission
    instructions are described later in this lab.)

4.  If you do not finish the lab during the lab period, you may either
    get together outside of class to complete it, or complete it on your
    own. If you choose to complete it on your own, be sure to indicate
    this in your submission.

5.  Examples of cheating or collaboration can be found from this
    [link](http://people.westminstercollege.edu/faculty/jliang/files/Cheating-or-Collaboration.html).

#### Instruction

Please download and unpack this tar file:

[lab7.tar](./lab7.tar)

In this lab, you are expected to solve [Tromino
Puzzle](http://www3.amherst.edu/~nstarr/trom/intro.html) using
divide-and-conquer strategy.

A tromino (more accurately, a right tromino) is an L-shaped tile formed
by three 1 × 1 squares. The problem is to cover any <span
class="katex"><span class="katex-mathml">2<sup>*n*</sup></span><span
class="katex-html" aria-hidden="true"><span class="base"><span
class="strut" style="height:0.6644em;"></span><span class="mord"><span
class="mord">2</span><span class="msupsub"><span class="vlist-t"><span
class="vlist-r"><span class="vlist" style="height:0.6644em;"><span
style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
style="height:2.7em;"></span><span
class="sizing reset-size6 size3 mtight"><span
class="mord mathnormal mtight">n</span></span></span></span></span></span></span></span></span></span></span>
by <span class="katex"><span
class="katex-mathml">2<sup>*n*</sup></span><span class="katex-html"
aria-hidden="true"><span class="base"><span class="strut"
style="height:0.6644em;"></span><span class="mord"><span
class="mord">2</span><span class="msupsub"><span class="vlist-t"><span
class="vlist-r"><span class="vlist" style="height:0.6644em;"><span
style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
style="height:2.7em;"></span><span
class="sizing reset-size6 size3 mtight"><span
class="mord mathnormal mtight">n</span></span></span></span></span></span></span></span></span></span></span>
chessboard with a missing square by trominoes. Trominoes can be oriented
in an arbitrary way, but they should cover all the squares of the board
except the missing one exactly and with no overlaps.

Please click this link
<https://www3.amherst.edu/~nstarr/trom/puzzle-8by8/> to play this puzzle
in a 8 by 8 board.

**board**

A board is a <span class="katex"><span
class="katex-mathml">2<sup>*n*</sup></span><span class="katex-html"
aria-hidden="true"><span class="base"><span class="strut"
style="height:0.6644em;"></span><span class="mord"><span
class="mord">2</span><span class="msupsub"><span class="vlist-t"><span
class="vlist-r"><span class="vlist" style="height:0.6644em;"><span
style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
style="height:2.7em;"></span><span
class="sizing reset-size6 size3 mtight"><span
class="mord mathnormal mtight">n</span></span></span></span></span></span></span></span></span></span></span>
by <span class="katex"><span
class="katex-mathml">2<sup>*n*</sup></span><span class="katex-html"
aria-hidden="true"><span class="base"><span class="strut"
style="height:0.6644em;"></span><span class="mord"><span
class="mord">2</span><span class="msupsub"><span class="vlist-t"><span
class="vlist-r"><span class="vlist" style="height:0.6644em;"><span
style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
style="height:2.7em;"></span><span
class="sizing reset-size6 size3 mtight"><span
class="mord mathnormal mtight">n</span></span></span></span></span></span></span></span></span></span></span>
grid with only one block at the initial step. For example, the left
board is 4 by 4 with a block at (2,3) - row 2, column 3, the right board
is 8 by 8 with a block at (1,1) - row 1 and column 1.

<img src="./picture/board_size_4_block_2_3.png" width="400" />
<img src="./picture/board_size_8_block_1_1.png" width="400" />

**tromino**

A tromino is a set of three squares on a 2 by 2 board. There are four
different types of tromino:

<img src="./picture/quadrant_1.png" width="100" /> Type 1
<img src="./picture/quadrant_2.png" width="100" /> Type 2
<img src="./picture/quadrant_3.png" width="100" /> Type 3
<img src="./picture/quadrant_4.png" width="100" /> Type 4

**solution**

A solution is a board filled by four different trominos except the
initial black block with no overlaps. For example, the left one is a
solution to the 4 by 4 example above and the right one is a solution to
the 8 by 8 example above.

<img src="./picture/result_size_4_block_2_3.png" width="400" />
<img src="./picture/result_size_8_block_1_1.png" width="400" />

**terms**

-   A board is represented by four integers <span
    class="katex-display"><span class="katex"><span
    class="katex-mathml">
    *l**e**f**t*, *r**i**g**h**t*, *b**o**t**t**o**m*, *t**o**p*
    </span><span class="katex-html" aria-hidden="true"><span
    class="base"><span class="strut"
    style="height:0.8889em;vertical-align:-0.1944em;"></span><span
    class="mord mathnormal"
    style="margin-right:0.01968em;">l</span><span
    class="mord mathnormal">e</span><span class="mord mathnormal"
    style="margin-right:0.10764em;">f</span><span
    class="mord mathnormal">t</span><span class="mpunct">,</span><span
    class="mspace" style="margin-right:0.1667em;"></span><span
    class="mord mathnormal"
    style="margin-right:0.02778em;">r</span><span
    class="mord mathnormal">i</span><span class="mord mathnormal"
    style="margin-right:0.03588em;">g</span><span
    class="mord mathnormal">h</span><span
    class="mord mathnormal">t</span><span class="mpunct">,</span><span
    class="mspace" style="margin-right:0.1667em;"></span><span
    class="mord mathnormal">b</span><span
    class="mord mathnormal">o</span><span
    class="mord mathnormal">tt</span><span
    class="mord mathnormal">o</span><span
    class="mord mathnormal">m</span><span class="mpunct">,</span><span
    class="mspace" style="margin-right:0.1667em;"></span><span
    class="mord mathnormal">t</span><span
    class="mord mathnormal">o</span><span
    class="mord mathnormal">p</span></span></span></span></span>, where
    left is the index of the column at the leftmost, right is the index
    of the column at the rightmost, bottom is the index of the row at
    the bottom, and top is the index of the row at the top. The **index
    is an integer as shown below**. For example, a 8 by 8 board is <span
    class="katex-display"><span class="katex"><span
    class="katex-mathml">
    1, 8, 1, 8
    </span><span class="katex-html" aria-hidden="true"><span
    class="base"><span class="strut"
    style="height:0.8389em;vertical-align:-0.1944em;"></span><span
    class="mord">1</span><span class="mpunct">,</span><span
    class="mspace" style="margin-right:0.1667em;"></span><span
    class="mord">8</span><span class="mpunct">,</span><span
    class="mspace" style="margin-right:0.1667em;"></span><span
    class="mord">1</span><span class="mpunct">,</span><span
    class="mspace" style="margin-right:0.1667em;"></span><span
    class="mord">8</span></span></span></span></span>, the sub-board at
    the first quadrant of a 8 by 8 board is <span
    class="katex-display"><span class="katex"><span
    class="katex-mathml">
    5, 8, 5, 8
    </span><span class="katex-html" aria-hidden="true"><span
    class="base"><span class="strut"
    style="height:0.8389em;vertical-align:-0.1944em;"></span><span
    class="mord">5</span><span class="mpunct">,</span><span
    class="mspace" style="margin-right:0.1667em;"></span><span
    class="mord">8</span><span class="mpunct">,</span><span
    class="mspace" style="margin-right:0.1667em;"></span><span
    class="mord">5</span><span class="mpunct">,</span><span
    class="mspace" style="margin-right:0.1667em;"></span><span
    class="mord">8</span></span></span></span></span>
-   A quadrant is 1/4 corner area of a board. There are four quadrants
    from 1 to 4 at top-right, top-left, bottom-left, and bottom-right.
    Each quadrant is a sub-board of the board.
-   A block is represented by a position (**row, column**). For example,
    the position shown below is (0,0).

Here is an example of these terms on a 8 by 8 board:

<img src="./picture/board.png" width="400" />

#### Divide-and-Conquer

1.  Base case: 2 by 2 block.

2.  Draw a tromino at the center of the board based on the position of
    the block, in order to have each quadrant of this board has a block.

3.  Recursively solve this puzzle on each quadrant of the board.

#### Python

Run puzzle.py in terminal like this:

``` language-python
python puzzle.py -size 8 -block 1 1
```

where:

-   size is the size of board. size must be a positive integer 2^n like
    2, 4, 8, 16.
-   block is the initial position (x,y) of the missing square. block
    must be two integers between 1 and size

#### Extra Credit

At most 5 more points will be awarded if you analyze the order of growth
of this algorithm.

#### What to Submit

You need to submit these files:

-   puzzle.py
-   result\_size\_4\_block\_2\_2.png
-   result\_size\_8\_block\_3\_6.png
-   result\_size\_16\_block\_16\_16.png
-   a text file showing your answer to the extra question about the
    order of the growth if you have.

Please do not use other file names. Both lab partners need to submit the
solution separately to the dropbox on Canvas.

</div>
