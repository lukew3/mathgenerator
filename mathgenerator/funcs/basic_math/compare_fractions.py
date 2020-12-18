from .__init__ import *


def compareFractionsFunc(maxVal=10, style='raw'):
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

    if style == 'latex':
        problem = f"Which symbol represents the comparison between \\(\\frac{{{a}}}{{{b}}}\\) and \\(\\frac{{{c}}}{{{d}}}\\)?"
    else:
        problem = f"Which symbol represents the comparison between {a}/{b} and {c}/{d}?"
    return problem, solution


compare_fractions = Generator(
    "Compare Fractions", 44,
    "Which symbol represents the comparison between a/b and c/d?", ">/</=",
    compareFractionsFunc)
