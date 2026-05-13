def read_matrix(path: str):
    with open(path) as f:
        return [list(map(int, line.strip().split(','))) for line in f]

def minimal_path_sum_three_ways(matrix):
    n = len(matrix)
    # dp[r] = minimale kost vanaf rij r in huidige kolom naar rechts
    dp = [matrix[r][n - 1] for r in range(n)]  # laatste kolom

    # kolommen van rechts naar links
    for c in range(n - 2, -1, -1):
        # 1) rechts-beweging
        for r in range(n):
            dp[r] = matrix[r][c] + dp[r]

        # 2) omlaag sweep
        for r in range(1, n):
            dp[r] = min(dp[r], dp[r - 1] + matrix[r][c])

        # 3) omhoog sweep
        for r in range(n - 2, -1, -1):
            dp[r] = min(dp[r], dp[r + 1] + matrix[r][c])

    return min(dp)




if __name__ == "__main__":
    matrix = read_matrix("problem81.txt")
    print(minimal_path_sum_three_ways(matrix))
