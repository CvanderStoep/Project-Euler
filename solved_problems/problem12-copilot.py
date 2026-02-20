from math import sqrt

def prime_factors(n):
    """Return prime factorization of n as a dict {prime: exponent}."""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def num_divisors_from_factors(factors):
    """Compute number of divisors from prime factorization."""
    total = 1
    for exp in factors.values():
        total *= (exp + 1)
    return total

def triangle_divisor_count(n):
    """
    Compute number of divisors of T_n = n(n+1)/2
    using factorization of n and n+1.
    """
    if n % 2 == 0:
        a = n // 2
        b = n + 1
    else:
        a = n
        b = (n + 1) // 2

    fa = prime_factors(a)
    fb = prime_factors(b)

    # merge factorizations
    for p, e in fb.items():
        fa[p] = fa.get(p, 0) + e

    return num_divisors_from_factors(fa)

def find_triangle_with_divisors(limit):
    n = 1
    while True:
        d = triangle_divisor_count(n)
        if d > limit:
            triangle = n * (n + 1) // 2
            return triangle, d
        n += 1

triangle, d = find_triangle_with_divisors(500)
print("Triangle number:", triangle)
print("Divisors:", d)
print(prime_factors(triangle))