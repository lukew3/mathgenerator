from .__init__ import *


def volumeSphereFunc(maxRadius=100):

    r = random.randint(1, maxRadius)

    problem = f"Volume of sphere with radius {r} m = "
    ans = (4 * math.pi / 3) * (r ** 3)
    solution = f"{ans} m^3"
    return problem, solution
