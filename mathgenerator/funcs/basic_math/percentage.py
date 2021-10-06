from .__init__ import *


def percentageFunc(maxValue=99, maxpercentage=99, format='string'):
    a = random.randint(1, maxpercentage)
    b = random.randint(1, maxValue)
    problem = f"What is {a}% of {b}?"
    percentage = a / 100 * b
    formatted_float = "{:.2f}".format(percentage)
    solution = f"{formatted_float}"

    if format == 'string':
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, formatted_float


percentage = Generator("Percentage of a number", 80, percentageFunc,
                       ["maxValue=99", "maxpercentage=99"])
