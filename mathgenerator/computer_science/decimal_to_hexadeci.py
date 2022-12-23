import random


def decimal_to_hexadeci(max_dec=1000):
    """Decimal to Hexadecimal"""
    a = random.randint(0, max_dec)
    b = hex(a)

    problem = f"Binary of ${a} = $"
    solution = f"${b}$"
    return problem, solution
