from ...generator import Generator
import random
import math


def gen_func(maxVal=100):
    a = random.randint(1, maxVal)
    c = random.randint(1, maxVal)
    b = random.randint(
        round(math.sqrt(4 * a * c)) + 1, round(math.sqrt(4 * maxVal * maxVal)))
    D = math.sqrt(b * b - 4 * a * c)
    res = {round((-b + D) / (2 * a), 2), round((-b - D) / (2 * a), 2)}

    problem = f"What are the zeros of the quadratic equation ${a}x^2+{b}x+{c}=0$"
    solution = f'${res}$'
    return problem, solution


quadratic_equation = Generator("Quadratic Equation", 50, gen_func,
                               ["maxVal=100"])
