from ...generator import Generator
import random
import math


def gen_func(minRealImaginaryNum=-20,
             maxRealImaginaryNum=20):
    num = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                  random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    a = num.real
    b = num.imag
    r = round(math.hypot(a, b), 2)
    theta = round(math.atan2(b, a), 2)

    problem = f'${r}({a}\\theta + i{b}\\theta)$'
    return problem, f'${theta}$'


complex_to_polar = Generator(
    "Complex To Polar Form", 92, gen_func,
    ["minRealImaginaryNum=-20, maxRealImaginaryNum=20"])
