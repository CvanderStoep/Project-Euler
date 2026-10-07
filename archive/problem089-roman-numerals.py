roman_map = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}

def read_file_lines(filepath):
    """Read a text file and return a list of its lines (stripped of trailing newlines).

    If the file does not exist or is not readable an empty list is returned.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return [line.rstrip('\n') for line in f]
    except Exception:
        return []

def number_to_roman(n: int) -> str:
    """Convert an integer to a Roman numeral string.

    Supports 1..5000. Returns an empty string for values outside this range.
    Note: 5000 is represented by the Unicode character '\u2181' (ROMAN NUMERAL FIVE THOUSAND, 'ↁ').
    Values 1000..4999 continue to use repeated 'M' for thousands (e.g. 4000 -> 'MMMM').
    """
    if not isinstance(n, int) or n <= 0 or n > 5000:
        print(f"Input {n} is out of range (1..5000). Returning empty string.")
        input()
        return ""
    # Create a list of tokens sorted by descending value
    tokens = sorted(roman_map.items(), key=lambda kv: kv[1], reverse=True)
    result = []
    remaining = n
    for sym, val in tokens:
        if remaining <= 0:
            break
        count, remaining = divmod(remaining, val)
        if count:
            result.append(sym * count)
    return ''.join(result)


def roman_to_values(roman_string):
    """Convert a Roman numeral string to a list of values."""
    values = []
    i = 0
    # Precompute two-character tokens to check first
    two_char_tokens = {k for k in roman_map.keys() if len(k) == 2}
    # Normalize input
    s = roman_string.strip().upper()
    while i < len(s):
        # Check for two-character Roman numerals first
        if i + 1 < len(s) and s[i:i+2] in two_char_tokens:
            values.append(roman_map[s[i:i+2]])
            i += 2
            continue
        # Then check for single-character Roman numerals
        if s[i] in roman_map:
            values.append(roman_map[s[i]])
            i += 1
            continue
        # Skip unknown characters
        i += 1
    return values

def is_valid_roman(roman_string):
    """Return True if the Roman numeral converts to a non-empty list of values
    that are in non-increasing (descending) order. Equal adjacent values allowed.
    """
    values = roman_to_values(roman_string)
    if not values:
        return False
    for prev, curr in zip(values, values[1:]):
        if curr > prev:
            return False
    return True


lines = read_file_lines('problem89.txt')

total_saved = 0
for roman_string in lines:
    original_length = len(roman_string)
    optimized_roman = number_to_roman(sum(roman_to_values(roman_string)))
    optimized_length = len(optimized_roman)
    saved = original_length - optimized_length
    total_saved += saved
    # print(f"{roman_string} -> {optimized_roman} (saved {saved} characters)")


print(f"Total characters saved: {total_saved}")