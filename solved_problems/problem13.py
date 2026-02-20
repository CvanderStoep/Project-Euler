with open('part_11_20/problem13.txt') as f:
    content = f.read().splitlines()
    content = list(map(int, content))
print(content)

# with open('part_11_20/problem13.txt') as f:
#     content = list(map(int, f))
# print(content)

first_digits = str(sum(content))
print(first_digits[:10])