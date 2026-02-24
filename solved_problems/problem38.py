pandigital = []

for n in range(10_000):
    for k in range(2, 10):
        p = ''
        for i in range(1, k + 1):
            p += str(n * i)
        # p = ''.join(str(n * i) for i in range(1, k + 1))
        if '0' in p:
            continue
        if len(p) > 9:
            break  # no need to continue increasing k
        if len(p) == len(set(p)) == 9:
            pandigital.append(int(p))
            print(n, k, p)

print(pandigital)
print(f'{max(pandigital)= }')


