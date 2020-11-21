from .__init__ import *


def volumeCuboid(maxSide=20, unit='m'):
    a = random.randint(1, maxSide)
    b = random.randint(1, maxSide)
    c = random.randint(1, maxSide)

    problem = f"Volume of cuboid with sides = {a}{unit}, {b}{unit}, {c}{unit} is"
    ans = a * b * c
    solution = f"{ans} {unit}^3"
    return problem, solution


volume_cuboid = Generator(
    "Volume of Cuboid", 36,
    "Volume of cuboid with sides = a units, b units, c units is", "d units^3",
    volumeCuboid)
