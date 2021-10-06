from .__init__ import *


def DiceSumProbFunc(maxDice=3, format='string'):
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

    if format == 'string':
        problem = f"If {a} dice are rolled at the same time, the probability of getting a sum of {b} ="
        solution = f"{count}/{6**a}"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, count, 6**a


dice_sum_probability = Generator(
    "Probability of a certain sum appearing on faces of dice", 52,
    DiceSumProbFunc, ["maxDice=3"])
