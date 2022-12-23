from ...generator import Generator
import random


def gen_func(maxMulti=12):
    a = random.randint(0, maxMulti)
    b = random.randint(0, maxMulti)
    c = a * b

    return f'${a}\\cdot{b}$', f'${c}$'


multiplication = Generator("Multiplication", 2, gen_func,
                           ["maxMulti=12"])
