import math
from helper.utils import pythagorean_triples

p_max = 1
total_p_max = 0
for p in range(1, 1001):
    triples = pythagorean_triples(p)
    total_p = len([t for t in triples if sum(t) == p])
    print(p, total_p) if total_p > total_p_max else None
    if total_p > total_p_max:
        total_p_max = total_p
        p_max = p

print(p_max, total_p_max)


