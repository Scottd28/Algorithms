<div class="crossnote markdown-preview">

### CMPT 306 Algorithms

#### Fall 2025

------------------------------------------------------------------------

#### Homework \#3 - code2word

#### 100 Total Points

##### How Homework are Managed and Graded

You should only work on homework by yourself. This assignment is neither
a paired-up lab nor a group project.

##### Instruction

This lab will involve writing python codes to find all possible English
words combined by three IATA airport codes.

Please download and unpack this tar file:

-   [hw3.tar](./hw3.tar)

which contains four files:

-   airports\_code.txt
-   words\_nine\_letters.txt
-   code2word\_method1.py
-   code2word\_method2.py

An [IATA airport code](https://en.wikipedia.org/wiki/IATA_airport_code)
is a three-letter code designating many airports around the world,
defined by the International Air Transport Association (IATA). For
example, BNA represents Nashville International Airport and SLC
represents Salt Lake International Airport. There are 4445 codes,
including all medium and large airports around the world, in file
***airports\_code.txt***.

You may wonder is it possible to find an English word which is combined
by three airport codes (codes can be repeat)? The answer is yes! Here is
an example, ABSTRACTS is combined by three codes: ABS (Abu Simbel
Airport in Egypt), TRA (Tarama Airport in Japan), and CTS (New Chitose
Airport in Japan). In this lab, your task is to find all such English
words.

In order to simplify your task, you only need to search from 908
nine-letter long words taking from [10,000 most common English
words](https://github.com/first20hours/google-10000-english). These
words are saved in ***words\_nine\_letters.txt***.

A trivial solution to this lab is to enumerate all permutations of three
codes with replacement from the pool of codes and then to check if the
permutation is one of 908 words. However, via a mathematical estimation,
you will find there are at least P(4445,3) = 87765155940 different
possible combinations of three codes. If we compare each of this
combination of codes with each word, the total number of comparisons is
at least 87765155940\*908 = 79690761593520 <span class="katex"><span
class="katex-mathml">≈</span><span class="katex-html"
aria-hidden="true"><span class="base"><span class="strut"
style="height:0.4831em;"></span><span
class="mrel">≈</span></span></span></span> 80 trillion. We need to find
a better way to do it!

Instead of using permutation method,
[Trie](https://en.wikipedia.org/wiki/Trie) is a wonderful data structure
designed for solving this kind of problem. Basically, trie is a search
tree - an ordered tree data structure which could be used to store a
dictionary. Here is an example from
[wiki](https://en.wikipedia.org/wiki/Trie).

<img src="./Trie_example.png" width="300" />

This is a trie for keys "A","to", "tea", "ted", "ten", "i", "in", and
"inn". After building this trie using these keys, we can apply two basic
methods: has\_key() and has\_subtrie():

-   has\_key(): Indicates whether a given key has value associated with
    this trie.

-   has\_subtrie(): Returns whether a given key is a prefix of another
    key in the trie.

For example, in this trie, these statements are true: has\_key("ted"),
has\_key("inn"), has\_key("in"), has\_subtrie("i"), and
has\_subtrie("te"), while these statements are false: has\_key("t"),
has\_key("te"), has\_subtrie("to"), and has\_subtrie("tea").

In this lab, you do not need to reinvent the wheel - trie. You can use
this library: [pygtrie](https://github.com/google/pygtrie). Simply run
"pip install pygtrie" in the terminal in pycharm to install it.

Here is an example of using pygtrie.

``` language-python
import pygtrie as trie

codes = ["BN", "BNA", "SLC", "USA"]
# build a trie
t = trie.CharTrie()
for code in codes:
    t[code] = True

words = ["B", "BN", "BNA"]
# search words in this trie
for word in words:
    print("has_key(", word, "): ", t.has_key(word))
    print("has_subtrie(", word, "): ", t.has_subtrie(word))
```

Here are test results:

> has\_key( B ): False  
> has\_subtrie( B ): True  
> has\_key( BN ): True  
> has\_subtrie( BN ): True  
> has\_key( BNA ): True  
> has\_subtrie( BNA ): False

##### Two methods

Make sure you understand above example, code, and output before
proceeding to next step. You are supposed to use both has\_key() and
has\_subtrie() in this lab.

We have two different ways solving this **code2word** problem.

###### Method 1

We can use all *codes* to build a trie. In next step, we can break down
a 9-letter long *word* into three successive 3-letter pieces. A word
should be saved if all its three pieces are keys of the trie. The
starting code of this method is **code2word\_method1.py**.

**hint**

Use
[slice](https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/)
of array, like `a[start:end], a[:end], a[start:]`.

###### Method 2

We also can use all *words* to build a trie. But in next step, we should
search *codes* in this trie. The starting code of this method is
**code2word\_method2.py**.

**hint**

Your code should run **less than 20 seconds**.

##### What to Submit

You need to submit four files: **code2word\_method1.py**,
**results1.txt**, **code2word\_method2.py**, and **results2.txt**.
Please **do not** use other file names. Both lab partners need to submit
the solution separately to the dropbox on Canvas.

</div>
