import random


def percentage_difference(maxValue=200, minValue=0):
    """Percentage difference between two numbers"""
    value_a = random.randint(minValue, maxValue)
    value_b = random.randint(minValue, maxValue)

    diff = 2 * (abs(value_a - value_b) / abs(value_a + value_b)) * 100
    diff = round(diff, 2)

    problem = f"What is the percentage difference between ${value_a}$ and ${value_b}$?"
    solution = f'${diff}$%'
    return problem, solution
