max_palindrome = 0
for i in range(100, 999):
    for j in range(100, 999):
        product = i * j
        str_product = str(product)
        if str_product == str_product[::-1]:
            max_palindrome = max(max_palindrome, product)

            # print(f'Palindrome found: {product} = {i} * {j}')
print(f'Maximum palindrome: {max_palindrome}')