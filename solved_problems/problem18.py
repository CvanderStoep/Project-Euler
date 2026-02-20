from collections import defaultdict
with open('problem18.txt', 'r') as f:
    content = f.read().splitlines()
print(content)
grid = [list(map(int, line.split())) for line in content]


# moving top-down
triangle_sum = defaultdict(int)
triangle_sum[(0,0)] = grid[0][0]

for j in range(1, len(grid)):
    for i in range(len(grid[j])):
        sum_l = triangle_sum[(i-1,j-1)]  + grid[j][i]
        sum_r = triangle_sum[(i,j-1)]  + grid[j][i]
        triangle_sum[(i, j)] = max(sum_l, sum_r)

print(triangle_sum)
triangle_sum = {k: v for k, v in triangle_sum.items() if v != 0}
print(triangle_sum)
print(max(triangle_sum.values()))

# Start from the bottom and collapse upward using DP
for row in range(len(grid) - 2, -1, -1):
    for col in range(len(grid[row])):
        grid[row][col] += max(grid[row + 1][col], grid[row + 1][col + 1])

print(grid[0][0])
print(grid)
