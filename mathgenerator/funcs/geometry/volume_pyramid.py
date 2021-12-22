from .__init__ import *


def gen_func(maxLength=20, maxWidth=20, maxHeight=50, unit='m', format='string'):
    l = random.randint(1, maxLength)
    w = random.randint(1, maxWidth)
    h = random.randint(1, maxHeight)

    ans = (l*w*h)/3

    if format == 'string':
        problem = f"Volume of cone with base length = {l} {unit}, base width = {w} {unit} and height = {h} {unit} is"
        solution = f"{ans} {unit}^3"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return l, w, h, ans, unit


volume_pyramid = Generator("Volume of pyramid", 122, gen_func,
                           ["maxLength=20", "maxWidth=20", "maxHeight=50", "unit='m'"])
