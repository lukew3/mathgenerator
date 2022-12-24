import random
from scipy.integrate import quad
import sympy


def definite_integral(max_coeff=100):
    """Definite Integral of Quadratic Equation"""
    def integrand(x, a, b, c):
        return a * x**2 + b * x + c

    a = random.randint(0, max_coeff)
    b = random.randint(0, max_coeff)
    c = random.randint(0, max_coeff)

    result = quad(integrand, 0, 1, args=(a, b, c))[0]
    S = round(result, 4)

    problem = f"The definite integral within limits $0$ to $1$ of the equation ${a}x^2 + {b}x + {c} = $"
    solution = f'${S}$'
    return problem, solution


def power_rule_differentiation(maxCoef=10,
                               maxExp=10,
                               maxTerms=5):
    """Power Rule Differentiation"""
    numTerms = random.randint(1, maxTerms)
    problem = "$"
    solution = "$"

    for i in range(numTerms):
        if i > 0:
            problem += " + "
            solution += " + "
        coefficient = random.randint(1, maxCoef)
        exponent = random.randint(1, maxExp)

        problem += f'{coefficient}x^{{{exponent}}}'
        solution += f'{coefficient * exponent}x^{{{exponent - 1}}}'

    return problem + '$', solution + '$'


def power_rule_integration(maxCoef=10,
                           maxExp=10,
                           maxTerms=5):
    """Power Rule Integration"""
    numTerms = random.randint(1, maxTerms)
    problem = "$"
    solution = "$"

    for i in range(numTerms):
        if i > 0:
            problem += " + "
            solution += " + "
        coefficient = random.randint(1, maxCoef)
        exponent = random.randint(1, maxExp)

        problem += f'{coefficient}x^{{{exponent}}}'
        solution += f'\\frac{{{coefficient}}}{{{exponent}}}x^{{{exponent + 1}}}'

    solution += " + C"

    return problem + '$', solution + '$'


def stationary_points(maxExp=3, maxCoef=10):
    """Stationary Points"""
    solution = ''
    while len(solution) == 0:
        x = sympy.symbols('x')
        problem = 0
        for exp in range(maxExp + 1):
            coefficient = random.randint(0, maxCoef)
            problem += coefficient * pow(x, exp)
        solution = sympy.stationary_points(problem, x)

    problem = 'f(x)=' + str(problem).replace('**', '^')
    return f'${problem}$', f'${sympy.latex(solution)[6:-8]}}}$'


def trig_differentiation():
    """Trigonometric Differentiation"""
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
