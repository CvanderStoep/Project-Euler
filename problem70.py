from mathlib.primes import euler_totient


def are_permutations(a, b):
    return sorted(str(a)) == sorted(str(b))


limit = 10**7
phi = euler_totient(limit)


n_min, q_min = 2, 2
for n in range(2, limit + 1):
    if are_permutations(n, phi[n]):
        q = n / phi[n]
        if q < q_min:
            n_min, q_min = n, q

print(n_min, q_min)
