'''
Give change for amount n using the minimum number of coins
of denominations d1 < d2 < . . . < dm, where d1=1 and
assuming availability of unlimited
quantities of coins for each of the m denominations.

For example, n = 6 and coin denominations 1, 3, and 4.
 The answer is 2 because you can use two 3 to add up to 6.
'''

def change_making(d, n):
    n_of_coins = [float("inf")] * (n+1)
    n_of_coins[0] = 0
    for i in range(1, n+1):
        for coin in d:
            if coin <= i:
                n_of_coins[i] = min(n_of_coins[i], n_of_coins[i-coin] + 1)
    if n_of_coins[n] == float("inf"):
        return -1
    return n_of_coins[n]








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

