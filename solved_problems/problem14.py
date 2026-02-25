from mathlib.sequences import collatz_generator, collatz_chain


max_index, longest_chain = 1, 1
for i in range(1, 1_000):
    chain = len(list(collatz_generator(i)))
    if chain > longest_chain:
        max_index, longest_chain = i, chain

print(f'{max_index= }  {longest_chain= }')

print(collatz_chain(837799))

max_index, longest_chain = 1, 1
for i in range(1, 1_000_000):
    chain = collatz_chain(i)
    if chain > longest_chain:
        max_index, longest_chain = i, chain

print(f'{max_index= }  {longest_chain= }')


cg = collatz_generator(13)
for value in cg:
    print(value, end=' ')
