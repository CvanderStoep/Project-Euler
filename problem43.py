from itertools import permutations
numbers = list(range(10))

primes = [2, 3, 5, 7, 11, 13, 17]

total_sum = 0
for p in permutations(numbers):
    n = ''.join(str(i) for i in p)
    divisible = True
    for i in range(1, 8): 
        d = int(n[i:i+3])
        if d % primes[i-1] == 0:
            continue
        else:
            divisible = False
            break
    if divisible:
        print(p)
        total_sum += int(n)

print(f'{total_sum= }')

#==================

def valid(p):
    return all(int(''.join(p[i+1:i+4])) % primes[i] == 0 for i in range(7))

total = sum(int(''.join(p)) for p in permutations('0123456789') if valid(p))
print(total)

#=================

def is_valid(p):
    for i, prime in enumerate(primes):
        if int(''.join(p[i+1:i+4])) % prime != 0:
            return False
    return True

total = 0
for p in permutations('0123456789'):
    if is_valid(p):
        total += int(''.join(p))

print(total)