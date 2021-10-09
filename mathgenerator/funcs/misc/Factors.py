from .__init__ import *


def gen_func(maxVal=1000, format='string'):
    n = x = random.randint(1, maxVal)
    
    factors = []

    for i in range(1, int(n**0.5) + 1) :
        if i**2 == n :
            factors.append(i)
        elif n%i ==0 :
            factors.append(i)
            factors.append(n//i)
        else :
            pass

    factors.sort()

    if format == 'string':
        problem = f"Factors of {n} = "
        solution = factors
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return n, factors


common_factors = Generator("Factors", 116, gen_func,
                           ["maxVal=1000"])