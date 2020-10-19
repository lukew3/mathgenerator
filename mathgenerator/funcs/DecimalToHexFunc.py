from .__init__ import *


def DecimalToHexFunc(max_dec=99):
    a = random.randint(1, max_dec)
    b = hex(a).replace("0x", "")

    problem = "Hexadecimal of " + str(a) + "="
    solution = str(b)
    
    return problem, solution
