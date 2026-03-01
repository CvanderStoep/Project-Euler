from mathlib.sequences import is_palindrome

limit = 10_000
max_iterations = 50

lychrel_count = 0

for n in range(1, limit):
    value = n
    reached_palindrome = False

    for _ in range(max_iterations):
        value += int(str(value)[::-1])
        if is_palindrome(value):
            reached_palindrome = True
            break

    if not reached_palindrome:
        lychrel_count += 1

print(f"{lychrel_count=}")

# Alternative
def reaches_palindrome(n: int, max_iter: int = 50) -> bool:
    value = n
    for _ in range(max_iter):
        value += int(str(value)[::-1])
        if is_palindrome(value):
            return True
    return False


limit = 10_000
lychrel_count = sum(
    1 for n in range(1, limit) if not reaches_palindrome(n)
)

print(f"{lychrel_count=}")