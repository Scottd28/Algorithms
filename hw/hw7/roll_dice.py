
def roll_dice(N,M):
    # Your code goes here:
    #Roll a fair six-sided dice N times.
    # The sum of the results is M.


    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # 1 way to reach sum 0 because we count nothing as a way

    for n in range(1, N + 1): #dices
        for t in range(1, M + 1): #target

            total = 0

            for face in range(1, 7):
                if t - face >= 0:
                    total += dp[n - 1][t - face]

            dp[n][t] = total


    return dp[N][M]



if __name__ == "__main__":
    print(roll_dice(2,7))
    print(roll_dice(3,9))
    print(roll_dice(8,24))
