from ...generator import Generator
import random


def gen_func(minVal=3, maxVal=20, format='string'):
    sideNum = random.randint(minVal, maxVal)
    problem = f"Find the angle of a regular polygon with ${sideNum}$ sides"

    exteriorAngle = round((360 / sideNum), 2)
    solution = f'${180 - exteriorAngle}$'

    return problem, solution


angle_regular_polygon = Generator("Angle of a Regular Polygon", 29,
                                  gen_func,
                                  ["minVal=3", "maxVal=20"])
