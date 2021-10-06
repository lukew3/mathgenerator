from .__init__ import *


def squareRootFunc(minNo=1, maxNo=12, format='string'):
    b = random.randint(minNo, maxNo)
    a = b * b

    if format == 'string':
        problem = "sqrt(" + str(a) + ")="
        solution = str(b)
        return problem, solution
    elif format == 'latex':
        problem = "\\(\\sqrt{" + str(a) + "}=\\)"
        solution = "\\(" + str(b) + "\\)"
        return problem, solution
    else:
        return a, b


square_root = Generator("Square Root", 6, squareRootFunc,
                        ["minNo=1", "maxNo=12"])
