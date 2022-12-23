import random


def compound_interest(maxPrinciple=10000,
                      maxRate=10,
                      maxTime=10):
    """Compound Interest"""
    p = random.randint(1000, maxPrinciple)
    r = random.randint(1, maxRate)
    n = random.randint(1, maxTime)
    a = round(p * (1 + r / 100)**n, 2)

    problem = f"Compound interest for a principle amount of ${p}$ dollars, ${r}$% rate of interest and for a time period of ${n}$ years is $=$"
    return problem, f'${a}$'
