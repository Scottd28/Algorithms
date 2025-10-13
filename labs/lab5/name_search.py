import numpy as np
import argparse

class NameSearch:

    def __init__(self, Name_List, Name_Algorithm, Name_Length):
        # Matrix of the word search puzzle
        self.matrix = np.load("./data/matrix.npy")
        # Name of the algorithm
        self.Name_Algorithm = Name_Algorithm
        # Length of the name
        self.Name_Length = Name_Length
        # List of all potential names
        with open("./data/names/"+Name_List+".txt", 'r') as f:
            self.names = f.read().splitlines()
        self.names = [n.upper().strip() for n in self.names]

    def match_BruteForce(self, pattern, text):
        # String matching by brute force
        # Your code goes here:
        # print(text)
            #print(pattern)

            for line in text:
                for i in range(len(line) - len(pattern) +1): # for i in the amount of options we have
                    # print("hey:" + "".join(text[i:i + len(pattern)]))
                    if line[i:i+len(pattern)] == pattern: #this is the word
                        path = line[i:i+len(pattern)]
                        # print("almost there" + path)
                        return path


    def match_Horspool(self, pattern, text):
        # String matching by Horspool's algorithm
        # Your code goes here:
        m = len(pattern)



    #BUILD THE TABLE
        alphabet = {chr(i): len(pattern) for i in range(ord('A'), ord('Z')+1)}

        for j in range(m-1):
            char = pattern[j]
            alphabet[char] = (m-1) -j

    #HARSPOOOL ALGORITHM
        for line in text:
            path = ''
            i = m-1
            n = len(line)
            while i < n:
                matchedChar = 0;

                while matchedChar <= m-1 and pattern[(m-1)-matchedChar] == line[i-matchedChar]:
                    # print("almost")
                    # print(pattern[(m - 1) - matchedChar] + " " + line[i - matchedChar])
                    path += pattern[(m - 1) - matchedChar]
                    matchedChar += 1

                if matchedChar == (m):

                    return path[::-1] # https://stackoverflow.com/questions/931092/how-do-i-reverse-a-string-in-python
                else:
                    i += alphabet.get(line[i], m)
        return None












    def search(self):
        # pattern is each name in self.names
        # text is each horizontal, vertical, and diagonal strings in self.matrix



        for pattern in self.names: # for each name
            text = []
            for r in range(20):
                text.append("".join(self.matrix[r, :])) # all rows
            for c in range(20):
                text.append("".join(self.matrix[:, c]))  # all columns
            for i in range(20):
                text.append("".join(self.matrix.diagonal(i)))
            for i in range(20):
                text.append("".join(self.matrix.diagonal(-i)))
            flipped_matrix = np.fliplr(self.matrix)
            for i in range(20):
                text.append("".join(flipped_matrix.diagonal(i)))  # diagonals starting from top row




            if self.Name_Algorithm == "BruteForce":
                result = self.match_BruteForce(pattern, text)
                if result != None:
                 print(result)
            elif self.Name_Algorithm == "Horspool":
                result = self.match_Horspool(pattern, text)
                if result != None:
                    print(result)
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Word Searching')
    parser.add_argument('-name', dest='Name_List', required = True, type = str, help='Name of name list')
    parser.add_argument('-algorithm', dest='Name_Algorithm', required = True, type = str, help='Name of algorithm')
    parser.add_argument('-length', dest='Name_Length', required = True, type = int, help='Length of the name')
    args = parser.parse_args()

    # Example:
    # python name_search.py -algorithm BruteForce -name Mexican -length 5

    obj = NameSearch(args.Name_List, args.Name_Algorithm, args.Name_Length)
    obj.search()