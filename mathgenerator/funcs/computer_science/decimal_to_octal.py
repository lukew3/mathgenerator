import random


def decimal_to_octal(maxDecimal=4096):
    """Decimal to Octal"""
    x = random.randint(0, maxDecimal)

    problem = "The decimal number ${x}$ in Octal is: "
    solution = f'${oct(x)}$'

    return problem, solution
