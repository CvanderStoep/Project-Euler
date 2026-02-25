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