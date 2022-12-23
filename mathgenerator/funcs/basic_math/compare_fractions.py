from ...generator import Generator
import random


def gen_func(maxVal=10):
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

    problem = f"Which symbol represents the comparison between $\\frac{{{a}}}{{{b}}}$ and $\\frac{{{c}}}{{{d}}}$?"
    return problem, solution


compare_fractions = Generator("Compare Fractions", 44, gen_func,
                              ["maxVal=10"])
