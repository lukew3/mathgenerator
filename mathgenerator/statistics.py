import random
import math


def combinations(max_lengthgth=20):
    """Combinations of Objects

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the number of combinations from $19$ objects picked $6$ at a time. | $27132$ |
    """
    a = random.randint(10, max_lengthgth)
    b = random.randint(0, 9)

    solution = int(math.factorial(
        a) / (math.factorial(b) * math.factorial(a - b)))

    problem = f"Find the number of combinations from ${a}$ objects picked ${b}$ at a time."
    return problem, f'${solution}$'


def conditional_probability():
    """Conditional Probability

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Someone tested positive for a nasty disease which only $1.18$% of the population have. Test sensitivity (true positive) is equal to $SN=98.73$% whereas test specificity (true negative) $SP=99.99$%. What is the probability that this guy really has that disease? | $99.16$% |
    """
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

    problem = "Someone tested positive for a nasty disease which only ${0:.2f}$% of the population have. " \
        "Test sensitivity (true positive) is equal to $SN={1:.2f}$% whereas test specificity (true negative) $SP={2:.2f}$%. " \
        "What is the probability that this guy really has that disease?".format(
            P_disease, true_positive, true_negative)
    solution = f'${answer}$%'
    return problem, solution


def confidence_interval():
    """Confidence interval For sample S

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | The confidence interval for sample $[234, 223, 210, 203, 258, 299, 281, 208, 278, 252, 295, 245, 280, 235, 219, 297, 214, 267, 212, 256, 232, 221]$ with $99$% confidence is | $(263.31, 229.33)$ |
    """
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
    upper = round(mean + standard_error, 2)
    lower = round(mean - standard_error, 2)

    problem = 'The confidence interval for sample ${}$ with ${}$% confidence is'.format(
        [x for x in lst], lst_per[j])
    solution = f'$({upper}, {lower})$'
    return problem, solution


def data_summary(number_values=15, min_val=5, max_val=50):
    """Mean, Standard Deviation and Variance

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the mean,standard deviation and variance for the data $9, 29, 46, 27, 46, 15, 10, 44, 19, 33, 38, 7, 34, 28, 8$ | The Mean is $26.2$, Standard Deviation is $186.29$, Variance is $13.65$ |
    """
    random_list = []

    for i in range(number_values):
        n = random.randint(min_val, max_val)
        random_list.append(n)

    a = sum(random_list)
    mean = round(a / number_values, 2)

    var = 0
    for i in range(number_values):
        var += (random_list[i] - mean)**2

    standardDeviation = round(var / number_values, 2)
    variance = round((var / number_values) ** 0.5, 2)

    problem = f"Find the mean,standard deviation and variance for the data ${', '.join(map(str, random_list))}$"
    solution = f"The Mean is ${mean}$, Standard Deviation is ${standardDeviation}$, Variance is ${variance}$"
    return problem, solution


def dice_sum_probability(max_dice=3):
    """Probability of a certain sum appearing on faces of dice

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | If $2$ dice are rolled at the same time, the probability of getting a sum of $5 =$ | $\frac{4}{36}$ |
    """
    a = random.randint(1, max_dice)
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
    solution = rf"\frac{{{count}}}{{{6**a}}}"
    return problem, solution


def mean_median(max_length=10):
    """Mean and Median

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Given the series of numbers $[4, 19, 21, 22, 43, 44, 60, 81, 87, 92]$. Find the arithmatic mean and median of the series | Arithmetic mean of the series is $47.3$ and arithmetic median of this series is $43.5$ |
    """
    randomlist = random.sample(range(1, 99), max_length)
    total = 0
    for n in randomlist:
        total = total + n
    mean = total / 10
    randomlist.sort()
    median = (randomlist[4] + randomlist[5]) / 2

    problem = f"Given the series of numbers ${randomlist}$. Find the arithmatic mean and median of the series"
    solution = f"Arithmetic mean of the series is ${mean}$ and arithmetic median of this series is ${median}$"
    return problem, solution


def permutation(max_lengthgth=20):
    """Permutations

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Number of Permutations from $18$ objects picked $5$ at a time is: | $1028160$ |
    """
    a = random.randint(10, max_lengthgth)
    b = random.randint(0, 9)
    solution = int(math.factorial(a) / (math.factorial(a - b)))

    problem = f"Number of Permutations from ${a}$ objects picked ${b}$ at a time is: "
    return problem, f"${solution}$"
