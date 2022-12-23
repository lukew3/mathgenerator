import random


def division(maxA=25, maxB=25):
    """Division"""
    a = random.randint(1, maxA)
    b = random.randint(1, maxB)

    divisor = a * b
    dividend = random.choice([a, b])
    quotient = int(divisor / dividend)

    return f'${divisor}\\div{dividend}=$', f'${quotient}$'
