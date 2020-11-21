from .__init__ import *

import math


def confidenceIntervalFunc():
    n = random.randint(20, 40)
    j = random.randint(0, 3)

    lst = random.sample(range(200, 300), n)
    lst_per = [80, 90, 95, 99]
    lst_t = [1.282, 1.645, 1.960, 2.576]

    mean = 0
    sd = 0

    for i in lst:
        count = i + mean
        mean = count

    mean = mean / n

    for i in lst:
        x = (i - mean)**2 + sd
        sd = x

    sd = sd / n
    standard_error = lst_t[j] * math.sqrt(sd / n)

    problem = 'The confidence interval for sample {} with {}% confidence is'.format(
        [x for x in lst], lst_per[j])
    solution = '({}, {})'.format(mean + standard_error, mean - standard_error)
    return problem, solution


confidence_interval = Generator("Confidence interval For sample S", 54,
                                "With X% confidence", "is (A,B)",
                                confidenceIntervalFunc)
