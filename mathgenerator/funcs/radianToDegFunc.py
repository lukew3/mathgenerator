from .__init__ import *
from numpy import pi

def degreeToRadFunc(max_rad=pi):
    a = random.randint(0, max_rad)
    b = (180*a)/pi
    b = round(b, 2)

    problem = "Angle " + str(a) + " in degrees is = "
    solution = str(b)

    return problem, solution

radianToDeg = Generator("Radians to Degrees", 87, "Angle a in degrees is = ", "b", radianToDegFunc)
