from .__init__ import *


def powerOfPowersFunc(maxBase=50, maxPower=10):
    base = random.randint(1, maxBase)
    power1 = random.randint(1, maxPower)
    power2 = random.randint(1, maxPower)
    step = power1 * power2

    problem = "The {base}^{power1}^{power2} = ".format(base=base,
                                                       power1=power1,
                                                       power2=power2)
    solution = str(base) + '^' + str(step)
    return problem, solution


power_of_powers = Generator("Power of Powers", 97, "6^4^2",
                            "6^8", powerOfPowersFunc)
