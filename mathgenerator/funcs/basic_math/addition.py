from ...generator import Generator
import random


def gen_func(maxSum=99, maxAddend=50):
    if maxAddend > maxSum:
        maxAddend = maxSum
    a = random.randint(0, maxAddend)
    # The highest value of b will be no higher than the maxsum minus the first number and no higher than the maxAddend as well
    b = random.randint(0, min((maxSum - a), maxAddend))
    c = a + b

    problem = f'${a}+{b}=$'
    solution = f'${c}$'
    return problem, solution


addition = Generator("Addition", 0, gen_func, ["maxSum=99", "maxAddend=50"])
