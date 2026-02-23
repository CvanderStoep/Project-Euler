from helper.utils import is_prime, get_primes
import math

def is_perfect_square(n):
    r = math.isqrt(n)
    return r * r == n

def composite_numbers():
    n = 9
    while True:
        if not is_prime(n):
            yield n
        n += 2

N = 10_000
primes = get_primes(3, N)
# print(primes)

def satisfies_goldbach(c, primes):
    for p in primes:
        if p > c:
            return False
        if is_perfect_square((c - p) // 2):
            return True
    return False


for c in composite_numbers():
    if not satisfies_goldbach(c, primes):
        print(c)
        break

