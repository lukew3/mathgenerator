from ...generator import Generator
import random


def gen_func(maxSides=12):
    side_count = random.randint(3, maxSides)
    sum = (side_count - 2) * 180

    problem = f"What is the sum of interior angles of a polygon with ${side_count}$ sides?"
    return problem, f'${sum}$'


sum_of_polygon_angles = Generator("Sum of Angles of Polygon", 58,
                                  gen_func, ["maxSides=12"])
