import random


def factorial(maxInput=6):
    """Factorial"""
    a = random.randint(0, maxInput)
    n = a
    b = 1
    while a != 1 and n > 0:
        b *= n
        n -= 1

    return f'${a}! =$', f'${b}$'
