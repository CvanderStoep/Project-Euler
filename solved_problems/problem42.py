with open('problem42.txt', 'r') as f:
    content = f.read()
names = content.split(',')
names = [n.strip('"') for n in names]
# print(names)

def letter_to_number(c):
    return ord(c.lower()) - ord('a') + 1

triangle_numbers = [int(1/2 * n * (n + 1)) for n in range(1,25)]
print(triangle_numbers)

total_score = 0


for index, name in enumerate(names, start=1):
    value = 0
    for letter in name:
        value += letter_to_number(letter)
    if value in triangle_numbers:
        total_score += 1
print(f'{total_score= }')

