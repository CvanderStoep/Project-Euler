from math import gcd

"""
triplets can be written as:
a = m^2 - n^2, b = 2mn, c = m^2 + n^2
m>n
m-n odd
gcd(m,n) = 1
"""

LIMIT = 1_500_000
counts = {}

# m^2 + n^2 grows fast, so m only needs to go up to sqrt(LIMIT)
m = 2
while 2 * m * (m + 1) <= LIMIT:  # smallest n=1
    for n in range(1, m):
        if (m - n) % 2 == 1 and gcd(m, n) == 1:
            p0 = 2 * m * (m + n)  # primitive perimeter

            # scale primitive triple
            k = 1
            while k * p0 <= LIMIT:
                counts[k * p0] = counts.get(k * p0, 0) + 1
                k += 1
    m += 1

keys_with_one = [k for k, v in counts.items() if v == 1]
print(len(keys_with_one))
