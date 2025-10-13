import Closest

def testClosest1():
    sequence = [-13, 5, 18, 7, -14, 21]
    # assert actual == expected
    assert Closest.closest_pair(sequence) == (-13, -14)



def testClosest2():
    sequence = [-13, 5, 18, 7, -14, 21, -13]
    # assert actual == expected
    assert Closest.closest_pair(sequence) == (-13, -13)