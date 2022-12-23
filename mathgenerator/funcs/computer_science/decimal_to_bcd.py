import random


def decimal_to_bcd(maxNumber=10000):
    """Decimal to Binary Coded Decimal"""
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
