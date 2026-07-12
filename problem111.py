import math
from itertools import product

def simple_sieve(limit):
    """Return list of primes up to limit using a basic sieve."""
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start:limit+1:step] = [False] * ((limit - start)//step + 1)
    return [i for i, is_p in enumerate(sieve) if is_p]


# Precompute small primes for fast primality test up to 10^10
PRIMES = simple_sieve(int(math.isqrt(10**10)))

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    limit = int(math.isqrt(n))
    for p in PRIMES:
        if p > limit:
            break
        if n % p == 0:
            return False
    return True


def generate_numbers_with_repeated_digit(n_digits: int, d: int, repeats: int):
    """
    Genereer alle n-digit getallen waarin digit d precies 'repeats' keer voorkomt.
    Andere posities worden gevuld met digits != d.
    """
    positions = list(range(n_digits))
    # Kies welke posities de repeated digit krijgen
    # We doen dit via een bitmask-benadering: True = d, False = andere digit
    mask = [True] * repeats + [False] * (n_digits - repeats)

    # We genereren unieke mask-permutaties via set
    from itertools import permutations
    seen_masks = set()
    for m in permutations(mask):
        if m in seen_masks:
            continue
        seen_masks.add(m)

        # Voor de False-posities moeten we digits != d kiezen
        other_positions = [i for i, flag in enumerate(m) if not flag]
        k = len(other_positions)
        # Andere digits: 0..9 behalve d
        other_digits = [x for x in range(10) if x != d]

        for combo in product(other_digits, repeat=k):
            digits = [None] * n_digits
            # Vul d op True-posities
            for i, flag in enumerate(m):
                if flag:
                    digits[i] = d
            # Vul andere digits
            for pos, val in zip(other_positions, combo):
                digits[pos] = val

            # Geen leading zero
            if digits[0] == 0:
                continue

            num = 0
            for x in digits:
                num = num * 10 + x
            yield num


def S_10_d(n_digits: int, d: int) -> int:
    """
    Bereken S(10, d): som van alle n-digit primes met
    maximale herhaling van digit d.
    """
    # We proberen eerst repeats = n_digits, n_digits-1, ...
    for repeats in range(n_digits, 0, -1):
        total = 0
        found_any = False
        for num in generate_numbers_with_repeated_digit(n_digits, d, repeats):
            if is_prime(num):
                total += num
                found_any = True
        if found_any:
            # Dit repeats is M(n,d); total is S(n,d)
            return total
    return 0


def euler_111():
    n_digits = 10
    ans = 0
    for d in range(10):
        ans += S_10_d(n_digits, d)
    return ans


if __name__ == "__main__":
    print(euler_111())
