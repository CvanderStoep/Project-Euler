from mathlib.primes import sieve_of_eratosthenes

def count_unique_change(n, numbers):
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in numbers:
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]

    return dp[n]
N = 1
max_count = 5000
while True:
    primes_list = sieve_of_eratosthenes(N) 
    count = count_unique_change(N, primes_list)
    # print(N, "count =", count)
    if count > max_count:
        print(f"{N= }, {count= }")
        break
    N += 1

print(sieve_of_eratosthenes(11))

