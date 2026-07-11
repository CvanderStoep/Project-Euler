from itertools import product

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']

combinations = product(l1, repeat=2)
for combination in combinations:
    print(combination)