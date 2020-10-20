from .__init__ import *


def angleBtwVectorsFunc(maxEltAmt=20):
    s = 0
    v1 = [random.uniform(0, 1000) for i in range(random.randint(2, maxEltAmt))]
    v2 = [random.uniform(0, 1000) for i in v1]
    for i in v1:
        for j in v2:
            s += i * j

    mags = math.sqrt(sum([i**2 for i in v1])) * math.sqrt(sum([i**2 for i in v2]))
    problem = f"angle between the vectors {v1} and {v2} is:"
    solution = ''
    try:
        solution = str(math.acos(s / mags))
    except MathDomainError:
        print('angleBtwVectorsFunc has some issues with math module, line 16')
        solution = 'NaN'
    # would return the answer in radians
    return problem, solution
