import random
import sympy


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
