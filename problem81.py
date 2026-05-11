import pandas as pd
import numpy as np

# Matrix inlezen met pandas
df = pd.read_csv("problem81.txt", header=None)
matrix = df.to_numpy()


rows, cols = matrix.shape

# DP array
dp = np.zeros((rows, cols), dtype=int)

dp[0, 0] = matrix[0, 0]

# Eerste rij
for j in range(1, cols):
    dp[0, j] = dp[0, j-1] + matrix[0, j]

# Eerste kolom
for i in range(1, rows):
    dp[i, 0] = dp[i-1, 0] + matrix[i, 0]

# Rest
for i in range(1, rows):
    for j in range(1, cols):
        dp[i, j] = matrix[i, j] + min(dp[i-1, j], dp[i, j-1])

print("Minimum path sum:", dp[-1, -1])
