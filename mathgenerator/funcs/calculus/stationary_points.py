from .__init__ import *
import sympy


def stationaryPointsFunc(maxExp=3, maxCoef=10, format='string'):
    while True:
        x = sympy.symbols('x')
        problem = 0
        for exp in range(maxExp + 1):
            coefficient = random.randint(0, maxCoef)
            problem += coefficient * pow(x, exp)
        solution = sympy.stationary_points(problem, x)

        # if len(solution) != 0:
        solution = ','.join(
            '({},{})'.format(str(p), sympy.sympify(problem.replace(x, p)))
            for p in solution)
        problem = 'f(x)=' + str(problem).replace('**', '^')
        if format == 'string':
            return problem, solution
        elif format == 'latex':
            return "Latex unavailable"
        else:
            return problem, solution


stationary_points = Generator("Stationary Points", 110, stationaryPointsFunc,
                              ["maxExp=3", "maxCoef=10"])
