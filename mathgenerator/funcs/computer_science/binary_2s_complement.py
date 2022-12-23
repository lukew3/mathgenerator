from ...generator import Generator
import random


def gen_func(maxDigits=10):
    digits = random.randint(1, maxDigits)
    question = ''.join([str(random.randint(0, 1))
                        for i in range(digits)]).lstrip('0')

    answer = []
    for i in question:
        answer.append(str(int(not bool(int(i)))))

    carry = True
    j = len(answer) - 1
    while j >= 0:
        if answer[j] == '0':
            answer[j] = '1'
            carry = False
            break
        answer[j] = '0'
        j -= 1

    if j == 0 and carry is True:
        answer.insert(0, '1')

    problem = f"2's complement of ${question} = $"
    solution = ''.join(answer).lstrip('0')
    return problem, f'${solution}$'


binary_2s_complement = Generator("Binary 2's Complement", 73,
                                 gen_func, ["maxDigits=10"])
