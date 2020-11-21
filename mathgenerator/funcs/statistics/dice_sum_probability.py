from .__init__ import *


def DiceSumProbFunc(maxDice=3):
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

    problem = "If {} dice are rolled at the same time, the probability of getting a sum of {} =".format(
        a, b)
    solution = "{}/{}".format(count, 6**a)
    return problem, solution


dice_sum_probability = Generator(
    "Probability of a certain sum appearing on faces of dice", 52,
    "If n dices are rolled then probabilty of getting sum of x is =", "z",
    DiceSumProbFunc)
