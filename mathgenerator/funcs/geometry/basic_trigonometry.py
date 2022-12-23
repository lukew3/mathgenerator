import random
import math


# Handles degrees in quadrant one
def basic_trigonometry(angles=[0, 30, 45, 60, 90],
             functions=["sin", "cos", "tan"]):
    """Trigonometric Values"""
    angle = random.choice(angles)
    function = random.choice(functions)

    problem = f"$\\{function}({angle}) = $"

    expression = 'math.' + function + '(math.radians(angle))'
    result_fraction_map = {
        0.0: "0",
        0.5: "\\frac{1}{2}",
        0.71: "\\frac{1}{\\sqrt{2}}",
        0.87: "\\frac{\\sqrt{3}}{2}",
        1.0: "1",
        0.58: "\\frac{1}{\\sqrt{3}}",
        1.73: "\\sqrt{3}",
    }

    solution = result_fraction_map[round(eval(expression), 2)] if round(
        eval(expression), 2) <= 99999 else "\\infty"  # for handling the ∞ condition

    return problem, f'${solution}$'
