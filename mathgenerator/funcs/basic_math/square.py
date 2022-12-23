from ...generator import Generator
import random


def gen_func(maxSquareNum=20):
    a = random.randint(1, maxSquareNum)
    b = a ** 2

    return f'${a}^2=$', f'${b}$'


square = Generator("Square", 8, gen_func, ["maxSquareNum=20"])
