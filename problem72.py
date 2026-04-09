from mathlib.primes import euler_totient


print(sum(euler_totient(1_000_000)) - 1)
