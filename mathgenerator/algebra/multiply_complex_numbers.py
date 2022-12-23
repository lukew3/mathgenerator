import random


def multiply_complex_numbers(minRealImaginaryNum=-20,
                             maxRealImaginaryNum=20):
    """Multiplication of 2 complex numbers"""
    num1 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                   random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    num2 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                   random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    product = num1 * num2

    problem = f"${num1} * {num2} = $"
    solution = f'${product}$'
    return problem, solution
