from mathlib.arithmetic import simplify_fraction

def has_increasing_digits(n):
    s = str(abs(int(n)))
    return all(s[i] <= s[i + 1] for i in range(len(s) - 1))

def has_decreasing_digits(n):
    s = str(abs(int(n)))
    return all(s[i] >= s[i + 1] for i in range(len(s) - 1))

def is_bouncy(n):
    return not (has_increasing_digits(n) or has_decreasing_digits(n))


i = 0
bouncy_count = 0
percentage_target = (99, 100) # 99% as a fraction   
# I thought the accuracy of floating point numbers might be an issue, so I used a fraction instead


while True:
    i += 1

    if is_bouncy(i):
        bouncy_count += 1

    bouncy_proportion = bouncy_count / i
    if bouncy_proportion == 0.99:
        print(f"Found number: {i} with bouncy proportion exactly 0.99")


    if simplify_fraction(bouncy_count, i) == percentage_target:
        print(f"Found number: {i} with bouncy proportion exactly {percentage_target[0]}/{percentage_target[1]}")
        break



