import random


def hcf(maxVal=20):
    """HCF (Highest Common Factor)"""
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    while (y):
        x, y = y, x % y

    problem = f"HCF of ${a}$ and ${b} = $"
    solution = f'${x}$'
    return problem, solution
