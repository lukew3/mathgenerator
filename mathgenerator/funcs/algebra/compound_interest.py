from ...generator import Generator
import random


def gen_func(maxPrinciple=10000,
             maxRate=10,
             maxTime=10):
    p = random.randint(1000, maxPrinciple)
    r = random.randint(1, maxRate)
    n = random.randint(1, maxTime)
    a = round(p * (1 + r / 100)**n, 2)

    problem = f"Compound interest for a principle amount of ${p}$ dollars, ${r}$% rate of interest and for a time period of ${n}$ years is $=$"
    return problem, f'${a}$'


compound_interest = Generator(
    "Compound Interest", 78, gen_func,
    ["maxPrinciple=10000", "maxRate=10", "maxTime=10"])
