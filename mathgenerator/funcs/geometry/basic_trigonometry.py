from .__init__ import *

import math


# Handles degrees in quadrant one
def basicTrigonometryFunc(angles=[0, 30, 45, 60, 90],
                          functions=["sin", "cos", "tan"]):
    angle = random.choice(angles)
    function = random.choice(functions)

    problem = f"What is {function}({angle})?"

    expression = 'math.' + function + '(math.radians(angle))'
    result_fraction_map = {
        0.0: "0",
        0.5: "1/2",
        0.71: "1/√2",
        0.87: "√3/2",
        1.0: "1",
        0.58: "1/√3",
        1.73: "√3"
    }

    solution = result_fraction_map[round(eval(expression), 2)] if round(
        eval(expression), 2) <= 99999 else "∞"  # for handling the ∞ condition
    return problem, solution


basic_trigonometry = Generator("Trigonometric Values", 57, "What is sin(X)?",
                               "ans", basicTrigonometryFunc)
