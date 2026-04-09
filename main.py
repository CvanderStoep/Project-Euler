from math import gcd, floor, ceil


def count_pairs(N: int):
    g = gcd
    total = 0

    for d in range(1, N + 1):
        start = floor(d / 3) + 1
        end = ceil(d / 2) - 1

        for p in range(start, end + 1):
            if g(p, d) == 1:
                total += 1

    return total


print(count_pairs(12_000))
