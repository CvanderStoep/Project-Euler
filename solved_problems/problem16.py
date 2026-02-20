number = 2 ** 1000
number_string = str(number)
number_list = map(int, number_string)
print(f'{sum(number_list)= }')