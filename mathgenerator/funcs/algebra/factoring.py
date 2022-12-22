from ...generator import Generator
import random


def gen_func(range_x1=10, range_x2=10):
    """Given a quadratic equation in the form x^2 + bx + c, factor it into it's roots (x - x1)(x -x2)"""
    x1 = random.randint(-range_x1, range_x1)
    x2 = random.randint(-range_x2, range_x2)

    def intParser(z):
        if (z > 0):
            return f"+{z}"
        elif (z < 0):
            return f"-{abs(z)}"
        else:
            return ""

    b = intParser(x1 + x2)
    c = intParser(x1 * x2)

    if b == "+1":
        b = "+"
    if b == "":
        problem = f"x^2{c}"
    else:
        problem = f"x^2{b}x{c}"

    x1 = intParser(x1)
    x2 = intParser(x2)
    solution = f"$(x{x1})(x{x2})$"
    return f"${problem}$", solution


factoring = Generator("Factoring Quadratic", 21, gen_func,
                      ["range_x1=10", "range_x2=10"])
