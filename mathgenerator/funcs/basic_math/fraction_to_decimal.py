from ...generator import Generator
import random


def gen_func(maxRes=99, maxDivid=99):
    a = random.randint(0, maxDivid)
    b = random.randint(1, min(maxRes, maxDivid))
    c = round(a / b, 2)

    return f'${a}\\div{b}=$', f'${c}$'


fraction_to_decimal = Generator("Fraction to Decimal", 13, gen_func,
                                ["maxRes=99", "maxDivid=99"])
