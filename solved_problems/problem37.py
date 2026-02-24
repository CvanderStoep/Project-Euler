from helper.utils import is_prime

sum_primes = 0
for n in range(10, 1_000_000):
    s = str(n)

# # Snelste eliminaties
# # Verboden digits behalve als ze de eerste digit zijn
#     if any(d in s[1:] for d in "024568"):
#         continue

    if not is_prime(n):
        continue

    is_trunc_prime = True
    left = s
    right = s

    # Truncate both sides in one loop
    for _ in range(len(s) - 1):
        left = left[1:]
        right = right[:-1]

        if not (is_prime(int(left)) and is_prime(int(right))):
            is_trunc_prime = False
            break

    if is_trunc_prime:
        sum_primes += n
        print(n)

print(f'{sum_primes= }')

