import random


def square_root(minNo=1, maxNo=12):
    """Square Root"""
    b = random.randint(minNo, maxNo)
    a = b ** 2

    return f'$\\sqrt{{{a}}}=$', f'${b}$'
