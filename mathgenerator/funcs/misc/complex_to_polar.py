import random
import math


def complex_to_polar(minRealImaginaryNum=-20,
             maxRealImaginaryNum=20):
    """Complex to polar form"""
    num = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                  random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    a = num.real
    b = num.imag
    r = round(math.hypot(a, b), 2)
    theta = round(math.atan2(b, a), 2)

    problem = f'${r}({a}\\theta + i{b}\\theta)$'
    return problem, f'${theta}$'
