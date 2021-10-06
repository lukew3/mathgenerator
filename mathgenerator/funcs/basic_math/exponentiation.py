from .__init__ import *


def exponentiationFunc(maxBase=20, maxExpo=10, format='string'):
    base = random.randint(1, maxBase)
    expo = random.randint(1, maxExpo)

    if format == 'string':
        return (f"{base}^{expo} =", str(base**expo))
    elif format == 'latex':
        return f"\\({base}^{{{expo}}}\\)", "\\(" + str(base**expo) + "\\)"
    else:
        return base, expo, base**expo


exponentiation = Generator("Exponentiation", 53, exponentiationFunc,
                           ["maxBase=20", "maxExpo=10"])
