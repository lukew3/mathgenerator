import random


def absolute_difference(maxA=100, maxB=100):
    """Absolute difference between two numbers"""
    a = random.randint(-1 * maxA, maxA)
    b = random.randint(-1 * maxB, maxB)
    absDiff = abs(a - b)

    return f'$|{a}-{b}|=$', f"${absDiff}$"
