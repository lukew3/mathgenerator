from .__init__ import *


def harmonicMeanFunc(maxValue=100, maxNum=4):

    a = random.randint(1, maxValue)
    b = random.randint(1, maxValue)
    c = random.randint(1, maxValue)
    d = random.randint(1, maxValue)
    num = random.randint(2, 4)
    if num == 2:
        sum = (1 / a) + (1 / b)
    elif num == 3:
        sum = (1 / a) + (1 / b) + (1 / c)
    elif num == 4:
        sum = (1 / a) + (1 / b) + (1 / c) + (1 / d)

    ans = num / sum
    if num == 2:
        problem = f"Harmonic mean of {num} numbers {a} and {b} = "
        solution = f" {num}/((1/{a}) + (1/{b})) = {ans}"
    elif num == 3:
        problem = f"Harmonic mean of {num} numbers {a} , {b} and {c} = "
        solution = f" {num}/((1/{a}) + (1/{b}) + (1/{c})) = {ans}"
    elif num == 4:
        problem = f"Harmonic mean of {num} numbers {a} , {b} , {c} , {d} = "
        solution = f" {num}/((1/{a}) + (1/{b}) + (1/{c}) + (1/{d})) = {ans}"
    return problem, solution


harmonic_mean = Generator("Harmonic Mean of N Numbers", 68,
                          "Harmonic mean of n numbers A1 , A2 , ... , An = ",
                          " n/((1/A1) + (1/A2) + ... + (1/An)) = ans",
                          harmonicMeanFunc)
