from ...generator import Generator
import random


def gen_func(maxBase=50, maxPower=10):
    base = random.randint(1, maxBase)
    power1 = random.randint(1, maxPower)
    power2 = random.randint(1, maxPower)
    step = power1 * power2

    problem = f"Simplify ${base}^{{{power1}^{{{power2}}}}}$"
    solution = f"${base}^{{{step}}}$"
    return problem, solution


power_of_powers = Generator("Power of Powers", 97, gen_func,
                            ["maxBase=50", "maxPower=10"])
