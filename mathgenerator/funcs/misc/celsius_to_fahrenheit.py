from .__init__ import *


def gen_func(maxTemp=100, format='string'):
    celsius = random.randint(-50, maxTemp)
    fahrenheit = (celsius * (9 / 5)) + 32

    if format == 'string':
        problem = "Convert " + str(
            celsius) + " degrees Celsius to degrees Fahrenheit ="
        solution = str(fahrenheit)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return celsius, fahrenheit


celsius_to_fahrenheit = Generator("Celsius To Fahrenheit", 81,
                                  gen_func, ["maxTemp=100"])
