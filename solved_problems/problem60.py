from mathlib.primes import sieve_of_eratosthenes, is_prime
from functools import lru_cache
from itertools import combinations

MAX_PRIME = 1000
SET_LENGTH = 4

@lru_cache(maxsize=None)
def valid_set(prime_set):
    for ps in combinations(prime_set, 2):
        p1, p2 = ps
        p3 = int(str(p1)+str(p2))
        p4 = int(str(p2)+str(p1))
        if not is_prime(p3) or not is_prime(p4):
            return False
    return True


primes = sieve_of_eratosthenes(MAX_PRIME)
p2 = set()


for prime_set in combinations(primes, SET_LENGTH):
    if valid_set(prime_set):
        print(prime_set)
        break


#-----------------------------------------------------------------
# Below is the solution for larger sets using CoPilot as my friend.

from mathlib.primes import sieve_of_eratosthenes, is_prime
from functools import lru_cache


# ------------------------------------------------------------
# Prime concatenation compatibility
# ------------------------------------------------------------

@lru_cache(maxsize=None)
def concat(p, q):
    return p * (10 ** len(str(q))) + q

@lru_cache(maxsize=None)
def compatible(p, q):
    return is_prime(concat(p, q)) and is_prime(concat(q, p))


# ------------------------------------------------------------
# Build compatibility graph
# ------------------------------------------------------------

def build_graph(primes):
    G = {p: set() for p in primes}
    for i, p in enumerate(primes):
        for q in primes[i+1:]:
            if compatible(p, q):
                G[p].add(q)
                G[q].add(p)
    return G


# ------------------------------------------------------------
# DFS clique search
# ------------------------------------------------------------

def find_minimal_cliques(G, primes, target):
    best_sum = None
    best_cliques = []

    def dfs(clique, candidates):
        nonlocal best_sum, best_cliques

        # Sum pruning
        if best_sum is not None and sum(clique) >= best_sum:
            return

        # Found full clique
        if len(clique) == target:
            s = sum(clique)
            if best_sum is None or s < best_sum:
                best_sum = s
                best_cliques = [clique.copy()]
            elif s == best_sum:
                best_cliques.append(clique.copy())
            return

        # Feasibility pruning
        if len(clique) + len(candidates) < target:
            return

        # DFS expansion
        for p in sorted(candidates):
            new_candidates = candidates.intersection(G[p])
            dfs(clique + [p], new_candidates)
            candidates = candidates - {p}

    dfs([], set(primes))
    return best_sum, best_cliques


# ------------------------------------------------------------
# Main entrypoint
# ------------------------------------------------------------

def main(max_prime=10000, target=5):
    primes = sieve_of_eratosthenes(max_prime)
    G = build_graph(primes)
    best_sum, cliques = find_minimal_cliques(G, primes, target)

    print(f"Minimal sum: {best_sum}")
    for c in cliques:
        print(c)


if __name__ == "__main__":
    main()