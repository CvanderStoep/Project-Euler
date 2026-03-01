from collections import Counter
from typing import Tuple, List

with open('problem54.txt', 'r') as f:
    content = f.read().splitlines()
    deals = []
    for deal in content:
        playing_cards = deal.split(" ")
        player1= playing_cards[:5]
        player2= playing_cards[5:]
        deals.append((player1, player2))


# Kaartwaarden: A = 14
VALUE_MAP = {
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}

def parse_hand(hand):
    # hand = ["AS", "KD", "3H", ...]
    values = sorted([VALUE_MAP[c[0]] for c in hand])
    suits = [c[1] for c in hand]
    return values, suits

from typing import Optional, Tuple, List

def is_straight(values: List[int]) -> Optional[int]:
    # Normale straight
    if len(set(values)) == 5 and values[-1] - values[0] == 4:
        return values[-1]

    # A-5 straight (wheel)
    if values == [2, 3, 4, 5, 14]:
        return 5

    return None

def hand_rank(hand) -> Tuple[int, Tuple[int, ...]]:
    values, suits = parse_hand(hand)
    counts = Counter(values)
    freq = sorted(counts.values(), reverse=True)
    unique_vals = sorted(counts.keys(), key=lambda v: (-counts[v], -v))

    is_flush = len(set(suits)) == 1
    high_straight = is_straight(values)

    # 8: Straight flush
    if high_straight is not None and is_flush:
        return (8, (high_straight,))

    # 7: Four of a kind
    if freq == [4, 1]:
        four = unique_vals[0]
        kicker = unique_vals[1]
        return (7, (four, kicker))

    # 6: Full house
    if freq == [3, 2]:
        three = unique_vals[0]
        pair = unique_vals[1]
        return (6, (three, pair))

    # 5: Flush
    if is_flush:
        return (5, tuple(sorted(values, reverse=True)))

    # 4: Straight
    if high_straight is not None:
        return (4, (high_straight,))

    # 3: Three of a kind
    if freq == [3, 1, 1]:
        three = unique_vals[0]
        kickers = unique_vals[1:]
        return (3, (three, *kickers))

    # 2: Two pair
    if freq == [2, 2, 1]:
        pair1, pair2, kicker = unique_vals
        return (2, (pair1, pair2, kicker))

    # 1: One pair
    if freq == [2, 1, 1, 1]:
        pair = unique_vals[0]
        kickers = unique_vals[1:]
        return (1, (pair, *kickers))

    # 0: High card
    return (0, tuple(sorted(values, reverse=True)))

hand1 = ["AS", "KS", "QS", "JS", "TS"]  # Royal flush
hand2 = ["9C", "9D", "9H", "9S", "2D"]  # Four of a kind
hand3 = ["KC", "6C", "7H", "6S", "9C"]  # One pair

print(hand_rank(hand1))  # (8, (14,))
print(hand_rank(hand2))  # (7, (9, 2))
print(hand_rank(hand3))  # (1, (6, 13, 9, 7))

print(hand_rank(hand1) > hand_rank(hand2))  # True

p1_wins = 0
for player1, player2 in deals:
    p1 = hand_rank(player1)
    p2 = hand_rank(player2)
    if p1 > p2:
        p1_wins += 1

print(f'{p1_wins= }')