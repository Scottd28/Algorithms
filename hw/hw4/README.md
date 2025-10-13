<div class="crossnote markdown-preview">

### CMPT 306 Algorithms

#### Fall 2025

------------------------------------------------------------------------

#### Homework 4 - Longest Pattern Lock

#### How Homework are Managed and Graded

You should only work on homework by yourself. This assignment is neither
a paired-up lab nor a group project.

##### Instruction

Please download and unpack this tar file:

-   [hw4.tar](./hw4.tar)

which contains these files:

-   PatternLock.py
-   draw.py
-   test.py

Pattern lock is a very common way to secure your smartphone. Here is one
possible design of the pattern lock:

<img src="./picture/lock_example.png" width="200" />

However, this password "Z" is not very hard to be hacked because the
length of this password is very short and the pattern is too simple. So,
in this assignment, let's find and draw the longest pattern lock in term
of the length of the password under two different rules.

##### Coordinate

In order to calculate the length of a password, we convert nine vertices
on the pattern lock to nine points on a x-y plane as shown below. For
example, the coordinate of point 1 is (0,0) and the coordinate of point
6 is (2,1).

<img src="./picture/coordinate.png" width="300" />

##### Path

A password on the pattern lock can be defined as a continuous line
segments. A password is thus also a path. We will use password and path
interchangeably in this assignment. The length of a password is the sum
of distances between every two adjacent points on the path.

If we use a string to represent a password, the above password "Z" is
"7895123" or "3215987", which length is distance(point 7, point8) +
distance(point 8, point9) + distance(point 9, point5) + distance(point
5, point1) + distance(point 1, point2) + distance(point 2, point3) =
<span class="katex"><span
class="katex-mathml">$4 + 2\\sqrt{2}$</span><span class="katex-html"
aria-hidden="true"><span class="base"><span class="strut"
style="height:0.7278em;vertical-align:-0.0833em;"></span><span
class="mord">4</span><span class="mspace"
style="margin-right:0.2222em;"></span><span class="mbin">+</span><span
class="mspace" style="margin-right:0.2222em;"></span></span><span
class="base"><span class="strut"
style="height:1.04em;vertical-align:-0.1328em;"></span><span
class="mord">2</span><span class="mord sqrt"><span
class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
style="height:0.9072em;"><span class="svg-align" style="top:-3em;"><span
class="pstrut" style="height:3em;"></span><span class="mord"
style="padding-left:0.833em;"><span
class="mord">2</span></span></span><span style="top:-2.8672em;"><span
class="pstrut" style="height:3em;"></span><span class="hide-tail"
style="min-width:0.853em;height:1.08em;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MDBlbSIgaGVpZ2h0PSIxLjA4ZW0iIHZpZXdib3g9IjAgMCA0MDAwMDAgMTA4MCIgcHJlc2VydmVhc3BlY3RyYXRpbz0ieE1pbllNaW4gc2xpY2UiPjxwYXRoIGQ9Ik05NSw3MDIKYy0yLjcsMCwtNy4xNywtMi43LC0xMy41LC04Yy01LjgsLTUuMywtOS41LC0xMCwtOS41LC0xNApjMCwtMiwwLjMsLTMuMywxLC00YzEuMywtMi43LDIzLjgzLC0yMC43LDY3LjUsLTU0CmM0NC4yLC0zMy4zLDY1LjgsLTUwLjMsNjYuNSwtNTFjMS4zLC0xLjMsMywtMiw1LC0yYzQuNywwLDguNywzLjMsMTIsMTAKczE3MywzNzgsMTczLDM3OGMwLjcsMCwzNS4zLC03MSwxMDQsLTIxM2M2OC43LC0xNDIsMTM3LjUsLTI4NSwyMDYuNSwtNDI5CmM2OSwtMTQ0LDEwNC41LC0yMTcuNywxMDYuNSwtMjIxCmwwIC0wCmM1LjMsLTkuMywxMiwtMTQsMjAsLTE0Ckg0MDAwMDB2NDBIODQ1LjI3MjQKcy0yMjUuMjcyLDQ2NywtMjI1LjI3Miw0NjdzLTIzNSw0ODYsLTIzNSw0ODZjLTIuNyw0LjcsLTksNywtMTksNwpjLTYsMCwtMTAsLTEsLTEyLC0zcy0xOTQsLTQyMiwtMTk0LC00MjJzLTY1LDQ3LC02NSw0N3oKTTgzNCA4MGg0MDAwMDB2NDBoLTQwMDAwMHoiPjwvcGF0aD48L3N2Zz4=)</span></span></span><span
class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
style="height:0.1328em;"></span></span></span></span></span></span></span>

In this assignment, we should draw the password using all 9 points since
we want to find the longest password. For example, one possible such
path "123456789" using all 9 points is

<img src="./picture/path_example.png" width="350" />

The length of "123456789" is <span class="katex"><span
class="katex-mathml">$6 + 2\\sqrt{5}$</span><span class="katex-html"
aria-hidden="true"><span class="base"><span class="strut"
style="height:0.7278em;vertical-align:-0.0833em;"></span><span
class="mord">6</span><span class="mspace"
style="margin-right:0.2222em;"></span><span class="mbin">+</span><span
class="mspace" style="margin-right:0.2222em;"></span></span><span
class="base"><span class="strut"
style="height:1.04em;vertical-align:-0.1328em;"></span><span
class="mord">2</span><span class="mord sqrt"><span
class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
style="height:0.9072em;"><span class="svg-align" style="top:-3em;"><span
class="pstrut" style="height:3em;"></span><span class="mord"
style="padding-left:0.833em;"><span
class="mord">5</span></span></span><span style="top:-2.8672em;"><span
class="pstrut" style="height:3em;"></span><span class="hide-tail"
style="min-width:0.853em;height:1.08em;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MDBlbSIgaGVpZ2h0PSIxLjA4ZW0iIHZpZXdib3g9IjAgMCA0MDAwMDAgMTA4MCIgcHJlc2VydmVhc3BlY3RyYXRpbz0ieE1pbllNaW4gc2xpY2UiPjxwYXRoIGQ9Ik05NSw3MDIKYy0yLjcsMCwtNy4xNywtMi43LC0xMy41LC04Yy01LjgsLTUuMywtOS41LC0xMCwtOS41LC0xNApjMCwtMiwwLjMsLTMuMywxLC00YzEuMywtMi43LDIzLjgzLC0yMC43LDY3LjUsLTU0CmM0NC4yLC0zMy4zLDY1LjgsLTUwLjMsNjYuNSwtNTFjMS4zLC0xLjMsMywtMiw1LC0yYzQuNywwLDguNywzLjMsMTIsMTAKczE3MywzNzgsMTczLDM3OGMwLjcsMCwzNS4zLC03MSwxMDQsLTIxM2M2OC43LC0xNDIsMTM3LjUsLTI4NSwyMDYuNSwtNDI5CmM2OSwtMTQ0LDEwNC41LC0yMTcuNywxMDYuNSwtMjIxCmwwIC0wCmM1LjMsLTkuMywxMiwtMTQsMjAsLTE0Ckg0MDAwMDB2NDBIODQ1LjI3MjQKcy0yMjUuMjcyLDQ2NywtMjI1LjI3Miw0NjdzLTIzNSw0ODYsLTIzNSw0ODZjLTIuNyw0LjcsLTksNywtMTksNwpjLTYsMCwtMTAsLTEsLTEyLC0zcy0xOTQsLTQyMiwtMTk0LC00MjJzLTY1LDQ3LC02NSw0N3oKTTgzNCA4MGg0MDAwMDB2NDBoLTQwMDAwMHoiPjwvcGF0aD48L3N2Zz4=)</span></span></span><span
class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
style="height:0.1328em;"></span></span></span></span></span></span></span>,
which is likely not the largest one.

Not all permutations of "123456789" are paths. We should follow one of
the following two rules when designing a password:

###### Rule 1 of Path

You **CANNOT** directly draw a line segment from a to b without passing
the middle point c. For example, "132456987" is not a feasible path
since you cannot draw a line segment from 1 to 3 without passing 2.
"123754896" is also not a feasible path since you cannot draw a line
segment from 3 to 7 without passing 5. The picture below is one feasible
longest path "592761834" under this rule:

<img src="./picture/one_result_rule1.png" width="350" />

###### Rule 2 of Path

You **CAN** directly draw a line segment from a to b without passing the
middle point c **if point c has already been used before a and b in the
path**. For example, "213456987" is not a feasible path under rule 1,
but is a feasible path under rule 2 since 2 has been used before 1 and 3
in this path. The picture below is one feasible longest path "519283764"
under this rule:

<img src="./picture/one_result_rule2.png" width="350" />

In this assignment, please find all paths having the longest length
under each rule. You are also required to save and draw these paths.

##### matplotlib

We will use matplotlib package to draw the password. Please use "pip
install matplotlib" or "pip3 install matplotlib" to install matplotlib.

##### Requirement

1.  Your code should be run less than 10 seconds for each rule.

#### Verify Your Answer

Here is the excepted output of this lab. You also can call verify() in
the class to verify your answer. Or you can call draw\_first\_result()
to draw one path of your answer.

``` language-python
> python PatternLock.py

The longest length using rule 1 is:
17.066689404871624

All paths with longest length using rule 1 is:
['276183495', '294381675', '438167295', '492761835', '516729438', '518349276', '534927618', '538167294', '572943816', '576183492', '592761834', '594381672', '618349275', '672943815', '816729435', '834927615']

True

The longest length using rule 2 is:
17.779271744364845

All paths with longest length using rule 2 is:
['519283764', '519467382', '537281946', '537649182', '573461928', '573829164', '591643728', '591827346']

True
```

### Python

Please read through and practice these python examples before starting
work on this lab. Please try to use most of these python skills in your
lab to make your code very simple, elegant, and pythonic.

``` language-python
from itertools import permutations
# permutations of "123"
p = permutations("123")
for i in p:
    print(i)
print()

# permutations of 2 elements in "123"
p = permutations("123",2)
for i in p:
    print(i)
```

``` language-text
('1', '2', '3')
('1', '3', '2')
('2', '1', '3')
('2', '3', '1')
('3', '1', '2')
('3', '2', '1')

('1', '2')
('1', '3')
('2', '1')
('2', '3')
('3', '1')
('3', '2')
```

``` language-python
# list comprehensive 
# generate a list in one line of code 
a = [i for i in range(5)]
print(a)

b = [(i,j) for i,j in permutations("123",2)]
print(b)

c = {i:(i,i+1) for i in range(3)}
for key in c:
    print(key,c[key])
```

``` language-text
[0, 1, 2, 3, 4]
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
0 (0, 1)
1 (1, 2)
2 (2, 3)
```

``` language-python
# join elements in a list 
a = ['1','2','3']
print(''.join(a))
print()

p = permutations("123")
for i in p:
    print(''.join(i))
```

``` language-text
123

123
132
213
231
312
321
```

``` language-python
# string
a = "465789321"

# find if 65 in a
if "65" in a:
    print(True)
    
# find index of 57 in a
if a.index("57") == 2:
    print(True)

# slice elements in a after index 3 (including 3)
print(a[3:])

# slice elements in a before index 4 (not including 4)
print(a[:4])
```

``` language-text
True
True
789321
4657
```

``` language-python
# str() and int()
print("integer 1 to string " + str(1))
print(1+int("3"))

# sum()
print(sum(range(10)))
```

``` language-text
integer 1 to string 1
4
45
```

### What to Submit

You need to submit five files: **PatternLock.py**,
**result\_rule1.txt**, **result\_rule2.txt**, **one\_result\_rule1.png**
and **one\_result\_rule2.png**. Please **do not** use other file names.
Both lab partners need to submit the solution separately to the dropbox
on Canvas.

</div>
