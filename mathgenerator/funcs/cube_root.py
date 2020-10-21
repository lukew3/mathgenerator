from .__init__ import *


def cubeRootFunc(minNo=1, maxNo=1000):
    b = random.randint(minNo, maxNo)
    a = b**(1 / 3)

    problem = "cuberoot of " + str(b) + " upto 2 decimal places is:"
    solution = str(round(a, 2))
    return problem, solution


cube_root = Generator("Cube Root", 47, "Cuberoot of a upto 2 decimal places is",
                      "b", cubeRootFunc)
