from .__init__ import *


def multiplyIntToMatrix22(maxMatrixVal=10, maxRes=100):
    a = random.randint(0, maxMatrixVal)
    b = random.randint(0, maxMatrixVal)
    c = random.randint(0, maxMatrixVal)
    d = random.randint(0, maxMatrixVal)
    
    constant = random.randint(0, int(maxRes / max(a, b, c, d)))
    problem = f"{constant} * [[{a}, {b}], [{c}, {d}]] = "
    solution = f"[[{a*constant},{b*constant}],[{c*constant},{d*constant}]]"
    return problem, solution
