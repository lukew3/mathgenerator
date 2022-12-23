import random


def addition(maxSum=99, maxAddend=50):
    """Addition of two numbers"""
    if maxAddend > maxSum:
        maxAddend = maxSum
    a = random.randint(0, maxAddend)
    # The highest value of b will be no higher than the maxsum minus the first number and no higher than the maxAddend as well
    b = random.randint(0, min((maxSum - a), maxAddend))
    c = a + b

    problem = f'${a}+{b}=$'
    solution = f'${c}$'
    return problem, solution
