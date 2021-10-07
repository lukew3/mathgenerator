from .__init__ import *


def gen_func(maxValXY=20, minValXY=-20, format='string'):
    point1X = random.randint(minValXY, maxValXY + 1)
    point1Y = random.randint(minValXY, maxValXY + 1)
    point2X = random.randint(minValXY, maxValXY + 1)
    point2Y = random.randint(minValXY, maxValXY + 1)

    distanceSq = (point1X - point2X)**2 + (point1Y - point2Y)**2

    if format == 'string':
        solution = f"sqrt({distanceSq})"
        problem = f"Find the distance between ({point1X}, {point1Y}) and ({point2X}, {point2Y})"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return point1X, point1Y, point2X, point2Y, distanceSq


distance_two_points = Generator("Distance between 2 points", 24,
                                gen_func,
                                ["maxValXY=20", "minValXY=-20"])
