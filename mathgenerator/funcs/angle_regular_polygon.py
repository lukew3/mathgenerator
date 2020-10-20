from .__init__ import *


def regularPolygonAngleFunc(minVal=3, maxVal=20):
    sideNum = random.randint(minVal, maxVal)
    problem = f"Find the angle of a regular polygon with {sideNum} sides"

    exteriorAngle = round((360 / sideNum), 2)
    solution = 180 - exteriorAngle
    return problem, solution


angle_regular_polygon = Generator(
    "Angle of a Regular Polygon", 29,
    "Find the angle of a regular polygon with 6 sides", "120",
    regularPolygonAngleFunc)
