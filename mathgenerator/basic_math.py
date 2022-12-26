import random


def absolute_difference(maxA=100, maxB=100):
    r"""Absolute difference between two numbers
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $|22-34|=$ | $12$ |
    """
    a = random.randint(-1 * maxA, maxA)
    b = random.randint(-1 * maxB, maxB)
    absDiff = abs(a - b)

    return f'$|{a}-{b}|=$', f"${absDiff}$"


def addition(maxSum=99, maxAddend=50):
    r"""Addition of two numbers

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $22+34=$ | $56$ |
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
    r"""Compare Fractions
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Which symbol represents the comparison between $\frac{1}{2}$ and $\frac{3}{4}$? | $>$ |
    """
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
    r"""Cube Root
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is the cube root of: $\sqrt[3]{125}=$ to 2 decimal places? | $5$ |
    """
    b = random.randint(minNo, maxNo)
    a = b**(1 / 3)

    return (f"What is the cube root of: $\\sqrt[3]{{{b}}}=$ to 2 decimal places?", f"${round(a, 2)}$")


def divide_fractions(maxVal=10):
    r"""Divide Fractions
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $\frac{7}{9}\div\frac{4}{1}=$ | $\frac{7}{36}$ |
    """
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
    r"""Division
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $216\div24=$ | $9$ |
    """
    a = random.randint(1, maxA)
    b = random.randint(1, maxB)

    divisor = a * b
    dividend = random.choice([a, b])
    quotient = int(divisor / dividend)

    return f'${divisor}\\div{dividend}=$', f'${quotient}$'


def exponentiation(maxBase=20, maxExpo=10):
    r"""Exponentiation
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $9^{5}=$ | $8$ |
    """
    base = random.randint(1, maxBase)
    expo = random.randint(1, maxExpo)

    return f'${base}^{{{expo}}}=$', f'${base**expo}$'


def factorial(maxInput=6):
    r"""Factorial

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $4! =$ | $24$ |
    """
    a = random.randint(0, maxInput)
    n = a
    b = 1
    while a != 1 and n > 0:
        b *= n
        n -= 1

    return f'${a}! =$', f'${b}$'


def fraction_multiplication(maxVal=10):
    r"""Fraction Multiplication
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $\frac{3}{10}\cdot\frac{6}{7}=$ | $\frac{9}{35} |
    """
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
    r"""Fraction to Decimal
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $83\div80=$ | $1.04$ |
    """
    a = random.randint(0, maxDivid)
    b = random.randint(1, min(maxRes, maxDivid))
    c = round(a / b, 2)

    return f'${a}\\div{b}=$', f'${c}$'


def greatest_common_divisor(numbersCount=2, maximalNumberLimit=10**9):
    r"""Greatest Common Divisor of N Numbers
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $GCD(488075608, 75348096)=$ | $8$ |
    """

    def greatestCommonDivisorOfTwoNumbers(number1, number2):
        number1 = abs(number1)
        number2 = abs(number2)
        while number2 > 0:
            number1, number2 = number2, number1 % number2
        return number1

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
    r"""Is Composite
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Is $171$ composite? | Yes |
    """
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
    r"""Is Prime
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Is $37$ prime? | Yes |
    """
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
    r"""Multiplication
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $10\cdot9=$ | $90$ |
    """
    a = random.randint(0, maxMulti)
    b = random.randint(0, maxMulti)
    c = a * b

    return f'${a}\\cdot{b}=$', f'${c}$'


def percentage(maxValue=99, maxpercentage=99):
    r"""Percentage of a number
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is $45$% of $39$? | $17.55$ |
    """
    a = random.randint(1, maxpercentage)
    b = random.randint(1, maxValue)
    problem = f"What is ${a}$% of ${b}$?"
    percentage = a / 100 * b
    formatted_float = "{:.2f}".format(percentage)
    solution = f"${formatted_float}$"

    return problem, solution


def percentage_difference(maxValue=200, minValue=0):
    r"""Percentage difference between two numbers
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is the percentage difference between $2$ and $10$? | $133.33$ |
    """
    value_a = random.randint(minValue, maxValue)
    value_b = random.randint(minValue, maxValue)

    diff = 2 * (abs(value_a - value_b) / abs(value_a + value_b)) * 100
    diff = round(diff, 2)

    problem = f"What is the percentage difference between ${value_a}$ and ${value_b}$?"
    solution = f'${diff}$%'
    return problem, solution


def percentage_error(maxValue=100, minValue=-100):
    r"""Percentage error
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the percentage error when observed value equals $32$ and exact value equals $81$. | $60.49$% |
    """
    observed_value = random.randint(minValue, maxValue)
    exact_value = random.randint(minValue, maxValue)

    if observed_value * exact_value < 0:
        observed_value *= -1

    error = (abs(observed_value - exact_value) / abs(exact_value)) * 100
    error = round(error, 2)

    problem = f"Find the percentage error when observed value equals ${observed_value}$ and exact value equals ${exact_value}$."
    solution = f'${error}$%'
    return problem, solution


def power_of_powers(maxBase=50, maxPower=10):
    r"""Power of Powers
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Simplify $18^{10^{8}}$ | $18^{80}$ |
    """
    base = random.randint(1, maxBase)
    power1 = random.randint(1, maxPower)
    power2 = random.randint(1, maxPower)
    step = power1 * power2

    problem = f"Simplify ${base}^{{{power1}^{{{power2}}}}}$"
    solution = f"${base}^{{{step}}}$"
    return problem, solution


def square(maxSquareNum=20):
    r"""Square
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $17^2=$ | $289$ |
    """
    a = random.randint(1, maxSquareNum)
    b = a ** 2

    return f'${a}^2=$', f'${b}$'


def square_root(minNo=1, maxNo=12):
    r"""Square Root
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $\sqrt{64}=$ | $8$ |
    """
    b = random.randint(minNo, maxNo)
    a = b ** 2

    return f'$\\sqrt{{{a}}}=$', f'${b}$'


def subtraction(maxMinuend=99, maxDiff=99):
    r"""Subtraction of two numbers
    
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $54-22=$ | $32$ |
    """
    a = random.randint(0, maxMinuend)
    b = random.randint(max(0, (a - maxDiff)), a)
    c = a - b

    return f'${a}-{b}=$', f'${c}$'
