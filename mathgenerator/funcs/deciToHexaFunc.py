from .__init__ import *
from ..__init__ import Generator


def deciToHexaFunc(max_dec=1000):
    a = random.randint(0, max_dec)
    b = hex(a)
    problem = "Binary of " + str(a) + "="
    solution = str(b)

    return problem, solution


decimalToHexadeci = Generator("Decimal to Hexadecimal", 79, "Binary of a=",
                              "b", deciToHexaFunc)
