from ...generator import Generator
import random


def gen_func(maxA=25, maxB=25):
    a = random.randint(1, maxA)
    b = random.randint(1, maxB)

    divisor = a * b
    dividend = random.choice([a, b])
    quotient = int(divisor / dividend)

    return f'${divisor}\\div{dividend}=$', f'${quotient}$'


division = Generator("Division", 3, gen_func, ["maxA=25", "maxB=25"])
