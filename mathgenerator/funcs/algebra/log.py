from ...generator import Generator
import random


def gen_func(maxBase=3, maxVal=8, format='string'):
    a = random.randint(1, maxVal)
    b = random.randint(2, maxBase)
    c = pow(b, a)

    problem = f'$log_{{{b}}}({c})=$'
    solution = f'${a}$'
    return problem, solution


log = Generator("Logarithm", 12, gen_func, ["maxBase=3", "maxVal=8"])
