from .__init__ import *
import sympy


def stationaryPointsFunc(maxExp=3, maxCoef=10):
    while True:
        x = sympy.symbols('x')
        problem = 0
        for exp in range(maxExp + 1):
            coefficient = random.randint(0, maxCoef)
            problem += coefficient * pow(x, exp)
        solution = sympy.stationary_points(problem, x)

        if len(solution) != 0:
            solution = ','.join('({},{})'.format(
                str(p),
                sympy.sympify(problem.replace(x, p))
            ) for p in solution)
            problem = 'f(x)=' + str(problem).replace('**', '^')
            return problem, solution


stationary_points = Generator("Stationary Points", 110, "f(x)=x^3-3x",
                              "(-1,2),(1,-2)", stationaryPointsFunc)
