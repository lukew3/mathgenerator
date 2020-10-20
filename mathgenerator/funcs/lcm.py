from .__init__ import *


def lcmFunc(maxVal=20):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    c = a * b
    x, y = a, b

    while y:
        x, y = y, x % y
    d = c // x

    problem = f"LCM of {a} and {b} ="
    solution = str(d)

    return problem, solution


lcm = Generator("LCM (Least Common Multiple)", 9, "LCM of a and b = ", "c",
                lcmFunc)
