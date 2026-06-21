target = 2_000_000
min_distance = target
best_width, best_height = 1, 1

def rects(width, height):
    return (width * (width + 1) // 2) * (height * (height + 1) // 2)

for width in range(1, 100):
    for height in range(1, 100):

        count = rects(width, height)
        distance = abs(target - count)

        if distance < min_distance:
            min_distance = distance
            best_width, best_height = width, height

print(best_width * best_height)
