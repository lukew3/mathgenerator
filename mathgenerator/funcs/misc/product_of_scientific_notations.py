from ...generator import Generator
import random


def gen_func(minExpVal=-100, maxExpVal=100):
    a = [round(random.uniform(1, 10), 2), random.randint(minExpVal, maxExpVal)]
    b = [round(random.uniform(1, 10), 2), random.randint(minExpVal, maxExpVal)]
    c = [a[0] * b[0], a[1] + b[1]]

    if c[0] >= 10:
        c[0] /= 10
        c[1] += 1

    problem = f"Product of scientific notations ${a[0]} \\times 10^{{{a[1]}}}$ and ${b[0]} \\times 10^{{{b[1]}}} = $"
    solution = f'${round(c[0], 2)} \\times 10^{{{c[1]}}}$'
    return problem, solution


product_of_scientific_notations = Generator("Product of scientific notations", 121, gen_func,
                                            ["minExpVal=-100", "maxExpVal=100"])
