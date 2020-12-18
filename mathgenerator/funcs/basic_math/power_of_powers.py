from .__init__ import *


def powerOfPowersFunc(maxBase=50, maxPower=10, style='raw'):
    base = random.randint(1, maxBase)
    power1 = random.randint(1, maxPower)
    power2 = random.randint(1, maxPower)
    step = power1 * power2

    if style == 'latex':
        problem = "Simplify \\(" + str(base) + "^{" + str(power1) + "^{" + str(power2) + "}}\\)"
        solution = f"\\({base}^{{{step}}}\\)"
    else:
        problem = f"Simplify {base}^{power1}^{power2}="
        solution = str(base) + '^' + str(step)
    return problem, solution


power_of_powers = Generator("Power of Powers", 97, "6^4^2",
                            "6^8", powerOfPowersFunc)
