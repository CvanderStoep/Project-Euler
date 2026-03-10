from mathlib.primes import is_prime
from itertools import combinations, product
import sys

for n_digits in range(5, 10):
    for n_wildcards in range(2, 5):
        patterns = []
        n_fixed = n_digits - n_wildcards

        # choose 2 wildcard positions out of 5


        for wc_positions in combinations(range(n_digits), n_wildcards):
            # the other 3 positions must be digits 0–9
            for digits in product(range(10), repeat=n_fixed):
                pattern = ["*"] * n_digits
                digit_index = 0

                for pos in range(n_digits):
                    if pos not in wc_positions:
                        pattern[pos] = str(digits[digit_index])
                        digit_index += 1

                patterns.append("".join(pattern))

        # print(len(patterns))   # should be 10000
        # print(patterns[:20])   # preview
        max_count = 0
        primes = []
        for pattern in patterns:
            prime_family = []
            # print(pattern)
            for d in range(10):
                p = pattern.replace("*", str(d))
                prime_family.append(int(p))
            # print(prime_family)
            count = sum(1 for n in prime_family if n > 10**(n_digits-1) and is_prime(n))
            if count > max_count:
                primes = prime_family
                max_count = count
        primes = [p for p in primes if is_prime(p)]
        print(primes)
        print(f'{n_digits,n_wildcards ,max_count= }')
        if max_count >= 8:
            sys.exit()


