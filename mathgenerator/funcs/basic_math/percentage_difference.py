from ...generator import Generator
import random


def gen_func(maxValue=200, minValue=0):
    value_a = random.randint(minValue, maxValue)
    value_b = random.randint(minValue, maxValue)

    diff = 2 * (abs(value_a - value_b) / abs(value_a + value_b)) * 100
    diff = round(diff, 2)

    problem = f"What is the percentage difference between ${value_a}$ and ${value_b}$?"
    solution = f'${diff}$%'
    return problem, solution


percentage_difference = Generator("Percentage difference", 118, gen_func,
                                  ["maxValue=200", "minValue=0"])
