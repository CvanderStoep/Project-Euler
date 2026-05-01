# def is_divisible_by_one_million(n: int) -> bool:
#     return n % 1_000_000 == 0


# def count_unique_change(n, numbers):
#     dp = [0] * (n + 1)
#     dp[0] = 1

#     for coin in numbers:
#         for amount in range(coin, n + 1):
#             dp[amount] += dp[amount - coin]

#     return dp[n]

# #compared to problem 76, N itself is also a solution
# #this algorithm takes too long to run, need different solution

# N = 1
# while True:
#     numbers = tuple(range(1, N))
#     count = count_unique_change(N, numbers) + 1
#     print(f'{N= }')  
#     if is_divisible_by_one_million(count):
#         print(N)
#         break
#     N += 1


def solve_euler_78(mod=1_000_000):
    # p[n] = number of partitions of n modulo mod
    p = [1]  # p[0] = 1

    n = 1
    while True:
        total = 0
        k = 1

        # Euler's pentagonal recurrence
        while True:
            g1 = k * (3 * k - 1) // 2
            g2 = k * (3 * k + 1) // 2

            if g1 > n:
                break

            sign = -1 if (k % 2 == 0) else 1

            total += sign * p[n - g1]
            if g2 <= n:
                total += sign * p[n - g2]

            k += 1

        total %= mod
        p.append(total)

        if total == 0:
            return n

        n += 1


# Run it
print(solve_euler_78())
