from helper.utils import is_prime

for p in range(1000, 10000):          # only 4-digit primes matter
    if not is_prime(p):
        continue

    for s in range(1, (10000 - p) // 2):
        a = p + s
        b = p + 2*s

        if not is_prime(a) or not is_prime(b):
            continue

        if sorted(str(p)) == sorted(str(a)) == sorted(str(b)):
            print(p, a, b)
            break
