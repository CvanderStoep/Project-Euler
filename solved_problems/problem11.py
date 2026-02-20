# Problem 11: Largest product in a grid
# Find the greatest product of four adjacent numbers in the same direction  
# (up, down, left, right, or diagonally) in the 20×20 grid. 
# The grid is provided in the file '11-20/problem11.txt'.
# as described in Project Euler Problem 11.

with open('11-20/problem11.txt', 'r') as f:
    content = f.read().splitlines()
print(content)

grid = [list(map(int, line.split())) for line in content]
print(grid[0][1])  # Example to show the grid is read correctly

max_product = 0
for i in range(20):
    for j in range(20):
        if j < 17:  # Check right
            product_right = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            # print(f'Product right at ({i},{j}): {product_right}')
            max_product = max(max_product, product_right)
        if i < 17:  # Check down
            product_down = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            # print(f'Product down at ({i},{j}): {product_down}')
            max_product = max(max_product, product_down)
        if i < 17 and j < 17:  # Check diagonal right-down
            product_diag_right = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            # print(f'Product diagonal right-down at ({i},{j}): {product_diag_right}')
            max_product = max(max_product, product_diag_right)
        if i < 17 and j >= 3:  # Check diagonal left-down
            product_diag_left = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
            # print(f'Product diagonal left-down at ({i},{j}): {product_diag_left}')
            max_product = max(max_product, product_diag_left)
print(f'Max product: {max_product}')

import numpy as np

# Load grid
with open('11-20/problem11.txt', 'r') as f:
    grid = np.array([[int(x) for x in line.split()] for line in f])

# Right (horizontal)
right = grid[:, :-3] * grid[:, 1:-2] * grid[:, 2:-1] * grid[:, 3:]

# Down (vertical)
down = grid[:-3, :] * grid[1:-2, :] * grid[2:-1, :] * grid[3:, :]

# Diagonal right-down
diag_rd = grid[:-3, :-3] * grid[1:-2, 1:-2] * grid[2:-1, 2:-1] * grid[3:, 3:]

# Diagonal left-down
diag_ld = grid[:-3, 3:] * grid[1:-2, 2:-1] * grid[2:-1, 1:-2] * grid[3:, :-3]

# Compute max
max_product = max(
    right.max(),
    down.max(),
    diag_rd.max(),
    diag_ld.max()
)

print(f"Max product: {max_product}")
print(grid.shape)
print(grid[:3, :3])






