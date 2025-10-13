'''
Hangman.py

Heidi and Scott
'''

import sys
import random

class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
        file = open('words.txt','r')
        self.words = []
        self.wordguess = []
        for line in file:
            self.words.append(line.rstrip())

    '''
    Outputs the current status of the guesses
    '''
    def printword(self):
        for c in self.wordguess:
            print(c,end="")
        print()

    def playgame(self):
        # generate random word
        word = self.words[random.randint(0,len(self.words)-1)]
        #print word
        self.wordguess = ['_'] * len(word)

        guesses = 0
        guessed_ch = []
        
        while guesses < 10:
            print('Number of guesses:' + str(guesses))
            print(self.wordguess)
            ch = input('\nEnter a guess:').lower()
            # if alphabetic character
            if ch.isalpha():
                # only one character input
                if len(ch) != 1:
                    print('Only one character is allowed in each input')
                else:
                    # if letter has been guessed
                    if ch not in guessed_ch:
                        guesses += 1
                        guessed_ch.append(ch)

                        # if letter is in the word
                        if ch in word:
                            # find every index of the letter in the word
                            letter = list(filter(lambda x: word[x] == ch, range(len(word))))
                            # substituting ch in each index (letter) for wordguess corresponding to word
                            for i in range(len(letter)):
                                for j in range(len(self.wordguess)):
                                    if letter[i] == j:
                                        self.wordguess[j] = ch
                        else:
                            print('The letter "' + ch + '" does not occur.')
                    else:
                        print('The letter "' + ch + '" is already used.')


            else:
                print('Only allow alphabetic characters.')

            # if word has been guessed (not more spaces left)
            if '_' not in self.wordguess:
                print("Congratulations!")
                print("The word is: " + word)
                break
            # if you ran out of guesses
            elif guesses == 10 :
                print('Sorry dude, the word is ' + word)
                break


if __name__ == "__main__":

    game = Hangman()

    game.playgame()
