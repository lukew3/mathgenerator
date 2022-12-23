import random
import math


def nth_fibonacci_number(maxN=100):
    """nth Fibonacci number"""
    gratio = (1 + math.sqrt(5)) / 2
    n = random.randint(1, maxN)

    problem = f"What is the {n}th Fibonacci number?"
    solution = int((math.pow(gratio, n) - math.pow(-gratio, -n)) / (math.sqrt(5)))

    return problem, f'${solution}$'
