import random


def absolute_difference(maxA=100, maxB=100):
    """Absolute difference between two numbers"""
    a = random.randint(-1 * maxA, maxA)
    b = random.randint(-1 * maxB, maxB)
    absDiff = abs(a - b)

    return f'$|{a}-{b}|=$', f"${absDiff}$"


def addition(maxSum=99, maxAddend=50):
    """Addition of two numbers

    ("$22+34=$", "$56$")
    """
    if maxAddend > maxSum:
        maxAddend = maxSum
    a = random.randint(0, maxAddend)
    # The highest value of b will be no higher than the maxsum minus the first number and no higher than the maxAddend as well
    b = random.randint(0, min((maxSum - a), maxAddend))
    c = a + b

    problem = f'${a}+{b}=$'
    solution = f'${c}$'
    return problem, solution


def compare_fractions(maxVal=10):
    """Compare Fractions"""
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    c = random.randint(1, maxVal)
    d = random.randint(1, maxVal)

    while (a == b):
        b = random.randint(1, maxVal)
    while (c == d):
        d = random.randint(1, maxVal)

    first = a / b
    second = c / d

    if (first > second):
        solution = ">"
    elif (first < second):
        solution = "<"
    else:
        solution = "="

    problem = f"Which symbol represents the comparison between $\\frac{{{a}}}{{{b}}}$ and $\\frac{{{c}}}{{{d}}}$?"
    return problem, solution


def cube_root(minNo=1, maxNo=1000):
    """Cube Root"""
    b = random.randint(minNo, maxNo)
    a = b**(1 / 3)

    return (f"What is the cube root of: $\\sqrt[3]{{{b}}}=$ to 2 decimal places?", f"${round(a, 2)}$")


def divide_fractions(maxVal=10):
    """Divide Fractions"""
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)

    while (a == b):
        b = random.randint(1, maxVal)

    c = random.randint(1, maxVal)
    d = random.randint(1, maxVal)
    while (c == d):
        d = random.randint(1, maxVal)

    def calculate_gcd(x, y):
        while (y):
            x, y = y, x % y
        return x

    tmp_n = a * d
    tmp_d = b * c

    gcd = calculate_gcd(tmp_n, tmp_d)
    sol_numerator = tmp_n // gcd
    sol_denominator = tmp_d // gcd

    return f'$\\frac{{{a}}}{{{b}}}\\div\\frac{{{c}}}{{{d}}}=$', f'$\\frac{{{sol_numerator}}}{{{sol_denominator}}}$'


def division(maxA=25, maxB=25):
    """Division"""
    a = random.randint(1, maxA)
    b = random.randint(1, maxB)

    divisor = a * b
    dividend = random.choice([a, b])
    quotient = int(divisor / dividend)

    return f'${divisor}\\div{dividend}=$', f'${quotient}$'


def exponentiation(maxBase=20, maxExpo=10):
    """Exponentiation"""
    base = random.randint(1, maxBase)
    expo = random.randint(1, maxExpo)

    return f'${base}^{expo} =$', f'${base**expo}$'


def factorial(maxInput=6):
    """Factorial"""
    a = random.randint(0, maxInput)
    n = a
    b = 1
    while a != 1 and n > 0:
        b *= n
        n -= 1

    return f'${a}! =$', f'${b}$'


def fraction_multiplication(maxVal=10):
    """Fraction Multiplication"""
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    c = random.randint(1, maxVal)
    d = random.randint(1, maxVal)

    while (a == b):
        b = random.randint(1, maxVal)

    while (c == d):
        d = random.randint(1, maxVal)

    def calculate_gcd(x, y):
        while (y):
            x, y = y, x % y
        return x

    tmp_n = a * c
    tmp_d = b * d

    gcd = calculate_gcd(tmp_n, tmp_d)

    problem = f"$\\frac{{{a}}}{{{b}}}\\cdot\\frac{{{c}}}{{{d}}}=$"
    if (tmp_d == 1 or tmp_d == gcd):
        solution = f"$\\frac{{{tmp_n}}}{{{gcd}}}$"
    else:
        solution = f"$\\frac{{{tmp_n//gcd}}}{{{tmp_d//gcd}}}$"
    return problem, solution


def fraction_to_decimal(maxRes=99, maxDivid=99):
    """Fraction to Decimal"""
    a = random.randint(0, maxDivid)
    b = random.randint(1, min(maxRes, maxDivid))
    c = round(a / b, 2)

    return f'${a}\\div{b}=$', f'${c}$'


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


def is_composite(maxNum=250):
    """Is Composite"""
    a = random.randint(2, maxNum)

    problem = f"Is ${a}$ composite?"
    if a == 0 or a == 1:
        return problem, "No"
    for i in range(2, a):
        if a % i == 0:
            return problem, "Yes"
    solution = "No"

    return problem, solution


def is_prime(max_num=100):
    """Is Prime"""
    a = random.randint(2, max_num)
    problem = f"Is ${a}$ prime?"
    if a == 2:
        return problem, "Yes"
    if a % 2 == 0:
        return problem, "No"
    for i in range(3, a // 2 + 1, 2):
        if a % i == 0:
            return problem, "No"
    solution = "Yes"

    return problem, solution


def multiplication(maxMulti=12):
    """Multiplication"""
    a = random.randint(0, maxMulti)
    b = random.randint(0, maxMulti)
    c = a * b

    return f'${a}\\cdot{b}$', f'${c}$'


def percentage(maxValue=99, maxpercentage=99):
    """Percentage of a number"""
    a = random.randint(1, maxpercentage)
    b = random.randint(1, maxValue)
    problem = f"What is ${a}$% of ${b}$?"
    percentage = a / 100 * b
    formatted_float = "{:.2f}".format(percentage)
    solution = f"${formatted_float}$"

    return problem, solution


def percentage_difference(maxValue=200, minValue=0):
    """Percentage difference between two numbers"""
    value_a = random.randint(minValue, maxValue)
    value_b = random.randint(minValue, maxValue)

    diff = 2 * (abs(value_a - value_b) / abs(value_a + value_b)) * 100
    diff = round(diff, 2)

    problem = f"What is the percentage difference between ${value_a}$ and ${value_b}$?"
    solution = f'${diff}$%'
    return problem, solution


def percentage_error(maxValue=100, minValue=-100):
    """Percentage error"""
    observed_value = random.randint(minValue, maxValue)
    exact_value = random.randint(minValue, maxValue)

    if observed_value * exact_value < 0:
        observed_value *= -1

    error = (abs(observed_value - exact_value) / abs(exact_value)) * 100
    error = round(error, 2)

    problem = f"Find the percentage error when observed value equals ${observed_value}$ and exact value equals ${exact_value}$."
    solution = f'${error}\\%$'
    return problem, solution


def power_of_powers(maxBase=50, maxPower=10):
    """Power of Powers"""
    base = random.randint(1, maxBase)
    power1 = random.randint(1, maxPower)
    power2 = random.randint(1, maxPower)
    step = power1 * power2

    problem = f"Simplify ${base}^{{{power1}^{{{power2}}}}}$"
    solution = f"${base}^{{{step}}}$"
    return problem, solution


def square(maxSquareNum=20):
    """Square"""
    a = random.randint(1, maxSquareNum)
    b = a ** 2

    return f'${a}^2=$', f'${b}$'


def square_root(minNo=1, maxNo=12):
    """Square Root"""
    b = random.randint(minNo, maxNo)
    a = b ** 2

    return f'$\\sqrt{{{a}}}=$', f'${b}$'


def subtraction(maxMinuend=99, maxDiff=99):
    """Subtraction of two numbers"""
    a = random.randint(0, maxMinuend)
    b = random.randint(max(0, (a - maxDiff)), a)
    c = a - b

    return f'${a}-{b}=$', f'${c}$'
