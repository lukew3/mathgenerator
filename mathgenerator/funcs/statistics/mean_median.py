from .__init__ import *
import random


def meanMedianFunc(maxlen=10, format='string'):
    randomlist = random.sample(range(1, 99), maxlen)
    total = 0
    for n in randomlist:
        total = total + n
    mean = total / 10
    randomlist.sort()
    median = (randomlist[4] + randomlist[5]) / 2

    if format == 'string':
        problem = f"Given the series of numbers {randomlist}. find the arithmatic mean and mdian of the series"
        solution = f"Arithmetic mean of the series is {mean} and Arithmetic median of this series is {median}"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return randomlist, mean, median


mean_median = Generator("Mean and Median", 76, meanMedianFunc, ["maxlen=10"])
