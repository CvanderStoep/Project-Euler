def permuted(a, b):
    return sorted(str(a)) == sorted(str(b))

n = 0
while True:
    n +=1
    checks = [
        permuted(n, 2*n),
        permuted(n, 3*n),
        permuted(n, 4*n),
        permuted(n, 5*n),
        permuted(n, 6*n),
    ]

    if all(checks):
        print(f'{n= }')
        break
