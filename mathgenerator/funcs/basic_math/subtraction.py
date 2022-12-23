import random


def subtraction(maxMinuend=99, maxDiff=99):
    """Subtraction of two numbers"""
    a = random.randint(0, maxMinuend)
    b = random.randint(max(0, (a - maxDiff)), a)
    c = a - b

    return f'${a}-{b}=$', f'${c}$'
