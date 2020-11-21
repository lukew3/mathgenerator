from .__init__ import *
import math


def angleBtwVectorsFunc(maxEltAmt=20):
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
    problem = f"angle between the vectors {v1} and {v2} is:"
    solution = ''
    try:
        solution = str(round(math.acos(s / mags), 2)) + " radians"
    except ValueError:
        print('angleBtwVectorsFunc has some issues with math module, line 16')
        solution = 'NaN'
    # would return the answer in radians
    return problem, solution


angle_btw_vectors = Generator(
    "Angle between 2 vectors", 70,
    "Angle Between 2 vectors V1=[v11, v12, ..., v1n] and V2=[v21, v22, ....., v2n]",
    "V1.V2 / (euclidNorm(V1)*euclidNorm(V2))", angleBtwVectorsFunc)
