from .__init__ import *

import math


def gen_func(minRealImaginaryNum=-20,
                       maxRealImaginaryNum=20,
                       format='string'):
    num = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                  random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    a = num.real
    b = num.imag
    r = round(math.hypot(a, b), 2)
    theta = round(math.atan2(b, a), 2)

    if format == 'string':
        problem = f'{r}({a}theta + i{b}theta)'
        return problem, theta
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return r, a, b, theta


complex_to_polar = Generator(
    "Complex To Polar Form", 92, gen_func,
    ["minRealImaginaryNum=-20, maxRealImaginaryNum=20"])
