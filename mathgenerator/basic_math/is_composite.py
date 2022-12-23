import random


def is_composite(maxNum=250):
    """Is Composite"""
    a = random.randint(2, maxNum)

    problem = f"Is ${a}$ composite?"
    if a == 0 or a == 1:
        return problem, "No"
    for i in range(2, a):
        if a % i == 0:
            return problem, "Yes"
    solution = "No"

    return problem, solution
