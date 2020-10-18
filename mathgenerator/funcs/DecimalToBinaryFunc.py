from .__init__ import *


def DecimalToBinaryFunc(max_dec=99):
    a = random.randint(1, max_dec)
    b = bin(a).replace("0b", "")

    problem = "Binary of " + str(a) + "="
    solution = str(b)
    
    return problem, solution
