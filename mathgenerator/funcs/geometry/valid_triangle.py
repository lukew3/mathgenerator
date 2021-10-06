from .__init__ import *


def isTriangleValidFunc(maxSideLength=50, format='string'):
    sideA = random.randint(1, maxSideLength)
    sideB = random.randint(1, maxSideLength)
    sideC = random.randint(1, maxSideLength)

    sideSums = [sideA + sideB, sideB + sideC, sideC + sideA]
    sides = [sideC, sideA, sideB]

    exists = True & (sides[0] < sideSums[0]) & (sides[1] < sideSums[1]) & (
        sides[2] < sideSums[2])

    if format == 'string':
        problem = f"Does triangle with sides {sideA}, {sideB} and {sideC} exist?"
        if exists:
            solution = "Yes"
        else:
            solution = "No"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return sideA, sideB, sideC, exists


valid_triangle = Generator("Triangle exists check", 19, isTriangleValidFunc,
                           ["maxSideLength=50"])
