from ...generator import Generator
import random


def gen_func(maxValue=20):
    x1 = random.randint(-20, maxValue)
    y1 = random.randint(-20, maxValue)
    x2 = random.randint(-20, maxValue)
    y2 = random.randint(-20, maxValue)
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2

    problem = f"The midpoint of $({x1},{y1})$ and $({x2},{y2}) = $"
    solution = f"$({xm},{ym})$"
    return problem, solution


midpoint_of_two_points = Generator("Midpoint of the two point", 20,
                                   gen_func, ["maxValue=20"])
