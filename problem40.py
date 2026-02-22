champernowne = ''.join(str(n) for n in range(1, 1_000_000))

product = 1
for i in range(7):
    product *= int(champernowne[10**i -1])
print(product)


# algorithm made using CoPilot
def champernowne_digit(n: int) -> int:
    """Return the nth digit (1-indexed) of the Champernowne constant."""
    k = 1
    count = 9

    # Step 1: find the block of k-digit numbers
    while n > k * count:
        n -= k * count
        k += 1
        count *= 10

    # Step 2: locate the exact number
    n -= 1  # zero-index
    number = 10**(k - 1) + n // k
    digit_index = n % k

    # Step 3: extract the digit
    return int(str(number)[digit_index])

import math

product = math.prod(champernowne_digit(10**i) for i in range(7))
print(product)

