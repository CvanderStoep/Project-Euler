from math import comb

def non_bouncy_below_10_pow_n(n: int) -> int:
    # Aantal niet-dalende (increasing) getallen < 10^n (inclusief 0)
    inc = comb(n + 9, 9) - 1          # -1 om 0 uit te sluiten

    # Aantal niet-stijgende (decreasing) getallen < 10^n (inclusief 0)
    dec = comb(n + 10, 10) - n - 1    # -n-1 corrigeert leading zeros + 0

    # Constant-digit getallen (1..9, voor alle lengtes) zijn dubbel geteld
    return inc + dec - 9 * n


# brute-force check
def is_increasing(n):
    last = 10
    while n:
        d = n % 10
        if d > last:
            return False
        last = d
        n //= 10
    return True

def is_decreasing(n):
    last = -1
    while n:
        d = n % 10
        if d < last:
            return False
        last = d
        n //= 10
    return True

def is_bouncy(n):
    return not (is_increasing(n) or is_decreasing(n))



non_bouncy_count = 0
for i in range(1, 10**6):
    if not is_bouncy(i):
        non_bouncy_count += 1

print("brute force:", non_bouncy_count)              # 12951
print("combinatorisch:", non_bouncy_below_10_pow_n(100))  # 12951
