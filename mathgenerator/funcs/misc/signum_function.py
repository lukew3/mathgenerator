from ...generator import Generator
import random


def gen_func(min=-999, max=999):
    a = random.randint(min, max)
    b = 0
    if (a > 0):
        b = 1
    if (a < 0):
        b = -1

    problem = f"signum of {a} is ="
    solution = f'${b}$'
    return problem, solution


signum_function = Generator("signum function", 106, gen_func,
                            ["min=-999", "max=999"])
