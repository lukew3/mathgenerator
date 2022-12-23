import random


def fraction_to_decimal(maxRes=99, maxDivid=99):
    """Fraction to Decimal"""
    a = random.randint(0, maxDivid)
    b = random.randint(1, min(maxRes, maxDivid))
    c = round(a / b, 2)

    return f'${a}\\div{b}=$', f'${c}$'
