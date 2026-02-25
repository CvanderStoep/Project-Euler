from math import prod as product
from mathlib.primes import get_primes


# Get primes between 0-10
primes = get_primes(0, 10)
print(primes)  # Output: [2, 3, 5, 7]
print(product(primes))  # Output: 210

smallest_number = 100

while True:
    # print(f'Testing {smallest_number}...')
    for i in range(3, 11):
        if smallest_number % i != 0:
            smallest_number += 2
            break
    else:
        # This runs only if the for-loop did NOT break
        print(f'Smallest number divisible by 1 to 10 is: {smallest_number}')
        break

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

result = 1
for i in range(1, 21):
    result = lcm(result, i)

print(f'Smallest number divisible by 1 to 20 is: {result}')

