from mathlib.utils import is_abundant

def can_be_written_as_sum(nums, target):
    s = set(nums)
    for x in nums:
        y = target - x
        if y in s:
            return True
    return False


abundant_numbers = [n for n in range(28123) if is_abundant(n)]

answer = 0
for n in range(28123):
    if not can_be_written_as_sum(abundant_numbers, n):
        answer += n

print(f'{answer= }')
