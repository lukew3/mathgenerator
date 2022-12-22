from ...generator import Generator
import random


def gen_func(number_values=15, minval=5, maxval=50):
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


data_summary = Generator("Mean,Standard Deviation,Variance", 59,
                         gen_func,
                         ["number_values=15", "minval=5", "maxval=50"])
