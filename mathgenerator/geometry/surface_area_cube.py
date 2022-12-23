import random


def surface_area_cube(maxSide=20, unit='m'):
    """Surface area of a cube"""
    a = random.randint(1, maxSide)
    ans = 6 * (a ** 2)

    problem = f"Surface area of cube with side $= {a}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution
