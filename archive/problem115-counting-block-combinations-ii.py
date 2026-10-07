from functools import lru_cache

def count_sequences(N, m=3):

    @lru_cache(None)
    def solve(i, r, open, must_gray):
        # Einde van de reeks
        if i == N:
            # Als we nog in een rode reeks zitten, moet die geldig zijn
            if open and r < m:
                return 0
            return 1

        total = 0

        # --- Plaats grijs ---
        if open:
            # Rode reeks afsluiten → alleen toegestaan als r >= m
            if r >= m:
                total += solve(i+1, 0, False, False)
        else:
            # We zitten al in grijs
            total += solve(i+1, 0, False, False)

        # --- Plaats rood ---
        if not must_gray:
            if open:
                # Rode reeks verlengen
                total += solve(i+1, r+1, True, False)
            else:
                # Nieuwe rode reeks starten
                total += solve(i+1, 1, True, False)

        return total

    return solve(0, 0, False, False)

m, n= 3, 1
while True:
    n += 1
    if count_sequences(n, m) > 1_000_000:
        print(f'{n= }')
        break

