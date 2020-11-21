from .__init__ import *

import math


def complexToPolarFunc(minRealImaginaryNum=-20, maxRealImaginaryNum=20):
    num = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                  random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    a = num.real
    b = num.imag
    r = round(math.hypot(a, b), 2)
    theta = round(math.atan2(b, a), 2)
    plr = str(r) + "exp(i" + str(theta) + ")"
    problem = "rexp(itheta) = "
    solution = plr
    return problem, solution


complex_to_polar = Generator("Complex To Polar Form", 92, "rexp(itheta) = ",
                             "plr", complexToPolarFunc)
