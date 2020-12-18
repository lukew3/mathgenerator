from .__init__ import *


def multiplyIntToMatrix22(maxMatrixVal=10, maxRes=100, style='raw'):
    a = random.randint(0, maxMatrixVal)
    b = random.randint(0, maxMatrixVal)
    c = random.randint(0, maxMatrixVal)
    d = random.randint(0, maxMatrixVal)

    constant = random.randint(0, int(maxRes / max(a, b, c, d)))

    a1 = a * constant
    b1 = b * constant
    c1 = c * constant
    d1 = d * constant

    if style == 'latex':
        problem = "\\(" + str(constant) + "\\cdot\\begin{bmatrix}" + str(a) + "&" + str(b) + "\\\\" + str(c) + "&" + str(d) + "\\end{bmatrix}=\\)"
        solution = "\\(\\begin{bmatrix}" + str(a1) + "&" + str(b1) + "\\\\" + str(c1) + "&" + str(d1) + "\\end{bmatrix}\\)"
    else:
        problem = f"{constant} * [[{a}, {b}], [{c}, {d}]] = "
        solution = f"[[{a1},{b1}],[{c1},{d1}]]"
    return problem, solution


multiply_int_to_22_matrix = Generator("Integer Multiplication with 2x2 Matrix",
                                      17, "k * [[a,b],[c,d]]=",
                                      "[[k*a,k*b],[k*c,k*d]]",
                                      multiplyIntToMatrix22)
