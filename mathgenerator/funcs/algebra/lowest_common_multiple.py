from .__init__ import *


def gen_func(maxA = 100, maxB = 100, format='string'):

    a = random.randint(1, maxA)
    b = random.randint(1, maxB)

    x = a
    y = b
    while (y) :
        x, y = y, x%y

    lcm = (a/x)*b
    
    if format == 'string':
        problem = f"LCM of ({a} and {b}) is : "
        solution = str(lcm)
        return problem, solution
    elif format == 'latex':
        return 'Latex unavailable'
    else:
        a, b, lcm


generator_name = Generator("Lowest Common Multiple", 122, gen_func,
                           ["maxA=100", "maxB=100"])