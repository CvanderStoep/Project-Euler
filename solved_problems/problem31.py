from functools import lru_cache

coins = [1, 2]
total_amount = 3

@lru_cache(None)
def make_change(amount, index=0):
    if amount == 0:
        return 1
    if amount < 0:
        return 0

    ways = 0
    for i in range(index, len(coins)):
        ways += make_change(amount - coins[i], i)

    return ways

print(make_change(total_amount))


# using Dynamic Programming
coins = [1, 2, 5, 10, 20, 50, 100, 200]
total_amount = 200

def make_change_dp(coins, total_amount):
    dp = [0] * (total_amount + 1)
    dp[0] = 1  # one way to make 0: use nothing

    for coin in coins:
        for amount in range(coin, total_amount + 1):
            dp[amount] += dp[amount - coin]

    return dp[total_amount]

number_of_changes = make_change_dp(coins, total_amount)
print(number_of_changes)