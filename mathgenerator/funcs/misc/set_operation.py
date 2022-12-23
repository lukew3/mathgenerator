from ...generator import Generator
import random


def gen_func(minval=3, maxval=7, n_a=4, n_b=5):
    number_variables_a = random.randint(minval, maxval)
    number_variables_b = random.randint(minval, maxval)
    a = []
    b = []
    for _ in range(number_variables_a):
        a.append(random.randint(1, 10))
    for _ in range(number_variables_b):
        b.append(random.randint(1, 10))
    a = set(a)
    b = set(b)

    problem = f"Given the two sets $a={a}$, $b={b}. " + \
        "Find the Union, intersection, a-b, b-a, and symmetric difference"
    solution = f"Union is ${a.union(b)}$. Intersection is ${a.intersection(b)}$" + \
        f", a-b is ${a.difference(b)}$, b-a is ${b.difference(a)}$." + \
        f" Symmetric difference is ${a.symmetric_difference(b)}$."
    return problem, solution


set_operation = Generator("Union,Intersection,Difference of Two Sets", 93,
                          gen_func,
                          ["minval=3", "maxval=7", "n_a=4", "n_b=5"])
