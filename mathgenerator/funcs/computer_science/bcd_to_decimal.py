from .__init__ import *


def BCDtoDecimalFunc(maxNumber=10000, format='string'):
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

    if format == 'string':
        problem = "Integer of Binary Coded Decimal " + str(n) + " is = "
        solution = int(binstring, 2)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return n, int(binstring, 2)


bcd_to_decimal = Generator("Binary Coded Decimal to Integer", 91,
                           BCDtoDecimalFunc, ["maxNumber=10000"])
