from dataclasses import dataclass
from itertools import product



@dataclass(frozen=True)
class Hit:
    score: int
    multiplier: int

    def __repr__(self):
        multiplier_str = {1: "S", 2: "D", 3: "T"}.get(self.multiplier, "")
        if self.score == 0:
            return "  "
        return f"{multiplier_str}{self.score}"


def valid_finish(combination: tuple[Hit, Hit, Hit], finish: int) -> bool:
    return combination[2].multiplier == 2 and sum(hit.score * hit.multiplier for hit in combination) == finish


def normalize_hit(c: tuple[Hit, Hit, Hit]) -> tuple[Hit, Hit, Hit]:
    # sort first two hits by (score, multiplier)
    first_two = tuple(sorted(c[:2], key=lambda h: (h.score, h.multiplier)))
    return first_two + (c[2],)

total_finishes = 0
for finish in range(1, 100):


    singles = [Hit(score=i, multiplier=1) for i in range(0, 21)] + [Hit(score=25, multiplier=1)]
    doubles = [Hit(score=i, multiplier=2) for i in range(1, 21)] + [Hit(score=25, multiplier=2)]
    trebles = [Hit(score=i, multiplier=3) for i in range(1, 21)]

    hits = singles + doubles + trebles

    all_combinations = product(hits, repeat=3)
    valid_combinations = {normalize_hit(c) for c in all_combinations if valid_finish(c, finish)}

    total_finishes += len(list(valid_combinations))

print(f"Total finishes: {total_finishes}")