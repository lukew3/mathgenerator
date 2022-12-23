import random


def sum_of_polygon_angles(maxSides=12):
    """Sum of Angles of Polygon"""
    side_count = random.randint(3, maxSides)
    sum = (side_count - 2) * 180

    problem = f"What is the sum of interior angles of a polygon with ${side_count}$ sides?"
    return problem, f'${sum}$'
