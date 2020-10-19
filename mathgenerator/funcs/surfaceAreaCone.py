from .__init__ import *


def surfaceAreaCone(maxRadius=20, maxHeight=50, unit='m'):
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)

    slopingHeight = math.sqrt(a**2 + b**2)
    problem = f"Surface area of cone with height = {a}{unit} and radius = {b}{unit} is"
    ans = int(math.pi * b * slopingHeight + math.pi * b * b)
    
    solution = f"{ans} {unit}^2"
    return problem, solution
