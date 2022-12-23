from ...latexBuilder import bmatrix
import random


def int_matrix_22_determinant(maxMatrixVal=100):
    """Determinant to 2x2 Matrix"""
    a = random.randint(0, maxMatrixVal)
    b = random.randint(0, maxMatrixVal)
    c = random.randint(0, maxMatrixVal)
    d = random.randint(0, maxMatrixVal)

    determinant = a * d - b * c
    lst = [[a, b], [c, d]]

    problem = f"$\\det {bmatrix(lst)}= $"
    solution = f"${determinant}$"
    return problem, solution
