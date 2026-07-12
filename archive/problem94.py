import math


def is_integer_area(a, b, c):
    # Convert to integers
    a, b, c = int(a), int(b), int(c)

    # Basic validity checks
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("sides must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("sides do not form a triangle")

    # Heron's formula without floats:
    # 16*A^2 = (a+b+c)(-a+b+c)(a-b+c)(a+b-c)
    s1 = a + b + c
    s2 = -a + b + c
    s3 = a - b + c
    s4 = a + b - c

    D = s1 * s2 * s3 * s4  # this equals 16*A^2

    if D < 0:
        return False  # shouldn't happen for valid triangles

    k = int(D**0.5)
    return k * k == D




if __name__ == '__main__':
    sum_of_perimeters = 0
    for a in range(1,350_000_000):
        if a % 1_000_000 == 0:
            print(f"checking a={a}...")
        b = a
        for c in [a-1, a+1]:
            if a + b <= c or a + c <= b or b + c <= a:
                continue
            if a + b + c >= 1_000_000_000:
                continue
            area = is_integer_area(a, b, c)
            if area:
                sum_of_perimeters += a + b + c
                print(f"sides=({a}, {b}, {c}) area={int(area)} (integer)", area)
    print(f"sum of perimeters: {sum_of_perimeters}")

