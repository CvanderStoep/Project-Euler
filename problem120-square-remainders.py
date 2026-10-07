def max_remainder(a):
    # For the Euler problem, the maximum remainder is:
    # a * (a - 1) when a is odd
    # a * (a - 2) when a is even
    if a % 2 == 0:
        return a * (a - 2)
    return a * (a - 1)


summation = sum(max_remainder(a) for a in range(3, 1001))
print(summation)
