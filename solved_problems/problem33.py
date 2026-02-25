from mathlib.utils import simplify_fraction
fractions = []
for numerator in range(10, 99):
    for denominator in range(numerator + 1, 100):
        s1 = str(numerator)
        s2 = str(denominator)
        if '0' in s1 and '0' in s2:
            continue
        common = set(s1) & set(s2)
        if not common:
            continue
        c = common.pop()
        s1 = s1.replace(c, "", 1)
        s2 = s2.replace(c, "", 1)
        if int(s1) * denominator == int(s2) * numerator:
            print(numerator, denominator, s1, s2)
            fractions.append((s1, s2))

numerator, denominator = 1, 1
for n, d in fractions:
    numerator *= int(n)
    denominator *= int(d)
print((numerator, denominator), '--> ', simplify_fraction(numerator, denominator))