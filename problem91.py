def check_right_angle(v1, v2):
    """Return True if triangle (0,0), v1, v2 is right-angled."""
    # Vector from point 1 to point 2
    v3 = (v2[0] - v1[0], v2[1] - v1[1])
    # Right angle at origin: v1 dot v2 == 0
    if v1[0] * v2[0] + v1[1] * v2[1] == 0:
        return True
    # Right angle at point 1: v1 dot v3 == 0
    if v1[0] * v3[0] + v1[1] * v3[1] == 0:
        return True
    # Right angle at point 2: v2 dot v3 == 0
    if v2[0] * v3[0] + v2[1] * v3[1] == 0:
        return True
    return False

def count_right_triangles(n):
    """
    Count right triangles with vertices at (0,0), (x1,y1), (x2,y2)
    where x1, y1, x2, y2 are integers between 0 and n
    """
    count = 0
    
    for x1 in range(n + 1):
        for y1 in range(n + 1):
            for x2 in range(n + 1):
                for y2 in range(n + 1):
                    # Skip if both points are at origin
                    if x1 == 0 and y1 == 0:
                        continue
                    if x2 == 0 and y2 == 0:
                        continue
                    # Skip if points are the same
                    if x1 == x2 and y1 == y2:
                        continue
                    
                    # Check for right angle using helper
                    v1 = (x1, y1)
                    v2 = (x2, y2)
                    if check_right_angle(v1, v2):
                        count += 1
    
    # Each triangle is counted twice (once for each ordering)
    return count // 2


# Example usage
if __name__ == "__main__":
    n = 50
    result = count_right_triangles(n)
    print(f"Number of right triangles with n={n}: {result}")


