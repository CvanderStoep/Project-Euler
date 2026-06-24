Bk = 15
Rk = 6
Total = Bk + Rk
k = 1
while Total < 10**12:
    Bk1 = 5 * Bk + 2 * Rk - 2
    Rk1 = 2 * Bk + Rk - 1
    Bk, Rk = Bk1, Rk1
    Total = Bk + Rk
    print(k, Bk, Rk, Total)
    k += 1