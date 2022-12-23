from ...generator import Generator
import random


def gen_func(maxVariable=10):
    a = random.randint(1, maxVariable)
    b = random.randint(1, maxVariable)
    c = random.randint(b, maxVariable)

    # calculate gcd
    def calculate_gcd(x, y):
        while (y):
            x, y = y, x % y
        return x

    i = calculate_gcd((c - b), a)
    x = f"{(c - b)//i}/{a//i}"

    if (c - b == 0):
        x = "0"
    elif a == 1 or a == i:
        x = f"{c - b}"

    problem = f"${a}x + {b} = {c}$"
    solution = f"${x}$"
    return problem, solution


basic_algebra = Generator("Basic Algebra", 11, gen_func,
                          ["maxVariable=10"])
