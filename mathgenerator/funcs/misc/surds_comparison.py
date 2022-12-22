from ...generator import Generator
import random
import math


def gen_func(maxValue=100, maxRoot=10):
    radicand1, radicand2 = tuple(random.sample(range(1, maxValue), 2))
    degree1, degree2 = tuple(random.sample(range(1, maxRoot), 2))
    first = math.pow(radicand1, 1 / degree1)
    second = math.pow(radicand2, 1 / degree2)

    solution = "="
    if first > second:
        solution = ">"
    elif first < second:
        solution = "<"

    problem = f"Fill in the blanks ${radicand1}^{{\\frac{{1}}{{{degree1}}}}}$ _ ${radicand2}^{{\\frac{{1}}{{{degree2}}}}}$"
    return problem, f'${solution}$'


surds_comparison = Generator("Comparing surds", 55, gen_func,
                             ["maxValue=100", "maxRoot=10"])
