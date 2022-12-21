from ...generator import Generator
import random


def gen_func(maxBase=20, maxExpo=10):
    base = random.randint(1, maxBase)
    expo = random.randint(1, maxExpo)

    return f'${base}^{expo} =$', f'${base**expo}$'


exponentiation = Generator("Exponentiation", 53, gen_func,
                           ["maxBase=20", "maxExpo=10"])
