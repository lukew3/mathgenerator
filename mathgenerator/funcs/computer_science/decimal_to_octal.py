from ...generator import Generator
import random


def gen_func(maxDecimal=4096):
    x = random.randint(0, maxDecimal)

    problem = "The decimal number ${x}$ in Octal is: "
    solution = f'${oct(x)}$'

    return problem, solution


decimal_to_octal = Generator("Converts decimal to octal", 84,
                             gen_func, ["maxDecimal=4096"])
