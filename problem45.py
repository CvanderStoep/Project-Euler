def triangle(n):
    return n * (n + 1) // 2

def pentagonal(n):
    return n * (3 * n - 1) // 2

def hexagonal(n):
    return n * (2 * n - 1)

N = 100000
pents = set([pentagonal(i) for i in range(1, N)])
trians = set([triangle(i) for i in range(1, N)])
hexas = set([hexagonal(i) for i in range(1, N)])

overlap = pents & trians & hexas
print(overlap)

