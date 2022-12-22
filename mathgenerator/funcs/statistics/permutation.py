from ...generator import Generator
import random
import math


def gen_func(maxlength=20):
    a = random.randint(10, maxlength)
    b = random.randint(0, 9)
    solution = int(math.factorial(a) / (math.factorial(a - b)))

    problem = f"Number of Permutations from ${a}$ objects picked ${b}$ at a time is: "
    return problem, f"${solution}$"


permutation = Generator("Permutations", 42, gen_func, ["maxlength=20"])
