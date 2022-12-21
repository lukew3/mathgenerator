from ...generator import Generator
import random


def gen_func(maxA=100, maxB=100):
    a = random.randint(-1 * maxA, maxA)
    b = random.randint(-1 * maxB, maxB)
    absDiff = abs(a - b)

    return f'$|{a}-{b}|=$', f"${absDiff}$"


absolute_difference = Generator("Absolute difference between two numbers", 71,
                                gen_func, ["maxA=100", "maxB=100"])
