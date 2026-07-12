def count_unique_change(n, numbers):
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in numbers:
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]

    return dp[n]


N = 100
numbers = tuple(range(1, N))
print("count =", count_unique_change(N, numbers))
