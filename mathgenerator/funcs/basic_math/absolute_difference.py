from .__init__ import *


def gen_func(maxA=100, maxB=100, format='string'):
    a = random.randint(-1 * maxA, maxA)
    b = random.randint(-1 * maxB, maxB)
    absDiff = abs(a - b)

    if format == "string":
        return "|" + str(a) + "-" + str(b) + "|=", absDiff
    elif format == 'latex':
        return ("\\(|" + str(a) + "-" + str(b) + "|=\\)", f"\\({absDiff}\\)")
    else:
        return a, b, absDiff


absolute_difference = Generator("Absolute difference between two numbers", 71,
                                gen_func, ["maxA=100", "maxB=100"])
