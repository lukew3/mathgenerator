from .__init__ import *


def gen_func(minRealImaginaryNum=-20,
             maxRealImaginaryNum=20,
             format='string'):
    num1 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                   random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    num2 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                   random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    product = num1 * num2

    if format == 'string':
        problem = f"{num1} * {num2} = "
        solution = str(product)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return num1, num2, product


multiply_complex_numbers = Generator(
    "Multiplication of 2 complex numbers", 65, gen_func,
    ["minRealImaginaryNum=-20", "maxRealImaginaryNum=20"])
