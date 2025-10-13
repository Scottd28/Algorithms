<div class="crossnote markdown-preview">

### CMPT 306 Algorithms

#### Fall 2025

------------------------------------------------------------------------

#### Lab 5 - Name Searching

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

#### Code

Please download and unpack this tar file:

[lab5.tar](./lab5.tar)

#### Personal Name in Different Cultures

A personal name or full name is the set of names by which an individual
is known \[1\]. In Western culture, nearly all individuals possess at
least one given name (also known as a first name), together with a
surname (also known as a last name or family name). Many individuals
also have a middle name. For example, if a person's first/given name is
Jacob, middle name is Mark, and last/sur/family name is Bayes, we can
call his name as `Jacob Mark Bayes` or `Bayes, Jacob Mark`. There are
many different name conventions in other cultures. Here are three
examples:

-   In Arabic culture, Arabic names have historically been based on a
    long naming system. Most Arabs have a chain of names. This system
    remains in use throughout the Arab world \[2\]. An Arabic name is a
    combination of a person's own name, father's name, grandfather's
    name, ..., and family/tribe name if this person has \[3\]. For
    example, `Muhammad Salman Amin`, his own name is Muhammad, his
    father's name is Salman, and his grandfather's name is Amin.

-   In East Asia (for example in China, Japan and Korea), the order of
    the name follows eastern order, which put family name at first and
    given name at last. For example, if a Chinese person's given name is
    Heping and family name is Liu, this person will be called as
    `Liu Heping` in China. The middle name does not exist in Chinese
    names. His name will be switched as `Heping Liu` in western order
    when he lives in United States.

-   In Spanish culture, a typical Spanish (Latin / Hispanic) name
    consists of four parts: first name, second first name, father's
    first surname, and mother's first surname \[4\]. The "middle" names
    are not middle names as we know them in English-speaking cultures
    \[5\] and there are two surnames in a full name. For example,
    `Raul Martinez Garcia` is married to `Alicia Fernandez Ochoa` and
    have a son who they decide to name Jose Roberto, then the boy's full
    name is `Jose Roberto Martinez Fernandez`. The first surname is
    primary, and the second sub-ordinate -- exactly the reverse of the
    middle and last names of non-Spanish speaking cultures
    (non-Hispanics). To a Hispanic, therefore, "Ornelas, Miguel
    Ledesma," would denote Miguel Ornelas Ledesma rather than, as a
    non-Hispanic would expect, Miguel Ledesma Ornelas.

#### Instructions

Make sure you understand **both** brute force and Horspool's algorithms
to find a pattern in a string before working on this lab. The pseudocode
of Horspool's algorithm can be found in this handout
[String\_Matching.pdf](../../handouts/brute-force/string_matching.pdf).

*Optional Task (10 points):* The complexity of Horspool's algorithms is
O(n+m), where n and m are the sizes of string and pattern. There is a
O(n+m) algorithm named KMP. You could earn 10 additional points by
implement KMP for this lab. For more information about KMP, please visit
[here](https://cp-algorithms.com/string/prefix-function.html) or
[here](https://www.geeksforgeeks.org/dsa/kmp-algorithm-for-pattern-searching/).

In this lab, you will need to search a group of names in a matrix of
`word search puzzle` below using both brute force and Horspool's
algorithms. For example, name `Mark` is on position (16, 13), (17,14),
(18,15), (19,16).

``` language-text
                                         1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2
                                                           0 1 2 3 4 5 6 7 8 9 0
                                        ________________________________________
                                       |                                         |
                                    1  | X K R J Z G D K C K R Q A N P K A I Y C |
                                    2  | L D Z C B O U I G H N Q V N K X A D I Q |
                                    3  | B H R P X A K S F G I M S E P C Z Y T G |
                                    4  | D A M X P C Y M A V A J K D Z X F C I N |
                                    5  | P R J A K L W E D S J Z F O L F U Q R G |
                                    6  | M U C C N Y T L S X M P P O P Z V X B B |
                                    7  | C N F R M U H B H N U E O O T Y Q O P E |
                                    8  | S K Z L B W E L H T H U S U G Q C Q J D |
                                    9  | F D F Z G X X L D X A I H G N A A O H A |
                                    10 | Y P V Q A R V S V M M O F G J X R V Z S |
                                    11 | Z R L J B B J L Z L M T J K J C Y D S M |
                                    12 | A C W K S L D G K C A O I H T W O J E P |
                                    13 | N I T C C W O U T T D E U F R H K R M I |
                                    14 | D L W A M G K I L I P D Z A T A V T Q M |
                                    15 | R O B S W V C V O L A R F F R J J W O E |
                                    16 | E P G T H C Q R H Q A N M A U F R C B T |
                                    17 | S E N I D U P D W K E T Y A Y J J U E Q |
                                    18 | W Z P L H L A H N B Z H B I R D H J K Z |
                                    19 | V V G L X P S N Q V W D X U S K B Z N R |
                                    20 | X D W O K M F G G W X P H G I K H L N X |
                                       |_________________________________________|
```

You can use a name as **pattern** and a horizontal, vertical, or
diagonal string of the matrix as **text** to search the pattern in the
text. For example, given a matrix below,

``` language-text
                                                  A B C
                                                  D E F
                                                  G H I
```

you will **only** need to search a pattern in these strings:

-   horizontal string from left to right: ABC, DEF, GHI
-   vertical string from top to bottom: ADG, BEH, CFI
-   diagonal string from top left to bottom right: G, DH, AEI, BF, C
-   diagonal string from top right to bottom left, A, BD, CEG, FH, I

A feasible way to organize your code is as following:

``` language-text
for pattern in self.names:
    for text in row/column/diagonal:
        if self.Name_Algorithm == "BruteForce":
             self.match_BruteForce(pattern, text)
        elif ....
```

#### Tasks

1.  A Mexican person's given names are Andres Manuel. The length of his
    father's surname is 5 and the length of his mother's surname is 8.
    Both two names are in a list
    [Mexican.txt](./lab5/data/names/Mexican.txt) \[7\] and in the word
    search puzzle. What is this person's full name?

2.  An Arabic person's own name is Harun. The length of his father's
    name is 7 and the length of his grandfather's name is 8. Both two
    names are in a list [Arabic.txt](./lab5/data/names/Arabic.txt) \[8\]
    and in the word search puzzle. What is this person's full name?

3.  A Chinese person's given name is Tianyi. The length of his family
    name is 5, which is in a list
    [Chinese.txt](./lab5/data/names/Chinese.txt) \[6\] and in the word
    search puzzle. What is his name in eastern order?

Please answer these three questions using BOTH brute force and
Horspool's algorithms and write all names in result.txt.

#### Python

You are not allowed to use `in` operation in a way like
`pattern in text`. You can use `for item in list` or `for key in dict`.
Since you are learning brute force, you have to manually implement the
brute force and Horspool algorithms using for loops and numpy.

**args**

You will need to run your code either using the configuration or running
the following commands in terminal:

``` language-python
python name_search.py -algorithm NameOfAlgorithm -name NameOfCulture -length LengthOfName
```

For example, you can run this command to find a Mexican name with 5
letters using brute force algorithm:

``` language-python
python name_search.py -algorithm BruteForce -name Mexican -length 5
```

You can use above command to run your code case by case or you can type
`python run.py` to run all cases at once.

**numpy**

Numpy (<http://www.numpy.org/>) is a fundamental package for scientific
computing with Python. In this lab, we will use numpy array instead of
list.

Here are some basic usage of numpy. For more information, please visit
this page (<http://cs231n.github.io/python-numpy-tutorial/#numpy>).

By using the numpy package, you can **easily retrieve one
row/column/diagonal line from a matrix**.

``` language-python
# create a numpy array
matrix = np.array([["A","B","C"],["D","E","F"],["G","H","I"]])
>>>
array([['A', 'B', 'C'],
       ['D', 'E', 'F'],
       ['G', 'H', 'I']], dtype='<U1')

# return the shape (row, column) of a numpy array
nRows, cColumns = matrix.shape

# access an element of numpy array
letter = matrix[row, column]

# return all letters on row r as a list
row = matrix[r, :]

# return all letters on column c as a list
column = matrix[:, c]

# return the diagonals 
>>> matrix.diagonal(0)
array(['A', 'E', 'I'], dtype='<U1')
>>> matrix.diagonal(1)
array(['B', 'F'], dtype='<U1')
>>> matrix.diagonal(-2)
array(['G'], dtype='<U1')
>>> matrix[:,::-1].diagonal(0)
array(['C', 'E', 'G'], dtype='<U1')
```

**debug**

Use this argument in the json file to debug your code and modify it for
different cases:
`"args": ["-algorithm", "BruteForce", "-name", "Mexican", "-length", "5"]`

#### Hint

1.  All letters in the matrix and names are capital letters. `ord()` is
    a function to return the int value of a letter in [ASCII
    table](http://www.asciitable.com/). For example, `ord("A")` is 65
    and `ord("P")` is 80. You can use `ord()` to convert a letter to a
    number when setting up the shift table in Horspool's algorithm. For
    example, you can initialize a list `table` with length 26.
    `table[ord("A")-65]` is the shift size for letter A.  
      

    You also can use a dictionary to record the table using the letter
    as key and the best shifting size as value.  
      

2.  If you do not use the numpy package to retrieve the
    row/column/diagonal lines from the matrix (**not recommended unless
    you want to earn extra points**), you can manually write the code on
    your own :

-   If the current position \[row, column\] in the matrix is \[r,c\],
    the next position on the bottom right direction is \[r+1, c+1\] and
    the next position on the bottom left direction is \[r+1, c-1\].

``` language-text
                                          r-1, c-1         r-1, c+1
                                                     r,c
                                          r+1, c-1         r+1, c+1  
```

-   For a matrix with m rows and n columns, there are m+n-1 diagonals
    from top left to bottom right and m+n-1 diagonals from top right to
    bottom left as well.

#### Extra Points

You will receive at most 5 points if you do not use library functions
like diagonal() from numpy in this lab.

#### What to Submit

You need to submit these files to the dropbox on Canvas:

-   name\_search.py
-   result.txt. (You must save names in correct formats based on
    different name conventions in different cultures in provided
    result.txt. You should not just save the output of your code in your
    own result.txt.)

Please DO NOT change the names of files you downloaded.

#### Reference

-   \[1\] <https://en.wikipedia.org/wiki/Personal_name>
-   \[2\] <https://en.wikipedia.org/wiki/Arabic_name>
-   \[3\] <https://www.quora.com/How-do-Arabic-names-work>
-   \[4\]
    <http://lrc.salemstate.edu/hispanics/other/Naming_Conventions_of_Spanish-Speaking_Cultures.htm>
-   \[5\]
    <https://www.quora.com/How-do-middle-names-and-last-names-work-in-Mexico-culture-in-Spanish>
-   \[6\] <https://www.jiawen.net/Chinesenamestext.txt>
-   \[7\]
    <https://en.wikipedia.org/wiki/List_of_common_Spanish_surnames>
-   \[8\] <https://family.disney.com/baby-names/arabic-names/>

</div>
