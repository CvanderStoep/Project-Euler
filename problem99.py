
from typing import List, Tuple
import math


def load_pairs(filepath: str = "problem99.txt") -> List[Tuple[int, int]]:
	"""Read a file of lines 'a,b' and return list of (a, b) integer pairs."""
	with open(filepath, "r", encoding="utf-8") as f:
		return [list(map(int, line.strip().split(","))) for line in f]



if __name__ == "__main__":
    pairs = load_pairs()
    max_index = None
    max_value = float("-inf")
    for index, (a, b) in enumerate(pairs, start=1):
        value = b * math.log(a)
        if value > max_value:
            max_value = value
            max_index = index
    if max_index is not None:
        print(f"Line {max_index}: {pairs[max_index - 1]} with value {max_value}")
