from ...generator import Generator
import random


def gen_func(minNo=1, maxNo=1000):
    b = random.randint(minNo, maxNo)
    a = b**(1 / 3)

    return (f"What is the cube root of: $\\sqrt[3]{{{b}}}=$ to 2 decimal places?", f"${round(a, 2)}$")


cube_root = Generator("Cube Root", 47, gen_func, ["minNo=1", "maxNo=1000"])
