import random


def valid_triangle(maxSideLength=50):
    """Valid Triangle"""
    sideA = random.randint(1, maxSideLength)
    sideB = random.randint(1, maxSideLength)
    sideC = random.randint(1, maxSideLength)

    sideSums = [sideA + sideB, sideB + sideC, sideC + sideA]
    sides = [sideC, sideA, sideB]

    exists = True & (sides[0] < sideSums[0]) & (sides[1] < sideSums[1]) & (
        sides[2] < sideSums[2])

    problem = f"Does triangle with sides ${sideA}, {sideB}$ and ${sideC}$ exist?"
    solution = "Yes" if exists else "No"
    return problem, f'${solution}$'
