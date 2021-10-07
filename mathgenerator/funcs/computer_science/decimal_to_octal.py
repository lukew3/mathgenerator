from .__init__ import *


def gen_func(maxDecimal=4096, format='string'):
    x = random.randint(0, maxDecimal)
    problem = "The decimal number " + str(x) + " in Octal is: "
    solution = oct(x)

    if format == 'string':
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return x, oct(x)


decimal_to_octal = Generator("Converts decimal to octal", 84,
                             gen_func, ["maxDecimal=4096"])
