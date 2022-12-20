from ...generator import Generator
import random


def gen_func(maxMatrixVal=100):
    a = random.randint(0, maxMatrixVal)
    b = random.randint(0, maxMatrixVal)
    c = random.randint(0, maxMatrixVal)
    d = random.randint(0, maxMatrixVal)

    determinant = a * d - b * c

    problem = f"$\det \left[ {{\begin{{array}}{{cc}} a & b \\\\ c & d \end{{array}}}} \\right] = $"
    solution = f"${determinant}$"
    return problem, solution


int_matrix_22_determinant = Generator("Determinant to 2x2 Matrix", 77,
                                      gen_func,
                                      ["maxMatrixVal=100"])
