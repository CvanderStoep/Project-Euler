max_sum = 0
for a in range(100):
    for b in range(100):
        value = a**b
        digit_sum = sum(int(d) for d in str(value))
        max_sum = max(digit_sum, max_sum)

print(f'{max_sum= }')


max_sum = max(
    sum(map(int, str(a**b)))
    for a in range(100)
    for b in range(100)
)

print(max_sum)
