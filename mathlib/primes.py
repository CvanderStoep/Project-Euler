from math import isqrt, gcd

def is_prime(n):
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

def prime_factors(n):
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
    primes = []
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [n for n in range(2, limit + 1) if is_prime[n]]


def euler_totient(limit: int) -> list[int]:
    """
    Compute Euler's totient function φ(n) for all integers 0 ≤ n ≤ limit.

    This uses a sieve-based approach:
    - Initialize phi[n] = n.
    - For each prime i, update all multiples j of i using:
          phi[j] -= phi[j] // i
      which applies the multiplicative totient formula.

    Parameters
    ----------
    limit : int
        The maximum integer n for which φ(n) will be computed.

    Returns
    -------
    list[int]
        A list phi where phi[n] gives the value of Euler's totient function φ(n).
    """
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i
    return phi

def relative_primes(n):
    return [k for k in range(1, n) if gcd(k, n) == 1]