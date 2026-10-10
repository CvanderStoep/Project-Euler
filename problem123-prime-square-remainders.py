def primes():
    """Yield primes in order using an incremental sieve."""
    composites = {}
    q = 2
    while True:
        if q not in composites:
            yield q
            composites[q * q] = [q]
        else:
            for p in composites.pop(q):
                composites.setdefault(p + q, []).append(p)
        q += 1


def remainder(n, p):
    # (p-1)^n + (p+1)^n mod p^2: expand binomially, only the first two terms survive.
    # n even -> 2, n odd -> 2*n*p (mod p^2)
    return 2 if n % 2 == 0 else (2 * n * p) % (p * p)


def solve(limit):
    for n, p in enumerate(primes(), start=1):
        if remainder(n, p) > limit:
            return n


if __name__ == "__main__":
    # sanity checks against the problem statement
    assert remainder(3, 5) == 5
    for n, p in enumerate(primes(), start=1):
        if n > 200:
            break
        assert remainder(n, p) == ((p - 1) ** n + (p + 1) ** n) % (p * p)
    assert solve(10**9) == 7037
    print(solve(10**10))