'''
Closest pair problem

This returns the closest pair of numbers.

Usage:
    
    python closest_pair.py [size of list of numbers]

[Heidi Andre]

[Scott R]
'''

import random
import sys

'''
return the distance between two parameters
'''
def distance(a,b):
    return abs(a-b)


'''
populate the array with listSize unique random numbers between 1 ... 5000
'''
def populate(listSize):
    a = []
    count = 0

    while count < listSize:
        number = random.randint(1,5000)
        if number in a:
            continue
        else:
            a.append(number)
            count += 1

    return a

'''
now determine the closest pair
using brute force algorithm
'''
def closest_pair(values):
    pt_a = values[0]
    pt_b = values[1]

    final_a = pt_a
    final_b = pt_b

    dist1 = distance(pt_a, pt_b)
    length = len(values)

    for i in range(length):
        for pt in values[1 + i:]:
            dist2 = distance(values[i], pt)
            if dist2 < dist1:
                dist1 = dist2
                final_a = values[i]
                final_b = pt

    return (final_a, final_b)
'''
This behaves just like the Java main() method
'''
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage python Closest.py [number of points]')
        quit()
    else:
        numbers = populate(int(sys.argv[1]))

        closest = closest_pair(numbers)

        print('The closest numbers are', closest[0], 'and', closest[1])
