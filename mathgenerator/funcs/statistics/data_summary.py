from .__init__ import *


def gen_func(number_values=15, minval=5, maxval=50, format='string'):
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
    variance = (var / number_values)**0.5

    if format == 'string':
        problem = "Find the mean,standard deviation and variance for the data" + \
            str(random_list)
        solution = f"The Mean is {mean} , Standard Deviation is {standardDeviation}, Variance is {variance}"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return random_list, mean, standardDeviation, variance


data_summary = Generator("Mean,Standard Deviation,Variance", 59,
                         gen_func,
                         ["number_values=15", "minval=5", "maxval=50"])
