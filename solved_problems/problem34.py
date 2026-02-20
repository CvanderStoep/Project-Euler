from math import factorial
total_sum = 0

upper_bound = 7 * factorial(9)
print(upper_bound)
for n in range(3, upper_bound):
    digits = [int(d) for d in str(n)]
    sum_factorial = sum(factorial(d) for d in digits)
    if n == sum_factorial:
        total_sum += n
        print(n, sum_factorial)
print(total_sum)