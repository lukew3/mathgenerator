import random


def cube_root(minNo=1, maxNo=1000):
    """Cube Root"""
    b = random.randint(minNo, maxNo)
    a = b**(1 / 3)

    return (f"What is the cube root of: $\\sqrt[3]{{{b}}}=$ to 2 decimal places?", f"${round(a, 2)}$")
