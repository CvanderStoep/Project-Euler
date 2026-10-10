LIMIT = 200


def solve(limit=LIMIT):
    inf = float("inf")
    best = [inf] * (limit + 1)
    best[1] = 0

    def dfs(chain, max_depth):
        depth = len(chain) - 1
        last = chain[-1]
        if depth < best[last]:
            best[last] = depth
        if depth == max_depth:
            return
        # extend the chain: last + (any earlier element), largest first
        for x in reversed(chain):
            s = last + x
            if s > limit:
                continue
            chain.append(s)
            dfs(chain, max_depth)
            chain.pop()

    # iterative deepening: grow the depth until every k <= limit has a chain
    depth = 0
    while any(b == inf for b in best[1:]):
        depth += 1
        dfs([1], depth)
    return sum(best[1:]), best


if __name__ == "__main__":
    total, best = solve()
    assert best[15] == 5
    print(best)  # sanity check
    print(total)