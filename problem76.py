from functools import lru_cache


@lru_cache(None)
def make_change_unique(n, start=0):
    if n == 0:
        return ((),)  # tuple of empty tuple
    if n < 0:
        return ()

    results = []
    for i in range(start, len(numbers)):
        coin = numbers[i]
        for tail in make_change_unique(n - coin, i):
            results.append((coin,) + tail)

    return tuple(results)


# Convert tuples back to lists if you want them pretty
N = 60
numbers = tuple(range(1, N))
# unique_sets = [list(t) for t in make_change_unique(N)]
# print(unique_sets)
# print("count =", len(unique_sets))

print("count =", len(make_change_unique(N)))

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
