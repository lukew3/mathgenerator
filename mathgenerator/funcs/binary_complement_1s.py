from .__init__ import *


def binaryComplement1sFunc(maxDigits=10):
    question = ''
    answer = ''

    for i in range(random.randint(1, maxDigits)):
        temp = str(random.randint(0, 1))
        question += temp
        answer += "0" if temp == "1" else "1"

    problem = question + "="
    solution = answer
    return problem, solution


binary_complement_1s = Generator("Binary Complement 1s", 4, "1010=", "0101",
                                 binaryComplement1sFunc)
