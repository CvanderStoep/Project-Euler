import random
from collections import defaultdict


# --- Board -------------------------------------------------------------------

class Board:
    def __init__(self):
        self.fields = [
            'GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL',
            'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP',
            'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J',
            'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2'
        ]
        self.size = len(self.fields)
        self.index = {name: i for i, name in enumerate(self.fields)}

    def next_of_type(self, pos, prefix):
        for i in range(1, self.size + 1):
            idx = (pos + i) % self.size
            if self.fields[idx].startswith(prefix):
                return idx
        return pos


# --- Card Decks --------------------------------------------------------------

class CardDeck:
    def __init__(self, board: Board):
        self.board = board

    def community_chest(self, pos):
        n = random.randint(1, 16)
        match n:
            case 1:
                return self.board.index['GO']
            case 2:
                return self.board.index['JAIL']
            case _:
                return pos

    def chance(self, pos):
        n = random.randint(1, 16)
        match n:
            case 1:
                return self.board.index['GO']
            case 2:
                return self.board.index['JAIL']
            case 3:
                return self.board.index['C1']
            case 4:
                return self.board.index['E3']
            case 5:
                return self.board.index['H2']
            case 6:
                return self.board.index['R1']
            case 7 | 8:
                return self.board.next_of_type(pos, "R")
            case 9:
                return self.board.next_of_type(pos, "U")
            case 10:
                return (pos - 3) % self.board.size
            case _:
                return pos


# --- Monopoly Game -----------------------------------------------------------

class MonopolyGame:
    def __init__(self, board: Board, cards: CardDeck):
        self.board = board
        self.cards = cards
        self.position = 0
        self.consecutive_doubles = 0

    def roll(self):
        d1 = random.randint(1, 4)
        d2 = random.randint(1, 4)
        return d1, d2, d1 + d2

    def step(self):
        d1, d2, throw = self.roll()

        # 3 doubles → jail
        if d1 == d2:
            self.consecutive_doubles += 1
            if self.consecutive_doubles == 3:
                self.position = self.board.index['JAIL']
                self.consecutive_doubles = 0
                return self.position
        else:
            self.consecutive_doubles = 0

        # Move
        self.position = (self.position + throw) % self.board.size

        field = self.board.fields[self.position]

        # Go to jail
        if field == 'G2J':
            self.position = self.board.index['JAIL']

        # Community Chest
        elif field.startswith('CC'):
            self.position = self.cards.community_chest(self.position)

        # Chance
        elif field.startswith('CH'):
            self.position = self.cards.chance(self.position)

        return self.position


# --- Simulator ---------------------------------------------------------------

class Simulator:
    def __init__(self, iterations=10_000_000):
        self.iterations = iterations
        self.board = Board()
        self.cards = CardDeck(self.board)
        self.game = MonopolyGame(self.board, self.cards)
        self.counts = defaultdict(int)

    def run(self):
        self.counts[self.game.position] += 1

        for _ in range(self.iterations):
            pos = self.game.step()
            self.counts[pos] += 1

    def report(self):
        total = sum(self.counts.values())

        top5 = sorted(self.counts.items(), key=lambda x: x[1], reverse=True)[:5]
        bottom3 = sorted(self.counts.items(), key=lambda x: x[1])[:3]

        print("top-5")
        for idx, c in top5:
            pct = (c / total) * 100
            print(f"{idx, self.board.fields[idx]}: {c} keer ({pct:.2f}%)")

        print("bottom-3")
        for idx, c in bottom3:
            pct = (c / total) * 100
            print(f"{idx, self.board.fields[idx]}: {c} keer ({pct:.2f}%)")


# --- Run ---------------------------------------------------------------------

if __name__ == "__main__":
    sim = Simulator(iterations=10_000_000)
    sim.run()
    sim.report()
