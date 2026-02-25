from functools import lru_cache

def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def rotate_left(s, k=1):
    k %= len(s)
    return s[k:] + s[:k]

def is_palindrome(s):
    return str(s) == str(s)[::-1]

def collatz_generator(n):
    while True:
        yield n
        if n == 1:
            break
        n = n // 2 if n % 2 == 0 else 3 * n + 1

@lru_cache(maxsize=None)
def collatz_chain(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz_chain(n // 2)
    return 1 + collatz_chain(3 * n + 1)