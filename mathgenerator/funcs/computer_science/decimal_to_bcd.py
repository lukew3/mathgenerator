from .__init__ import *


def gen_func(maxNumber=10000, format='string'):
    n = random.randint(1000, maxNumber)
    x = n
    # binstring = ''
    bcdstring = ''
    while x > 0:
        nibble = x % 16
        bcdstring = str(nibble) + bcdstring
        x >>= 4

    if format == 'string':
        problem = "BCD of Decimal Number " + str(n) + " is = "
        solution = bcdstring
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return n, int(bcdstring)


decimal_to_bcd = Generator("Decimal to Binary Coded Decimal", 103,
                           gen_func, ["maxNumber=10000"])
