from .__init__ import *


def determinantToMatrix22(maxMatrixVal=100, format='string'):
    a = random.randint(0, maxMatrixVal)
    b = random.randint(0, maxMatrixVal)
    c = random.randint(0, maxMatrixVal)
    d = random.randint(0, maxMatrixVal)

    determinant = a * d - b * c

    if format == 'string':
        problem = f"Det([[{a}, {b}], [{c}, {d}]]) = "
        solution = f" {determinant}"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, c, d, determinant


int_matrix_22_determinant = Generator("Determinant to 2x2 Matrix", 77,
                                      determinantToMatrix22,
                                      ["maxMatrixVal=100"])
