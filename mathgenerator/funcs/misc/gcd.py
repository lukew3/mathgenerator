from .__init__ import *


def gcdFunc(maxVal=20, format='string'):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    while y:
        x, y = y, x % y

    if format == 'string':
        problem = f"GCD of {a} and {b} = "
        solution = str(x)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, x


gcd = Generator("GCD (Greatest Common Denominator)", 10, gcdFunc,
                ["maxVal=20"])
