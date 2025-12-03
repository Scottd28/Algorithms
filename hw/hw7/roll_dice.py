
def roll_dice(N,M):
    # Your code goes here:
    #Roll a fair six-sided dice N times.
    # The sum of the results is M.

    dices= [float("inf")] * (N+1)
    dices[0] = 0
    for i in range(1, N + 1):
        choices = []
        for i in range(6):
            if


    # for i in range(1, n+1):
    #     for coin in d:
    #         if coin <= i:
    #             n_of_coins[i] = min(n_of_coins[i], n_of_coins[i-coin] + 1)
    if dices[N] == float("inf"):
        return -1
    return dices[N]











    pass




if __name__ == "__main__":
    print(roll_dice(2,7))
    print(roll_dice(3,9))
    print(roll_dice(8,24))
