from ...generator import Generator
import random


def gen_func(maxMinuend=99, maxDiff=99):
    a = random.randint(0, maxMinuend)
    b = random.randint(max(0, (a - maxDiff)), a)
    c = a - b

    return f'${a}-{b}=$', f'${c}$'


subtraction = Generator("Subtraction", 1, gen_func,
                        ["maxMinuend=99", "maxDiff=99"])
