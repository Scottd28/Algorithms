<div class="crossnote markdown-preview">

### CMPT 306 Algorithms

#### Fall 2025

------------------------------------------------------------------------

#### Lab 6 - Topological Sorting

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

#### Instruction

Please download and unpack this tar file:

-   [lab6.tar](./lab6.tar)

which contains five file:

-   TopologicalSorting.py
-   graph\_courses.txt
-   graph\_example.txt
-   graph\_spider.txt

Topological sorting or topological ordering requires using a directed
acyclic graph (or DAG). A topological ordering of the vertices in a
directed graph such that, if there appears a path from Vi to Vj, Vj
appears after Vi in the ordering.

<img src="./picture/top-sort-example.png" width="200" />

For example, a topological sorting of this directed graph is
C1,C2,C3,C4,C5. In this sorted list, for example, C3 is after C1 because
there is a path from C1 to C3, C5 is after C2 because there is a path
from C2 to C5.

One algorithm of sorting vertices topologically is based on a direct
implementation of the decrease-by-one-and-conquer technique: repeatedly,
identify in a remaining digraph a source, which is a vertex with no
incoming edges, and delete it along with all the edges outgoing from it.
The order in which the vertices are deleted yields a solution to the
topological sorting problem.

Here is an example implementing this idea on the graph above:

<img src="./picture/top-sort-steps.png" width="700" />

Please implement this algorithm in ***sort()*** in
***TopologicalSorting.py***. You can test your code using above example
- ***graph\_example.txt***.

There are many different ways implementing this algorithm. One idea is
to remove the vertex you just deleted from the unvisited list of
vertices, which is initialized as all vertices, until the unvisited list
of vertices is empty.

##### Task 1: courses

One application of topological sorting is courses arrangement which
involves a multitude of interrelated courses with known prerequisites.
For example, the relationship of courses in our CS program at
Westminster is shown below:

<img src="./picture/cs-courses.jpg" width="500" />

The data of this directed graph is stored in ***graph\_courses.txt***,
but ***it is not complete yet***. Please finish this txt file at first
and then run your code on this file. The sorted list will be saved in
***result\_graph\_courses.txt***.

##### Task 2: spider's web

A spider sits at the bottom (point A) of its web, and a fly sits at the
top (F).

<img src="./picture/spider-with-letters.jpg" width="400" />

The data of this directed graph is stored in a *completed* file
***graph\_spider.txt***. Please run your code again on this file to
sorted all vertices topologically and save it to
***result\_graph\_spider.txt***.

##### Task 3: spider and fly

How many different ways can the spider reach the fly by moving along the
web’s lines in the directions indicated by the arrows? Please save your
result in ***result\_spider\_count.txt***.

Hint: use DFS for task 3.

#### What to Submit

You need to submit these files: **TopologicalSorting.py**,
**graph\_courses.txt**, **result\_graph\_courses.txt**,
**result\_graph\_spider.txt** and **result\_spider\_count.txt**. Please
**do not** use other file names. Both lab partners need to submit the
solution separately to the dropbox on Canvas.

</div>
