import random


def binary_complement_1s(maxDigits=10):
    """Binary Complement 1s"""
    question = ''
    answer = ''

    for _ in range(random.randint(1, maxDigits)):
        temp = str(random.randint(0, 1))
        question += temp
        answer += "0" if temp == "1" else "1"

    problem = f'${question} = $'
    return problem, f'${answer}$'
