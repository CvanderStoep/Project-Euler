def next_num(n):
    return sum(int(d)**2 for d in str(n))

cache = {1: 1, 89: 89}

def resolve(n):
    chain = []
    # Loop totdat we een getal tegenkomen dat al in de cache staat.
    # We bewaren tussentijdse getallen in 'chain' zodat we achteraf
    # de bekende uitkomst (1 of 89) kunnen terugschrijven voor elk
    # van die tussenliggende getallen.
    while n not in cache:
        chain.append(n)
        n = next_num(n)
    # Zodra we een bekend eindpunt bereiken, halen we dat resultaat op
    # uit de cache (cache[n] is 1 of 89).
    result = cache[n]
    for c in chain:
        cache[c] = result
    return result

total_89 = sum(1 for n in range(1, 10_000_000) if resolve(n) == 89)
print(total_89)
