# digits(k^n) == n
# n log(k) < n => k < 10
# the largest k == 9
# 9^n must have n digits
# 9 ^22 only has 21 digits, so maximum n is found: 21

count = 0
for k in range(1, 10):
    for n in range(1, 22):
        d = k ** n
        if len(str(d)) == n:
            print(d, k, n)
            count += 1
print(f'{count = }')
