import random


def angle_regular_polygon(minVal=3, maxVal=20, format='string'):
    """Angle of a Regular Polygon"""
    sideNum = random.randint(minVal, maxVal)
    problem = f"Find the angle of a regular polygon with ${sideNum}$ sides"

    exteriorAngle = round((360 / sideNum), 2)
    solution = f'${180 - exteriorAngle}$'

    return problem, solution
