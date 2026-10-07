from itertools import permutations

numbers = list(range(1, 7))
print(numbers)

def check_magic(p) -> bool:
    a, b, c, d, e, f = p
    s1 = a + b + c
    s2 = d + c + e
    s3 = b + e + f
    return s1 == s2 == s3


def magic_string(p):
    a, b, c, d, e, f = p
    triples = [
        (a, b, c),
        (d, c, e),
        (f, e, b),
    ]

    # choose rotation so smallest outer value is first
    outer = [a, d, f]
    start = outer.index(min(outer))

    # rotate triples
    rotated = triples[start:] + triples[:start]

    # flatten into a single string
    return "".join(str(x) for triple in rotated for x in triple)


solutions = set()
for p in permutations(numbers):
    if check_magic(p):
        s = magic_string(p)
        solutions.add(s)

for s in solutions:
    print(s, '  ', int(s[0]) + int(s[1]) + int(s[2]))
        