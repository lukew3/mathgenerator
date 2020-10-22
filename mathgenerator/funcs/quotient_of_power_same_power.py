from .__init__ import *


def quotientOfPowerSamePowerFunc(maxBase=50, maxPower=10):
    base1 = random.randint(1, maxBase)
    base2 = random.randint(1, maxBase)
    power = random.randint(1, maxPower)
    step = base1 / base2

    problem = "The Quotient of {base1}^{power} and {base2}^{power} = " \
              "({base1}/{base2})^{power} = {step}^{power}".format(base1=base1,
                                                                  base2=base2,
                                                                  power=power,
                                                                  step=step)
    solution = str(step**power)
    return problem, solution


quotient_of_power_same_power = Generator("Quotient of Powers with Same Power",
                                         99, "6^4 / 3^4 = (6/3)^4 = 2^4", "16",
                                         quotientOfPowerSamePowerFunc)
