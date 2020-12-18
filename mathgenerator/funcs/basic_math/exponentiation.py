from .__init__ import *


def exponentiationFunc(maxBase=20, maxExpo=10, style='raw'):
    base = random.randint(1, maxBase)
    expo = random.randint(1, maxExpo)

    if style == 'latex':
        problem = f"\\({base}^{{{expo}}}\\)"
        solution = "\\(" + str(base**expo) + "\\)"
    else:
        problem = f"{base}^{expo} ="
        solution = str(base**expo)
    return problem, solution


exponentiation = Generator("Exponentiation", 53, "a^b = ", "c",
                           exponentiationFunc)
