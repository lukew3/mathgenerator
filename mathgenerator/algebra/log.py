import random


def log(maxBase=3, maxVal=8):
    """Logarithm"""
    a = random.randint(1, maxVal)
    b = random.randint(2, maxBase)
    c = pow(b, a)

    problem = f'$log_{{{b}}}({c})=$'
    solution = f'${a}$'
    return problem, solution
