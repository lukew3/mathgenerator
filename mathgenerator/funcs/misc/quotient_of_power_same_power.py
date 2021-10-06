from .__init__ import *


def quotientOfPowerSamePowerFunc(maxBase=50, maxPower=10, format='string'):
    base1 = random.randint(1, maxBase)
    base2 = random.randint(1, maxBase)
    power = random.randint(1, maxPower)
    step = base1 / base2
    solution = step**power

    if format == 'string':
        problem = f"The Quotient of {base1}^{power} and {base2}^{power} = " \
            f"({base1}/{base2})^{power} = {step}^{power}"
        return problem, str(solution)
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return base1, base2, power, step, solution


quotient_of_power_same_power = Generator("Quotient of Powers with Same Power",
                                         99, quotientOfPowerSamePowerFunc,
                                         ["maxBase=50", "maxPower=10"])
