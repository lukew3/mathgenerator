import random


def celsius_to_fahrenheit(maxTemp=100):
    """Celsius to Fahrenheit"""
    celsius = random.randint(-50, maxTemp)
    fahrenheit = (celsius * (9 / 5)) + 32

    problem = f"Convert ${celsius}$ degrees Celsius to degrees Fahrenheit"
    solution = f'${fahrenheit}$'
    return problem, solution
