from .__init__ import *


def decimalToOctalFunc(maxDecimal=4096):
    x = random.randint(0, maxDecimal)
    problem = "The decimal number " + str(x) + " in Octal is: "
    solution = oct(x)
    return problem, solution


decimalToOctal = Generator("Converts decimal to octal", 82, "What's the octal representation of 98?", "0o142", decimalToOctalFunc)
