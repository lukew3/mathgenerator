from .__init__ import *


def pythagoreanTheoremFunc(maxLength=20):
    a = random.randint(1, maxLength)
    b = random.randint(1, maxLength)
    c = (a**2 + b**2)**0.5

    problem = f"The hypotenuse of a right triangle given the other two lengths {a} and {b} = "
    solution = f"{c:.0f}" if c.is_integer() else f"{c:.2f}"
    return problem, solution


pythagorean_theorem = Generator(
    "Pythagorean Theorem", 25,
    "The hypotenuse of a right triangle given the other two lengths a and b = ",
    "hypotenuse", pythagoreanTheoremFunc)
