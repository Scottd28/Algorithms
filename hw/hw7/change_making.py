'''
Give change for amount n using the minimum number of coins
of denominations d1 < d2 < . . . < dm, where d1=1 and
assuming availability of unlimited
quantities of coins for each of the m denominations.

For example, n = 6 and coin denominations 1, 3, and 4.
 The answer is 2 because you can use two 3 to add up to 6.
'''
ways = {}
def change_making(d, n):
    global ways
    if n in ways:
        return ways[n]
    else:
        choices = []
        for coin in d:
            if n % coin == 0:
                #find the best coin combo for n
                print("here")
                choices.append(n/coin)

        return ways[n]





if __name__ == "__main__":
    d=[1,3,4,5,6]
    n=10
    print(change_making(d,n))
    
    d=[1,2,4,6,8,10,22,23]
    n=40
    print(change_making(d,n))

    d=[1,2,10,11,12,15,19,30]
    n=1900
    print(change_making(d,n))

