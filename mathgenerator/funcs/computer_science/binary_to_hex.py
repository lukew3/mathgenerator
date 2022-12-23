import random


def binary_to_hex(max_dig=10):
    """Binary to Hexidecimal"""
    problem = ''.join([str(random.randint(0, 1)) for _ in range(random.randint(1, max_dig))])
    solution = f'${hex(int(problem, 2))}$'
    return f'${problem}$', solution
