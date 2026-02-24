from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]

def is_valid(p):
    for i, prime in enumerate(primes):
        if int(''.join(p[i+1:i+4])) % prime != 0:
            return False
    return True

total = 0
for p in permutations('0123456789'):
    if is_valid(p):
        total += int(''.join(p))

print(f'{total= }')