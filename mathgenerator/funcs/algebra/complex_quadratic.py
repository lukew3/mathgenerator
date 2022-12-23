from ...generator import Generator
import random


def gen_func(prob_type=0, max_range=10, format='string'):
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

    problem = f'Find the roots of given Quadratic Equation ${eq}$'

    if d < 0:
        sqrt_d = (-d)**0.5

        if sqrt_d - int(sqrt_d) == 0:
            sqrt_d = int(sqrt_d)
            solution = f'(\\frac{{{-b} + {sqrt_d}i}}{{2*{a}}}, \\frac{{{-b} - {sqrt_d}i}}{{2*{a}}})'
        else:
            solution = f'(\\frac{{{-b} + \\sqrt{{{-d}}}i}}{{2*{a}}}, \\frac{{{-b} - \\sqrt{{{-d}}}i}}{{2*{a}}})'

        return problem, solution

    else:
        s_root1 = round((-b + (d)**0.5) / (2 * a), 3)
        s_root2 = round((-b - (d)**0.5) / (2 * a), 3)

        sqrt_d = (d)**0.5

        if sqrt_d - int(sqrt_d) == 0:
            sqrt_d = int(sqrt_d)
            g_sol = f'(\\frac{{{-b} + {sqrt_d}}}{{2*{a}}}, \\frac{{{-b} - {sqrt_d}}}{{2*{a}}})'
        else:
            g_sol = f'(\\frac{{{-b} + \\sqrt{{{d}}}}}{{2*{a}}}, (\\frac{{{-b} - \\sqrt{{{d}}}}}{{2*{a}}})'

        solution = f'$({s_root1, s_root2}) = {g_sol}$'

        return problem, solution


complex_quadratic = Generator("complex Quadratic Equation", 100,
                              gen_func,
                              ["prob_type=0", "max_range=10"])
