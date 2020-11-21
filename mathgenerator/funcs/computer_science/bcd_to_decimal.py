from .__init__ import *


def BCDtoDecimalFunc(maxNumber=10000):
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

    problem = "Integer of Binary Coded Decimal " + str(n) + " is = "
    solution = int(binstring, 2)
    return problem, solution


bcd_to_decimal = Generator("Binary Coded Decimal to Integer", 91,
                           "Integer of Binary Coded Decimal b is ", "n",
                           BCDtoDecimalFunc)
