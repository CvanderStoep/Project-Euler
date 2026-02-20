from sympy import factorint
from helper.utils import is_prime, prime_factors





# Example usage
if __name__ == "__main__":
    number = 600851475143
    result = prime_factors(number)
    print(f"Prime factors of {number}: {result}")
    largest = max(result)
    print(f"Largest prime factor: {largest}")
    print(f"Is {largest} prime (helpers.is_prime)? {is_prime(largest)}")
    if factorint is not None:
        print(factorint(600851475143))
    else:
        print("sympy not installed; skipping factorint() output")