import random
from collections import defaultdict

# --- Board setup -------------------------------------------------------------

monopoly_board = [
    'GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL',
    'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP',
    'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J',
    'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2'
]

BOARD_LEN = len(monopoly_board)

# Precompute indices for speed
INDEX = {name: i for i, name in enumerate(monopoly_board)}


# --- Helpers ----------------------------------------------------------------

def next_of_type(pos, prefix):
    """Find next board index starting with prefix (R or U)."""
    for i in range(1, BOARD_LEN + 1):
        idx = (pos + i) % BOARD_LEN
        if monopoly_board[idx].startswith(prefix):
            return idx
    return pos   # fallback (should never happen)


# --- Card logic --------------------------------------------------------------

def community_chest(pos):
    n = random.randint(1, 16)
    match n:
        case 1:
            return INDEX['GO']
        case 2:
            return INDEX['JAIL']
        case _:
            return pos   # no movement


def chance(pos):
    n = random.randint(1, 16)
    match n:
        case 1:
            return INDEX['GO']
        case 2:
            return INDEX['JAIL']
        case 3:
            return INDEX['C1']
        case 4:
            return INDEX['E3']
        case 5:
            return INDEX['H2']
        case 6:
            return INDEX['R1']
        case 7 | 8:
            return next_of_type(pos, "R")
        case 9:
            return next_of_type(pos, "U")
        case 10:
            return (pos - 3) % BOARD_LEN
        case _:
            return pos   # no movement


# --- Simulation --------------------------------------------------------------

current_position = 0
counts = defaultdict(int)
counts[current_position] += 1
consecutive_doubles = 0

for _ in range(10_000_000):
    d1 = random.randint(1, 4)
    d2 = random.randint(1, 4)
    throw = d1 + d2

    # 3 doubles → jail
    if d1 == d2:
        consecutive_doubles += 1
        if consecutive_doubles == 3:
            current_position = INDEX['JAIL']
            counts[current_position] += 1
            consecutive_doubles = 0
            continue
    else:
        consecutive_doubles = 0

    # Move
    current_position = (current_position + throw) % BOARD_LEN

    # Go to jail
    if monopoly_board[current_position] == 'G2J':
        current_position = INDEX['JAIL']

    # Community Chest
    elif monopoly_board[current_position].startswith('CC'):
        current_position = community_chest(current_position)

    # Chance
    elif monopoly_board[current_position].startswith('CH'):
        current_position = chance(current_position)

    counts[current_position] += 1


# --- Results ----------------------------------------------------------------

total = sum(counts.values())

top5 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]
bottom3 = sorted(counts.items(), key=lambda x: x[1])[:3]

print("top-5")
for idx, c in top5:
    pct = (c / total) * 100
    print(f"{idx, monopoly_board[idx]}: {c} keer ({pct:.2f}%)")

print("bottom-3")
for idx, c in bottom3:
    pct = (c / total) * 100
    print(f"{idx, monopoly_board[idx]}: {c} keer ({pct:.2f}%)")
