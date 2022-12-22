from ...generator import Generator
import random


def gen_func(max_dig=10):
    problem = ''

    for _ in range(random.randint(1, max_dig)):
        temp = str(random.randint(0, 1))
        problem += temp

    solution = f'${int(problem, 2)}$'
    return f'${problem}$', solution


binary_to_decimal = Generator("Binary to Decimal", 15, gen_func,
                              ["max_dig=10"])
