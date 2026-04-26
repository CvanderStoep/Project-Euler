import math
from mathlib.number_theory import sqrt_continued_fraction


# ------------------------------------------------------------
# Number utilities
# ------------------------------------------------------------

def is_perfect_square(n: int) -> bool:
    """Return True if n is a perfect square."""
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


# ------------------------------------------------------------
# Continued fraction utilities
# ------------------------------------------------------------

def continued_fraction_term(k: int, a0: int, period: list[int]) -> int:
    """
    Return the k-th term a_k of the continued fraction expansion of sqrt(d).
    a_0 is the initial term, and the rest repeat periodically.
    """
    if k == 0:
        return a0
    period_length = len(period)
    return period[(k - 1) % period_length]


# ------------------------------------------------------------
# Pell equation solvers
# ------------------------------------------------------------

def solve_pell_bruteforce(d: int) -> int:
    """
    Solve x^2 - d y^2 = 1 by brute force search over x = d*n ± 1.
    Returns the minimal x satisfying the equation.
    """
    if is_perfect_square(d):
        return 0

    n = 1
    while True:
        for x in (d * n - 1, d * n + 1):
            if x <= 1:
                continue
            value = (x * x - 1) // d
            if (x * x - 1) % d == 0 and is_perfect_square(value):
                return x
        n += 1


def solve_pell_via_continued_fraction(d: int) -> tuple[int, int]:
    """
    Solve x^2 - d y^2 = 1 using the continued fraction expansion of sqrt(d).
    Returns (x, y) as the minimal positive solution.
    """
    if is_perfect_square(d):
        return 0, 0

    a0, period = sqrt_continued_fraction(d)

    # Initial convergent values:
    # p[-2] = 0, p[-1] = 1
    # q[-2] = 1, q[-1] = 0
    p_prev2, p_prev1 = 0, 1
    q_prev2, q_prev1 = 1, 0

    k = 0
    while True:
        a_k = continued_fraction_term(k, a0, period)

        p_k = a_k * p_prev1 + p_prev2
        q_k = a_k * q_prev1 + q_prev2

        if p_k * p_k - d * q_k * q_k == 1:
            return p_k, q_k

        p_prev2, p_prev1 = p_prev1, p_k
        q_prev2, q_prev1 = q_prev1, q_k
        k += 1


# ------------------------------------------------------------
# Example: find d ≤ 1000 with largest minimal x
# ------------------------------------------------------------

def find_largest_pell_solution(limit: int = 1000) -> tuple[int, int]:
    """
    For 2 ≤ d ≤ limit, find the d for which the minimal Pell solution x is maximal.
    Returns (d_max, x_max).
    """
    d_max, x_max = 0, 0

    for d in range(2, limit + 1):
        x, y = solve_pell_via_continued_fraction(d)
        if x > x_max:
            d_max, x_max = d, x

    return d_max, x_max


if __name__ == "__main__":
    d_max, x_max = find_largest_pell_solution(1000)
    print(f"Largest minimal x occurs at d = {d_max}, x = {x_max}")