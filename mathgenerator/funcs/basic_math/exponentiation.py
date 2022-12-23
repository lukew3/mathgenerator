import random


def exponentiation(maxBase=20, maxExpo=10):
    """Exponentiation"""
    base = random.randint(1, maxBase)
    expo = random.randint(1, maxExpo)

    return f'${base}^{expo} =$', f'${base**expo}$'
