from itertools import combinations

digits = range(10)

def has(die, d):
    if d in (6, 9):
        return 6 in die or 9 in die
    return d in die

squares = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(6,4),(8,1)]

dice = list(combinations(digits, 6))

count = 0
for d1, d2 in combinations(dice, 2):
    ok = True
    for a, b in squares:
        if not ((has(d1,a) and has(d2,b)) or (has(d1,b) and has(d2,a))):
            ok = False
            break
    if ok:
        count += 1
        print(f"Valid pair: {d1} and {d2}")

print(count)
