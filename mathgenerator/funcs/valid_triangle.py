from .__init__ import *


def isTriangleValidFunc(maxSideLength=50):
    sideA = random.randint(1, maxSideLength)
    sideB = random.randint(1, maxSideLength)
    sideC = random.randint(1, maxSideLength)

    sideSums = [sideA + sideB, sideB + sideC, sideC + sideA]
    sides = [sideC, sideA, sideB]

    exists = True & (sides[0] < sideSums[0]) & (sides[1] < sideSums[1]) & (
        sides[2] < sideSums[2])
    problem = f"Does triangle with sides {sideA}, {sideB} and {sideC} exist?"

    if exists:
        solution = "Yes"
        return problem, solution
    solution = "No"
    return problem, solution


valid_triangle = Generator("Triangle exists check", 19,
                           "Does triangle with sides a, b and c exist?",
                           "Yes/No", isTriangleValidFunc)
