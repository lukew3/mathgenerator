from ...generator import Generator
import random


def gen_func(maxNumber=10000):
    n = random.randint(1000, maxNumber)
    x = n
    # binstring = ''
    bcdstring = ''
    while x > 0:
        nibble = x % 16
        bcdstring = str(nibble) + bcdstring
        x >>= 4

    problem = f"BCD of Decimal Number ${n} = $"
    return problem, f'${bcdstring}$'


decimal_to_bcd = Generator("Decimal to Binary Coded Decimal", 103,
                           gen_func, ["maxNumber=10000"])
