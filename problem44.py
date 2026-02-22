def pentagonal(n):
    return n * (3 * n - 1) // 2

N = 10000
pents = [pentagonal(i) for i in range(1, N)]
pent_set = set(pents)

best = None

for j in range(len(pents)):
    for k in range(j+1, len(pents)):
        pj = pents[j]
        pk = pents[k]

        diff = pk - pj
        if best and diff > best:
            break  # no need to continue

        if diff in pent_set and (pk + pj) in pent_set:
            best = diff
            print("Found:", j+1, k+1, diff)
            break