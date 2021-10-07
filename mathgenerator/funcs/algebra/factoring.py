from .__init__ import *


def gen_func(range_x1=10, range_x2=10, format='string'):
    x1 = random.randint(-range_x1, range_x1)
    x2 = random.randint(-range_x2, range_x2)

    def intParser(z):
        if (z == 0):
            return ""
        if (z > 0):
            return "+" + str(z)
        if (z < 0):
            return "-" + str(abs(z))

    b = intParser(x1 + x2)
    c = intParser(x1 * x2)

    if b == "+1":
        b = "+"
    if b == "":
        problem = f"x^2{c}"
    else:
        problem = f"x^2{b}x{c}"

    if format == 'string':
        x1 = intParser(x1)
        x2 = intParser(x2)
        solution = f"(x{x1})(x{x2})"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return b, c, x1, x2


factoring = Generator("Factoring Quadratic", 21, gen_func,
                      ["range_x1=10", "range_x2=10"])
