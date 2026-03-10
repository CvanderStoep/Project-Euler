def sqrt_continued_fraction(N: int):
    """
    Compute the continued fraction expansion of sqrt(N).
    Returns (a0, period) where:
      - a0 is the integer part
      - period is the repeating block [a1, ..., a_L]
    """
    a0 = int(N**0.5)
    if a0 * a0 == N:
        return (a0, [])  # perfect square

    m, d, a = 0, 1, a0
    period = []

    while True:
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d
        period.append(a)
        if a == 2 * a0:
            break

    return (a0, period)

number_odd_periods = 0
for n in range(1, 10001):
    a0, period = sqrt_continued_fraction(n)
    if len(period) % 2 == 1:
        number_odd_periods += 1
print(f'{number_odd_periods= }')

