from functools import lru_cache

N = 50

@lru_cache(None)
def solve(pos):
    if pos == N:
        return 1

    total = solve(pos + 1)  # 1-cell tile
    for tile in (2, 3, 4):
        if pos + tile <= N:
            total += solve(pos + tile)
    return total

print(solve(0))
