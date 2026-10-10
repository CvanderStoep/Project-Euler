def remainder(a, n):
    """r = ((a-1)^n + (a+1)^n) mod a^2"""
    return (pow(a - 1, n, a * a) + pow(a + 1, n, a * a)) % (a * a)

def remainder_fast(a, n):
    """r = ((a-1)^n + (a+1)^n) mod a^2"""
    return 2 if n % 2 == 0 else (2 * n * a) % (a * a)

def r_max_brute(a):
    # the remainders repeat with period dividing 2a, so n in 1..2a is enough
    return max(remainder(a, n) for n in range(1, 2 * a + 1))


def r_max(a):
    # (a-1)^n + (a+1)^n = 2 (n even) or 2*n*a (n odd) modulo a^2.
    # Odd n: maximise 2*n*a mod a^2 = a * (2n mod a).
    # a odd  -> 2n mod a can reach a-1      -> a*(a-1)
    # a even -> 2n mod a is even, max a-2   -> a*(a-2)
    return a * (a - 1) if a % 2 else a * (a - 2)


if __name__ == "__main__":
    # sanity checks
    assert remainder(5, 3) == 5  # 4^3 + 6^3 = 280 = 5 (mod 25)
    for a in range(3, 200):
        assert r_max(a) == r_max_brute(a), a

    print(sum(r_max(a) for a in range(3, 1001)))

    total = 0
    for a in range(3, 1001):
        rmax = 0
        for n in range(1, 2 * a + 1):
            r = remainder_fast(a, n)
            if r > rmax:
                rmax = r
                # print(f"n={n}, r={r}")
        total += rmax   

    print(f"Total sum of maximum remainders: {total}")

    print(remainder(5, 3), remainder_fast(5, 3))