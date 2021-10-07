from .__init__ import *


def gen_func(max_dec=1000, format='string'):
    a = random.randint(0, max_dec)
    b = hex(a)

    if format == 'string':
        problem = "Binary of " + str(a) + "="
        solution = str(b)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, str(b)


decimal_to_hexadeci = Generator("Decimal to Hexadecimal", 79, gen_func,
                                ["max_dec=1000"])
