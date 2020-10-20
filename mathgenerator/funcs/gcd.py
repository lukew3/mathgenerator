from .__init__ import *


def gcdFunc(maxVal=20):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    while y:
        x, y = y, x % y
    problem = f"GCD of {a} and {b} = "
    solution = str(x)
    return problem, solution


gcd = Generator("GCD (Greatest Common Denominator)", 10, "GCD of a and b = ",
                "c", gcdFunc)
