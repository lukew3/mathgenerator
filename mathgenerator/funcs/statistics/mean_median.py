from .__init__ import *
import random


def meanMedianFunc(maxlen=10):
    randomlist = random.sample(range(1, 99), maxlen)
    total = 0
    for n in randomlist:
        total = total + n
    mean = total / 10
    problem = f"Given the series of numbers {randomlist}. find the arithmatic mean and mdian of the series"
    randomlist.sort()
    median = (randomlist[4] + randomlist[5]) / 2
    solution = f"Arithmetic mean of the series is {mean} and Arithmetic median of this series is {median}"
    return problem, solution


mean_median = Generator("Mean and Median", 76,
                        "Mean and median of given set of numbers",
                        "Mean, Median", meanMedianFunc)
