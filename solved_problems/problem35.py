from helper.utils import rotate_left, is_prime
number_circular_primes = 0
for n in range(2,1_000_000):
    if not is_prime(n):
        continue
    n_string = str(n)
    l = len(n_string)
    circular_prime = True
    for _ in range(l-1):
        n_string = rotate_left(n_string)
        if not is_prime(int(n_string)):
            circular_prime = False
            break
    if circular_prime:
        number_circular_primes += 1
        print(n)
print(f'{number_circular_primes= }')
