import numpy as np

def length_longest_increasing_sequence(nums):
    n = len(nums)
    dp = [1] * n
    print(dp)
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+ 1)

    print(dp)
    return max(dp)



if __name__ == "__main__":
    nums = [3, 1, 5, 2, 4, 1, 7]
    l = length_longest_increasing_sequence(nums)
    print(f'longest increasing subsequence {l}')

