from itertools import permutations

unusual = set()
all_digits = list(range(1, 10))
for digits in permutations(all_digits):
# digits = [3,9,1,8,6,7,2,5,4]
    for location_multiplyer in range(1, 8):
        for location_equal in range(location_multiplyer+2, 10):
            number1 = digits[:location_multiplyer]
            number1 = int("".join(str(d) for d in number1))
            number2 = digits[location_multiplyer:location_equal-1]
            number2 = int("".join(str(d) for d in number2))
            product = digits[location_equal-1:]
            product = int("".join(str(d) for d in product))
            if number1*number2==product:
                print(number1, number2, product, number1*number2==product)
                unusual.add(product)
print(f'{sum(unusual)= }')



from itertools import permutations

unusual = set()
digits = "123456789"

for p in permutations(digits):
    # Pre-join once — avoid repeated string joins
    s = "".join(p)

    # Try all split positions
    for i in range(1, 8):              # number1 ends at i
        number1 = int(s[:i])

        for j in range(i+1, 9):        # number2 ends at j
            number2 = int(s[i:j])
            product = int(s[j:])

            if number1 * number2 == product:
                print(number1, number2, product)
                unusual.add(product)

print(f"sum(unusual) = {sum(unusual)}")


unusual = set()

def is_pandigital_1_to_9(a, b, c):
    s = f"{a}{b}{c}"
    return len(s) == 9 and '0' not in s and len(set(s)) == 9

# Case A: 1-digit × 4-digit = 4-digit
for a in range(1, 10):              # 1-digit
    for b in range(1234, 9877):     # 4-digit (rough bounds)
        c = a * b
        if 1000 <= c <= 9999 and is_pandigital_1_to_9(a, b, c):
            unusual.add(c)

# Case B: 2-digit × 3-digit = 4-digit
for a in range(12, 99):             # 2-digit
    for b in range(123, 988):       # 3-digit
        c = a * b
        if 1000 <= c <= 9999 and is_pandigital_1_to_9(a, b, c):
            unusual.add(c)

print(f"sum(unusual) = {sum(unusual)}")