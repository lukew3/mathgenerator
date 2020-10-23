from .__init__ import *


def genDifferentiationProblem(diff_lvl):
    problem = ''

    types = {
        'Logrithmic': ['ln'],
        'Trigonometric': ['sin', 'cos', 'tan', 'cot', 'sec'],
        'Exponentional': ['exp']
    }

    if diff_lvl == 1:
        coeff = random.randrange(2, 10)
        power = random.randint(2, 4)
        flag = random.random()
        if flag > 0.5:
            power *= -1
            problem += str(coeff) + '*x^' + '(' + str(power) + ')'
        else:
            problem += str(coeff) + '*x^' + str(power)
    if diff_lvl == 2:
        func_type = random.choices(list(types.keys()), weights=(1, 4, 1))[0]
        func = random.choice(types[func_type])
        problem += func + '(x)' + '+' + genDifferentiationProblem(1)
    if diff_lvl == 3:
        func_type = random.choices(list(types.keys()), weights=(1, 4, 1))[0]
        func = random.choice(types[func_type])
        problem += func + '(' + genDifferentiationProblem(1) + ')'
    if diff_lvl == 4:
        operator = random.choice(('/', '*'))
        problem = '(' + genDifferentiationProblem(2) + ')' + \
            operator + '(' + genDifferentiationProblem(3) + ')'

    return problem


def differentiationFunc(diff_lvl=2):
    if diff_lvl < 1 or diff_lvl > 4:
        print("diff_lvl not supported")
        return None
    problem = genDifferentiationProblem(diff_lvl)

    x = sympy.symbols('x')
    solution = str(sympy.diff(problem.replace('^', '**'), x))
    solution = solution.replace('**', '^')
    problem = f"differentiate w.r.t x : d({problem})/dx"

    return problem, solution


differentiation = Generator("Differentiation", 88,
                            "differentiate w.r.t x : d(f(x))/dx", "g(x)",
                            differentiationFunc)
