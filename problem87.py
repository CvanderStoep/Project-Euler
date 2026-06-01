from mathlib.primes import sieve_of_eratosthenes
from mathlib.decorators import timed

@timed
def compute():
    m = 50_000_000
    numbers = set()

    # Precompute primes and powers
    a2 = sorted(a*a for a in sieve_of_eratosthenes(8000))
    b3 = sorted(b**3 for b in sieve_of_eratosthenes(400))
    c4 = sorted(c**4 for c in sieve_of_eratosthenes(85))

    for A in a2:
        if A >= m:
            break
        for B in b3:
            if A + B >= m:
                break
            for C in c4:
                S = A + B + C
                if S >= m:
                    break
                numbers.add(S)

    print(len(numbers))

compute()


