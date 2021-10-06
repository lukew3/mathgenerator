from .__init__ import *
import math


def angleBtwVectorsFunc(maxEltAmt=20, format='string'):
    s = 0
    v1 = [
        round(random.uniform(0, 1000), 2)
        for i in range(random.randint(2, maxEltAmt))
    ]
    v2 = [round(random.uniform(0, 1000), 2) for i in v1]
    for i in range(len(v1)):
        s += v1[i] * v2[i]

    mags = math.sqrt(sum([i**2
                          for i in v1])) * math.sqrt(sum([i**2 for i in v2]))
    solution = ''
    ans = 0
    try:
        ans = round(math.acos(s / mags), 2)
        solution = str(ans) + " radians"
    except ValueError:
        print('angleBtwVectorsFunc has some issues with math module, line 16')
        solution = 'NaN'
        ans = 'NaN'
    # would return the answer in radians
    if format == 'string':
        problem = f"angle between the vectors {v1} and {v2} is:"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return v1, v2, ans


angle_btw_vectors = Generator("Angle between 2 vectors", 70,
                              angleBtwVectorsFunc, ["maxEltAmt=20"])
