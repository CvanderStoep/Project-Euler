
def climb_stairs(n, memo=None):
    # avoid global side-effects by using a fresh memo dict for each top-level call
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    return memo[n]

print(climb_stairs(7))   # → 21


def climb_stairs(n, memo=None):
    if memo is None:
        memo = {}
        print(f"Created fresh memo dict for top-level call: {memo}")

    if n in memo:
        print(f"memo hit: n={n}, memo={memo}")
        return memo[n]

    print(f"computing n={n}, current memo={memo}")

    if n <= 1:
        memo[n] = 1
        print(f"base case: n={n}, memo={memo}")
        return 1

    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    print(f"computed n={n}, memo now={memo}")
    return memo[n]


print(climb_stairs(7))

def climbStairs(n):
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]     
    return ways[n]

print(climbStairs(7))   # → 21

def climb_stairs_with_costs(costs):

    n = len(costs) - 1  # Adjust n to be the last index of costs
    
    min_cost = [0] * (n + 1)
    min_cost[0] = costs[0]
    min_cost[1] = costs[1]
    
    for i in range(2, n + 1):
        min_cost[i] = min(min_cost[i - 1], min_cost[i - 2]) + costs[i]
    print(min_cost)
    
    return min(min_cost[n-1], min_cost[n])  # Return the minimum cost to reach the top


costs = [5, 18, 4, 15, 6]
print(climb_stairs_with_costs(costs))  # → 15

def rob(nums):
    n = len(nums)
    if not nums:
        return 0
    if n == 1:
        return nums[0]
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    return dp[-1]

print(f"Maximum amount that can be robbed: {rob([2, 7, 9, 3, 1])}")  # → 12

