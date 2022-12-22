from ...generator import Generator
import random


def gen_func(maxDice=3):
    a = random.randint(1, maxDice)
    b = random.randint(a, 6 * a)

    count = 0
    for i in [1, 2, 3, 4, 5, 6]:
        if a == 1:
            if i == b:
                count = count + 1
        elif a == 2:
            for j in [1, 2, 3, 4, 5, 6]:
                if i + j == b:
                    count = count + 1
        elif a == 3:
            for j in [1, 2, 3, 4, 5, 6]:
                for k in [1, 2, 3, 4, 5, 6]:
                    if i + j + k == b:
                        count = count + 1

    problem = f"If ${a}$ dice are rolled at the same time, the probability of getting a sum of ${b} =$"
    solution = f"\\frac{{{count}}}{{{6**a}}}"
    return problem, solution


dice_sum_probability = Generator(
    "Probability of a certain sum appearing on faces of dice", 52,
    gen_func, ["maxDice=3"])
