from math import comb
from mathlib.decorators import timed
from time import perf_counter

t0 = perf_counter()
total = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if comb(n, r) > 1_000_000:
            total += 1
print(f'{total= }')
t1 = perf_counter()

print(f"time={t1 - t0:.6f}s")
print(t1)


