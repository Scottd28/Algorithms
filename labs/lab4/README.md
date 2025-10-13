<div class="crossnote markdown-preview">

### CMPT 306 Algorithms

#### Fall 2025

------------------------------------------------------------------------

#### Lab 4 - DFS and BFS

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

##### Instruction

Please download and unpack this tar file:

-   [lab4.tar](./lab4.tar)

which contains following files:

-   Graph.py \# Class
-   UseGraph.py \# Usage example
-   testGraph.py \# Testing
-   graph1.txt
-   graph2.txt
-   graph3.txt
-   graph4.txt

##### graph-1:

![](./graph-1.png)

##### graph-2:

![](./graph-2.png)

##### graph-3:

<img src="./graph-3.png" width="350" />

##### graph-4:

<img src="./graph-4.png" width="200" />

This lab will involve designing breadth-first and depth-first
searches/traversals unweighted and undirected graphs. Be sure to read
the [graph handout](../../handouts/graphs/index.html) as well as [notes
on graphs](../../handouts/graphs/graph-handouts.pdf) prior to beginning
this lab.

You will need to write four functions in **Graph.py** and test them on
four graphs in **testGraph.py** in this lab:

1.  DFS\_recur() \# Find a DFS path using recursive method
2.  DFS\_stack() \# Find a DFS path using a stack
3.  BFS() \# Find a BFS path using a queue
4.  hasCycle() \# Determine if there is a cycle in a graph

You will get at most 5 extra points if you work on another function
(This one is not required):

1.  shortestpath(p,q) \# Find the shortest path between p and q in a
    graph using BFS. **You can assume that p and q are connected in one
    component.**

##### Instruction of hasCycle()

The algorithm may also encounter an edge leading to a previously visited
vertex other than its immediate predecessor (i.e., its parent in the
tree). Such an edge is called a back edge (DFS) or cross edge (BFS)
because it connects a vertex to its ancestor. As for checking for a
cycle presence in a graph, if the graph does not have back or cross
edges, the graph is clearly acyclic.

In hasCycle, you may need to define a dictionary ImmediateParent = {} to
record the relationship between child and immediate parent. Return true
if a visited child of a vertex is not this vertex's parent, which is
ImmediateParent\[vertex\].

##### Instruction of shortestpath()

In shortestpath, you can label each vertex using a level when searching
a BFS path starting from p. The level of starting vertex p is 0, the
level of all children of p is 1, and so on. The algorithm stops when
reaching to end vertex q. Then the shortest path between p and q is
level\[q\] - level\[p\].

##### Hints

1.  You should follow and modify the pseudo code in the handout to work
    on three functions: DFS\_recur(), DFS\_stack(), and BFS(). Each of
    these functions needs to return a path, which is a string
    initialized as "".

2.  Use a dictionary to represent the adjacency list of an undirected
    and unweighted graph. I already read and put all four graphs in
    self.adjacencyList.

3.  All children of one node have been sorted in \_*init\_*. You **do
    not** need to sort them again in the code. You can directly use a
    for loop over children of one node when it is needed.

##### Testing

You can use the testing tool in PyCharm or using command line
`pytest testGraph.py` to test all functions or
`pytest testGraph.py -k testDFS_recursive` to test one specific
function.

##### Example of using dictionary, stack, and queue in python.

``` language-python
# dictionary
# d is a dictionary
d = {'a':['b','c'], 'p':['e']}
# print all keys of d
print("All keys of d:")
for k in d: 
    print(k)
    
# check is a is a key in d
if 'a' in d: print("a is a key")
    
# print all children of key a in d
print("All children of d: ", d['a'])

# list
# remove one element from a list
l = ['a','b','c','a']
l.remove('a') # Remeber that only first a is removed!

# stack
# initialize stack as an empty list
stack = []
# push
stack.append('a')
# pop
vertex = stack.pop()

# queue
# initialize queue as an empty list
queue = []
# add
queue.insert(0,'a')
# remove
vertex = queue.pop()
```

``` language-text
All keys of d:
a
p
a is a key
All children of d:  ['b', 'c']
```

##### What to Submit

You need to submit this file: **Graph.py**. Please **do not** use other
file names. Both lab partners need to submit the solution separately to
the dropbox on Canvas.

</div>
