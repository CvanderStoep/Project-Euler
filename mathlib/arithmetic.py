from math import gcd, isqrt
from decimal import Decimal, getcontext


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


# ------------------------------------------------------------
# Number utilities
# ------------------------------------------------------------

def is_perfect_square(n: int) -> bool:
    """Return True if n is a perfect square."""
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n

def first_N_digits_sqrt(n: int, digits: int) -> str:

    """
Return the first `digits` digits of the decimal expansion of √n,
starting from the integer part and using truncation (not rounding).

The function computes √n with extra internal precision to ensure
that the first `digits` digits are correct, removes the decimal
point, and returns the leading `digits` characters of the resulting
digit string.

Example
-------
>>> first_N_digits_sqrt(2, 10)
'1414213562'
"""
    # Use extra precision so we can safely truncate
    getcontext().prec = digits + 10

    root = Decimal(n).sqrt()
    s = str(root)          # e.g. '1.41421356...'
    s = s.replace('.', '') # remove decimal point
    return s[:digits]         # first 100 digits (including integer part)