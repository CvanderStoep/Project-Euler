import numpy as np

def longest_palindrone_subsequence(string1):
    n = len(string1)
    grid = np.identity((n), dtype=int)

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l -1
            if string1[i] == string1[j]:
                grid[i, j] = grid[i+1, j-1] + 2
            else:
                grid[i,j] = max(grid[i+1, j], grid[i, j-1])

    print(grid)

    return grid[0, n-1]



if __name__ == "__main__":
    word = "lool"
    l = longest_palindrone_subsequence(word)
    print(f'longest sub palindrone {l}')

