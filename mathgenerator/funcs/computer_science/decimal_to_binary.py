from ...generator import Generator
import random


def gen_func(max_dec=99):
    a = random.randint(1, max_dec)
    b = bin(a).replace("0b", "")

    problem = f'Binary of ${a} = $'
    solution = f'${b}$'
    return problem, solution


decimal_to_binary = Generator("Decimal to Binary", 14, gen_func,
                              ["max_dec=99"])
