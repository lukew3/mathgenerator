from .__init__ import *


def powerOfPowersFunc(maxBase=50, maxPower=10, format='string'):
    base = random.randint(1, maxBase)
    power1 = random.randint(1, maxPower)
    power2 = random.randint(1, maxPower)
    step = power1 * power2

    if format == 'string':
        problem = f"Simplify {base}^{power1}^{power2}="
        solution = str(base) + '^' + str(step)
        return problem, solution
    elif format == 'latex':
        problem = "Simplify \\(" + str(base) + \
            "^{" + str(power1) + "^{" + str(power2) + "}}\\)"
        solution = f"\\({base}^{{{step}}}\\)"
        return problem, solution
    else:
        return base, power1, power2, base, step


power_of_powers = Generator("Power of Powers", 97, powerOfPowersFunc,
                            ["maxBase=50", "maxPower=10"])
