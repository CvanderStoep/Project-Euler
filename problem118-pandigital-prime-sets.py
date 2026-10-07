from itertools import permutations
from functools import lru_cache

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

FULL = (1 << 9) - 1  # bit d-1 represents digit d
print(FULL)  # 511

# cnt[mask] = how many primes use exactly the digits in mask (each once)
cnt = [0] * (FULL + 1)

digits = range(1, 10)
for r in range(1, 10):
    for p in permutations(digits, r):
        last = p[-1]
        # quick filter: only 1-digit primes may end in an even digit or 5
        if r > 1 and (last % 2 == 0 or last == 5):
            continue
        n = int("".join(map(str, p)))
        if is_prime(n):
            mask = 0
            for d in p:
                mask |= 1 << (d - 1)
            cnt[mask] += 1

@lru_cache(maxsize=None)
def count(used: int) -> int:
    if used == FULL:
        return 1
    remaining = FULL & ~used
    low = remaining & -remaining          # lowest unused digit
    rest = remaining ^ low
    total = 0
    sub = rest
    while True:                            # iterate all submasks of `rest`
        s = sub | low
        if cnt[s]:
            total += cnt[s] * count(used | s)
        if sub == 0:
            break
        sub = (sub - 1) & rest
    return total

print(count(0))   # 44680

print(list(permutations(range(1, 5), 3)))