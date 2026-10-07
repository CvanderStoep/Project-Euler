from mathlib.number_theory import sqrt_continued_fraction

number_odd_periods = 0
for n in range(1, 10001):
    a0, period = sqrt_continued_fraction(n)
    if len(period) % 2 == 1:
        number_odd_periods += 1
print(f'{number_odd_periods= }')

