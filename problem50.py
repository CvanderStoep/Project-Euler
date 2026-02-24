from helper.utils import sieve_of_eratosthenes
N = 1_000_000

primes = sieve_of_eratosthenes(N)
number_of_primes = len(primes)
max_prime, max_length = 2, 1
prime_set = set(primes)
for start_index in range(number_of_primes):
    running_sum = 0
    for end_index in range(start_index, number_of_primes):
        running_sum += primes[end_index]
        if running_sum > N:
            break
        if running_sum in prime_set:
            length = end_index - start_index + 1
            if length > max_length:
                max_length = length
                max_prime = running_sum

print(max_prime, max_length)


