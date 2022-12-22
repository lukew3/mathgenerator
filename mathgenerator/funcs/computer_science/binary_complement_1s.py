from ...generator import Generator
import random


def gen_func(maxDigits=10):
    question = ''
    answer = ''

    for _ in range(random.randint(1, maxDigits)):
        temp = str(random.randint(0, 1))
        question += temp
        answer += "0" if temp == "1" else "1"

    problem = f'${question} = $'
    return problem, f'${answer}$'


binary_complement_1s = Generator("Binary Complement 1s", 4,
                                 gen_func, ["maxDigits=10"])
