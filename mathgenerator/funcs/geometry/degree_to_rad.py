from .__init__ import *
from numpy import pi


def degreeToRadFunc(max_deg=360):
    a = random.randint(0, max_deg)
    b = (pi * a) / 180
    b = round(b, 2)

    problem = "Angle " + str(a) + " in radians is = "
    solution = str(b)

    return problem, solution


degree_to_rad = Generator("Degrees to Radians", 86, "Angle a in radians is = ",
                          "b", degreeToRadFunc)
