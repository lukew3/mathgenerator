from .__init__ import *


def DecimalToBinaryFunc(max_dec=99):
    a = random.randint(1, max_dec)
    b = bin(a).replace("0b", "")

    problem = "Binary of " + str(a) + "="
    solution = str(b)

    return problem, solution


decimal_to_binary = Generator("Decimal to Binary", 14, "Binary of a=", "b",
                              DecimalToBinaryFunc)
