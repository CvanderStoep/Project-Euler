from helper.utils import divisors
def sum_divisors(n):
    return sum(divisors(n)[:-1])


amicable_numbers = set()
for a in range(10000):
    b = sum_divisors(a)
    if sum_divisors(b) == a and a != b:
        amicable_numbers.add(a)
        amicable_numbers.add(b)
print(amicable_numbers)
print(f'{sum(amicable_numbers)= }')

amicable_numbers = set()
cache = {}

for a in range(1, 10000):
    if a not in cache:
        cache[a] = sum_divisors(a)
    b = cache[a]

    if b < 10000:
        if b not in cache:
            cache[b] = sum_divisors(b)

        if cache[b] == a and a != b:
            amicable_numbers.add(a)
            amicable_numbers.add(b)

print(amicable_numbers)
print(f"{sum(amicable_numbers)=}")
