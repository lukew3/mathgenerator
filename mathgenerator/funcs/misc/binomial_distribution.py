from ...generator import Generator
import random


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def newton_symbol(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def gen_func():
    rejected_fraction = float(random.randint(30, 40)) + random.random()
    batch = random.randint(10, 20)
    rejections = random.randint(1, 9)

    answer = 0
    rejected_fraction = round(rejected_fraction, 2)
    for i in range(0, rejections + 1):
        answer += newton_symbol(float(batch), float(i)) * ((rejected_fraction / 100.) ** float(i)) * \
            ((1 - (rejected_fraction / 100.)) ** (float(batch) - float(i)))

    answer = round(100 * answer, 2)

    problem = "A manufacturer of metal pistons finds that, on average, ${0:}$% "\
        "of the pistons they manufacture are rejected because " \
        "they are incorrectly sized. What is the probability that a "\
        "batch of ${1:}$ pistons will contain no more than ${2:}$ " \
        "rejected pistons?".format(rejected_fraction, batch, rejections)
    return problem, f'${answer}$'


binomial_distribution = Generator("Binomial distribution", 109,
                                  gen_func, [""])
