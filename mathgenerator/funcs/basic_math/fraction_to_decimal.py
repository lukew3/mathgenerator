from ...__init__ import Generator
import random


def gen_func(maxRes=99, maxDivid=99, format='string'):
    a = random.randint(0, maxDivid)
    b = random.randint(1, min(maxRes, maxDivid))
    c = round(a / b, 2)

    if format == "string":
        return (str(a) + "/" + str(b) + "=", str(c))
    elif format == 'latex':
        return ("\\(" + str(a) + "\\div" + str(b) + "=\\)",
                "\\(" + str(c) + "\\)")
    else:
        return a, b, c


fraction_to_decimal = Generator("Fraction to Decimal", 13, gen_func,
                                ["maxRes=99", "maxDivid=99"])
