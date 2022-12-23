import random


def binary_complement_1s(maxDigits=10):
    """Binary Complement 1s"""
    question = ''.join([str(random.randint(0, 1)) for _ in range(random.randint(1, maxDigits))])
    answer = ''.join(["0" if digit == "1" else "1" for digit in question])

    problem = f'${question} = $'
    return problem, f'${answer}$'
