from mathlib.primes import relative_primes

# print(euler_totient(12000))
# print(relative_primes(12000))

N = 12_000
# pairs = []
count = 0
for d in range(1, N + 1):
    rel_primes = relative_primes(d)
    rel_primes = [p for p in rel_primes if d / 3 < p < d / 2]
    for n in rel_primes:
        # pairs.append((n, d))
        count += 1


# print(len(pairs))
print(count)
