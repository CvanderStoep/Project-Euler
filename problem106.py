from math import comb


def catalan_number(k):
    """Return the k-th Catalan number."""
    return comb(2 * k, k) // (k + 1)

def count_euler_106_pairs(n):
    """Count the number of subset pairs requiring comparison for Project Euler 106."""
    total = 0
    for k in range(1, n // 2 + 1):
        total += comb(n, 2 * k) * (comb(2 * k, k) // 2 - catalan_number(k))
    return total

# ------------------------------------------------------------
# DEMO FOR EULER 106
# ------------------------------------------------------------

if __name__ == "__main__":
    n = 12
    result = count_euler_106_pairs(n)
    print(f"Euler 106 count for n={n}: {result}")

