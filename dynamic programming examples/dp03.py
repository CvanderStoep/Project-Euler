# longest common subsequence

def longest_common_subsequence(first, second):
    n, m = len(first), len(second)
    grid = [[0] * (m + 1) for _ in range(n + 1)]


    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first[i-1] == second[j-1]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
    return(grid[n][m])

    # print(grid)  # → [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 2, 2, 2], [0, 1, 1, 2, 2, 3], [0, 1, 1, 2, 2, 3]]

def min_distance(first, second):
    n, m = len(first), len(second)
    grid = [[0 for _ in range(m+1)] for _ in range(n + 1)]
    for i in range(m+1):
        grid[0][i] = i
    for i in range(n+1):
        grid[i][0] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first[i-1] == second[j-1]:
                grid[i][j] = grid[i - 1][j - 1]
            else:
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1], grid[i-1][j-1]) + 1
    return(grid[n][m])
    


if __name__ == "__main__":
    first = 'tower'
    second = 'stone'
    lcs= longest_common_subsequence(first, second)
    print(lcs)

    first = 'almost'
    second = 'algomonster'

    md = min_distance(first, second)
    print(md)