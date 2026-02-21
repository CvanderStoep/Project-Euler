from functools import lru_cache
import time
from math import gcd, isqrt

def simplify_fraction(a, b):
    g = gcd(a, b)
    return a //g, b //g

def timed(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

def repeating_decimal(p, q):   

    # Reduce fraction
    p, q = p // gcd(p, q), q // gcd(p, q)

    # Remove factors of 2 and 5 (terminating part)
    t = q
    for prime in (2, 5):
        while t % prime == 0:
            t //= prime

    if t == 1:
        return "", ""  # no repeating part

    # Find repeating cycle by long division
    seen = {}
    digits = []
    remainder = p % q
    pos = 0

    while remainder not in seen:
        seen[remainder] = pos
        remainder *= 10
        digits.append(str(remainder // q))
        remainder %= q
        pos += 1

    start = seen[remainder]
    non_repeating = "".join(digits[:start])
    repeating = "".join(digits[start:])
    return non_repeating, repeating

def pythagorean_triples(n):
    """Returns pythagorean triples with maximum value of n"""
    triples = []
    for a in range(1, n+1):
        for b in range(a, n+1):  # b >= a to avoid duplicates like (3,4,5) and (4,3,5)
            c2 = a*a + b*b
            c = isqrt(c2)
            if c <= n and c*c == c2:
                triples.append((a, b, c))
    return triples

def is_prime(n):
    """Return True if n is prime (n >= 2). Simple deterministic check."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fib_generator():
    """Generate Fibonacci numbers indefinitely"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_factors(n):
    """
    Calculate all prime factors of a given number.
    
    Args:
        n: A positive integer
        
    Returns:
        A list of prime factors
    """
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors

def get_primes(start, end):
    """Return all prime numbers between start and end (inclusive)."""
    primes = []
    for num in range(max(2, start), end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def sieve_of_eratosthenes(limit):
    """Return all prime numbers up to the given limit (inclusive)."""
    if limit < 2:
        return []
    
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    return [num for num in range(2, limit + 1) if is_prime[num]]

def divisors(n):
    """
    Return all positive divisors of n.
    """
    divs = set()
    d = 1
    
    while d * d <= n:
        if n % d == 0:
            divs.add(d)
            divs.add(n // d)
        d += 1
    
    return sorted(divs)

def collatz_generator(n):
    while True:
        yield n
        if n == 1:
            break
        n = n // 2 if n % 2 == 0 else 3 * n + 1

@lru_cache(maxsize=None)
def collatz_chain(n):
    """returns the lenght of a collatz chain starting with n"""
    if n == 1:
        return 1
    else:
        if n %2 == 0:
            return 1 + collatz_chain(n //2)
        else:
            return 1 + collatz_chain(3 * n + 1)
        
def is_abundant(n):
    # a number is abundant if the sum of its proper divisors > number
    proper_divisors = divisors(n)[:-1]
    return sum(proper_divisors) > n

def rotate_left(s, k = 1):
    k %= len(s)
    return s[k:] + s[:k]

def is_palindrome(s):
    return s == s[::-1]