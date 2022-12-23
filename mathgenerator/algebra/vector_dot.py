import random


def vector_dot(minVal=-20, maxVal=20):
    """Dot product of 2 vectors"""
    a = [random.randint(minVal, maxVal) for i in range(3)]
    b = [random.randint(minVal, maxVal) for i in range(3)]
    c = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

    problem = f'${a}\\cdot{b}=$'
    solution = f'${c}$'
    return problem, solution
