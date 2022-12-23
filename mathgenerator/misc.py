import random


def arithmetic_progression_sum(maxd=100,
                               maxa=100,
                               maxn=100):
    """Arithmetic Progression Sum"""
    d = random.randint(-1 * maxd, maxd)
    a1 = random.randint(-1 * maxa, maxa)
    a2 = a1 + d
    a3 = a1 + 2 * d
    n = random.randint(4, maxn)
    apString = str(a1) + ', ' + str(a2) + ', ' + str(a3) + ' ... '
    an = a1 + (n - 1) * d
    solution = n * (a1 + an) / 2

    problem = f'Find the sum of first ${n}$ terms of the AP series: ${apString}$'
    return problem, f'${solution}$'

import random


def arithmetic_progression_term(maxd=100,
                                maxa=100,
                                maxn=100):
    """Arithmetic Progression Term"""
    d = random.randint(-1 * maxd, maxd)
    a1 = random.randint(-1 * maxa, maxa)
    a2 = a1 + d
    a3 = a2 + d
    n = random.randint(4, maxn)
    apString = str(a1) + ', ' + str(a2) + ', ' + str(a3) + ' ... '
    solution = a1 + ((n - 1) * d)

    problem = f'Find term number ${n}$ of the AP series: ${apString}$'
    return problem, f'${solution}$'

import random


# base from 2 to 36
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def fromBaseTenTo(n, toBase):
    assert type(
        toBase
    ) == int and toBase >= 2 and toBase <= 36, "toBase({}) must be >=2 and <=36"
    # trivial cases
    if toBase == 2:
        return bin(n)[2:]
    elif toBase == 8:
        return oct(n)[2:]
    elif toBase == 10:
        return str(n)
    elif toBase == 16:
        return hex(n)[2:].upper()
    res = alpha[n % toBase]
    n = n // toBase
    while n > 0:
        res = alpha[n % toBase] + res
        n = n // toBase
    return res


# Useful to check answers, but not needed here
# def toBaseTen(n,fromBase):
#     return int(n,fromBase)


def base_conversion(maxNum=60000, maxBase=16):
    """Base Conversion"""
    assert type(
        maxNum
    ) == int and maxNum >= 100 and maxNum <= 65536, "maxNum({}) must be >=100 and <=65536".format(
        maxNum)
    assert type(
        maxBase
    ) == int and maxBase >= 2 and maxBase <= 36, "maxBase({}) must be >= 2 and <=36".format(
        maxBase)

    n = random.randint(40, maxNum)
    dist = [10] * 10 + [2] * 5 + [16] * 5 + [i for i in range(2, maxBase + 1)]
    # set this way since converting to/from bases 2,10,16 are more common -- can be changed if needed.
    bases = random.choices(dist, k=2)
    while bases[0] == bases[1]:
        bases = random.choices(dist, k=2)

    problem = f"Convert ${fromBaseTenTo(n, bases[0])}$ from base ${bases[0]}$ to base ${bases[1]}$."
    ans = fromBaseTenTo(n, bases[1])
    return problem, f'${ans}$'

import random


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def newton_symbol(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def binomial_distribution():
    """Binomial distribution"""
    rejected_fraction = float(random.randint(30, 40)) + random.random()
    batch = random.randint(10, 20)
    rejections = random.randint(1, 9)

    answer = 0
    rejected_fraction = round(rejected_fraction, 2)
    for i in range(0, rejections + 1):
        answer += newton_symbol(float(batch), float(i)) * ((rejected_fraction / 100.) ** float(i)) * \
            ((1 - (rejected_fraction / 100.)) ** (float(batch) - float(i)))

    answer = round(100 * answer, 2)

    problem = "A manufacturer of metal pistons finds that, on average, ${0:}$% "\
        "of the pistons they manufacture are rejected because " \
        "they are incorrectly sized. What is the probability that a "\
        "batch of ${1:}$ pistons will contain no more than ${2:}$ " \
        "rejected pistons?".format(rejected_fraction, batch, rejections)
    return problem, f'${answer}$'

import random


def celsius_to_fahrenheit(maxTemp=100):
    """Celsius to Fahrenheit"""
    celsius = random.randint(-50, maxTemp)
    fahrenheit = (celsius * (9 / 5)) + 32

    problem = f"Convert ${celsius}$ degrees Celsius to degrees Fahrenheit"
    solution = f'${fahrenheit}$'
    return problem, solution

import random


def common_factors(maxVal=100):
    """Common Factors"""
    a = x = random.randint(1, maxVal)
    b = y = random.randint(1, maxVal)

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

import random
import math


def complex_to_polar(minRealImaginaryNum=-20,
                     maxRealImaginaryNum=20):
    """Complex to polar form"""
    num = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                  random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    a = num.real
    b = num.imag
    r = round(math.hypot(a, b), 2)
    theta = round(math.atan2(b, a), 2)

    problem = f'${r}({a}\\theta + i{b}\\theta)$'
    return problem, f'${theta}$'

import random
import math


def decimal_to_roman_numerals(maxDecimal=4000):
    """Decimal to Roman Numerals"""
    x = random.randint(0, maxDecimal)
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

    problem = f"The number ${x}$ in Roman Numerals is: "
    return problem, f'${solution}$'

import random
import math


def euclidian_norm(maxEltAmt=20):
    """Euclidian norm or L2 norm of a vector"""
    vec = [
        random.uniform(0, 1000) for i in range(random.randint(2, maxEltAmt))
    ]
    solution = round(math.sqrt(sum([i**2 for i in vec])), 2)

    problem = f"Euclidian norm or L2 norm of the vector ${vec}$ is:"
    return problem, f'${solution}$'

import random


def factors(maxVal=1000):
    """Factors of a number"""
    n = random.randint(1, maxVal)

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

import random


def gcd(maxVal=20):
    """GCD (Greatest Common Denominator)"""
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    while y:
        x, y = y, x % y

    problem = f"GCD of ${a}$ and ${b} = $"
    solution = f'${x}$'
    return problem, solution

import random
import numpy as np


def geometric_mean(maxValue=100, maxCount=4):
    """Geometric Mean of N Numbers"""
    count = random.randint(2, maxCount)
    nums = [random.randint(1, maxValue) for i in range(count)]
    product = np.prod(nums)

    ans = round(product ** (1 / count), 2)
    problem = f"Geometric mean of ${count}$ numbers ${nums} = $"
    # solution = f"$({'*'.join(map(str, nums))}^{{\\frac{{1}}{{{count}}}}} = {ans}$"
    solution = f"${ans}$"
    return problem, solution

import random


def geometric_progression(number_values=6,
                          min_value=2,
                          max_value=12,
                          n_term=7,
                          sum_term=5):
    """Geometric Progression"""
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

import random


def harmonic_mean(maxValue=100, maxCount=4):
    """Harmonic Mean of N Numbers"""
    count = random.randint(2, maxCount)
    nums = [random.randint(1, maxValue) for _ in range(count)]
    sum = 0
    for num in nums:
        sum += (1 / num)
    ans = num / sum

    problem = f"Harmonic mean of ${count}$ numbers ${', '.join(map(str, nums))} = $"
    solution = f"${ans}$"
    return problem, solution

import random


def hcf(maxVal=20):
    """HCF (Highest Common Factor)"""
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    while (y):
        x, y = y, x % y

    problem = f"HCF of ${a}$ and ${b} = $"
    solution = f'${x}$'
    return problem, solution

import random


def is_leap_year(minNumber=1900, maxNumber=2099):
    """Is Leap Year or Not"""
    year = random.randint(minNumber, maxNumber)
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

import random


def lcm(maxVal=20):
    """LCM (Least Common Multiple)"""
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    c = a * b
    x, y = a, b

    while y:
        x, y = y, x % y
    d = c // x

    problem = f"LCM of ${a}$ and ${b} =$"
    solution = f'${d}$'
    return problem, solution

import random


def minutes_to_hours(maxMinutes=999):
    """Convert minutes to hours and minutes"""
    minutes = random.randint(1, maxMinutes)
    ansHours = minutes // 60
    ansMinutes = minutes % 60

    problem = f"Convert ${minutes}$ minutes to hours & minutes"
    solution = f"${ansHours}$ hours and ${ansMinutes}$ minutes"
    return problem, solution

import random


def prime_factors(minVal=1, maxVal=200):
    """Prime Factors"""
    a = random.randint(minVal, maxVal)
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

import random


def product_of_scientific_notations(minExpVal=-100, maxExpVal=100):
    """Product of scientific notations"""
    a = [round(random.uniform(1, 10), 2), random.randint(minExpVal, maxExpVal)]
    b = [round(random.uniform(1, 10), 2), random.randint(minExpVal, maxExpVal)]
    c = [a[0] * b[0], a[1] + b[1]]

    if c[0] >= 10:
        c[0] /= 10
        c[1] += 1

    problem = f"Product of scientific notations ${a[0]} \\times 10^{{{a[1]}}}$ and ${b[0]} \\times 10^{{{b[1]}}} = $"
    solution = f'${round(c[0], 2)} \\times 10^{{{c[1]}}}$'
    return problem, solution

import random


def profit_loss_percent(maxCP=1000, maxSP=1000):
    """Profit or Loss Percent"""
    cP = random.randint(1, maxCP)
    sP = random.randint(1, maxSP)
    diff = abs(sP - cP)
    if (sP - cP >= 0):
        profitOrLoss = "Profit"
    else:
        profitOrLoss = "Loss"
    percent = round(diff / cP * 100, 2)

    problem = f"{profitOrLoss} percent when $CP = {cP}$ and $SP = {sP}$ is: "
    return problem, f'${percent}$'

import random


def quotient_of_power_same_base(maxBase=50, maxPower=10):
    """Quotient of Powers with Same Base"""
    base = random.randint(1, maxBase)
    power1 = random.randint(1, maxPower)
    power2 = random.randint(1, maxPower)
    step = power1 - power2
    solution = base ** step

    problem = f"The Quotient of ${base}^{{{power1}}}$ and ${base}^{{{power2}}} = " \
        f"${base}^{{{power1}-{power2}}} = {base}^{{{step}}}$"
    return problem, f'${solution}$'

import random


def quotient_of_power_same_power(maxBase=50, maxPower=10):
    """Quotient of Powers with Same Power"""
    base1 = random.randint(1, maxBase)
    base2 = random.randint(1, maxBase)
    power = random.randint(1, maxPower)
    step = base1 / base2
    solution = step ** power

    problem = f"The Quotient of ${base1}^{{{power}}}$ and ${base2}^{{{power}}} = " \
        f"({base1}/{base2})^{power} = {step}^{{{power}}}$"
    return problem, f'${solution}$'

import random


def set_operation(minval=3, maxval=7, n_a=4, n_b=5):
    """Union, Intersection, Difference of Two Sets"""
    number_variables_a = random.randint(minval, maxval)
    number_variables_b = random.randint(minval, maxval)
    a = []
    b = []
    for _ in range(number_variables_a):
        a.append(random.randint(1, 10))
    for _ in range(number_variables_b):
        b.append(random.randint(1, 10))
    a = set(a)
    b = set(b)

    problem = f"Given the two sets $a={a}$, $b={b}. " + \
        "Find the Union, intersection, a-b, b-a, and symmetric difference"
    solution = f"Union is ${a.union(b)}$. Intersection is ${a.intersection(b)}$" + \
        f", a-b is ${a.difference(b)}$, b-a is ${b.difference(a)}$." + \
        f" Symmetric difference is ${a.symmetric_difference(b)}$."
    return problem, solution

import random


def signum_function(min=-999, max=999):
    """Signum Function"""
    a = random.randint(min, max)
    b = 0
    if (a > 0):
        b = 1
    if (a < 0):
        b = -1

    problem = f"signum of {a} is ="
    solution = f'${b}$'
    return problem, solution

import random
import math


def surds_comparison(maxValue=100, maxRoot=10):
    """Comparing Surds"""
    radicand1, radicand2 = tuple(random.sample(range(1, maxValue), 2))
    degree1, degree2 = tuple(random.sample(range(1, maxRoot), 2))
    first = math.pow(radicand1, 1 / degree1)
    second = math.pow(radicand2, 1 / degree2)

    solution = "="
    if first > second:
        solution = ">"
    elif first < second:
        solution = "<"

    problem = f"Fill in the blanks ${radicand1}^{{\\frac{{1}}{{{degree1}}}}}$ _ ${radicand2}^{{\\frac{{1}}{{{degree2}}}}}$"
    return problem, f'${solution}$'

