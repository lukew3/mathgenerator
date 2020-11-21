from .__init__ import *


def celsiustofahrenheitFunc(maxTemp=100):
    celsius = random.randint(-50, maxTemp)
    fahrenheit = (celsius * (9 / 5)) + 32
    problem = "Convert " + str(
        celsius) + " degrees Celsius to degrees Fahrenheit ="
    solution = str(fahrenheit)
    return problem, solution


celsius_to_fahrenheit = Generator("Celsius To Fahrenheit", 81,
                                  "(C +(9/5))+32=", "F",
                                  celsiustofahrenheitFunc)
