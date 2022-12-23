from ...generator import Generator
import random


def gen_func(minNo=1, maxNo=12):
    b = random.randint(minNo, maxNo)
    a = b ** 2

    return f'$\\sqrt{{{a}}}=$', f'${b}$'


square_root = Generator("Square Root", 6, gen_func,
                        ["minNo=1", "maxNo=12"])
