import random
import math


def surface_area_sphere(maxSide=20, unit='m'):
    """Surface area of a sphere"""
    r = random.randint(1, maxSide)
    ans = 4 * math.pi * r * r

    problem = f"Surface area of Sphere with radius $= {r}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution
