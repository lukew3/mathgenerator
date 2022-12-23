import random


def area_of_triangle(maxA=20, maxB=20):
    """Area of Triangle"""
    a = random.randint(1, maxA)
    b = random.randint(1, maxB)
    c = random.randint(abs(b - a) + 1, abs(a + b) - 1)

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c))**0.5

    problem = f"Area of triangle with side lengths: ${a}, {b} {c} = $"
    solution = f'${round(area, 2)}$'
    return problem, solution
