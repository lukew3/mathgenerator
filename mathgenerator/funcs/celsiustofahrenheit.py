from  .__init__ import *
from ..__init__ import Generator

def celsiustofahrenheit(maxTemp=100):
    celsius = random.randint(-50, maxTemp)
    fahrenheit = (celsius * (9/5)) +32
    problem = "Convert", str(celsius), "deg Celsius to degrees Fahrenheit ="
    solution = str(fahrenheit)
    return problem, solution

celsiustofahrenheit = Generator("Celsius To Fahrenheit", 81, "(C +(9/5))+32=", "F", celsiustofahrenheit)
