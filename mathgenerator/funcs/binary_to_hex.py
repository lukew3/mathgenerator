from .__init__ import *


def binaryToHexFunc(max_dig=10):
    problem = ''
    for i in range(random.randint(1, max_dig)):
        temp = str(random.randint(0, 1))
        problem += temp

    solution = hex(int(problem, 2))
    return problem, solution


binary_to_hex = Generator("Binary to Hexidecimal", 64, "Hexidecimal of a=",
                          "b", binaryToHexFunc)
