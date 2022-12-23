from ...generator import Generator
import random


def gen_func(max_dec=1000):
    a = random.randint(0, max_dec)
    b = hex(a)

    problem = f"Binary of ${a} = $"
    solution = f"${b}$"
    return problem, solution


decimal_to_hexadeci = Generator("Decimal to Hexadecimal", 79, gen_func,
                                ["max_dec=1000"])
