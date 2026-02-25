from mathlib.primes import sieve_of_eratosthenes, get_primes


# Example usage
limit = 1000
primes = sieve_of_eratosthenes(limit)
print(f"Primes up to {limit}: {primes[-10:]}...")  # Print only the last 10 primes for brevity
print(f"Total number of primes up to {limit}: {len(primes)}")
print(f"Sum of all primes up to {limit}: {sum(primes)}")

print(sieve_of_eratosthenes(7))
print(get_primes(1,7))