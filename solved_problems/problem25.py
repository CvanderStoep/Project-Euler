from helper.utils import fib_generator

fib_gen = fib_generator()

n = 0
next(fib_gen) # in this problem we start with F1

while True:
    f = next(fib_gen)
    n += 1
    digits = len(str(f))
    if digits >= 1000:
        print(n, f)
        break
