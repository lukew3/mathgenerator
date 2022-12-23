import random


def square(maxSquareNum=20):
    """Square"""
    a = random.randint(1, maxSquareNum)
    b = a ** 2

    return f'${a}^2=$', f'${b}$'
