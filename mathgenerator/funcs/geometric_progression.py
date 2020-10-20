from .__init__ import *


def geomProgrFunc(number_values=6,
                  min_value=2,
                  max_value=12,
                  n_term=7,
                  sum_term=5):
    r = random.randint(min_value, max_value)
    a = random.randint(min_value, max_value)
    n_term = random.randint(number_values, number_values + 5)
    sum_term = random.randint(number_values, number_values + 5)
    GP = []
    for i in range(number_values):
        GP.append(a * (r**i))
    problem = "For the given GP " + str(
        GP) + " ,Find the value of a,common ratio," + str(
            n_term) + "th term value, sum upto " + str(sum_term) + "th term"
    value_nth_term = a * (r**(n_term - 1))
    sum_till_nth_term = a * ((r**sum_term - 1) / (r - 1))
    solution = "The value of a is {}, common ratio is {} , {}th term is {} , sum upto {}th term is {}".format(
        a, r, n_term, value_nth_term, sum_term, sum_till_nth_term)
    return problem, solution


geometric_progression = Generator(
    "Geometric Progression", 66,
    "Initial value,Common Ratio,nth Term,Sum till nth term =",
    "a,r,ar^n-1,sum(ar^n-1", geomProgrFunc)
