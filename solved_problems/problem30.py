power = 5
sum_armstrong = 0
for n in range(2, 1_000_000):
    digits = str(n)
    total = sum([(int(d))**power for d in digits])
    if total == n:
        sum_armstrong += total
        print(n)

print(f'{sum_armstrong= }')
