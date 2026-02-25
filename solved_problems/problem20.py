from math import factorial

number = factorial(100)
number_string = str(number)
digit_sum = sum(map(int, number_string))
print(f'{digit_sum= }')