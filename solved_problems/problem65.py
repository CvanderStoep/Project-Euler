from mathlib.number_theory import continued_fraction_e

a_0 = continued_fraction_e(0)

p_minus_1 = 1
p_0 = a_0
q_minus_1 = 0
q_0= 1


for n in range(1, 100):
    a_n = continued_fraction_e(n)
    p_n = a_n * p_0 + p_minus_1
    q_n = a_n * q_0 + q_minus_1
    p_minus_1 = p_0
    p_0 = p_n
    q_minus_1 = q_0
    q_0 = q_n
print(n, p_n, q_n)

sum_digits = sum(int(c) for c in str(p_n))
print(f'{sum_digits= }')


# refactored using CoPilot
from mathlib.number_theory import continued_fraction_e


def convergent_of_e(index: int) -> tuple[int, int]:
    """
    Return the `index`-th convergent (p, q) of the continued fraction of e,
    where index is 1-based:
        index = 1 -> first convergent
    """
    if index < 1:
        raise ValueError("index must be >= 1")

    a0 = continued_fraction_e(0)

    # Initial convergents:
    # p[-1] = 1, p[0] = a0  -> 1st convergent
    # q[-1] = 0, q[0] = 1
    p_prev2, p_prev1 = 1, a0
    q_prev2, q_prev1 = 0, 1

    if index == 1:
        return p_prev1, q_prev1

    # We already have the 1st convergent, so we need to go up to index-1
    for n in range(1, index):
        a_n = continued_fraction_e(n)
        p_n = a_n * p_prev1 + p_prev2
        q_n = a_n * q_prev1 + q_prev2

        p_prev2, p_prev1 = p_prev1, p_n
        q_prev2, q_prev1 = q_prev1, q_n

    return p_prev1, q_prev1


def digit_sum(n: int) -> int:
    """Return the sum of decimal digits of n."""
    return sum(int(c) for c in str(n))


if __name__ == "__main__":
    # 100th convergent of e (Euler 65)
    p_100, q_100 = convergent_of_e(100)
    print("p_100 =", p_100)
    print("q_100 =", q_100)

    s = digit_sum(p_100)
    print(f"sum_digits = {s}")