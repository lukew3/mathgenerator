from .__init__ import *


def DecimalToBCDFunc(maxNumber=10000):
    n = random.randint(1000, maxNumber)
    x = n
    # binstring = ''
    bcdstring = ''
    while x > 0:
        nibble = x % 16
        bcdstring = str(nibble) + bcdstring
        x >>= 4

    problem = "BCD of Decimal Number " + str(n) + " is = "
    solution = int(bcdstring)
    return problem, solution


decimal_to_bcd = Generator("Decimal to Binary Coded Decimal", 103,
                           "Binary Coded Decimal of Decimal n is ", "b",
                           DecimalToBCDFunc)
