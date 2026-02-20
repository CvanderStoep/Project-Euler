with open('1-10/problem08.txt', 'r') as f:
    content = f.read().replace('\n', '')
position = 0
max_product = 0
series_length = 13
while position < len(content)-(series_length-1):
    sub_string = content[position:position+series_length]
    # print(sub_string)
    product = 1
    for char in sub_string:
        product *= int(char)
    max_product = max(max_product, product)
    position += 1
print('the greatest product is:', max_product)
