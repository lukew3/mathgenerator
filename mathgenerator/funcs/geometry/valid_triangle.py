from ...generator import Generator
import random


def gen_func(maxSideLength=50):
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


valid_triangle = Generator("Triangle exists check", 19, gen_func,
                           ["maxSideLength=50"])
