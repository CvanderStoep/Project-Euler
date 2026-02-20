from itertools import permutations
items = list(range(10))
print(items)

gen_items = permutations(items)

for i in range(1_000_000 -1):
    next(gen_items)
million_number = next(gen_items)
million_number = ''.join(str(x) for x in million_number)
print(million_number)

