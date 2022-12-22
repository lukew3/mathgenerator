from ...generator import Generator
import random


def gen_func(maxLength=20, maxWidth=20, maxHeight=50, unit='m'):
    length = random.randint(1, maxLength)
    width = random.randint(1, maxWidth)
    height = random.randint(1, maxHeight)

    ans = (length * width * height) / 3

    problem = f"Volume of pyramid with base length $= {length} {unit}$, base width $= {width} {unit}$ and height $= {height} {unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


volume_pyramid = Generator("Volume of pyramid", 122, gen_func,
                           ["maxLength=20", "maxWidth=20", "maxHeight=50", "unit='m'"])
