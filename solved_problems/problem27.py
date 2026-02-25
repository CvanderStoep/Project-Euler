from mathlib.primes import is_prime
def form(a, b, n):
    return n*n + a * n + b

max_prime_length = 0
a_max, b_max = 0, 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while True:
            number = form(a, b, n)
            if not is_prime(number):
                break
            n += 1
        if n > max_prime_length:
            max_prime_length = n
            a_max, b_max = a, b

print(f'{a_max, b_max, max_prime_length= }')
print(f'{a_max * b_max= }')
