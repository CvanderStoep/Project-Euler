def numbers_in_layer(n):
    return (2*n-3)**2 + 1, (2*n-1)**2

layer = 1
# 1001 x 1001 spiral = 501 layers
total_sum_diagonal = 0
for layer in range(2, 502):
    square = 2*layer -1
    _, stop = numbers_in_layer(layer)
    down_right = stop
    down_left = down_right - square + 1
    upper_left = down_left - square + 1
    upper_right = upper_left - square + 1
    total_sum_diagonal += upper_left + upper_right + down_left + down_right

print(f'{total_sum_diagonal + 1= }')



