import random


def bcd_to_decimal(maxNumber=10000):
    """Binary Coded Decimal to Integer"""
    n = random.randint(1000, maxNumber)
    binstring = ''
    while True:
        q, r = divmod(n, 10)
        nibble = bin(r).replace('0b', "")
        while len(nibble) < 4:
            nibble = '0' + nibble
        binstring = nibble + binstring
        if q == 0:
            break
        else:
            n = q

    problem = f"Integer of Binary Coded Decimal ${n}$ is $=$ "
    solution = f'${int(binstring, 2)}$'
    return problem, solution
