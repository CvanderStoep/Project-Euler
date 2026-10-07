from itertools import combinations
def all_subsets(s):
    """
    Return all subsets of the input set s.
    """
    elements = list(s)
    subsets = []
    for r in range(len(elements) + 1):
        for combo in combinations(elements, r):
            subsets.append(set(combo))
    return subsets

def all_subset_pairs(s):
    """
    Return all combinations of two distinct subsets from s.
    """
    subsets = all_subsets(s)
    return [(a, b) for a, b in combinations(subsets, 2)]

def is_special_sum_set(s):
    """
    Check if a set of numbers is a special sum set.
    
    A set of numbers is a special sum set if:
    1. The sum of any two disjoint subsets is not equal.
    2. The sum of the elements in the larger subset is greater than the sum of the elements in the smaller subset.
    
    Args:
        s (list): A list of integers representing the set.
    
    Returns:
        bool: True if the set is a special sum set, False otherwise.
    """
    for a, b in all_subset_pairs(s):
        if len(a) == 0 or len(b) == 0:
            # print("One of the subsets is empty, skipping this pair.")
            continue
        if a.isdisjoint(b):
            sum_a = sum(a)
            sum_b = sum(b)
            if sum_a == sum_b:
                return False
            if len(a) > len(b) and sum_a <= sum_b:
                return False
            if len(b) > len(a) and sum_b <= sum_a:
                return False
    return True


s = {6, 9, 11, 12, 13}
s = {11,17,20,22,23,24}
s = {11, 18, 19, 20, 22, 25}
s = {20, 31, 38, 39, 40, 42, 45}



# for subset in all_subsets(s):
#     print(subset)
# print(is_special_sum_set(s), sum(s))  # Output: True


#alternative implementation of is_special_sum_set
from itertools import combinations

# ------------------------------------------------------------
# VALIDATION
# ------------------------------------------------------------

def disjoint_subsets(S):
    """Generate all pairs of disjoint non-empty subsets."""
    n = len(S)
    idx = range(n)
    for r1 in range(1, n+1):
        for c1 in combinations(idx, r1):
            set1 = set(c1)
            for r2 in range(1, n+1):
                for c2 in combinations(idx, r2):
                    set2 = set(c2)
                    if set1.isdisjoint(set2):
                        yield tuple(S[i] for i in c1), tuple(S[i] for i in c2)

def is_valid(S):
    """Check both special-sum-set rules for a sorted set S."""
    S = sorted(S)

    # Rule 2: larger subset must have larger sum
    for k in range(1, len(S)):
        if sum(S[:k+1]) <= sum(S[-k:]):
            return False

    # Rule 1: disjoint subsets must have different sums
    for A, B in disjoint_subsets(S):
        if sum(A) == sum(B):
            return False

    return True

# ------------------------------------------------------------
# BACKTRACKING SEARCH WITH PRUNING
# ------------------------------------------------------------

def find_optimal_set(n, max_val=50):
    """Search for the minimal-sum special-sum set of length n."""
    best_sum = float('inf')
    best_set = None

    def backtrack(prefix, next_min):
        nonlocal best_sum, best_set

        # If we have n elements, validate and update best
        if len(prefix) == n:
            if is_valid(prefix):
                s = sum(prefix)
                if s < best_sum:
                    best_sum = s
                    best_set = prefix[:]
            return

        remaining = n - len(prefix)

        # Pruning: even with smallest possible future values, sum >= best?
        min_possible_sum = sum(prefix) + sum(range(next_min, next_min + remaining))
        if min_possible_sum >= best_sum:
            return

        # Try next values in increasing order
        for x in range(next_min, max_val + 1):
            prefix.append(x)
            backtrack(prefix, x + 1)
            prefix.pop()

    backtrack([], 1)
    return best_set, best_sum

# ------------------------------------------------------------
# DEMO FOR n = 6
# ------------------------------------------------------------

if __name__ == "__main__":
    n = 6
    optimal_set, total = find_optimal_set(n, max_val=50)
    print(f"Optimal set {{n={n}}}: {optimal_set}")
    print(f"Sum: {total}")

