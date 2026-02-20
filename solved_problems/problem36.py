from helper.utils import is_palindrome

sum_palindrome = 0
for n in range(1, 1_000_000):
    binary = bin(n)[2:]
    string_n = str(n)
    string_b = str(binary)
    if is_palindrome(string_n) and is_palindrome(string_b):
        print(n, binary)
        sum_palindrome += n
print(f'{sum_palindrome= }')