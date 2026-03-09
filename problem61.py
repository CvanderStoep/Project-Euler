# ------------------------------------------------------------
# Polygonal functions
# ------------------------------------------------------------

def triangle(n):   return n * (n + 1) // 2
def square(n):     return n * n
def pentagonal(n): return n * (3 * n - 1) // 2
def hexagonal(n):  return n * (2 * n - 1)
def heptagonal(n): return n * (5 * n - 3) // 2
def octagonal(n):  return n * (3 * n - 2)


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

def four_digit(values):
    return [v for v in values if 1000 <= v <= 9999]

def match(a, b):
    return str(a)[-2:] == str(b)[:2]


# ------------------------------------------------------------
# Build polygonal families
# ------------------------------------------------------------

def build_families(N=200):
    return [
        four_digit([triangle(n)   for n in range(1, N)]),
        four_digit([square(n)     for n in range(1, N)]),
        four_digit([pentagonal(n) for n in range(1, N)]),
        four_digit([hexagonal(n)  for n in range(1, N)]),
        four_digit([heptagonal(n) for n in range(1, N)]),
        four_digit([octagonal(n)  for n in range(1, N)]),
    ]


# ------------------------------------------------------------
# DFS search allowing ANY order of polygonal families
# ------------------------------------------------------------

def find_cyclic_set(families):
    solution = None

    def dfs(path, used_families):
        nonlocal solution

        if solution is not None:
            return

        # 6 numbers chosen → check cyclic closure
        if len(path) == 6:
            if match(path[-1][1], path[0][1]):
                solution = [x for (_, x) in path]
            return

        # Try each unused family
        for fi in range(6):
            if fi in used_families:
                continue

            for x in families[fi]:
                # First element: no match needed
                if not path:
                    dfs([(fi, x)], {fi})
                    ...
                else:
                    prev = path[-1][1]
                    if match(prev, x):
                        dfs(path + [(fi, x)], used_families | {fi})

    dfs([], set())
    return solution


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

def main():
    families = build_families()
    result = find_cyclic_set(families)

    if result:
        print("Cyclic set:", result)
        print("Sum:", sum(result))
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()