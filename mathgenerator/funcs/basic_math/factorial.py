from .__init__ import *


def factorialFunc(maxInput=6, format='string'):
    a = random.randint(0, maxInput)
    n = a
    b = 1
    while a != 1 and n > 0:
        b *= n
        n -= 1

    if format == 'string':
        return str(a) + "! = ", str(b)
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b


factorial = Generator("Factorial", 31, factorialFunc, ["maxInput=6"])
