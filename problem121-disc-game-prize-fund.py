from fractions import Fraction

def max_prize(turns):
    # dp[b] = probability of having drawn exactly b blue discs so far
    dp = {0: Fraction(1)}
    for i in range(1, turns + 1):
        p_blue = Fraction(1, i + 1)        # turn i: 1 blue among i + 1 discs
        new = {}
        for b, p in dp.items():
            new[b + 1] = new.get(b + 1, 0) + p * p_blue
            new[b] = new.get(b, 0) + p * (1 - p_blue)
        dp = new
    p_win = sum(p for b, p in dp.items() if b > turns - b)
    return int(1 / p_win)                  # floor(1 / P)

print(max_prize(4))    # 10 (sanity check)
print(max_prize(15))   # answer