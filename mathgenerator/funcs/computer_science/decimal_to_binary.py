import random


def decimal_to_binary(max_dec=99):
    """Decimal to Binary"""
    a = random.randint(1, max_dec)
    b = bin(a).replace("0b", "")

    problem = f'Binary of ${a} = $'
    solution = f'${b}$'
    return problem, solution
