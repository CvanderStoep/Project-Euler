from math import gcd

def simplify_fraction(a, b):
    g = gcd(a, b)
    return a // g, b // g

def divisors(n):
    """Return all positive divisors of n."""
    divs = set()
    d = 1
    while d * d <= n:
        if n % d == 0:
            divs.add(d)
            divs.add(n // d)
        d += 1
    return sorted(divs)

def is_abundant(n):
    """Return True if n is an abundant number."""
    proper = divisors(n)[:-1]
    return sum(proper) > n