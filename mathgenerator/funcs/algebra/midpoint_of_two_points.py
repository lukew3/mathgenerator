from .__init__ import *


def MidPointOfTwoPointFunc(maxValue=20, format='string'):
    x1 = random.randint(-20, maxValue)
    y1 = random.randint(-20, maxValue)
    x2 = random.randint(-20, maxValue)
    y2 = random.randint(-20, maxValue)
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2

    if format == 'string':
        problem = f"({x1},{y1}),({x2},{y2})="
        solution = f"({xm},{ym})"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return x1, y1, x2, y2, xm, ym


midPoint_of_two_points = Generator("Midpoint of the two point", 20,
                                   MidPointOfTwoPointFunc, ["maxValue=20"])
