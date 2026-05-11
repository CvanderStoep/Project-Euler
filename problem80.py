from decimal import Decimal, getcontext
from mathlib.arithmetic import first_N_digits_sqrt


squares = {i*i for i in range(1, 11)}  # 1,4,...,100

total = 0
N_digits = 100
for i in range(1, 101):
    if i not in squares:
        digits = first_N_digits_sqrt(i, N_digits)
        sum_digits = sum(int(d) for d in digits)
        # print(i, sum_digits, digits)
        total += sum_digits

print(f'{total= }')