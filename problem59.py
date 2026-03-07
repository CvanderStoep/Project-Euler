import itertools
with open('problem59.txt') as f:
    message = [int(x) for x in f.read().split(',')]


def englishish(word):
    w = word.lower()

    # Mostly alphabetic characters
    if sum(c.isalpha() for c in w) / max(len(w), 1) < 0.8:
        return False

    # Contains at least one vowel
    if not any(v in w for v in "aeiou"):
        return False

    # Not too short
    if len(w) < 2:
        return False

    return True

# ciphertext bytes → XOR → plaintext bytes → decode → string
for combo in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=3):
    # Generate a 3‑letter lowercase key candidate, e.g. ('a','b','c')
    s = "".join(combo)

    # Convert the key string to ASCII bytes, e.g. b"abc"
    key = s.encode("ascii")
    klen = len(key)

    decrypted = bytes(m ^ key[i % klen] for i, m in enumerate(message))

    # Convert decrypted bytes to ASCII text
    decrypted = decrypted.decode("ascii")

    # Split the decrypted text into words separated by spaces
    words = decrypted.split(" ")

    # Count how many words look like English according to englishish()
    word_count = sum(1 for w in words if englishish(w))

    # If more than 80% of the words look English, assume we found the key
    if word_count / len(words) > 0.8:
        break

original_text = ' '.join(words)
print(original_text)
total = sum(ord(c) for c in original_text)
print(f'{total= }')



# encode() converts a string into a bytes object using a character encoding such as ASCII
s = "abc"
b = s.encode("ascii")
print(b)        # b'abc'
print(b[0])     # 97   (ASCII code for 'a')
print(list(b))

# decode() converts bytes back into a string, using the same encoding.
b = b'ABC'
s = b.decode("ascii")
print(s)        # "ABC"

