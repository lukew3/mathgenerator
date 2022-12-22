from ...generator import Generator
import random


def gen_func(maxTemp=100):
    celsius = random.randint(-50, maxTemp)
    fahrenheit = (celsius * (9 / 5)) + 32

    problem = f"Convert ${celsius}$ degrees Celsius to degrees Fahrenheit"
    solution = f'${fahrenheit}$'
    return problem, solution


celsius_to_fahrenheit = Generator("Celsius To Fahrenheit", 81,
                                  gen_func, ["maxTemp=100"])
