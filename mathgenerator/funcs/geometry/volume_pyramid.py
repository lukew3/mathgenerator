from ...__init__ import Generator
import random


def gen_func(maxLength=20, maxWidth=20, maxHeight=50, unit='m', format='string'):
    length = random.randint(1, maxLength)
    width = random.randint(1, maxWidth)
    height = random.randint(1, maxHeight)

    ans = (length * width * height) / 3

    if format == 'string':
        problem = f"Volume of pyramid with base length = {length} {unit}, base width = {width} {unit} and height = {height} {unit} is"
        solution = f"{ans} {unit}^3"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return length, width, height, ans, unit


volume_pyramid = Generator("Volume of pyramid", 122, gen_func,
                           ["maxLength=20", "maxWidth=20", "maxHeight=50", "unit='m'"])
