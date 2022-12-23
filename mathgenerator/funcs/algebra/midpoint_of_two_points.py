import random


def midpoint_of_two_points(maxValue=20):
    """Midpoint of two points"""
    x1 = random.randint(-20, maxValue)
    y1 = random.randint(-20, maxValue)
    x2 = random.randint(-20, maxValue)
    y2 = random.randint(-20, maxValue)
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2

    problem = f"The midpoint of $({x1},{y1})$ and $({x2},{y2}) = $"
    solution = f"$({xm},{ym})$"
    return problem, solution
