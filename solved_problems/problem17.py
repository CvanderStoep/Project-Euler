from num2words import num2words
from collections import Counter
import string

def count_letters(word):
    word = word.lower()
    letters_only = [c for c in word if c in string.ascii_lowercase]
    # print(letters_only)
    return Counter(letters_only)

total_letters = 0
for i in range(1, 1001):
    number = num2words(i)
    counter = count_letters(number)
    total_letters += sum(counter.values())

print(f'{total_letters= }')
print(string.digits)
