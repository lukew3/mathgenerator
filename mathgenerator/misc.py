import random
import math
import numpy as np

def arithmetic_progression_sum(max_d=100, max_a=100, max_n=100):
    """Arithmetic Progression Sum
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the sum of first $44$ terms of the AP series: $49, 145, 241 ... $ | $92972.0$ |
    """
    d = random.randint(-1 * max_d, max_d)
    a1 = random.randint(-1 * max_a, max_a)
    a2 = a1 + d
    a3 = a1 + 2 * d
    n = random.randint(4, max_n)
    apString = str(a1) + ', ' + str(a2) + ', ' + str(a3) + ' ... '
    an = a1 + (n - 1) * d
    solution = n * (a1 + an) / 2

    problem = f'Find the sum of first ${n}$ terms of the AP series: ${apString}$'
    return problem, f'${solution}$'


def arithmetic_progression_term(max_d=100, max_a=100, max_n=100):
    """Arithmetic Progression Term
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find term number $12$ of the AP series: $-54, 24, 102 ... $ | $804$ |
    """
    d = random.randint(-1 * max_d, max_d)
    a1 = random.randint(-1 * max_a, max_a)
    a2 = a1 + d
    a3 = a1 + 2 * d
    n = random.randint(4, max_n)
    apString = str(a1) + ', ' + str(a2) + ', ' + str(a3) + ' ... '
    solution = a1 + ((n - 1) * d)

    problem = f'Find term number ${n}$ of the AP series: ${apString}$'
    return problem, f'${solution}$'


def _fromBaseTenTo(n, to_base):
    """Converts a decimal number n to another base, to_base.
    Utility of base_conversion()
    """
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert type(
        to_base
    ) == int and to_base >= 2 and to_base <= 36, "to_base({}) must be >=2 and <=36"
    # trivial cases
    if to_base == 2:
        return bin(n)[2:]
    elif to_base == 8:
        return oct(n)[2:]
    elif to_base == 10:
        return str(n)
    elif to_base == 16:
        return hex(n)[2:].upper()
    res = alpha[n % to_base]
    n = n // to_base
    while n > 0:
        res = alpha[n % to_base] + res
        n = n // to_base
    return res


def base_conversion(max_num=60000, max_base=16):
    """Base Conversion
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Convert $45204$ from base $10$ to base $4$ | $23002110$ |
    """
    assert type(
        max_num
    ) == int and max_num >= 100 and max_num <= 65536, "max_num({}) must be >=100 and <=65536".format(
        max_num)
    assert type(
        max_base
    ) == int and max_base >= 2 and max_base <= 36, "max_base({}) must be >= 2 and <=36".format(
        max_base)

    n = random.randint(40, max_num)
    dist = [10] * 10 + [2] * 5 + [16] * 5 + [i for i in range(2, max_base + 1)]
    # set this way since converting to/from bases 2,10,16 are more common -- can be changed if needed.
    bases = random.choices(dist, k=2)
    while bases[0] == bases[1]:
        bases = random.choices(dist, k=2)

    problem = f"Convert ${_fromBaseTenTo(n, bases[0])}$ from base ${bases[0]}$ to base ${bases[1]}$."
    ans = _fromBaseTenTo(n, bases[1])
    return problem, f'${ans}$'


def _newton_symbol(n, k):
    """Utility of binomial_distribution()"""
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def binomial_distribution():
    """Binomial distribution
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | A manufacturer of metal pistons finds that, on average, $30.56$% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of $20$ pistons will contain no more than $2$ rejected pistons? | $3.17$ |
    """
    rejected_fraction = float(random.randint(30, 40)) + random.random()
    batch = random.randint(10, 20)
    rejections = random.randint(1, 9)

    answer = 0
    rejected_fraction = round(rejected_fraction, 2)
    for i in range(0, rejections + 1):
        answer += _newton_symbol(float(batch), float(i)) * ((rejected_fraction / 100.) ** float(i)) * \
            ((1 - (rejected_fraction / 100.)) ** (float(batch) - float(i)))

    answer = round(100 * answer, 2)

    problem = "A manufacturer of metal pistons finds that, on average, ${0:}$% "\
        "of the pistons they manufacture are rejected because " \
        "they are incorrectly sized. What is the probability that a "\
        "batch of ${1:}$ pistons will contain no more than ${2:}$ " \
        "rejected pistons?".format(rejected_fraction, batch, rejections)
    return problem, f'${answer}$'


def celsius_to_fahrenheit(max_temp=100):
    """Celsius to Fahrenheit
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Convert $-46$ degrees Celsius to degrees Fahrenheit | $-50.8$ |
    """
    celsius = random.randint(-50, max_temp)
    fahrenheit = (celsius * (9 / 5)) + 32

    problem = f"Convert ${celsius}$ degrees Celsius to degrees Fahrenheit"
    solution = f'${fahrenheit}$'
    return problem, solution


def common_factors(max_val=100):
    """Common Factors
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Common Factors of $100$ and $44 = $ | $[1, 2, 4]$ |
    """
    a = random.randint(1, max_val)
    b = random.randint(1, max_val)
    factors = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]

    problem = f"Common Factors of ${a}$ and ${b} = $"
    solution = f'${factors}$'
    return problem, solution


def complex_to_polar(min_real_imaginary_num=-20, max_real_imaginary_num=20):
    """Complex to polar form
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Convert $-12 + 5i$ to polar form | $13.0 \text{cis}(\arctan(-5/12))$ |
    """
    real_part = random.randint(min_real_imaginary_num, max_real_imaginary_num)
    imaginary_part = random.randint(min_real_imaginary_num, max_real_imaginary_num)

    r = math.sqrt(real_part**2 + imaginary_part**2)
    theta = math.degrees(math.atan2(imaginary_part, real_part))

    problem = f"Convert ${real_part} + {imaginary_part}i$ to polar form"
    solution = f'${r:.1f} \\text{{cis}}({theta:.1f})$'
    return problem, solution


def decimal_to_roman_numerals(max_decimal=4000):
    """Decimal to Roman Numerals
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Convert $2732$ to Roman numerals | $MMDCCXXXII$ |
    """
    x = random.randint(0, max_decimal)
    x_copy = x
    roman_dict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }
    div = 1
    while x >= div:
        div *= 10
    div /= 10
    solution = ""
    while x:
        last_value = int(x / div)
        if last_value <= 3:
            solution += (roman_dict[div] * last_value)
        elif last_value == 4:
            solution += (roman_dict[div] + roman_dict[div * 5])
        elif 5 <= last_value <= 8:
            solution += (roman_dict[div * 5] + (roman_dict[div] * (last_value - 5)))
        elif last_value == 9:
            solution += (roman_dict[div] + roman_dict[div * 10])
        x = math.floor(x % div)
        div /= 10

    problem = f"The number ${x_copy}$ in roman numerals is: "
    return problem, f'${solution}$'

def decimal_to_binary_octal_hex(max_decimal=1000):
    """Decimal to Binary, Octal, Hexadecimal
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Convert $278$ to binary, octal, and hexadecimal | $(100010010)_2, (422)_8, (116)_16$ |
    """
    num = random.randint(1, max_decimal)
    binary = bin(num)[2:]
    octal = oct(num)[2:]
    hexadecimal = hex(num)[2:]

    problem = f"Convert ${num}$ to binary, octal, and hexadecimal"
    solution = f"$({binary})_2, ({octal})_8, ({hexadecimal})_{16}$"
    return problem, solution


def decimal_to_binary(max_decimal=1000):
    """Decimal to Binary
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Convert $243$ to binary | $11110011_2$ |
    """
    num = random.randint(1, max_decimal)
    binary = bin(num)[2:]

    problem = f"Convert ${num}$ to binary"
    solution = f"${binary}_2$"
    return problem, solution


def discriminant(max_a=10, max_c=10):
    """Discriminant of a Quadratic Equation
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the discriminant of $3x^2 + 5x + 2 = 0$ | $41$ |
    """
    a = random.randint(1, max_a)
    b = random.randint(-1 * max_c, max_c)
    c = random.randint(-1 * max_c, max_c)
    while b**2 - 4 * a * c < 0:  # Ensure the discriminant is non-negative
        a = random.randint(1, max_a)
        b = random.randint(-1 * max_c, max_c)
        c = random.randint(-1 * max_c, max_c)

    problem = f"Find the discriminant of ${a}x^2 + {b}x + {c} = 0$"
    solution = f"${b**2 - 4*a*c}$"
    return problem, solution


def exponential_growth_decay(max_rate=0.1, max_time=10):
    """Exponential Growth/Decay
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | A population grows at a rate of $8$% per year. If the current population is $500$, find the population after $6$ years. | $725.63$ |
    """
    rate = random.uniform(0.01, max_rate)
    time = random.randint(1, max_time)
    initial_population = random.randint(100, 1000)

    final_population = initial_population * math.exp(rate * time)

    problem = f"A population grows at a rate of ${rate*100}$% per year. If the current population is ${initial_population}$, find the population after ${time}$ years."
    solution = f"${final_population:.2f}$"
    return problem, solution


def factorial(max_n=10):
    """Factorial
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find $8!$ | $40320$ |
    """
    n = random.randint(1, max_n)
    fact_n = math.factorial(n)

    problem = f"Find ${n}!$"
    solution = f"${fact_n}$"
    return problem, solution


def geometric_progression_term(max_ratio=5, max_a=100, max_n=10):
    """Geometric Progression Term
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find term number $7$ of the GP series: $-2, 4, -8 ...$ | $-64$ |
    """
    ratio = random.uniform(0.1, max_ratio)
    a1 = random.randint(-1 * max_a, max_a)
    n = random.randint(1, max_n)
    gpString = str(a1) + ', ' + str(a1 * ratio) + ', ' + str(a1 * ratio**2) + ' ... '
    solution = a1 * ratio**(n - 1)

    problem = f'Find term number ${n}$ of the GP series: ${gpString}$'
    return problem, f'${solution}$'


def geometric_progression_sum(max_ratio=5, max_a=100, max_n=10):
    """Geometric Progression Sum
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the sum of first $5$ terms of the GP series: $3, -6, 12 ...$ | $3.875$ |
    """
    ratio = random.uniform(0.1, max_ratio)
    a1 = random.randint(-1 * max_a, max_a)
    n = random.randint(1, max_n)
    gpString = str(a1) + ', ' + str(a1 * ratio) + ', ' + str(a1 * ratio**2) + ' ... '
    an = a1 * ratio**(n - 1)
    if ratio == 1:
        solution = n * a1
    else:
        solution = a1 * (1 - ratio**n) / (1 - ratio)

    problem = f'Find the sum of first ${n}$ terms of the GP series: ${gpString}$'
    return problem, f'${solution:.3f}$'


def greatest_common_divisor(max_val=100):
    """Greatest Common Divisor (GCD)
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the GCD of $48$ and $60$ | $12$ |
    """
    a = random.randint(1, max_val)
    b = random.randint(1, max_val)
    gcd = math.gcd(a, b)

    problem = f"Find the GCD of ${a}$ and ${b}$"
    solution = f"${gcd}$"
    return problem, solution


def greatest_common_factorization(max_val=100):
    """Greatest Common Factorization
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Express $36$ as the product of its prime factors | $2^2 \\times 3^2$ |
    """
    num = random.randint(1, max_val)
    factors = []

    i = 2
    while i <= num:
        if num % i == 0:
            factors.append(i)
            num = num / i
        else:
            i = i + 1

    prime_factors = [
        f'{factor}^{factors.count(factor)}' for factor in set(factors)
    ]

    problem = f"Express ${num}$ as the product of its prime factors"
    solution = f"${' \\times '.join(prime_factors)}$"
    return problem, solution


