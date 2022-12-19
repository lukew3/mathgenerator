from ...__init__ import Generator
import random
import math


def gen_func(max_rad=3, format='string'):
    # max_rad is supposed to be pi but random can't handle non-integer
    a = random.randint(0, max_rad)
    b = (180 * a) / math.pi
    b = round(b, 2)

    if format == 'string':
        problem = "Angle " + str(a) + " in degrees is = "
        solution = str(b)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b


radian_to_deg = Generator("Radians to Degrees", 87, gen_func,
                          ["max_rad=3"])
