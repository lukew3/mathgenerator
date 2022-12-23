from ...generator import Generator
import random
import math


def gen_func(maxlength=20):
    a = random.randint(10, maxlength)
    b = random.randint(0, 9)

    solution = int(math.factorial(a) / (math.factorial(b) * math.factorial(a - b)))

    problem = f"Find the number of combinations from ${a}$ objects picked ${b}$ at a time."
    return problem, f'${solution}$'


combinations = Generator("Combinations of Objects", 30, gen_func,
                         ["maxlength=20"])
