from decimal import Decimal, getcontext
from mathlib.utils import repeating_decimal

getcontext().prec = 60   # enough precision for 48 digits

for d in range(2, 10):
    x = Decimal(1) / Decimal(d)
    print(f"1/{d} = {x:.14f}")

d, longest_cycle = 2, 0
for n in range(2, 1000):
    non_repeating, repeating = repeating_decimal(1,n)
    repeating_length = len(repeating)
    # print(repeating_decimal(1,n))
    if repeating_length > longest_cycle:
        d = n
        longest_cycle = repeating_length

print(d, longest_cycle)

