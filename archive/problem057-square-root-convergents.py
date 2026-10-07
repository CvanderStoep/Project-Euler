# calculate continued franction of sqrt(2)
# 1 + 1/2 = 3/2; 1 + 1/(2+ 1/2) = 7/5, etc
# a/b -> (a+2b)/(a+b)
a, b = 3, 2

total = 0
for _ in range(1000):
    a, b = a + 2 * b, a + b
    if len(str(a)) > len(str(b)):
        total += 1

print(f'{total= }')
