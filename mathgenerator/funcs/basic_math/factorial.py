from ...generator import Generator
import random


def gen_func(maxInput=6):
    a = random.randint(0, maxInput)
    n = a
    b = 1
    while a != 1 and n > 0:
        b *= n
        n -= 1

    return f'${a}! =$', f'${b}$'


factorial = Generator("Factorial", 31, gen_func, ["maxInput=6"])
