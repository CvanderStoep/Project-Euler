from functools import lru_cache
N = 50

"""
    Tel het aantal geldige rijen van lengte N met rood/grijs, waarbij:
    - elk rood blok exact lengte m heeft
    - tussen twee rode blokken mag 0 of meer grijs staan (niet verplicht)
    - grijs mag verder overal en in elke hoeveelheid staan
"""

# hieronder is een alternatieve, eenvoudigere versie van de functie die alleen het aantal geldige rijen telt zonder de extra parameters voor rood blok lengte en open status. 
# Deze versie is minder flexibel maar kan nuttig zijn voor specifieke gevallen.

@lru_cache(None)
def solve(i, l):
    if i == N:
        return 1
    total = solve(i + 1, l)          # plaats grijs
    if i + l <= N:
        total += solve(i + l, l)     # plaats compleet rood blok (RR)
    return total



total = solve(0, 2) + solve(0, 3) + solve(0, 4) - 3  # -1 omdat we de lege rij hebben meegeteld
print(total)

