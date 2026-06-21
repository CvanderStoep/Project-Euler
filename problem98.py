"""
Generate all assignments of unique digits (0-9) to letters in a word.
The resulting mapping ensures the word does not start with 0.

Usage: run the script and input a word, or call get_mappings(word).
"""
from mathlib.arithmetic import is_perfect_square
from itertools import permutations, combinations



def get_mappings(word):
    """Yield dictionaries mapping each distinct letter in word to a digit (as int).

    The word cannot start with a mapping to 0.
    Letters are case-sensitive by default; you can .upper() or .lower() the word beforehand.
    """
    if not word:
        return
    letters = []
    seen = set()
    for ch in word:
        if ch not in seen:
            seen.add(ch)
            letters.append(ch)
    n = len(letters)
    if n > 10:
        return
    digits = '0123456789'
    for perm in permutations(digits, n):
        # leading letter cannot map to '0'
        if perm[letters.index(word[0])] == '0':
            continue
        mapping = {letters[i]: int(perm[i]) for i in range(n)}
        yield mapping


def format_mapped(word, mapping):
    return ''.join(str(mapping[ch]) for ch in word)


def word_to_number(mapping, word):
    """Convert a word to a number using the given mapping."""
    return int(''.join(str(mapping[ch]) for ch in word))


def main():
    largest_square = 0
    # Read all words from problem98.txt
    with open('problem98.txt', 'r') as f:
        words = [word.strip().strip('"') for line in f for word in line.split(',')]
    
    for word1, word2 in combinations(words, 2):
        if len(word1) != len(word2):
            continue
        if sorted(word1) != sorted(word2):
            continue
        print(f"Processing word pair: {word1}, {word2}")
        for mapping in get_mappings(word1):
            mapped_value = format_mapped(word1, mapping)
            if is_perfect_square(int(mapped_value)):
                # Now check if the same mapping can be applied to word2
                if mapping[word2[0]] == 0:
                    continue
                mapped_value2 = format_mapped(word2, mapping)
                if is_perfect_square(int(mapped_value2)):
                    print(f"Mapping: {mapping}, Word1: {word_to_number(mapping, word1)}, Word2: {word_to_number(mapping, word2)}")
                    largest_square = max(largest_square, int(mapped_value), int(mapped_value2))

    print(f"Largest square found: {largest_square}")


if __name__ == '__main__':
    main()
