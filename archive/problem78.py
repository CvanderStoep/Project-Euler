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
print(solve_euler_78(1_000_000))
