from helper.utils import prime_factors

def distinct_pf(n):
    return set(prime_factors(n))

for n in range(2, 1_000_000):
    p1 = distinct_pf(n)
    if len(p1) != 4:
        continue

    p2 = distinct_pf(n + 1)
    if len(p2) != 4:
        continue

    p3 = distinct_pf(n + 2)
    if len(p3) != 4:
        continue

    p4 = distinct_pf(n + 3)
    if len(p4) != 4:
        continue

    print(n, p1, p2, p3, p4)
    break
