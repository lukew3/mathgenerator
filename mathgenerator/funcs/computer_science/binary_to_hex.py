from ...generator import Generator
import random


def gen_func(max_dig=10):
    problem = ''
    for _ in range(random.randint(1, max_dig)):
        temp = str(random.randint(0, 1))
        problem += temp

    solution = f'${hex(int(problem, 2))}$'
    return f'${problem}$', solution


binary_to_hex = Generator("Binary to Hexidecimal", 64, gen_func,
                          ["max_dig=10"])
