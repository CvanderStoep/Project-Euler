# from mathlib.number_theory import factorial
from math import factorial

# how many routes can be found in a 20x20 grid:
# 40! / (20! * 20!)
# math.factorial(n)

routes = factorial(40) / (factorial(20) * factorial(20))
print(f'{routes= }')


