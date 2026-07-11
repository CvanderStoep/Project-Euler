from mathlib.arithmetic import divisors

# 1/x + 1/y = 1/n -> 1/n = (x+y)/(xy) -> xy = n(x+y) -> xy - nx - ny = 0 -> (x-n)(y-n) = n^2
# x-n=d, y-n=n^2/d -> x=d+n, y=n^2/d+n
# d is a divisor of n^2, and we can generate all solutions by iterating through the divisors of n^2.


n = 4
while True:
    n += 1
    # factors = divisors(n*n) #this is slower than the below, but still works
    factors = divisors(n)
    factors = sorted({a * b for a in factors for b in factors})
    solutions = set()

    for factor in factors:
        x = n + factor
        y = n + (n*n) // factor
        if x > y:
            x, y = y, x
        solutions.add((x, y))

    if len(solutions) > 1000:
        break

print(f"Number of solutions for n={n}: {len(solutions)}")


