from .__init__ import *


def distanceTwoPointsFunc(maxValXY=20, minValXY=-20):
    point1X = random.randint(minValXY, maxValXY + 1)
    point1Y = random.randint(minValXY, maxValXY + 1)
    point2X = random.randint(minValXY, maxValXY + 1)
    point2Y = random.randint(minValXY, maxValXY + 1)

    distanceSq = (point1X - point2X)**2 + (point1Y - point2Y)**2

    solution = f"sqrt({distanceSq})"
    problem = f"Find the distance between ({point1X}, {point1Y}) and ({point2X}, {point2Y})"
    return problem, solution


distance_two_points = Generator(
    "Distance between 2 points", 24,
    "Find the distance between (x1,y1) and (x2,y2)", "sqrt(distanceSquared)",
    distanceTwoPointsFunc)
