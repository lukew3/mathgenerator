from .__init__ import *


def complexQuadraticFunc(prob_type=0, max_range=10):
    if prob_type < 0 or prob_type > 1:
        print("prob_type not supported")
        print("prob_type = 0 for real roots problems ")
        print("prob_tpye = 1 for imaginary roots problems")
        return None
    if prob_type == 0:
        d = -1
        while d < 0:
            a = random.randrange(1, max_range)
            b = random.randrange(1, max_range)
            c = random.randrange(1, max_range)

            d = (b**2 - 4 * a * c)
    else:
        d = 0
        while d >= 0:
            a = random.randrange(1, max_range)
            b = random.randrange(1, max_range)
            c = random.randrange(1, max_range)

            d = (b**2 - 4 * a * c)

    eq = ''

    if a == 1:
        eq += 'x^2 + '
    else:
        eq += str(a) + 'x^2 + '

    if b == 1:
        eq += 'x + '
    else:
        eq += str(b) + 'x + '

    eq += str(c) + ' = 0'

    problem = 'Find the roots of given Quadratic Equation ' + eq

    if d < 0:
        sqrt_d = (-d)**0.5

        if sqrt_d - int(sqrt_d) == 0:
            sqrt_d = int(sqrt_d)
            solution = f'(({-b} + {sqrt_d}i)/2*{a}, ({-b} - {sqrt_d}i)/2*{a})'
        else:
            solution = f'(({-b} + sqrt({-d})i)/2*{a}, ({-b} - sqrt({-d})i)/2*{a})'

        return problem, solution

    else:
        s_root1 = round((-b + (d)**0.5) / (2 * a), 3)
        s_root2 = round((-b - (d)**0.5) / (2 * a), 3)

        sqrt_d = (d)**0.5

        if sqrt_d - int(sqrt_d) == 0:
            sqrt_d = int(sqrt_d)
            g_sol = f'(({-b} + {sqrt_d})/2*{a}, ({-b} - {sqrt_d})/2*{a})'
        else:
            g_sol = f'(({-b} + sqrt({d}))/2*{a}, ({-b} - sqrt({d}))/2*{a})'

        solution = f'simplified solution : ({s_root1, s_root2}), generalized solution : ' + g_sol

        return problem, solution


complex_quadratic = Generator(
    "complex Quadratic Equation", 100,
    "Find the roots of given Quadratic Equation ",
    "simplified solution : (x1, x2), generalized solution : ((-b + sqrt(d))/2a, (-b - sqrt(d))/2a) or ((-b + sqrt(d)i)/2a, (-b - sqrt(d)i)/2a)",
    complexQuadraticFunc)
