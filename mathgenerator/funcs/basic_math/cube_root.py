from .__init__ import *


def cubeRootFunc(minNo=1, maxNo=1000, style='raw'):
    b = random.randint(minNo, maxNo)
    a = b**(1 / 3)

    if style == 'latex':
        problem = f"\\(\\sqrt[3]{{{b}}}=\\)"
        solution = "\\(" + str(round(a, 2)) + "\\)"
    else:
        problem = "What is the cube root of " + str(b) + " up to 2 decimal places?"
        solution = str(round(a, 2))
    return problem, solution


cube_root = Generator("Cube Root", 47,
                      "Cuberoot of a upto 2 decimal places is", "b",
                      cubeRootFunc)
