from .__init__ import *


def hcfFunc(maxVal=20):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    while (y):
        x, y = y, x % y
    problem = f"HCF of {a} and {b} = "
    solution = str(x)
    return problem, solution


hcf = Generator("HCF (Highest Common Factor)", 51, "HCF of a and b = ", "c",
                hcfFunc)
