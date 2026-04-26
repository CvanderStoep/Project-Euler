from itertools import permutations

numbers = list(range(1, 11))
print(numbers)

def check_magic(p) -> bool:
    a, b, c, d, e, f, g, h, i, j  = p
    s1 = a + b + c
    s2 = d + c + f
    s3 = e + f + g
    s4 = i + g + h
    s5 = b + i + j
    return s1 == s2 == s3 == s4 == s5


def magic_string(p):
    a, b, c, d, e, f, g, h, i, j  = p
    triples = [
        (a, b, c),
        (d, c, f),
        (e, f, g),
        (h, g, i), 
        (j, i, b)
    ]

    # choose rotation so smallest outer value is first
    outer = [a, d, e, h, j]
    start = outer.index(min(outer))

    # rotate triples
    rotated = triples[start:] + triples[:start]

    # flatten into a single string
    return "-".join(str(x) for triple in rotated for x in triple)


solutions = set()
for p in permutations(numbers):
    if check_magic(p):
        s = magic_string(p)
        solutions.add(s)

for s in solutions:
    if len(s) == 30: # 16 digits + 14 dashes
        nums = list(map(int, s.split("-")))
        total = sum(nums[:3])
        print(s, '   sum= ', total)
        