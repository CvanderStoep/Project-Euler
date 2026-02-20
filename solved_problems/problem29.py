terms = set()
for a in range(2, 101):
    for b in range(2, 101):
        n = a ** b
        terms.add(n)
print(len(terms))

