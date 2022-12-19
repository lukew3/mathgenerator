from ...__init__ import Generator
import random


def greatestCommonDivisorOfTwoNumbers(number1, number2):
    number1 = abs(number1)
    number2 = abs(number2)
    while number2 > 0:
        number1, number2 = number2, number1 % number2
    return number1


def gen_func(numbersCount=2, maximalNumberLimit=10**9, format='string'):
    numbersCount = max(numbersCount, 2)
    numbers = [random.randint(0, maximalNumberLimit)
               for number in range(numbersCount)]

    greatestCommonDivisor = greatestCommonDivisorOfTwoNumbers(
        numbers[0], numbers[1])

    for index in range(1, numbersCount):
        greatestCommonDivisor = greatestCommonDivisorOfTwoNumbers(
            numbers[index], greatestCommonDivisor)

    if format == "string":
        return "GCD(" + ",".join(map(str, numbers)) + ")=", str(greatestCommonDivisor)
    elif format == "latex":
        return ("\\(GCD(" + ",".join(map(str, numbers)) + ")=", f"\\({greatestCommonDivisor}\\)")
    else:
        return greatestCommonDivisor


greatest_common_divisor = Generator("Greatest Common Divisor of N Numbers", 120, gen_func, [
                                    "numbersCount=2", "maximalNumberLimit=10**9"])
