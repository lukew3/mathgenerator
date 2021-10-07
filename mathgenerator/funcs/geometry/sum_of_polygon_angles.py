from .__init__ import *


def gen_func(maxSides=12, format='string'):
    side_count = random.randint(3, maxSides)
    sum = (side_count - 2) * 180

    if format == 'string':
        problem = f"Sum of angles of polygon with {side_count} sides = "
        return problem, sum
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return side_count, sum


sum_of_polygon_angles = Generator("Sum of Angles of Polygon", 58,
                                  gen_func, ["maxSides=12"])
