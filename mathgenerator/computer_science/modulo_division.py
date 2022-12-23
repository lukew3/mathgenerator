import random


def modulo_division(maxRes=99, maxModulo=99):
    """Modulo Division"""
    a = random.randint(0, maxModulo)
    b = random.randint(0, min(maxRes, maxModulo))
    c = a % b if b != 0 else 0

    problem = f'${a}$ % ${b} = $'
    solution = f'${c}$'
    return problem, solution
