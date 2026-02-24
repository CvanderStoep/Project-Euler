from itertools import permutations
from helper.utils import is_prime
numbers = list(range(1,8))  # tried 9 and 8 digits numbers, but did not exist
print(numbers)

largest_pandigital_prime = 2
for p in permutations(numbers):
    n = int(''.join(str(i) for i in p))
    if is_prime(n):
        largest_pandigital_prime = max(largest_pandigital_prime, n)
print(f'{largest_pandigital_prime= }')
