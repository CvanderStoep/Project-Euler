# number of unique paths in a grid
n, m = 3, 3
grid = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        grid[i][j] = grid[i-1][j] + grid[i][j-1] if i > 0 and j > 0 else 1

print(grid)  # → [[1, 1, 1], [1, 2, 3], [1, 3, 6]]

import numpy as np

n, m = 3, 3
grid = np.zeros((n, m), dtype=int)

for i in range(n):
    for j in range(m):
        grid[i, j] = grid[i-1, j] + grid[i, j-1] if i > 0 and j > 0 else 1

print(grid)
