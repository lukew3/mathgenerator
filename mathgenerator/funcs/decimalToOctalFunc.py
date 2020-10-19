from .__init__ import *


#converts decimal into octal
def decimalToOctalFunc(maxDecimal = 4096):
    x = random.randint(0, maxDecimal)
    problem = "The decimal number " + str(x) + " in Octal is: "
    solution = oct(x)
    return problem, solution
