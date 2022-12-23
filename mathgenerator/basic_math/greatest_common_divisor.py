import random


def greatestCommonDivisorOfTwoNumbers(number1, number2):
    number1 = abs(number1)
    number2 = abs(number2)
    while number2 > 0:
        number1, number2 = number2, number1 % number2
    return number1


def greatest_common_divisor(numbersCount=2, maximalNumberLimit=10**9):
    """Greatest Common Divisor of N Numbers"""
    numbersCount = max(numbersCount, 2)
    numbers = [random.randint(0, maximalNumberLimit)
               for number in range(numbersCount)]

    greatestCommonDivisor = greatestCommonDivisorOfTwoNumbers(
        numbers[0], numbers[1])

    for index in range(1, numbersCount):
        greatestCommonDivisor = greatestCommonDivisorOfTwoNumbers(
            numbers[index], greatestCommonDivisor)

    return f'$GCD({",".join(map(str, numbers))})=$', f"${greatestCommonDivisor}$"
