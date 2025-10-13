<div class="crossnote markdown-preview">

### CMPT 306 Algorithms

#### Fall 2025

------------------------------------------------------------------------

#### Homework \#1 - CoPrime

#### 100 Total Points

##### How Homework are Managed and Graded

You should only work on homework by yourself. This assignment is neither
a paired-up lab nor a group project.

##### Code

Please download and unpack this tar file:

[hw1.tar](./hw1.tar)

which contains one file:

-   CoPrime.py

##### Instructions

Two numbers are said to be co-prime if their only common factor is 1.
For example, 4 and 9 are co-prime as their only common factor is 1.
However, the numbers 4 and 10 are not co-prime. (Co-prime numbers are
also referred to as relatively prime.)

This assignment will involve writing a Python script that is passed two
values M and N, and it will determine all the co-prime pairs between
(1,1) and (M,N). It will present these co-primes by outputting them as a
grid. For example, the following displays the co-prime pairs of of M =
15 N = 15

<img src="./coprimes.png" width="400" />

where an asterisk represents a co-prime pair. The following image shows
the relative positions of each pair (notice that (1,1) is the lower
left-hand corner) where the blue circle is the co-prime pair (4,9), and
the yellow circle indicates (4,10) is not co-prime.

<img src="./coprimes-annotated.png" width="400" />

##### Assignment

Write a Python script that is passed two parameters representing the
pairs to generate. It currently expects two parameters passed on the
command line.

This script provides a few helpful features. Notably, it declares result
as a list of lists. The statement

``` language-python
result = [None] * (m + 1)
```

declares result as a list containing (m + 1) entries where each entry
contains the value None (Python uses None to represent null.)

The statements

``` language-python
for i in range (0, m+1):
    result[i] = ['^'] * (n + 1)
```

assigns each entry in result to be a list of size (n + 1) where each
entry is a '^' character.

The subsequent for loop displays the contents of result.

Please design and implement an algorithm that displays the co-prime
pairs from (1,1) to (m,n). You should not call functions like gcd() from
libraries.

##### What to Submit

You need to submit these files to the dropbox on Canvas:

-   CoPrime.py

Please DO NOT change the names of files you downloaded.

</div>
