from math import gcd, isqrt
from itertools import combinations


def repeating_decimal(p, q):
    p, q = p // gcd(p, q), q // gcd(p, q)

    t = q
    for prime in (2, 5):
        while t % prime == 0:
            t //= prime

    if t == 1:
        return "", ""

    seen = {}
    digits = []
    remainder = p % q
    pos = 0

    while remainder not in seen:
        seen[remainder] = pos
        remainder *= 10
        digits.append(str(remainder // q))
        remainder %= q
        pos += 1

    start = seen[remainder]
    non_rep = "".join(digits[:start])
    rep = "".join(digits[start:])
    return non_rep, rep


def pythagorean_triples(n):
    """
    Generate all Pythagorean triples (a, b, c) with 1 ≤ a ≤ b ≤ c ≤ n.

    A Pythagorean triple satisfies:
        a^2 + b^2 = c^2

    Parameters
    ----------
    n : int
        The maximum value allowed for a, b, and c.

    Returns
    -------
    list[tuple[int, int, int]]
        A list of tuples (a, b, c), where each tuple is a valid Pythagorean
        triple and all values are ≤ n.

    Notes
    -----
    - This function performs a brute‑force search over all pairs (a, b)
      with 1 ≤ a ≤ b ≤ n, so the time complexity is O(n²).
    - Only triples with a ≤ b ≤ c are included, so permutations of the same
      triple are not repeated.
    - The function checks whether a^2 + b^2 is a perfect square using
      `math.isqrt`.

    Examples
    --------
    >>> pythagorean_triples(20)
    [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)]
    """

    triples = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c2 = a * a + b * b
            c = isqrt(c2)
            if c <= n and c * c == c2:
                triples.append((a, b, c))
    return triples


def sqrt_continued_fraction(N: int):
    """
    Compute the continued fraction expansion of sqrt(N).
    Returns (a0, period) where:
      - a0 is the integer part
      - period is the repeating block [a1, ..., a_L]
    """
    a0 = int(N**0.5)
    if a0 * a0 == N:
        return (a0, [])  # perfect square

    m, d, a = 0, 1, a0
    period = []

    while True:
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d
        period.append(a)
        if a == 2 * a0:
            break

    return (a0, period)


def continued_fraction_e(n):
    # e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...]
    if n == 0:
        return 2
    if n % 3 == 2:
        return 2 * (n + 1) // 3
    return 1

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