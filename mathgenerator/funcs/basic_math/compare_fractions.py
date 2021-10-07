from .__init__ import *


def gen_func(maxVal=10, format='string'):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    c = random.randint(1, maxVal)
    d = random.randint(1, maxVal)

    while (a == b):
        b = random.randint(1, maxVal)
    while (c == d):
        d = random.randint(1, maxVal)

    first = a / b
    second = c / d

    if (first > second):
        solution = ">"
    elif (first < second):
        solution = "<"
    else:
        solution = "="

    if format == "string":
        return (
            f"Which symbol represents the comparison between {a}/{b} and {c}/{d}?",
            solution)
    elif format == 'latex':
        return (
            f"Which symbol represents the comparison between \\(\\frac{{{a}}}{{{b}}}\\) and \\(\\frac{{{c}}}{{{d}}}\\)?",
            solution)
    else:
        return a, b, c, d, solution


compare_fractions = Generator("Compare Fractions", 44, gen_func,
                              ["maxVal=10"])
