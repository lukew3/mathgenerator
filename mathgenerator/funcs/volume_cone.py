from .__init__ import *


def volumeCone(maxRadius=20, maxHeight=50, unit='m'):
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)

    problem = f"Volume of cone with height = {a}{unit} and radius = {b}{unit} is"
    ans = int(math.pi * b * b * a * (1 / 3))
    solution = f"{ans} {unit}^3"
    return problem, solution


volume_cone = Generator(
    "Volume of cone", 39,
    "Volume of cone with height = a units and radius = b units is",
    "c units^3", volumeCone)
