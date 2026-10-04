import numpy as np

def knapsack(nums):
    total_sum = sum(nums)
    print(f'{total_sum= }')
    if total_sum %2 != 0:
        return False

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for s in range(target - num, -1, -1):
            if dp[s]:
                dp[s+num] = True

    print(dp)


    return dp[-1]




if __name__ == "__main__":
    nums = [1, 5, 5, 11]
    l = knapsack(nums)
    print(f'longest increasing subsequence {l}')

