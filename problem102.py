


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    
    results = []
    for s in lines:
        nums = list(map(int, s.split(",")))
        coords = list(zip(nums[0::2], nums[1::2]))
        results.append(coords)
    
    return results

def area2(x1, y1, x2, y2, x3, y3):
    # Twice the signed area of triangle
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

def point_in_triangle(p, a, b, c):
    px, py = p
    ax, ay = a
    bx, by = b
    cx, cy = c
    # Total area * 2
    A = area2(ax, ay, bx, by, cx, cy)
    # Sub-areas * 2
    A1 = area2(px, py, bx, by, cx, cy)
    A2 = area2(ax, ay, px, py, cx, cy)
    A3 = area2(ax, ay, bx, by, px, py)

    # Inside if areas match exactly
    return A == A1 + A2 + A3



if __name__ == '__main__':
    coordinates_list = read_file('problem102.txt')
    number_of_triangles_containing_origin = 0
    for coords in coordinates_list:
        x, y, z = coords
        origin = (0, 0)
        if point_in_triangle(origin, x, y, z):
            number_of_triangles_containing_origin += 1
    print(f"Number of triangles containing the origin: {number_of_triangles_containing_origin}")


