from ...generator import Generator
import random


def gen_func():
    pairs = {
        '\\sin': '\\cos',
        '\\cos': '-\\sin',
        '\\tan': '\\sec^{{2}}',
        '\\cot': '-\\csc^{{2}}',
        '\\sec': '\\sec \\cdot \\tan',
        '\\csc': '-\\csc \\cdot \\cot'
    }
    problem = random.choice(list(pairs.keys()))
    solution = f'${pairs[problem]}$'
    problem = f'$\\frac{{d}}{{dx}}({problem})=$'

    return problem, solution


trig_differentiation = Generator("Trigonometric Differentiation", 88, gen_func,
                                 [])
