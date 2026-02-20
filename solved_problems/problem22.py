with open('problem22.txt', 'r') as f:
    content = f.read()
names = content.split(',')
names = [n.strip('"') for n in names]
names.sort()

def letter_to_number(c):
    return ord(c.lower()) - ord('a') + 1

total_score = 0
for index, name in enumerate(names, start=1):
    value = 0
    for letter in name:
        value += letter_to_number(letter)
    total_score += value * index

print(f'{total_score= }')


# and more pythonic using copilot

with open('problem22.txt') as f:
    names = sorted(n.strip('"') for n in f.read().split(','))

total_score = sum(
    (sum(letter_to_number(c) for c in name)) * index
    for index, name in enumerate(names, start=1)
)

print(f'{total_score= }')