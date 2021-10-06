from .__init__ import *


def DecimalToBinaryFunc(max_dec=99, format='string'):
    a = random.randint(1, max_dec)
    b = bin(a).replace("0b", "")

    if format == 'string':
        problem = "Binary of " + str(a) + "="
        solution = str(b)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, str(b)


decimal_to_binary = Generator("Decimal to Binary", 14, DecimalToBinaryFunc,
                              ["max_dec=99"])
