from ...generator import Generator
import random
from scipy.integrate import quad


def gen_func(max_coeff=100):
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


definite_integral = Generator("Definite Integral of Quadratic Equation", 89,
                              gen_func, ["max_coeff=100"])
