from mathlib.primes import is_prime

def generate_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Example usage
if __name__ == "__main__":
    prime_generator = generate_primes()
    for _ in range(10001):  # Change the range for more primes
        print(next(prime_generator))