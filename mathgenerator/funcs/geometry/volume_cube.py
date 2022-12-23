import random


def volume_cube(maxSide=20, unit='m'):
    """Volume of a cube"""
    a = random.randint(1, maxSide)
    ans = a**3

    problem = f"Volume of cube with a side length of ${a}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution
