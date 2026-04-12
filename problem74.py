from math import factorial

loop_length = 60
total_loop_length_sixty = 0

# Precompute factorials for speed
fact = {str(i): factorial(i) for i in range(10)}

for start in range(1_000_000):
    seen = []
    n = start

    while n not in seen:
        seen.append(n)
        n = sum(fact[d] for d in str(n))
        if len(seen) > loop_length:
            break

    if len(seen) == loop_length:
        total_loop_length_sixty += 1

print(total_loop_length_sixty)
