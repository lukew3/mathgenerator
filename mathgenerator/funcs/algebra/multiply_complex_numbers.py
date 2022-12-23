from ...generator import Generator
import random


def gen_func(minRealImaginaryNum=-20,
             maxRealImaginaryNum=20):
    num1 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                   random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    num2 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                   random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    product = num1 * num2

    problem = f"${num1} * {num2} = $"
    solution = f'${product}$'
    return problem, solution


multiply_complex_numbers = Generator(
    "Multiplication of 2 complex numbers", 65, gen_func,
    ["minRealImaginaryNum=-20", "maxRealImaginaryNum=20"])
