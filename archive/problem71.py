import math

# the closest value of n/d to the left of 3/7: floor(3d-1/7)
pairs = []
for d in range(1, 1_000_000):
    n = (3*d - 1) // 7
    if n > 0 and math.gcd(n, d) ==1:
        pairs.append((n, d))

sorted_pairs = sorted(pairs, key=lambda p: p[0] / p[1])
print(sorted_pairs[-1])
