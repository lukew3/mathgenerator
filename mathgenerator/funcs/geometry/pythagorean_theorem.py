from ...generator import Generator
import random


def gen_func(maxLength=20):
    a = random.randint(1, maxLength)
    b = random.randint(1, maxLength)
    c = round((a ** 2 + b ** 2) ** 0.5, 2)

    problem = f"What is the hypotenuse of a right triangle given the other two sides have lengths ${a}$ and ${b}$?"
    solution = f"${c}$"
    return problem, solution


pythagorean_theorem = Generator("Pythagorean Theorem", 25,
                                gen_func, ["maxLength=20"])
