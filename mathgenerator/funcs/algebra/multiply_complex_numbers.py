from .__init__ import *


def multiplyComplexNumbersFunc(minRealImaginaryNum=-20,
                               maxRealImaginaryNum=20):
    num1 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                   random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    num2 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                   random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    problem = f"{num1} * {num2} = "
    solution = str(num1 * num2)
    return problem, solution


multiply_complex_numbers = Generator("Multiplication of 2 complex numbers", 65,
                                     "(x + j) (y + j) = ", "xy + xj + yj -1",
                                     multiplyComplexNumbersFunc)
