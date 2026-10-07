from mathlib.sequences import fib_generator

import math

def first_9_digits(n):
    # log10(n) = k + f, where k is integer, f fractional
    log10n = math.log10(n)
    frac = log10n - math.floor(log10n)

    # first 9 digits = floor(10^(frac + 8))
    return int(10 ** (frac + 8))

def is_tail_pandigital(f):
    # check last 9 digits pandigital (1-9 each exactly once)
    f = f % 10**9
    # s = str(f)
    # if len(s) < 9:
    #     return False
    # s = s[-9:]
    return set(str(f)) == set("123456789")


def is_head_pandigital(f):
    # check first 9 digits pandigital (1-9 each exactly once)
    f = first_9_digits(f)
    # s = str(f)
    # if len(s) < 9:
    #     return False
    # s = s[:9]
    return set(str(f)) == set("123456789")



f = fib_generator()
fib = next(f)
k = 1
while True:
    fib = next(f)
    if is_head_pandigital(fib) and is_tail_pandigital(fib):
        print(k)
        break
    k += 1

    


