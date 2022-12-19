from ...__init__ import Generator
import random


def gen_func(maxValue=100, minValue=-100, format='string'):
    observed_value = random.randint(minValue, maxValue)
    exact_value = random.randint(minValue, maxValue)

    if observed_value * exact_value < 0:
        observed_value *= -1

    error = (abs(observed_value - exact_value) / abs(exact_value)) * 100
    error = round(error, 2)

    if format == 'string':
        problem = f"Find the percentage error when observed value equals {observed_value} and exact value equals {exact_value}."
        solution = str(error) + "%"
        return problem, solution

    elif format == 'latex':
        return 'Latex unavailable'

    else:
        return observed_value, exact_value, error


percentage_error = Generator(
    "Percentage error", 119, gen_func,
    ["maxValue=100", "minValue=-100"])
