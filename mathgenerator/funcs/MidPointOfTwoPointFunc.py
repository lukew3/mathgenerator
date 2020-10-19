from .__init__ import *


def MidPointOfTwoPointFunc(maxValue=20):
    x1 = random.randint(-20, maxValue)
    y1 = random.randint(-20, maxValue)
    x2 = random.randint(-20, maxValue)
    y2 = random.randint(-20, maxValue)
    
    problem = f"({x1},{y1}),({x2},{y2})="
    solution = f"({(x1+x2)/2},{(y1+y2)/2})"
    return problem, solution
