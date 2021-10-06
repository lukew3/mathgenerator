from .__init__ import *


def binaryComplement1sFunc(maxDigits=10, format='string'):
    question = ''
    answer = ''

    for i in range(random.randint(1, maxDigits)):
        temp = str(random.randint(0, 1))
        question += temp
        answer += "0" if temp == "1" else "1"

    if format == 'string':
        problem = question + "="
        return problem, answer
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return problem, answer


binary_complement_1s = Generator("Binary Complement 1s", 4,
                                 binaryComplement1sFunc, ["maxDigits=10"])
