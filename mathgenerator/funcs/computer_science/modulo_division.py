from ...generator import Generator
import random


def gen_func(maxRes=99, maxModulo=99):
    a = random.randint(0, maxModulo)
    b = random.randint(0, min(maxRes, maxModulo))
    c = a % b if b != 0 else 0

    problem = f'${a}$ % ${b} = $'
    solution = f'${c}$'
    return problem, solution


modulo_division = Generator("Modulo Division", 5, gen_func,
                            ["maxRes=99", "maxModulo=99"])
