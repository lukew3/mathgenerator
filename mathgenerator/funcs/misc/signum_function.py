import random


def signum_function(min=-999, max=999):
    """Signum Function"""
    a = random.randint(min, max)
    b = 0
    if (a > 0):
        b = 1
    if (a < 0):
        b = -1

    problem = f"signum of {a} is ="
    solution = f'${b}$'
    return problem, solution
