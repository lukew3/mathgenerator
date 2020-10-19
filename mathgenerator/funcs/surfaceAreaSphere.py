from .__init__ import *


def surfaceAreaSphere(maxSide = 20, unit = 'm'):
    r = random.randint(1, maxSide)
    
    problem = f"Surface area of Sphere with radius = {r}{unit} is"
    ans = 4 * math.pi * r * r
    solution = f"{ans} {unit}^2"
    return problem, solution
