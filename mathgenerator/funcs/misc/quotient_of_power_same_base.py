from .__init__ import *


def gen_func(maxBase=50, maxPower=10, format='string'):
    base = random.randint(1, maxBase)
    power1 = random.randint(1, maxPower)
    power2 = random.randint(1, maxPower)
    step = power1 - power2
    solution = base**step

    if format == 'string':
        problem = f"The Quotient of {base}^{power1} and {base}^{power2} = " \
            f"{base}^({power1}-{power2}) = {base}^{step}"
        return problem, str(solution)
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return base, power1, power2, step, solution


quotient_of_power_same_base = Generator("Quotient of Powers with Same Base",
                                        98, gen_func,
                                        ["maxBase=50", "maxPower=10"])
