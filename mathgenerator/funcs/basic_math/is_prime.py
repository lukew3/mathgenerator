from ...generator import Generator
import random


def gen_func(max_num=100):
    a = random.randint(2, max_num)
    problem = f"Is ${a}$ prime?"
    if a == 2:
        return problem, "Yes"
    if a % 2 == 0:
        return problem, "No"
    for i in range(3, a // 2 + 1, 2):
        if a % i == 0:
            return problem, "No"
    solution = "Yes"

    return problem, solution


is_prime = Generator('isprime', 90, gen_func, ["max_num=100"])
