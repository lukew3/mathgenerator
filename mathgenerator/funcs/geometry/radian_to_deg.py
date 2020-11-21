from .__init__ import *
from numpy import pi


def radianToDegFunc(max_rad=3):
    # max_rad is supposed to be pi but random can't handle non-integer
    a = random.randint(0, max_rad)
    b = (180 * a) / pi
    b = round(b, 2)

    problem = "Angle " + str(a) + " in degrees is = "
    solution = str(b)

    return problem, solution


radian_to_deg = Generator("Radians to Degrees", 87, "Angle a in degrees is = ",
                          "b", radianToDegFunc)
