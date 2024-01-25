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
    a3 = a2 + d
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
    a = x = random.randint(1, max_val)
    b = y = random.randint(1, max_val)

    if (x < y):
        min = x
    else:
        min = y

    count = 0
    arr = []

    for i in range(1, min + 1):
        if (x % i == 0):
            if (y % i == 0):
                count = count + 1
                arr.append(i)

    problem = f"Common Factors of ${a}$ and ${b} = $"
    solution = f'${arr}$'
    return problem, solution


def complex_to_polar(min_real_imaginary_num=-20, max_real_imaginary_num=20):
    r"""Complex to polar form

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $19.42(-19.0\theta + i-4.0\theta)$ | $-2.93$ |
    """
    num = complex(
        random.randint(min_real_imaginary_num, max_real_imaginary_num),
        random.randint(min_real_imaginary_num, max_real_imaginary_num))
    a = num.real
    b = num.imag
    r = round(math.hypot(a, b), 2)
    theta = round(math.atan2(b, a), 2)

    problem = rf'${r}({a}\theta + i{b}\theta)$'
    return problem, f'${theta}$'


def decimal_to_roman_numerals(max_decimal=4000):
    """Decimal to Roman Numerals

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | The number $92$ in roman numerals is:  | $XCII$ |
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


def euclidian_norm(maxEltAmt=20):
    """Euclidian norm or L2 norm of a vector

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Euclidian norm or L2 norm of the vector $[659.9225071540442, 243.40887829281564, 128.79950053874424, 263.19226900031344]$ is: | $761.97$ |
    """
    vec = [
        random.uniform(0, 1000) for i in range(random.randint(2, maxEltAmt))
    ]
    solution = round(math.sqrt(sum([i**2 for i in vec])), 2)

    problem = f"Euclidian norm or L2 norm of the vector ${vec}$ is:"
    return problem, f'${solution}$'


def factors(max_val=1000):
    """Factors of a number

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Factors of $176 = $ | $[1, 2, 4, 8, 11, 16, 22, 44, 88, 176]$ |
    """
    n = random.randint(1, max_val)

    factors = []

    for i in range(1, int(n**0.5) + 1):
        if i**2 == n:
            factors.append(i)
        elif n % i == 0:
            factors.append(i)
            factors.append(n // i)
        else:
            pass

    factors.sort()

    problem = f"Factors of ${n} = $"
    solution = factors
    return problem, f'${solution}$'


def geometric_mean(max_value=100, max_count=4):
    """Geometric Mean of N Numbers

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Geometric mean of $3$ numbers $[72, 21, 87] = $ | $50.86$ |
    """
    count = random.randint(2, max_count)
    nums = [random.randint(1, max_value) for i in range(count)]
    product = np.prod(nums)

    ans = round(product**(1 / count), 2)
    problem = f"Geometric mean of ${count}$ numbers ${nums} = $"
    # solution = rf"$({'*'.join(map(str, nums))}^{{\frac{{1}}{{{count}}}}} = {ans}$"
    solution = f"${ans}$"
    return problem, solution


def geometric_progression(number_values=6,
                          min_value=2,
                          max_value=12,
                          n_term=7,
                          sum_term=5):
    """Geometric Progression

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | For the given GP $[11, 44, 176, 704, 2816, 11264]$. Find the value of a common ratio, 7th term value, sum upto 10th term | The value of a is $11$, common ratio is $4$ , 7th term is $45056$, sum upto 10th term is $3844775.0$ |
    """
    r = random.randint(min_value, max_value)
    a = random.randint(min_value, max_value)
    n_term = random.randint(number_values, number_values + 5)
    sum_term = random.randint(number_values, number_values + 5)
    GP = []
    for i in range(number_values):
        GP.append(a * (r**i))
    value_nth_term = a * (r**(n_term - 1))
    sum_till_nth_term = a * ((r**sum_term - 1) / (r - 1))

    problem = f"For the given GP ${GP}$. Find the value of a common ratio, {n_term}th term value, sum upto {sum_term}th term"
    solution = "The value of a is ${}$, common ratio is ${}$ , {}th term is ${}$, sum upto {}th term is ${}$".format(
        a, r, n_term, value_nth_term, sum_term, sum_till_nth_term)
    return problem, solution


def harmonic_mean(max_value=100, max_count=4):
    """Harmonic Mean of N Numbers

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Harmonic mean of $4$ numbers $52, 56, 25, 57 = $ | $602.33$ |
    """
    count = random.randint(2, max_count)
    nums = [random.randint(1, max_value) for _ in range(count)]
    sum = 0
    for num in nums:
        sum += (1 / num)
    ans = round(num / sum, 2)

    problem = f"Harmonic mean of ${count}$ numbers ${', '.join(map(str, nums))} = $"
    solution = f"${ans}$"
    return problem, solution


def is_leap_year(minNumber=1900, max_number=2099):
    """Is Leap Year or Not

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Is $2000$ a leap year? | $2000$ is a leap year |
    """
    year = random.randint(minNumber, max_number)
    problem = f"Is {year} a leap year?"
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                ans = True
            else:
                ans = False
        else:
            ans = True
    else:
        ans = False

    solution = f"{year} is{' not' if not ans else ''} a leap year"
    return problem, solution


def lcm(max_val=20):
    """LCM (Least Common Multiple)

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | LCM of $3$ and $18 = $ | $18$ |
    """
    a = random.randint(1, max_val)
    b = random.randint(1, max_val)
    c = a * b
    x, y = a, b

    while y:
        x, y = y, x % y
    d = c // x

    problem = f"LCM of ${a}$ and ${b} =$"
    solution = f'${d}$'
    return problem, solution


def minutes_to_hours(max_minutes=999):
    """Convert minutes to hours and minutes

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Convert $836$ minutes to hours & minutes | $13$ hours and $56$ minutes |
    """
    minutes = random.randint(1, max_minutes)
    ansHours = minutes // 60
    ansMinutes = minutes % 60

    problem = f"Convert ${minutes}$ minutes to hours & minutes"
    solution = f"${ansHours}$ hours and ${ansMinutes}$ minutes"
    return problem, solution


def prime_factors(min_val=1, max_val=200):
    """Prime Factors

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find prime factors of $30$ | $2, 3, 5$ |
    """
    a = random.randint(min_val, max_val)
    n = a
    i = 2
    factors = []

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    problem = f"Find prime factors of ${a}$"
    solution = f"${', '.join(map(str, factors))}$"
    return problem, solution


def product_of_scientific_notations(min_exp_val=-100, max_exp_val=100):
    r"""Product of scientific notations

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Product of scientific notations $5.11 \times 10^{67}$ and $3.64 \times 10^{-59} = $ | $1.86 \times 10^{9}$ |
    """
    a = [
        round(random.uniform(1, 10), 2),
        random.randint(min_exp_val, max_exp_val)
    ]
    b = [
        round(random.uniform(1, 10), 2),
        random.randint(min_exp_val, max_exp_val)
    ]
    c = [a[0] * b[0], a[1] + b[1]]

    if c[0] >= 10:
        c[0] /= 10
        c[1] += 1

    problem = rf"Product of scientific notations ${a[0]} \times 10^{{{a[1]}}}$ and ${b[0]} \times 10^{{{b[1]}}} = $"
    solution = rf'${round(c[0], 2)} \times 10^{{{c[1]}}}$'
    return problem, solution


def profit_loss_percent(max_cp=1000, max_sp=1000):
    """Profit or Loss Percent

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Loss percent when $CP = 751$ and $SP = 290$ is: | $61.38$ |
    """
    cP = random.randint(1, max_cp)
    sP = random.randint(1, max_sp)
    diff = abs(sP - cP)
    if (sP - cP >= 0):
        profitOrLoss = "Profit"
    else:
        profitOrLoss = "Loss"
    percent = round(diff / cP * 100, 2)

    problem = f"{profitOrLoss} percent when $CP = {cP}$ and $SP = {sP}$ is: "
    return problem, f'${percent}$'


def quotient_of_power_same_base(max_base=50, max_power=10):
    """Quotient of Powers with Same Base

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | The Quotient of $5^{6}$ and $5^{8} = 5^{6-8} = 5^{-2}$ | $0.04$ |
    """
    base = random.randint(1, max_base)
    power1 = random.randint(1, max_power)
    power2 = random.randint(1, max_power)
    step = power1 - power2
    solution = base**step

    problem = f"The Quotient of ${base}^{{{power1}}}$ and ${base}^{{{power2}}} = " \
        f"{base}^{{{power1}-{power2}}} = {base}^{{{step}}}$"
    return problem, f'{solution}'


def quotient_of_power_same_power(max_base=50, max_power=10):
    """Quotient of Powers with Same Power

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | The quotient of $19^{8}$ and $10^{8} = (19/10)^8 = 1.9^{8}$ | $169.84$ |
    """
    base1 = random.randint(1, max_base)
    base2 = random.randint(1, max_base)
    power = random.randint(1, max_power)
    step = base1 / base2
    solution = round(step**power, 2)

    problem = f"The quotient of ${base1}^{{{power}}}$ and ${base2}^{{{power}}} = " \
        f"({base1}/{base2})^{power} = {step}^{{{power}}}$"
    return problem, f'{solution}'


def set_operation(min_size=3, max_size=7):
    """Union, Intersection, Difference of Two Sets

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Given the two sets $a={1, 2, 4, 5}$, $b={8, 1, 2}$. Find the Union, intersection, $a-b$, $b-a$, and symmetric difference | Union is ${1, 2, 4, 5, 8}$. Intersection is ${1, 2}$, $a-b$ is ${4, 5}$, $b-a$ is ${8}$. Symmetric difference is ${4, 5, 8}$. |
    """
    number_variables_a = random.randint(min_size, max_size)
    number_variables_b = random.randint(min_size, max_size)
    a = []
    b = []
    for _ in range(number_variables_a):
        a.append(random.randint(1, 10))
    for _ in range(number_variables_b):
        b.append(random.randint(1, 10))
    a = set(a)
    b = set(b)

    problem = f"Given the two sets $a={a}$, $b={b}$. " + \
        "Find the Union, intersection, $a-b$, $b-a$, and symmetric difference"
    solution = f"Union is ${a.union(b)}$. Intersection is ${a.intersection(b)}$" + \
        f", $a-b$ is ${a.difference(b)}$, $b-a$ is ${b.difference(a)}$." + \
        f" Symmetric difference is ${a.symmetric_difference(b)}$."
    return problem, solution


def signum_function(min=-999, max=999):
    """Signum Function

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Signum of $-229$ is = | $-1$ |
    """
    a = random.randint(min, max)
    b = 0
    if (a > 0):
        b = 1
    if (a < 0):
        b = -1

    problem = f"Signum of ${a}$ is ="
    solution = f'{b}'
    return problem, solution


def surds_comparison(max_value=100, max_root=10):
    r"""Comparing Surds

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Fill in the blanks $42^{\frac{1}{2}}$ _ $45^{\frac{1}{5}}$ | $>$ |
    """
    radicand1, radicand2 = tuple(random.sample(range(1, max_value), 2))
    degree1, degree2 = tuple(random.sample(range(1, max_root), 2))
    first = math.pow(radicand1, 1 / degree1)
    second = math.pow(radicand2, 1 / degree2)

    solution = "="
    if first > second:
        solution = ">"
    elif first < second:
        solution = "<"

    problem = rf"Fill in the blanks ${radicand1}^{{\frac{{1}}{{{degree1}}}}}$ _ ${radicand2}^{{\frac{{1}}{{{degree2}}}}}$"
    return problem, f'${solution}$'


def velocity_of_object(max_displacement=1000, max_time=100):
    """Velocity of object

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | An object travels at uniform velocity a distance of $100 m$ in $4$ seconds. What is the velocity of the car? | $25 m/s$ |
    """

    displacement = random.randint(1, max_displacement)
    time_taken = random.randint(1, max_time)
    velocity = "${} m/s$".format(round(displacement / time_taken, 2))

    problem = f"An object travels at uniform velocity a distance of ${displacement} m$ in ${time_taken}$ seconds. What is the velocity of the car? "
    return problem, velocity
