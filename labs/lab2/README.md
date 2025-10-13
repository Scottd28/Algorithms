<div class="crossnote markdown-preview">

### CMPT 306 Algorithms

#### Fall 2025

------------------------------------------------------------------------

#### Lab 2 - Residency Matching Problem

#### Total Points: 100 points

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

##### Overview

This lab will involve solving the Residency Match Problem as described
in class.

##### Starting code

[lab2.tar](./lab2.tar)

##### The Algorithm

Given these two preferences lists:

``` language-text
Residents:
Tom: UT, TN, WA
Jack: TN, UT, WA
Anna: TN, UT, WA

Hospital:
UT: Anna, Tom, Jack
TN: Jack, Anna, Tom
WA: Jack, Tom, Anna
```

For example, Tom prefers UT over TN, UT prefers Anna over Jack.

A one-to-one match between residents and hospitals could be like this:

``` language-text
Tom: UT
Jack: TN
Anna: WA
```

Given a one-to-one match M between residents and hospitals, a pair (r,
h) of resident and hospital is said to be a blocking pair if r and h are
not matched in M, but they prefer each other to their mates in M.

In the previous match, the pair (Anna, UT) is a blocking pair since Anna
prefers UT over WA and UT prefers Anna over Tom.

The task of this stable matching problem is to find a one-to-one match
between residents and hospitals, so that there is no blocking pair in
it.

The stable matching of the above lists is {Tom: WA, Jack: TN, Anna: UT}.

Working with your partner, step through the Residency Match algorithm
for the following preference files and ensure you are comfortable with
the algorithm. Only begin coding once you are comfortable with the
algorithm!

``` language-text
Hospitals:
CA, Doris, Charlie, Alex, Barbara
VT, Barbara, Doris, Alex, Charlie
WA, Doris, Alex, Charlie, Barbara
NY, Charlie, Barbara, Alex, Doris

Residents:
Alex , CA, VT, WA,NY
Barbara, CA, NY, WA, VT
Charlie, VT, CA, WA, NY
Doris,NY,VT,WA,CA
```

The respective lists of residents and hospital preferences are stored in
these two files:

-   hospitalsprefs.txt

-   residentsprefs.txt

You can solve this problem however you wish, but one general idea is to
follow this chart which we have discussed in class: (You can exchange
hospital and resident in this chart to make another version of this
solution.)

<img src="./CMPT306-lab2.png" width="700" />

##### How to run your code

There are several places marked by "pass" in the starting code. Your are
supposed to replace "pass" by your code. You do not need to modify any
other places in the starting code.

You can run your code using this line in the terminal:
`python ResidencyMatch.py residentsprefs.txt hospitalsprefs.txt`

You can also run your code in PyCharm by selecting Modify Run
Configuration in the menu under ResidencyMatch.py:

<img src="run.png" width="600" />

and then set the parameters and the working directory:

<img src="run_args.png" width="600" />

##### How to debug your code

To debug your code in PyCharm, enter Debug Mode and then set breakpoints
and track variable values:

<img src="debug.png" width="600" />

##### Python Background Hints

Your logic will likely rely on dictionaries as well as list operations.

**Helpful List Operations**

Imagine you have the following list in Python:

``` language-python
fruits = ['apple', 'banana', 'cherry', 'date']
```

-   'apple' is at position zero of the list, 'banana' is at position 1,
    and so forth.

-   The **index()** function returns the index of a particular item in
    the list. For example,

    ``` language-python
    fruits.index('cherry')
    ```

    returns 2.

-   One easy way to obtain the first item in the list is by using the
    **pop()** operation, specifying the position in the list you want to
    pop:

    ``` language-python
    snack = fruits.pop(0)
    ```

    where snack is assigned the value 'apple'.

**Helpful Dictionary Operations**

Dictionaries map **\[key:value\]** pairs. Dictionaries can be quite
powerful - For example we could map a string to a list:

``` language-python
lunch = {'fruits':['apple', 'banana', 'cherry', 'date']}
```

where lunch is the dictionary and it specifies that the string 'fruits'
is mapped to the list containing \['apple', 'banana', 'cherry', 'date'\]

-   To retrieve the first fruit in the list for lunch, we could perform

    ``` language-python
    favorite = (lunch['fruits'])[0]
    ```

    where favorite is the value 'apple'.

-   To remove the third fruit, we could perform

    ``` language-python
    dessert = (lunch['fruits']).pop(2)
    ```

    where dessert is the value 'cherry'.

##### What to Submit

Be sure to include your names at the top of each source file. Refer to
program grading guidelines for best practices for submitting source
code.

Please submit your ResidencyMatch.py to Canvas. Be sure to include the
names of each partner on the submission.

Please do not use other file names. Both lab partners need to submit the
solution separately to the dropbox on Canvas.

</div>
