import random


def mean_median(maxlen=10):
    """Mean and Median"""
    randomlist = random.sample(range(1, 99), maxlen)
    total = 0
    for n in randomlist:
        total = total + n
    mean = total / 10
    randomlist.sort()
    median = (randomlist[4] + randomlist[5]) / 2

    problem = f"Given the series of numbers ${randomlist}$. Find the arithmatic mean and mdian of the series"
    solution = f"Arithmetic mean of the series is ${mean}$ and Arithmetic median of this series is ${median}$"
    return problem, solution
