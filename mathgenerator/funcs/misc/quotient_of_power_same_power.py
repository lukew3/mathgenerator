from ...generator import Generator
import random


def gen_func(maxBase=50, maxPower=10):
    base1 = random.randint(1, maxBase)
    base2 = random.randint(1, maxBase)
    power = random.randint(1, maxPower)
    step = base1 / base2
    solution = step ** power

    problem = f"The Quotient of ${base1}^{{{power}}}$ and ${base2}^{{{power}}} = " \
        f"({base1}/{base2})^{power} = {step}^{{{power}}}$"
    return problem, f'${solution}$'


quotient_of_power_same_power = Generator("Quotient of Powers with Same Power",
                                         99, gen_func,
                                         ["maxBase=50", "maxPower=10"])
