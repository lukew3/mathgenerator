from .__init__ import *


def gen_func(maxRadius=100, format='string'):
    r = random.randint(1, maxRadius)
    ans = round((2 * math.pi / 3) * r**3, 3)

    if format == 'string':
        problem = f"Volume of hemisphere with radius {r} m = "
        solution = f"{ans} m^3"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return r, ans


volume_sphere = Generator("Volume of Hemisphere", 61, gen_func,
                          ["maxRadius=100"])