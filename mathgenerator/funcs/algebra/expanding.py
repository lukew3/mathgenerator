from ...generator import Generator
import random


def gen_func(range_x1=10,
             range_x2=10,
             range_a=10,
             range_b=10):
    x1 = random.randint(-range_x1, range_x1)
    x2 = random.randint(-range_x2, range_x2)
    a = random.randint(-range_a, range_a)
    b = random.randint(-range_b, range_b)

    def intParser(z):
        if (z > 0):
            return f"+{z}"
        elif (z < 0):
            return f"-{abs(z)}"
        else:
            return ""

    c1 = intParser(a * b)
    c2 = intParser((a * x2) + (b * x1))
    c3 = intParser(x1 * x2)

    p1 = intParser(a)
    p2 = intParser(x1)
    p3 = intParser(b)
    p4 = intParser(x2)

    if p1 == "+1":
        p1 = ""
    elif len(p1) > 0 and p1[0] == "+":
        p1 = p1[1:]
    if p3 == "+1":
        p3 = ""
    elif p3[0] == "+":
        p3 = p3[1:]

    if c1 == "+1":
        c1 = ""
    elif len(c1) > 0 and c1[0] == "+":
        c1 = c1[1:]  # Cuts off the plus for readability
    if c2 == "+1":
        c2 = ""

    problem = f"$({p1}x{p2})({p3}x{p4})$"
    solution = f"${c1}x^2{c2}x{c3}$"
    return problem, solution


expanding = Generator(
    "Expanding Factored Binomial", 111, gen_func,
    ["range_x1=10", "range_x2=10", "range_a=10", "range_b=10"])
