from ...generator import Generator
import random


def gen_func(maxVal=20):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    while y:
        x, y = y, x % y

    problem = f"GCD of ${a}$ and ${b} = $"
    solution = f'${x}$'
    return problem, solution


gcd = Generator("GCD (Greatest Common Denominator)", 10, gen_func,
                ["maxVal=20"])
