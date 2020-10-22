from .__init__ import *


def powerOfPowersFunc(maxBase=50, maxPower=10):
    base = random.randint(1, maxBase)
    power1 = random.randint(1, maxPower)
    power2 = random.randint(1, maxPower)
    step = power1 * power2

    problem = "The {base}^{power1}^{power2} = " \
              "{base}^({power1}*{power2}) = {base}^{step}".format(base=base,
                                                                  power1=power1,
                                                                  power2=power2,
                                                                  step=step)
    solution = str(base**step)
    return problem, solution


power_of_powers = Generator("Power of Powers", 97, "6^4^2 = 6^(4*2) = 6^6",
                            "46656", powerOfPowersFunc)
