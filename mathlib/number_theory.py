from math import gcd, isqrt

def repeating_decimal(p, q):
    p, q = p // gcd(p, q), q // gcd(p, q)

    t = q
    for prime in (2, 5):
        while t % prime == 0:
            t //= prime

    if t == 1:
        return "", ""

    seen = {}
    digits = []
    remainder = p % q
    pos = 0

    while remainder not in seen:
        seen[remainder] = pos
        remainder *= 10
        digits.append(str(remainder // q))
        remainder %= q
        pos += 1

    start = seen[remainder]
    non_rep = "".join(digits[:start])
    rep = "".join(digits[start:])
    return non_rep, rep

def pythagorean_triples(n):


    triples = []
    for a in range(1, n+1):
        for b in range(a, n+1):
            c2 = a*a + b*b
            c = isqrt(c2)
            if c <= n and c*c == c2:
                triples.append((a, b, c))
    return triples

def sqrt_continued_fraction(N: int):
    """
    Compute the continued fraction expansion of sqrt(N).
    Returns (a0, period) where:
      - a0 is the integer part
      - period is the repeating block [a1, ..., a_L]
    """
    a0 = int(N**0.5)
    if a0 * a0 == N:
        return (a0, [])  # perfect square

    m, d, a = 0, 1, a0
    period = []

    while True:
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d
        period.append(a)
        if a == 2 * a0:
            break

    return (a0, period)

def continued_fraction_e(n):
    # e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...]
    if n == 0:
        return 2
    if n % 3 == 2:
        return 2 * (n + 1) // 3
    return 1
