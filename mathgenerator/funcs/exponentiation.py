from .__init__ import *


def exponentiationFunc(maxBase=20, maxExpo=10):
    base = random.randint(1, maxBase)
    expo = random.randint(1, maxExpo)

    problem = f"{base}^{expo} ="
    solution = str(base**expo)
    return problem, solution


exponentiation = Generator("Exponentiation", 53, "a^b = ", "c",
                           exponentiationFunc)
