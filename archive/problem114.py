from functools import lru_cache

def count_sequences(N):
    """
    Count the number of valid sequences of length N consisting of red and grey squares.

    A valid sequence satisfies:
    - Red blocks have a minimum length of 3.
    - Any two red blocks are separated by at least one grey square.
    - Grey squares may appear anywhere and in any quantity.

    The DP state is defined by solve(i, r, open):
    - i     : current index in the row (0 ≤ i ≤ N)
    - r     : length of the current red block (only meaningful when open=True)
    - open  : whether we are currently inside a red block (True) or in grey (False)

    Transitions:
    - Placing grey:
        * Allowed always when open=False.
        * Allowed when open=True only if the current red block has length ≥ 3.
        * Ends any red block.
    - Placing red:
        * If open=True: extend the current red block (r → r+1).
        * If open=False: start a new red block (r = 1).

    The recursion ends at i == N, where a final validity check ensures that
    an unfinished red block must have length ≥ 3.

    Returns:
        int: number of valid sequences of length N.
    """


    @lru_cache(None)
    def solve(i, r, open):
        # Einde van de rij
        if i == N:
            # Rode reeks moet geldig eindigen
            if open and r < 3:
                return 0
            return 1

        total = 0

        # --- Plaats grijs ---
        if open:
            # Rode reeks afsluiten → alleen als r >= 3
            if r >= 3:
                total += solve(i+1, 0, False)
        else:
            # We zitten al in grijs
            total += solve(i+1, 0, False)

        # --- Plaats rood ---
        if open:
            # Rode reeks verlengen
            total += solve(i+1, r+1, True)
        else:
            # Nieuwe rode reeks starten
            total += solve(i+1, 1, True)

        return total

    return solve(0, 0, False)


print(count_sequences(7))   # 17
print(count_sequences(40))  # < 1 ms
print(count_sequences(50))  # < 2 ms
