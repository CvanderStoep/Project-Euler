def solve(limit_target=1_000_000):
    M = 0
    count = 0

    while count < limit_target:
        M += 1

        # For each possible sum X = a + b
        for X in range(2, 2*M + 1):
            c2 = X*X + M*M
            c = int(c2**0.5)
            if c*c == c2:
                # Count valid (a,b) pairs with a ≤ b ≤ M and a+b = X
                if X <= M:
                    count += X // 2
                else:
                    count += 1 + (M - (X+1)//2)

        print(f"M={M}, count={count}")

    return M


print("Result:", solve())
