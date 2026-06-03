def solve(limit=1_000_000_000):
    per_sum = 0

    # Pell recurrences for the two families
    # Family 1: c = a + 1
    x, y = 2, 1  # corresponds to a = 1
    while True:
        a = (2*x - 1) // 3
        c = a + 1
        P = 2*a + c
        if P >= limit:
            break
        per_sum += P
        x, y = 2*x + 3*y, x + 2*y  # Pell recurrence

    # Family 2: c = a - 1
    x, y = 2, 1
    while True:
        a = (2*x + 1) // 3
        c = a - 1
        P = 2*a + c
        if P >= limit:
            break
        per_sum += P
        x, y = 2*x + 3*y, x + 2*y

    return per_sum


if __name__ == "__main__":
    print(solve())
