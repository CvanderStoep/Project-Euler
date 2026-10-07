from mathlib.primes import get_primes
PRIMES = get_primes(2, 100)
print(PRIMES)

TARGET = 4_000_000
REQUIRED = 2 * TARGET - 1

best_n = float('inf')

def search(idx, current_n, current_divisors, max_exp):
    global best_n

    if current_divisors > REQUIRED:
        best_n = min(best_n, current_n)
        return

    if idx == len(PRIMES):
        return

    p = PRIMES[idx]

    for exp in range(1, max_exp + 1):
        new_n = current_n * (p ** exp)
        if new_n >= best_n:
            break

        new_divisors = current_divisors * (2 * exp + 1)
        search(idx + 1, new_n, new_divisors, exp)

search(0, 1, 1, 100)

print("Smallest n =", best_n)

