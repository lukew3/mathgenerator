from ...generator import Generator
from ...latexBuilder import bmatrix
import random


def gen_func(maxMatrixVal=100):
    a = random.randint(0, maxMatrixVal)
    b = random.randint(0, maxMatrixVal)
    c = random.randint(0, maxMatrixVal)
    d = random.randint(0, maxMatrixVal)

    determinant = a * d - b * c
    lst = [[a, b], [c, d]]

    problem = f"$\\det {bmatrix(lst)}= $"
    solution = f"${determinant}$"
    return problem, solution


int_matrix_22_determinant = Generator("Determinant to 2x2 Matrix", 77,
                                      gen_func,
                                      ["maxMatrixVal=100"])
