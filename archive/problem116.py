from functools import lru_cache

def count_sequences(N, m=2):
    """
    Tel het aantal geldige rijen van lengte N met rood/grijs, waarbij:
    - elk rood blok exact lengte m heeft
    - tussen twee rode blokken mag 0 of meer grijs staan (niet verplicht)
    - grijs mag verder overal en in elke hoeveelheid staan
    """

    @lru_cache(None)
    def solve(i, r, open):
        # Einde van de rij
        if i == N:
            # Een lopend rood blok moet exact op lengte m eindigen
            if open and r != m:
                return 0
            return 1

        total = 0

        # --- Plaats grijs ---
        if open:
            # Blok afsluiten met grijs mag alleen als het al compleet is (r == m)
            if r == m:
                total += solve(i + 1, 0, False)
        else:
            total += solve(i + 1, 0, False)

        # --- Plaats rood ---
        if open:
            if r < m:
                # Blok nog niet compleet -> verlengen
                total += solve(i + 1, r + 1, True)
            else:
                # Blok is compleet (r == m) -> direct nieuw blok starten, geen grijs nodig
                total += solve(i + 1, 1, True)
        else:
            # Nieuw blok starten
            total += solve(i + 1, 1, True)

        return total

    return solve(0, 0, False) -1 # -1 omdat we de lege rij hebben meegeteld


n = 50
total = count_sequences(n, 2) + count_sequences(n, 3) + count_sequences(n, 4)
print(total)

# hieronder is een alternatieve, eenvoudigere versie van de functie die alleen het aantal geldige rijen telt zonder de extra parameters voor rood blok lengte en open status. 
# Deze versie is minder flexibel maar kan nuttig zijn voor specifieke gevallen.

# @lru_cache(None)
# def solve(i):
#     if i == N:
#         return 1
#     total = solve(i + 1)          # plaats grijs
#     if i + 2 <= N:
#         total += solve(i + 2)     # plaats compleet rood blok (RR)
#     return total