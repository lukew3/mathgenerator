from ...generator import Generator
import random
import numpy as np


def gen_func(maxValue=100, maxCount=4):
    count = random.randint(2, maxCount)
    nums = [random.randint(1, maxValue) for i in range(count)]
    product = np.prod(nums)

    ans = round(product ** (1 / count), 2)
    problem = f"Geometric mean of ${count}$ numbers ${nums} = $"
    # solution = f"$({'*'.join(map(str, nums))}^{{\\frac{{1}}{{{count}}}}} = {ans}$"
    solution = f"${ans}$"
    return problem, solution


geometric_mean = Generator("Geometric Mean of N Numbers", 67,
                           gen_func, ["maxValue=100", "maxCount=4"])
