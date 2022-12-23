from ...generator import Generator
import random
import math


def gen_func(maxN=100):
    gratio = (1 + math.sqrt(5)) / 2
    n = random.randint(1, maxN)

    problem = f"What is the {n}th Fibonacci number?"
    solution = int((math.pow(gratio, n) - math.pow(-gratio, -n)) / (math.sqrt(5)))

    return problem, f'${solution}$'


nth_fibonacci_number = Generator("nth Fibonacci number", 62,
                                 gen_func, ["maxN=100"])
