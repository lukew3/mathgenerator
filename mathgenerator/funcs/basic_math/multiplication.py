import random


def multiplication(maxMulti=12):
    """Multiplication"""
    a = random.randint(0, maxMulti)
    b = random.randint(0, maxMulti)
    c = a * b

    return f'${a}\\cdot{b}$', f'${c}$'
