from ...generator import Generator
import random


def list_to_tex(lst):
    out = '\\begin{bmatrix} '
    lst = [' & '.join(map(str, row)) for row in lst]
    out += ' \\\\ '.join(lst)
    out += ' \\end{bmatrix}'
    return out


def gen_func(maxMatrixVal=10, maxRes=100, format='string'):
    a = random.randint(0, maxMatrixVal)
    b = random.randint(0, maxMatrixVal)
    c = random.randint(0, maxMatrixVal)
    d = random.randint(0, maxMatrixVal)

    constant = random.randint(0, int(maxRes / max(a, b, c, d)))

    a1 = a * constant
    b1 = b * constant
    c1 = c * constant
    d1 = d * constant
    lst = [[a, b], [c, d]]
    lst1 = [[a1, b1], [c1, d1]]

    problem = f'${constant} * {list_to_tex(lst)} =$'
    solution = f'${list_to_tex(lst1)}$'
    return problem, solution


multiply_int_to_22_matrix = Generator("Integer Multiplication with 2x2 Matrix",
                                      17, gen_func,
                                      ["maxMatrixVal=10", "maxRes=100"])
