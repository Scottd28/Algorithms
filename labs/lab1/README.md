<div class="crossnote markdown-preview">

### CMPT 306 Algorithms

#### Fall 2025

------------------------------------------------------------------------

#### Lab 1 - Introduction to Python

#### Due at 9 AM on August 27, 2025

##### How Labs are Managed and Graded

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
    [link](http://cs.westminstercollege.edu/~jingsai/files/Cheating-or-Collaboration.html).

##### Objectives

-   Understand the basics of Python programming

-   Run and develop Python tests

-   Explore the debugger running Python using VS Code.

##### Anaconda and PyCharm

Please refer this [page](../../handouts/software/software.html) to
install necessary software and this
[page](../../handouts/software/pycharm.html) to set up your first
assignment.

##### Code

Download the following tar file and unpack it as a folder lab1. For Mac
users, you can run `tar xvf lab1.tar` in the terminal to unpack it. For
Windows users, you can install free software
[7-Zip](https://www.7-zip.org/) to unpack it.

[lab1.tar](./lab1.tar)

As a class, we will use the Fibonacci files to demonstrate how to design
tests and run Python programs, as well as the debugging process.

-   Fibonacci.py

-   RunFib.py

-   testFib.py

-   Closest.py

##### Closest Pair Problem

The closest pair problem is a simple geometric problem whereby you have
n points in a plane and you must find the closest pair of points. For
example, if your points are

``` language-text
[-13, 5, 18, 7, -14, 21]
```

the closest pair are (-13, -14) with a distance of 1 separating them.

**Your program only needs to return any one pair of closest numbers if
there are more than one pairs having the same closest distance.**

The simplest algorithm is a brute force whereby you compare each point
to all others, and keep track of the closest pair of points.

The Python program Closest.py sketches a simple start to the problem.
However it is missing the implementation of the closest\_pair()
function.

Notice the stubbed version of closest\_pair() returns the tuple (-100,
100) . This is one interesting feature of Python - the ability for
functions to return multiple values.

##### Steps

1.  Write a testing case to test the closest\_pair() function. (This is
    known as test-driven development whereby you write your test before
    implementing the function/method you are testing.) Name your Python
    program containing your test as testClosest.py (Look at testFib.py
    as an example for writing a new test.) Do not name it as
    TestClosest.py

The actual lines of test code will look something like

``` language-python
expected = (-13, -14)
actual = Closest.closest_pair([-13, 5, 18, 7, -14, 21])
```

followed by an assertion that actual equals expected.

The \[-13, 5, 18, 7, -14, 21\] in the call to closest\_pair() creates a
list with the values -13, 5, 18, 7, -14, 21.

The existing implementation of closest\_pair() should fail this test.

2.  Implement the closest\_pair() function

Implement closest\_pair() so that your implementation passes your test.

Choose the brute force algorithm that compares each number with every
other number.

I strongly suggest you and your partner think about the algorithm for
solving this problem before implementing it in python.

This may require using the debugger.

##### Run

Please refer this [page](../../handouts/software/pycharm.html) to run,
test, and debug your code.

##### Same Values in List

Once you get your implementation working for the above test with the
list containing \[-13, 5, 18, 7, -14, 21\], next make sure it works if
the list contains the same values. For example:

``` language-python
expected = (-13, -13)
actual = Closest.closest_pair([-13, 5, 18, 7, -14, 21, -13])
```

followed by an assertion that expected equals actual.

##### What to Submit

Be sure to include your names at the top of each source file. Refer to
program grading guidelines for best practices for submitting source
code.

Please submit your Closest.py as well as testClosest.py test files to
Canvas. Be sure to include the names of each partner on the submission.

Please do not use other file names. Both lab partners need to submit the
solution separately to the dropbox on Canvas.

</div>
