import random


def gcd(maxVal=20):
    """GCD (Greatest Common Denominator)"""
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    while y:
        x, y = y, x % y

    problem = f"GCD of ${a}$ and ${b} = $"
    solution = f'${x}$'
    return problem, solution
