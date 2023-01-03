import random


def absolute_difference(max_a=100, max_b=100):
    r"""Absolute difference between two numbers

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $|22-34|=$ | $12$ |
    """
    a = random.randint(-1 * max_a, max_a)
    b = random.randint(-1 * max_b, max_b)
    absDiff = abs(a - b)

    return f'$|{a}-{b}|=$', f"${absDiff}$"


def addition(max_sum=99, max_addend=50):
    r"""Addition of two numbers

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $22+34=$ | $56$ |
    """
    if max_addend > max_sum:
        max_addend = max_sum
    a = random.randint(0, max_addend)
    # The highest value of b will be no higher than the max_sum minus the first number and no higher than the max_addend as well
    b = random.randint(0, min((max_sum - a), max_addend))
    c = a + b

    problem = f'${a}+{b}=$'
    solution = f'${c}$'
    return problem, solution


def compare_fractions(max_val=10):
    r"""Compare Fractions

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Which symbol represents the comparison between $\frac{1}{2}$ and $\frac{3}{4}$? | $>$ |
    """
    a = random.randint(1, max_val)
    b = random.randint(1, max_val)
    c = random.randint(1, max_val)
    d = random.randint(1, max_val)

    while (a == b):
        b = random.randint(1, max_val)
    while (c == d):
        d = random.randint(1, max_val)

    first = a / b
    second = c / d

    if (first > second):
        solution = ">"
    elif (first < second):
        solution = "<"
    else:
        solution = "="

    problem = rf"Which symbol represents the comparison between $\frac{{{a}}}{{{b}}}$ and $\frac{{{c}}}{{{d}}}$?"
    return problem, solution


def cube_root(min_no=1, max_no=1000):
    r"""Cube Root

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is the cube root of: $\sqrt[3]{125}=$ to 2 decimal places? | $5$ |
    """
    b = random.randint(min_no, max_no)
    a = b**(1 / 3)

    return (rf"What is the cube root of: $\sqrt[3]{{{b}}}=$ to 2 decimal places?", f"${round(a, 2)}$")


def divide_fractions(max_val=10):
    r"""Divide Fractions

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $\frac{7}{9}\div\frac{4}{1}=$ | $\frac{7}{36}$ |
    """
    a = random.randint(1, max_val)
    b = random.randint(1, max_val)

    while (a == b):
        b = random.randint(1, max_val)

    c = random.randint(1, max_val)
    d = random.randint(1, max_val)
    while (c == d):
        d = random.randint(1, max_val)

    def calculate_gcd(x, y):
        while (y):
            x, y = y, x % y
        return x

    tmp_n = a * d
    tmp_d = b * c

    gcd = calculate_gcd(tmp_n, tmp_d)
    sol_numerator = tmp_n // gcd
    sol_denominator = tmp_d // gcd

    return rf'$\frac{{{a}}}{{{b}}}\div\frac{{{c}}}{{{d}}}=$', f'$\frac{{{sol_numerator}}}{{{sol_denominator}}}$'


def division(max_a=25, max_b=25):
    r"""Division

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $216\div24=$ | $9$ |
    """
    a = random.randint(1, max_a)
    b = random.randint(1, max_b)

    divisor = a * b
    dividend = random.choice([a, b])
    quotient = int(divisor / dividend)

    return rf'${divisor}\div{dividend}=$', f'${quotient}$'


def exponentiation(max_base=20, max_expo=10):
    r"""Exponentiation

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $9^{5}=$ | $8$ |
    """
    base = random.randint(1, max_base)
    expo = random.randint(1, max_expo)

    return f'${base}^{{{expo}}}=$', f'${base**expo}$'


def factorial(max_input=6):
    r"""Factorial

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $4! =$ | $24$ |
    """
    a = random.randint(0, max_input)
    n = a
    b = 1
    while a != 1 and n > 0:
        b *= n
        n -= 1

    return f'${a}! =$', f'${b}$'


def fraction_multiplication(max_val=10):
    r"""Fraction Multiplication

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $\frac{3}{10}\cdot\frac{6}{7}=$ | $\frac{9}{35}$ |
    """
    a = random.randint(1, max_val)
    b = random.randint(1, max_val)
    c = random.randint(1, max_val)
    d = random.randint(1, max_val)

    while (a == b):
        b = random.randint(1, max_val)

    while (c == d):
        d = random.randint(1, max_val)

    def calculate_gcd(x, y):
        while (y):
            x, y = y, x % y
        return x

    tmp_n = a * c
    tmp_d = b * d

    gcd = calculate_gcd(tmp_n, tmp_d)

    problem = rf"$\frac{{{a}}}{{{b}}}\cdot\frac{{{c}}}{{{d}}}=$"
    if (tmp_d == 1 or tmp_d == gcd):
        solution = rf"$\frac{{{tmp_n}}}{{{gcd}}}$"
    else:
        solution = rf"$\frac{{{tmp_n//gcd}}}{{{tmp_d//gcd}}}$"
    return problem, solution


def fraction_to_decimal(max_res=99, max_divid=99):
    r"""Fraction to Decimal

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $83\div80=$ | $1.04$ |
    """
    a = random.randint(0, max_divid)
    b = random.randint(1, min(max_res, max_divid))
    c = round(a / b, 2)

    return rf'${a}\div{b}=$', f'${c}$'


def greatest_common_divisor(numbers_count=2, max_num=10**3):
    r"""Greatest Common Divisor of N Numbers ( GCD / HCF )

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

    numbers_count = max(numbers_count, 2)
    numbers = [random.randint(0, max_num)
               for _ in range(numbers_count)]

    greatestCommonDivisor = greatestCommonDivisorOfTwoNumbers(
        numbers[0], numbers[1])

    for index in range(1, numbers_count):
        greatestCommonDivisor = greatestCommonDivisorOfTwoNumbers(
            numbers[index], greatestCommonDivisor)

    return f'$GCD({",".join(map(str, numbers))})=$', f"${greatestCommonDivisor}$"


def is_composite(max_num=250):
    r"""Is Composite

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Is $171$ composite? | Yes |
    """
    a = random.randint(2, max_num)

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


def multiplication(max_multi=12):
    r"""Multiplication

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $10\cdot9=$ | $90$ |
    """
    a = random.randint(0, max_multi)
    b = random.randint(0, max_multi)
    c = a * b

    return rf'${a}\cdot{b}=$', f'${c}$'


def percentage(max_value=99, max_percentage=99):
    r"""Percentage of a number

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is $45$% of $39$? | $17.55$ |
    """
    a = random.randint(1, max_percentage)
    b = random.randint(1, max_value)
    problem = f"What is ${a}$% of ${b}$?"
    percentage = a / 100 * b
    formatted_float = "{:.2f}".format(percentage)
    solution = f"${formatted_float}$"

    return problem, solution


def percentage_difference(max_value=200, min_value=0):
    r"""Percentage difference between two numbers

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is the percentage difference between $2$ and $10$? | $133.33$ |
    """
    value_a = random.randint(min_value, max_value)
    value_b = random.randint(min_value, max_value)

    diff = 2 * (abs(value_a - value_b) / abs(value_a + value_b)) * 100
    diff = round(diff, 2)

    problem = f"What is the percentage difference between ${value_a}$ and ${value_b}$?"
    solution = f'${diff}$%'
    return problem, solution


def percentage_error(max_value=100, min_value=-100):
    r"""Percentage error

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the percentage error when observed value equals $32$ and exact value equals $81$. | $60.49$% |
    """
    observed_value = random.randint(min_value, max_value)
    exact_value = random.randint(min_value, max_value)

    if observed_value * exact_value < 0:
        observed_value *= -1

    error = (abs(observed_value - exact_value) / abs(exact_value)) * 100
    error = round(error, 2)

    problem = f"Find the percentage error when observed value equals ${observed_value}$ and exact value equals ${exact_value}$."
    solution = f'${error}$%'
    return problem, solution


def power_of_powers(max_base=50, max_power=10):
    r"""Power of Powers

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Simplify $18^{10^{8}}$ | $18^{80}$ |
    """
    base = random.randint(1, max_base)
    power1 = random.randint(1, max_power)
    power2 = random.randint(1, max_power)
    step = power1 * power2

    problem = f"Simplify ${base}^{{{power1}^{{{power2}}}}}$"
    solution = f"${base}^{{{step}}}$"
    return problem, solution


def square(max_square_num=20):
    r"""Square

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $17^2=$ | $289$ |
    """
    a = random.randint(1, max_square_num)
    b = a ** 2

    return f'${a}^2=$', f'${b}$'


def square_root(min_no=1, max_no=12):
    r"""Square Root

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $\sqrt{64}=$ | $8$ |
    """
    b = random.randint(min_no, max_no)
    a = b ** 2

    return rf'$\sqrt{{{a}}}=$', f'${b}$'


def simplify_square_root(max_variable=100):
    r"""Simplify Square Root

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $\sqrt{63}$ | $3\sqrt{7}$ |
    """
    y = x = random.randint(1, max_variable)
    factors = {}
    f = 2
    while x != 1:
        if x % f == 0:
            if f not in factors:
                factors[f] = 0
            factors[f] += 1
            x /= f
        else:
            f += 1
    a = b = 1
    for i in factors.keys():
        if factors[i] & 1 == 0:
            a *= i ** (factors[i] // 2)
        else:
            a *= i ** ((factors[i] - 1) // 2)
            b *= i
    if a == 1 or b == 1:
        return simplify_square_root(max_variable)
    else:
        return rf'$\sqrt{{{y}}}$', rf'${a}\sqrt{{{b}}}$'


def subtraction(max_minuend=99, max_diff=99):
    r"""Subtraction of two numbers

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $54-22=$ | $32$ |
    """
    a = random.randint(0, max_minuend)
    b = random.randint(max(0, (a - max_diff)), a)
    c = a - b

    return f'${a}-{b}=$', f'${c}$'
