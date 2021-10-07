from .__init__ import *


def gen_func(maxA=25, maxB=25, format='string'):
    a = random.randint(1, maxA)
    b = random.randint(1, maxB)

    divisor = a * b
    dividend = random.choice([a, b])
    quotient = int(divisor / dividend)

    if format == 'string':
        return f"{divisor}/{dividend}=", str(quotient)
    elif format == 'latex':
        return ("\\(" + str(divisor) + "\\div" + str(dividend) + "=\\)",
                "\\(" + str(quotient) + "\\)")
    else:
        return divisor, dividend, quotient


division = Generator("Division", 3, gen_func, ["maxA=25", "maxB=25"])
