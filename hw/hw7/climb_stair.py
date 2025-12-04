'''
There are n steps in a stair.
You can either climb 1 or 2 steps each time.
Find how many different ways you can climb to the top?
'''
ways = {0: 1, 1: 1, 2:2} # 0:1 because we count climbing 0 steps as a way
def climb_stair(n):
    # Your code goes here:
    global ways

    if n in ways:
        return ways[n]
    else:
        ways[n] = climb_stair(n-1)+climb_stair(n-2)
        return ways[n]






if __name__ == "__main__":
    print(climb_stair(10))
    print(climb_stair(20))
    print(climb_stair(30))

