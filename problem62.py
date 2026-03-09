from collections import Counter, defaultdict

def canonical(n: int) -> str:
    return ''.join(sorted(str(n)))

def permutation_stats(numbers: list):
    counts = Counter()
    groups = defaultdict(list)

    for n in numbers:
        key = canonical(n)
        counts[key] += 1
        groups[key].append(n)

    return counts, groups


N_MAX = 10_000
cubes = [n*n*n for n in range(N_MAX)]

counts, groups = permutation_stats(cubes)

item, count = counts.most_common(1)[0]
print(item, count)

print(groups[item])

# alternative solution using yield and without the need for N_MAX

def permutation_groups_stream():
    groups = defaultdict(list)      # key → list of cubes
    counts = defaultdict(int)       # key → count
    best_key = None
    best_count = 0

    n = 1
    while True:
        cube = n * n * n
        key = canonical(cube)

        counts[key] += 1
        groups[key].append(cube)

        if counts[key] > best_count:
            best_count = counts[key]
            best_key = key

        yield n, cube, best_key, best_count, groups[best_key]
        n += 1

stream = permutation_groups_stream()

for n, cube, key, count, group in stream:
    if count == 5:
        print(f'{n= }')
        print("key:", key)
        print("group:", group)
        print("smallest cube:", min(group))
        break