from ...generator import Generator
import random


def gen_func(maxNumber=10000):
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


bcd_to_decimal = Generator("Binary Coded Decimal to Integer", 91,
                           gen_func, ["maxNumber=10000"])
