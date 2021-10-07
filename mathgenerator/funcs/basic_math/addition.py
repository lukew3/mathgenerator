from .__init__ import *


def gen_func(maxSum=99, maxAddend=50, format='string'):
    if maxAddend > maxSum:
        maxAddend = maxSum
    a = random.randint(0, maxAddend)
    # The highest value of b will be no higher than the maxsum minus the first number and no higher than the maxAddend as well
    b = random.randint(0, min((maxSum - a), maxAddend))
    c = a + b

    if format == "string":
        problem = str(a) + "+" + str(b) + "="
        solution = str(c)
        return problem, solution
    elif format == 'latex':
        problem = "\\(" + str(a) + '+' + str(b) + "\\)"
        solution = str(c)
        return problem, solution
    else:
        return a, b, c


addition = Generator("Addition", 0, gen_func, ["maxSum=99", "maxAddend=50"])
