from .__init__ import *


def volumeSphereFunc(maxRadius=100, format='string'):
    r = random.randint(1, maxRadius)
    ans = (4 * math.pi / 3) * r**3

    if format == 'string':
        problem = f"Volume of sphere with radius {r} m = "
        solution = f"{ans} m^3"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return r, ans


volume_sphere = Generator("Volume of Sphere", 61, volumeSphereFunc,
                          ["maxRadius=100"])
