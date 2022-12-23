import random


def vector_cross(minVal=-20, maxVal=20):
    """Cross product of 2 vectors"""
    a = [random.randint(minVal, maxVal) for _ in range(3)]
    b = [random.randint(minVal, maxVal) for _ in range(3)]
    c = [
        a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

    problem = f"${a} \\times {b} = $"
    solution = f"${c}$"
    return problem, solution
