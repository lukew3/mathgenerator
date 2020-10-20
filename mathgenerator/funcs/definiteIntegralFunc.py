from .__init__ import *
from ..__init__ import Generator
from scipy.integrate import quad


def definiteIntegralFunc(max_coeff=100):

    def integrand(x, a, b, c):
        return a*x**2 + b*x + c

    a = random.randint(0, max_coeff)
    b = random.randint(0, max_coeff)
    c = random.randint(0, max_coeff)

    I = quad(integrand, 0, 1, args=(a, b, c))[0]
    I = round(I, 4)

    problem = "The definite integral within limits 0 to 1 of the equation "+ str(a) +"x^2 + "+ str(b) +"x + "+ str(c) +" is = "

    solution = str(I)

    return problem, solution


definiteIntegral = Generator("Definite Integral of Quadratic Equation", 110, "The definite integral within limits 0 to 1 of quadratic equation ax^2+bx+c is = ", "I", definiteIntegralFunc)
