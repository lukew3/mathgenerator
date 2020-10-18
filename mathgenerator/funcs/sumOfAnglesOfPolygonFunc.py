from .__init__ import *


def sumOfAnglesOfPolygonFunc(maxSides = 12):
    side = random.randint(3, maxSides)
    sum = (side - 2) * 180
    
    problem = f"Sum of angles of polygon with {side} sides = "
    solution = sum
    return problem, solution
