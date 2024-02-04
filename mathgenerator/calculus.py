import random
from scipy.integrate import quad
import sympy


def definite_integral(max_coef=100):
    r"""Definite Integral of Quadratic Equation

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | The definite integral within limits $0$ to $1$ of the equation $28x^2 + 32x + 66 = $ | $91.33$ |
    """
    def integrand(x, a, b, c):
        return a * x**2 + b * x + c

    a = random.randint(0, max_coef)
    b = random.randint(0, max_coef)
    c = random.randint(0, max_coef)

    result = quad(integrand, 0, 1, args=(a, b, c))[0]
    solution = round(result, 2)

    problem = f"The definite integral within limits $0$ to $1$ of the equation ${a}x^2 + {b}x + {c} = $"
    return problem, f'{solution}'


def power_rule_differentiation(max_coef=10, max_exp=10, max_terms=5, max_x = 20):
    r"""Power Rule Differentiation

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Differentiate $1x^{5} + 4x^{7} + 4x^{4}$ | $5x^{4} + 28x^{6} + 16x^{3}$ |
    """
    numTerms = random.randint(1, max_terms)
    problem = "Find the derivative of  $"
    solution = ""

    for i in range(numTerms):
        if i > 0:
            problem += " + "
            solution += " + "
        coefficient = random.randint(1, max_coef)
        exponent = random.randint(1, max_exp)

        problem += f'{coefficient}x^{{{exponent}}}'
        solution += f'{coefficient * exponent}x^{{{exponent - 1}}}'
        x = random.randint(1, max_x)
        solution = solution.replace('^', '**').replace('x', '*' + str(x)).replace('{', '').replace('}', '')
        solution = str(eval(solution))

    return problem + f'$ at x = {x}', solution


def power_rule_integration(max_coef=10, max_exp=10, max_terms=5):
    r"""Power Rule Integration

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Integrate $9x^{6} + 2x^{6} + 4x^{3}$ | $\frac{9}{6}x^{7} + \frac{2}{6}x^{7} + \frac{4}{3}x^{4} + C$ |
    """
    numTerms = random.randint(1, max_terms)
    problem = "Integrate $"
    solution = "$"

    for i in range(numTerms):
        if i > 0:
            problem += " + "
            solution += " + "
        coefficient = random.randint(1, max_coef)
        exponent = random.randint(1, max_exp)

        problem += f'{coefficient}x^{{{exponent}}}'
        solution += rf'\frac{{{coefficient}}}{{{exponent}}}x^{{{exponent + 1}}}'

    solution += " + C"

    return problem + '$', solution + '$'


def stationary_points(max_exp=3, max_coef=10):
    r"""Stationary Points

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $f(x)=6x^3 + 6x^2 + x + 8$ | ${- \frac{1}{3} - \frac{\sqrt{2}}{6}, - \frac{1}{3} + \frac{\sqrt{2}}{6}}$ |
    """
    solution = ''
    while len(solution) == 0:
        x = sympy.symbols('x')
        problem = 0
        for exp in range(max_exp + 1):
            coefficient = random.randint(0, max_coef)
            problem += coefficient * pow(x, exp)
        solution = sympy.stationary_points(problem, x)

    problem = 'f(x)=' + str(problem).replace('**', '^').replace('*', '')
    return f'${problem}$', f'${sympy.latex(solution)[6:-8]}}}$'


def trig_differentiation():
    r"""Trigonometric Differentiation

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $\frac{d}{dx}(\csc)=$ | $-\csc \cdot \cot$ |
    """
    pairs = {
        r'\sin': r'\cos',
        r'\cos': r'-\sin',
        r'\tan': r'\sec^{{2}}',
        r'\cot': r'-\csc^{{2}}',
        r'\sec': r'\sec \cdot \tan',
        r'\csc': r'-\csc \cdot \cot'
    }
    problem = random.choice(list(pairs.keys()))
    solution = f'${pairs[problem]}$'
    problem = rf'$\frac{{d}}{{dx}}({problem})=$'

    return problem, solution
