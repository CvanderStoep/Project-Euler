from mathlib.primes import is_prime

def numbers_in_layer(n):
    return (2*n-3)**2 + 1, (2*n-1)**2


n_primes = 0
layer = 1
while True:
    layer += 1
    side_length = 2 * layer - 1
    diagonal_numbers = 2 * side_length - 1
    square = 2*layer -1
    _, stop = numbers_in_layer(layer)
    down_right = stop
    down_left = down_right - square + 1
    upper_left = down_left - square + 1
    upper_right = upper_left - square + 1
    if is_prime(down_right):
        n_primes += 1
    if is_prime(down_left):
        n_primes += 1
    if is_prime(upper_right):
        n_primes += 1
    if is_prime(upper_left):
        n_primes += 1
    if n_primes/diagonal_numbers < 0.1:
        print(f'{layer, side_length, diagonal_numbers, n_primes, n_primes/diagonal_numbers= }')
        break
    






