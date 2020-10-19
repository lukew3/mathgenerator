from .__init__ import *


def volumeCube(maxSide=20, unit='m'):
    a = random.randint(1, maxSide)
    
    problem = f"Volume of cube with side = {a}{unit} is"
    ans = a * a * a
    solution = f"{ans} {unit}^3"
    return problem, solution
