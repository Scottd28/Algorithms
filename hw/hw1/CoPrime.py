'''
    CoPrime.py

    Generates a graph of the m x n co-primes
    
    [Scott R]
'''

import sys
from math import remainder

'''
generates the co-primes in an m x n matrix
'''
def coprimes(m, n):
    '''
    creates a list of size n each with
    each element initialized to None
    '''
    result = [None] * (m + 1)

    '''
    each element in the list is now a
    list of size m where each value
    is initialized to a space ' '
    '''
    for i in range(0,m+1):
        result[i] = [''] * (n + 1)


    '''
        YOUR WORK WILL GO HERE
    '''
    for r in range(1,m+1):
        # x[:] is a list "slice"
        for l in range(1,n+1):
            bigger = 0;
            smaller = 0;



            # Find bigger of the two numbers
            if (r > l ):
                bigger = r;
                smaller = l;
            else:
                 bigger = l;
                 smaller = r;




            while(smaller != 0): # while the remainer is not 0
                remainder =  bigger % smaller;
                bigger = smaller;
                smaller = remainder;

            if (bigger == 1): # the GCD was 1
                result[(m+1)-r][l] = '*';  # it is a coprime
            else:
                result[(m + 1) - r][l] = ' '  # it is not a coprime



    '''
    output the contents of result
    '''
    for x in result:
        # x[:] is a list "slice"
        for y in x[:]:
            '''
            by putting a comma at the end, we prevent a newline
            '''
            print(y + ' ', end="")

        print()


# behaves like main() method

if __name__ == "__main__":
    # some error checking
    if len(sys.argv) != 3:
        print('Usage\n python CoPrime [int] [int]')
        quit()

    coprimes(int(sys.argv[1]), int(sys.argv[2]))
