from .__init__ import *


def pythagoreanTheoremFunc(maxLength=20, format='string'):
    a = random.randint(1, maxLength)
    b = random.randint(1, maxLength)
    c = (a**2 + b**2)**0.5

    if format == 'string':
        problem = f"The hypotenuse of a right triangle given the other two lengths {a} and {b} = "
        solution = f"{c:.0f}" if c.is_integer() else f"{c:.2f}"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, round(c, 2)


pythagorean_theorem = Generator("Pythagorean Theorem", 25,
                                pythagoreanTheoremFunc, ["maxLength=20"])
