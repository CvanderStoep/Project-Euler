from mathlib.decorators import timed


@timed
def fibonacci(n: int) -> int:
    """Generate the nth Fibonacci number."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    n = 100
    # print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
    print(fibonacci(n))