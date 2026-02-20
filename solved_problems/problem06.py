sum_squares = sum(i**2 for i in range(1, 101))
square_sum = sum(range(1, 101)) ** 2

difference = square_sum - sum_squares
print(f'Difference between square of sums and sum of squares for first 100 natural numbers: {difference}')


# sum of squares = 1^2 + 2^2 + ... + 100^2 == n/6 (2n+1)(n+1) where n=100
# square of sums = (1 + 2 + ... + 100)^2 == (n(n+1)/2)^2 where n=100

n = 100
sum_of_squares_formula = n * (n + 1) * (2 * n + 1) // 6
square_of_sums_formula = (n * (n + 1) // 2) ** 2    
difference_formula = square_of_sums_formula - sum_of_squares_formula
print(f'Calculated using formula: {difference_formula}')

