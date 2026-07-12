def factorisations(n, start=2):
    """Alle multiplicatieve factorisaties van n."""
    yield [n]
    for i in range(start, int(n**0.5) + 1):
        if n % i == 0:
            for rest in factorisations(n // i, i):
                yield [i] + rest


def minimal_product_sum(N):
    best = {n: float('inf') for n in range(2, N+1)}

    # zoek S tot een redelijke grens
    for S in range(2, 25000):
        for F in factorisations(S):
            k = len(F)
            P = S
            Q = sum(F)
            delta = P - Q
            n = k + delta
            if 2 <= n <= N:
                if max(F) <= n:
                    best[n] = min(best[n], S)

    return best


N = 12_000
sum_set = set()
for key, value in minimal_product_sum(N).items():
    print(key, value)
    sum_set.add(value)
print(sum(sum_set))
