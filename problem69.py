from mathlib.primes import euler_totient

limit = 1_000_000
phi = euler_totient(limit)

n_max, q_max = 2, 2
for n in range(2, limit + 1):
    q = n / phi[n]
    if q > q_max:
        n_max, q_max = n, q

print(n_max, q_max)
