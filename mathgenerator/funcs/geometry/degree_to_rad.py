from .__init__ import *
from numpy import pi


def degreeToRadFunc(max_deg=360, format='string'):
    a = random.randint(0, max_deg)
    b = (pi * a) / 180
    b = round(b, 2)

    if format == 'string':
        problem = "Angle " + str(a) + " in radians is = "
        solution = str(b)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b


degree_to_rad = Generator("Degrees to Radians", 86, degreeToRadFunc,
                          ["max_deg=360"])
