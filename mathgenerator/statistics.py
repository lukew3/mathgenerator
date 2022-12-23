import random
import math


def combinations(maxlength=20):
    """Combinations of Objects"""
    a = random.randint(10, maxlength)
    b = random.randint(0, 9)

    solution = int(math.factorial(a) / (math.factorial(b) * math.factorial(a - b)))

    problem = f"Find the number of combinations from ${a}$ objects picked ${b}$ at a time."
    return problem, f'${solution}$'

import random


def conditional_probability():
    """Conditional Probability"""
    P_disease = round(2. * random.random(), 2)
    true_positive = round(random.random() + float(random.randint(90, 99)), 2)
    true_negative = round(random.random() + float(random.randint(90, 99)), 2)

    def BayesFormula(P_disease, true_positive, true_negative):
        P_notDisease = 100. - P_disease
        false_positive = 100. - true_negative
        P_plus = (P_disease) * (true_positive) + \
            (P_notDisease) * (false_positive)
        P_disease_plus = ((true_positive) * (100 * P_disease)) / P_plus

        return P_disease_plus

    answer = round(BayesFormula(P_disease, true_positive, true_negative), 2)

    problem = "Someone tested positive for a nasty disease which only ${0:.2f}\\%$ of the population have. " \
        "Test sensitivity (true positive) is equal to $SN={1:.2f}$% whereas test specificity (true negative) $SP={2:.2f}\\%$. " \
        "What is the probability that this guy really has that disease?".format(
            P_disease, true_positive, true_negative)
    solution = f'${answer}$%'
    return problem, solution

import random
import math


def confidence_interval():
    """Confidence interval For sample S"""
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
    upper = mean + standard_error
    lower = mean - standard_error

    problem = 'The confidence interval for sample ${}$ with ${}$% confidence is'.format(
        [x for x in lst], lst_per[j])
    solution = f'$({upper}, {lower})$'
    return problem, solution

import random


def data_summary(number_values=15, minval=5, maxval=50):
    """Mean, Standard Deviation and Variance"""
    random_list = []

    for i in range(number_values):
        n = random.randint(minval, maxval)
        random_list.append(n)

    a = sum(random_list)
    mean = a / number_values

    var = 0
    for i in range(number_values):
        var += (random_list[i] - mean)**2

    standardDeviation = var / number_values
    variance = (var / number_values) ** 0.5

    problem = f"Find the mean,standard deviation and variance for the data ${', '.join(map(str, random_list))}$"
    solution = f"The Mean is ${mean}$, Standard Deviation is ${standardDeviation}$, Variance is ${variance}$"
    return problem, solution

import random


def dice_sum_probability(maxDice=3):
    """Probability of a certain sum appearing on faces of dice"""
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

import random
import math


def permutation(maxlength=20):
    """Permutations"""
    a = random.randint(10, maxlength)
    b = random.randint(0, 9)
    solution = int(math.factorial(a) / (math.factorial(a - b)))

    problem = f"Number of Permutations from ${a}$ objects picked ${b}$ at a time is: "
    return problem, f"${solution}$"

