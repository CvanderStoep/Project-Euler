# Explanations of different methods shown above:
# 1) Modular exponentiation via built-in pow(base, exp, mod):
#    Efficient, uses repeated squaring under the modulus. This is the
#    preferred method to get the last n digits: pow(base, exp, 10**n).
# 2) Compute large number then take modulus:
#    Shown with `number = (28433 * pow(2, 7830457, 10**10)) + 1` and
#    then `number % 10**10`. This still uses pow with modulus for the
#    large power to avoid huge intermediates; taking % afterwards is
#    equivalent to computing everything modulo 10**10.
# 3) Iterative multiplication with modulus in a loop:
#    Repeatedly multiply and reduce modulo 10**10. Works but is slower
#    for very large exponents compared to built-in pow which is C-optimized.

# All methods rely on modular arithmetic: (a*b) % m == ((a % m)*(b % m)) % m,
# so you can keep reducing intermediate results to stay within bounds.

def last_n_digits_of_power(base: int, exp: int, n: int) -> int:
    modulus = 10 ** n
    return pow(base, exp, modulus)  # efficient modular exponentiation

# Example: last 10 digits of 2**1000
print(last_n_digits_of_power(2, 7830457, 10))

number = (28433 * pow(2, 7830457, 10**10)) + 1
print(number % 10**10)  

ans = 2
for i in range(1, 7830457):
    ans = (ans * 2) % 10**10
ans = (ans * 28433 + 1) % 10**10
print(f"Final answer: {ans}")



