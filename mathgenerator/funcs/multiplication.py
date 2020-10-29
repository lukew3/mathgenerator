from .__init__ import *


def multiplicationFunc(maxMulti=99):
    a = random.randint(0, maxMulti)
    b = random.randint(0, maxMulti)

    problem = str(a) + "*" + str(b) + "="
    solution = str(c)
    return problem, solution


multiplication = Generator("Multiplication", 2, "a*b=", "c",
                           multiplicationFunc)
