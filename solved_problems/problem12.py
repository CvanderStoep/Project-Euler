from mathlib.arithmetic import divisors

def triangle_generator():
    """Generate Triangle numbers indefinitely"""
    a, triangle = 1, 1
    while True:
        yield triangle
        a += 1
        triangle += a

triangle = triangle_generator()

n = 500
    # get triangle
    # get factors
    # stop when #factors > N
while True:
    next_triangle = next(triangle)
    print(next_triangle)
    divisor_list = divisors(next_triangle)
    if len(divisor_list) > n:
        print(next_triangle)
        print(divisor_list)
        break


