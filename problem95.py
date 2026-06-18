from mathlib.arithmetic import divisors

N = 1_000_0000
sum_proper_divisors = {i: sum(divisors(i)[:-1]) for i in range(0, N + 1)}
# print(sum_proper_divisors)

visited = [False] * (N + 1)
longest_chain = []
for start in range(1, N + 1):
    if visited[start]:
        continue
    chain = []
    current = start
    while current not in chain and current <= N and not visited[current]:
        chain.append(current)
        current = sum_proper_divisors[current]
    if current == start:
        if len(chain) > len(longest_chain) or (len(chain) == len(longest_chain) and min(chain) < min(longest_chain)):
            longest_chain = chain
        for value in chain:
            visited[value] = True
    elif current in chain:
        cycle_start = chain.index(current)
        for value in chain[:cycle_start]:
            visited[value] = True
    else:
        for value in chain:
            visited[value] = True
print(longest_chain)


