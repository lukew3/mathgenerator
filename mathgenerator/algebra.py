from .latexBuilder import bmatrix
import random
import math
import fractions
import sympy


def basic_algebra(maxVariable=10):
    """Basic Algebra"""
    a = random.randint(1, maxVariable)
    b = random.randint(1, maxVariable)
    c = random.randint(b, maxVariable)

    # calculate gcd
    def calculate_gcd(x, y):
        while (y):
            x, y = y, x % y
        return x

    i = calculate_gcd((c - b), a)
    x = f"{(c - b)//i}/{a//i}"

    if (c - b == 0):
        x = "0"
    elif a == 1 or a == i:
        x = f"{c - b}"

    problem = f"${a}x + {b} = {c}$"
    solution = f"${x}$"
    return problem, solution


def combine_like_terms(maxCoef=10, maxExp=20, maxTerms=10):
    """Combine Like Terms"""
    numTerms = random.randint(1, maxTerms)

    coefs = [random.randint(1, maxCoef) for _ in range(numTerms)]
    exponents = [random.randint(1, max(maxExp - 1, 2)) for _ in range(numTerms)]

    problem = " + ".join([f"{coefs[i]}x^{{{exponents[i]}}}" for i in range(numTerms)])
    d = {}
    for i in range(numTerms):
        if exponents[i] in d:
            d[exponents[i]] += coefs[i]
        else:
            d[exponents[i]] = coefs[i]
    solution = " + ".join([f"{d[k]}x^{{{k}}}" for k in sorted(d)])

    return f'${problem}$', f'${solution}$'


def complex_quadratic(prob_type=0, max_range=10, format='string'):
    """Complex Quadratic Equation"""
    if prob_type < 0 or prob_type > 1:
        print("prob_type not supported")
        print("prob_type = 0 for real roots problems ")
        print("prob_tpye = 1 for imaginary roots problems")
        return None
    if prob_type == 0:
        d = -1
        while d < 0:
            a = random.randrange(1, max_range)
            b = random.randrange(1, max_range)
            c = random.randrange(1, max_range)

            d = (b**2 - 4 * a * c)
    else:
        d = 0
        while d >= 0:
            a = random.randrange(1, max_range)
            b = random.randrange(1, max_range)
            c = random.randrange(1, max_range)

            d = (b**2 - 4 * a * c)

    eq = ''

    if a == 1:
        eq += 'x^2 + '
    else:
        eq += str(a) + 'x^2 + '

    if b == 1:
        eq += 'x + '
    else:
        eq += str(b) + 'x + '

    eq += str(c) + ' = 0'

    problem = f'Find the roots of given Quadratic Equation ${eq}$'

    if d < 0:
        sqrt_d = (-d)**0.5

        if sqrt_d - int(sqrt_d) == 0:
            sqrt_d = int(sqrt_d)
            solution = f'(\\frac{{{-b} + {sqrt_d}i}}{{2*{a}}}, \\frac{{{-b} - {sqrt_d}i}}{{2*{a}}})'
        else:
            solution = f'(\\frac{{{-b} + \\sqrt{{{-d}}}i}}{{2*{a}}}, \\frac{{{-b} - \\sqrt{{{-d}}}i}}{{2*{a}}})'

        return problem, solution

    else:
        s_root1 = round((-b + (d)**0.5) / (2 * a), 3)
        s_root2 = round((-b - (d)**0.5) / (2 * a), 3)

        sqrt_d = (d)**0.5

        if sqrt_d - int(sqrt_d) == 0:
            sqrt_d = int(sqrt_d)
            g_sol = f'(\\frac{{{-b} + {sqrt_d}}}{{2*{a}}}, \\frac{{{-b} - {sqrt_d}}}{{2*{a}}})'
        else:
            g_sol = f'(\\frac{{{-b} + \\sqrt{{{d}}}}}{{2*{a}}}, (\\frac{{{-b} - \\sqrt{{{d}}}}}{{2*{a}}})'

        solution = f'$({s_root1, s_root2}) = {g_sol}$'

        return problem, solution


def compound_interest(maxPrinciple=10000,
                      maxRate=10,
                      maxTime=10):
    """Compound Interest"""
    p = random.randint(1000, maxPrinciple)
    r = random.randint(1, maxRate)
    n = random.randint(1, maxTime)
    a = round(p * (1 + r / 100)**n, 2)

    problem = f"Compound interest for a principle amount of ${p}$ dollars, ${r}$% rate of interest and for a time period of ${n}$ years is $=$"
    return problem, f'${a}$'


def distance_two_points(maxValXY=20, minValXY=-20):
    """Distance between 2 points"""
    point1X = random.randint(minValXY, maxValXY + 1)
    point1Y = random.randint(minValXY, maxValXY + 1)
    point2X = random.randint(minValXY, maxValXY + 1)
    point2Y = random.randint(minValXY, maxValXY + 1)

    distanceSq = (point1X - point2X) ** 2 + (point1Y - point2Y) ** 2

    solution = f"$\\sqrt{{{distanceSq}}}$"
    problem = f"Find the distance between $({point1X}, {point1Y})$ and $({point2X}, {point2Y})$"
    return problem, solution


def expanding(range_x1=10,
              range_x2=10,
              range_a=10,
              range_b=10):
    """Expanding Factored Binomial"""
    x1 = random.randint(-range_x1, range_x1)
    x2 = random.randint(-range_x2, range_x2)
    a = random.randint(-range_a, range_a)
    b = random.randint(-range_b, range_b)

    def intParser(z):
        if (z > 0):
            return f"+{z}"
        elif (z < 0):
            return f"-{abs(z)}"
        else:
            return ""

    c1 = intParser(a * b)
    c2 = intParser((a * x2) + (b * x1))
    c3 = intParser(x1 * x2)

    p1 = intParser(a)
    p2 = intParser(x1)
    p3 = intParser(b)
    p4 = intParser(x2)

    if p1 == "+1":
        p1 = ""
    elif len(p1) > 0 and p1[0] == "+":
        p1 = p1[1:]
    if p3 == "+1":
        p3 = ""
    elif p3[0] == "+":
        p3 = p3[1:]

    if c1 == "+1":
        c1 = ""
    elif len(c1) > 0 and c1[0] == "+":
        c1 = c1[1:]  # Cuts off the plus for readability
    if c2 == "+1":
        c2 = ""

    problem = f"$({p1}x{p2})({p3}x{p4})$"
    solution = f"${c1}x^2{c2}x{c3}$"
    return problem, solution


def factoring(range_x1=10, range_x2=10):
    """Factoring Quadratic
    Given a quadratic equation in the form x^2 + bx + c, factor it into it's roots (x - x1)(x -x2)"""
    x1 = random.randint(-range_x1, range_x1)
    x2 = random.randint(-range_x2, range_x2)

    def intParser(z):
        if (z > 0):
            return f"+{z}"
        elif (z < 0):
            return f"-{abs(z)}"
        else:
            return ""

    b = intParser(x1 + x2)
    c = intParser(x1 * x2)

    if b == "+1":
        b = "+"
    if b == "":
        problem = f"x^2{c}"
    else:
        problem = f"x^2{b}x{c}"

    x1 = intParser(x1)
    x2 = intParser(x2)
    solution = f"$(x{x1})(x{x2})$"
    return f"${problem}$", solution


def int_matrix_22_determinant(maxMatrixVal=100):
    """Determinant to 2x2 Matrix"""
    a = random.randint(0, maxMatrixVal)
    b = random.randint(0, maxMatrixVal)
    c = random.randint(0, maxMatrixVal)
    d = random.randint(0, maxMatrixVal)

    determinant = a * d - b * c
    lst = [[a, b], [c, d]]

    problem = f"$\\det {bmatrix(lst)}= $"
    solution = f"${determinant}$"
    return problem, solution


def intersection_of_two_lines(minM=-10,
                              maxM=10,
                              minB=-10,
                              maxB=10,
                              minDenominator=1,
                              maxDenominator=6):
    """Intersection of two lines"""
    def generateEquationString(m, b):
        """
        Generates an equation given the slope and intercept.
        It handles cases where m is fractional.
        It also ensures that we don't have weird signs such as y = mx + -b.
        """
        if m[0] == 0:
            m = 0
        elif abs(m[0]) == abs(m[1]):
            m = m[0] // m[1]
        elif m[1] == 1:
            m = m[0]
        else:
            m = f"{m[0]}/{m[1]}"
        base = "y ="
        if m != 0:
            if m == 1:
                base = f"{base} x"
            elif m == -1:
                base = f"{base} -x"
            else:
                base = f"{base} {m}x"
        if b > 0:
            if m == 0:
                return f"{base} {b}"
            else:
                return f"{base} + {b}"
        elif b < 0:
            if m == 0:
                return f"{base} -{b * -1}"
            else:
                return f"{base} - {b * -1}"
        else:
            if m == 0:
                return f"{base} 0"
            else:
                return base

    def fractionToString(x):
        """
        Converts the given fractions.Fraction into a string.
        """
        if x.denominator == 1:
            x = x.numerator
        else:
            x = f"{x.numerator}/{x.denominator}"
        return x

    m1 = (random.randint(minM,
                         maxM), random.randint(minDenominator, maxDenominator))
    m2 = (random.randint(minM,
                         maxM), random.randint(minDenominator, maxDenominator))

    b1 = random.randint(minB, maxB)
    b2 = random.randint(minB, maxB)

    eq1 = generateEquationString(m1, b1)
    eq2 = generateEquationString(m2, b2)

    problem = f"Find the point of intersection of the two lines: ${eq1}$ and ${eq2}$"

    m1 = fractions.Fraction(*m1)
    m2 = fractions.Fraction(*m2)
    # if m1 == m2 then the slopes are equal
    # This can happen if both line are the same
    # Or if they are parallel
    # In either case there is no intersection

    if m1 == m2:
        solution = "No Solution"
    else:
        intersection_x = (b1 - b2) / (m2 - m1)
        intersection_y = ((m2 * b1) - (m1 * b2)) / (m2 - m1)
        solution = f"$({fractionToString(intersection_x)}, {fractionToString(intersection_y)})$"

    return problem, solution


def invert_matrix(SquareMatrixDimension=3,
                  MaxMatrixElement=99,
                  OnlyIntegerElementsInInvertedMatrix=True):
    """Invert Matrix"""
    if OnlyIntegerElementsInInvertedMatrix is True:
        isItOk = False
        Mat = list()
        while (isItOk is False):
            Mat = list()
            for i in range(0, SquareMatrixDimension):
                z = list()
                for j in range(0, SquareMatrixDimension):
                    z.append(0)
                z[i] = 1
                Mat.append(z)
            MaxAllowedMatrixElement = math.ceil(
                pow(MaxMatrixElement, 1 / (SquareMatrixDimension)))
            randomlist = random.sample(range(0, MaxAllowedMatrixElement + 1),
                                       SquareMatrixDimension)

            for i in range(0, SquareMatrixDimension):
                if i == SquareMatrixDimension - 1:
                    Mat[0] = [
                        j + (k * randomlist[i])
                        for j, k in zip(Mat[0], Mat[i])
                    ]
                else:
                    Mat[i + 1] = [
                        j + (k * randomlist[i])
                        for j, k in zip(Mat[i + 1], Mat[i])
                    ]

            for i in range(1, SquareMatrixDimension - 1):
                Mat[i] = [
                    sum(i) for i in zip(Mat[SquareMatrixDimension - 1], Mat[i])
                ]

            isItOk = True
            for i in Mat:
                for j in i:
                    if j > MaxMatrixElement:
                        isItOk = False
                        break
                if isItOk is False:
                    break

        random.shuffle(Mat)
        Mat = sympy.Matrix(Mat)
        Mat = sympy.Matrix.transpose(Mat)
        Mat = Mat.tolist()
        random.shuffle(Mat)
        Mat = sympy.Matrix(Mat)
        Mat = sympy.Matrix.transpose(Mat)

    else:
        randomlist = list(sympy.primerange(0, MaxMatrixElement + 1))
        plist = random.sample(randomlist, SquareMatrixDimension)
        randomlist = random.sample(
            range(0, MaxMatrixElement + 1),
            SquareMatrixDimension * SquareMatrixDimension)
        randomlist = list(set(randomlist) - set(plist))
        n_list = random.sample(
            randomlist, SquareMatrixDimension * (SquareMatrixDimension - 1))
        Mat = list()
        for i in range(0, SquareMatrixDimension):
            z = list()
            z.append(plist[i])
            for j in range(0, SquareMatrixDimension - 1):
                z.append(n_list[(i * SquareMatrixDimension) + j - i])
            random.shuffle(z)
            Mat.append(z)
        Mat = sympy.Matrix(Mat)

    problem = 'Inverse of Matrix $' + bmatrix(Mat.tolist()) + '$ is:'
    solution = bmatrix(sympy.Matrix.inv(Mat).tolist())
    return problem, solution


def linear_equations(n=2, varRange=20, coeffRange=20):
    """Linear Equations"""
    if n > 10:
        print("[!] n cannot be greater than 10")
        return None, None

    vars = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'][:n]
    soln = [random.randint(-varRange, varRange) for i in range(n)]
    problem = list()
    solution = "$, $".join(
        ["{} = {}".format(vars[i], soln[i]) for i in range(n)])

    for _ in range(n):
        coeff = [random.randint(-coeffRange, coeffRange) for i in range(n)]
        res = sum([coeff[i] * soln[i] for i in range(n)])
        prob = [
            "{}{}".format(coeff[i], vars[i]) if coeff[i] != 0 else ""
            for i in range(n)
        ]

        while "" in prob:
            prob.remove("")
        prob = " + ".join(prob) + " = " + str(res)
        problem.append(prob)

    # problem = "\n".join(problem)
    problem = "$ and $".join(problem)

    return f'Given the equations ${problem}$, solve for $x$ and $y$', f'${solution}$'


def log(maxBase=3, maxVal=8):
    """Logarithm"""
    a = random.randint(1, maxVal)
    b = random.randint(2, maxBase)
    c = pow(b, a)

    problem = f'$log_{{{b}}}({c})=$'
    solution = f'${a}$'
    return problem, solution


def matrix_multiplication(maxVal=100, max_dim=10):
    """Multiply Two Matrices"""
    m = random.randint(2, max_dim)
    n = random.randint(2, max_dim)
    k = random.randint(2, max_dim)

    # generate matrices a and b
    a = [[random.randint(-maxVal, maxVal) for _ in range(n)] for _ in range(m)]
    b = [[random.randint(-maxVal, maxVal) for _ in range(k)] for _ in range(n)]

    res = []
    for r in range(m):
        res.append([])
        for c in range(k):
            temp = 0
            for t in range(n):
                temp += a[r][t] * b[t][c]
            res[r].append(temp)

    problem = f"Multiply ${bmatrix(a)}$ and ${bmatrix(b)}$"
    solution = f'${bmatrix(res)}$'
    return problem, solution


def midpoint_of_two_points(maxValue=20):
    """Midpoint of two points"""
    x1 = random.randint(-20, maxValue)
    y1 = random.randint(-20, maxValue)
    x2 = random.randint(-20, maxValue)
    y2 = random.randint(-20, maxValue)
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2

    problem = f"The midpoint of $({x1},{y1})$ and $({x2},{y2}) = $"
    solution = f"$({xm},{ym})$"
    return problem, solution


def multiply_complex_numbers(minRealImaginaryNum=-20,
                             maxRealImaginaryNum=20):
    """Multiplication of 2 complex numbers"""
    num1 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                   random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    num2 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                   random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    product = num1 * num2

    problem = f"${num1} * {num2} = $"
    solution = f'${product}$'
    return problem, solution


def multiply_int_to_22_matrix(maxMatrixVal=10, maxRes=100):
    """Multiply Integer to 2x2 Matrix"""
    a = random.randint(0, maxMatrixVal)
    b = random.randint(0, maxMatrixVal)
    c = random.randint(0, maxMatrixVal)
    d = random.randint(0, maxMatrixVal)

    constant = random.randint(0, int(maxRes / max(a, b, c, d)))

    a1 = a * constant
    b1 = b * constant
    c1 = c * constant
    d1 = d * constant
    lst = [[a, b], [c, d]]
    lst1 = [[a1, b1], [c1, d1]]

    problem = f'${constant} * {bmatrix(lst)} =$'
    solution = f'${bmatrix(lst1)}$'
    return problem, solution


def quadratic_equation(maxVal=100):
    """Quadratic Equation"""
    a = random.randint(1, maxVal)
    c = random.randint(1, maxVal)
    b = random.randint(
        round(math.sqrt(4 * a * c)) + 1, round(math.sqrt(4 * maxVal * maxVal)))
    D = math.sqrt(b * b - 4 * a * c)
    res = {round((-b + D) / (2 * a), 2), round((-b - D) / (2 * a), 2)}

    problem = f"What are the zeros of the quadratic equation ${a}x^2+{b}x+{c}=0$"
    solution = f'${res}$'
    return problem, solution


def simple_interest(maxPrinciple=10000,
                    maxRate=10,
                    maxTime=10):
    """Simple Interest"""
    p = random.randint(1000, maxPrinciple)
    r = random.randint(1, maxRate)
    t = random.randint(1, maxTime)
    s = round((p * r * t) / 100, 2)

    problem = f"Simple interest for a principle amount of ${p}$ dollars, ${r}$% rate of interest and for a time period of ${t}$ years is $=$ "
    solution = f'${s}$'
    return problem, solution


def system_of_equations(range_x=10,
                        range_y=10,
                        coeff_mult_range=10):
    """Solve a System of Equations in R^2"""
    # Generate solution point first
    x = random.randint(-range_x, range_x)
    y = random.randint(-range_y, range_y)
    # Start from reduced echelon form (coeffs 1)
    c1 = [1, 0, x]
    c2 = [0, 1, y]

    def randNonZero():
        return random.choice(
            [i for i in range(-coeff_mult_range, coeff_mult_range) if i != 0])

    # Add random (non-zero) multiple of equations (rows) to each other
    c1_mult = randNonZero()
    c2_mult = randNonZero()
    new_c1 = [c1[i] + c1_mult * c2[i] for i in range(len(c1))]
    new_c2 = [c2[i] + c2_mult * c1[i] for i in range(len(c2))]
    # For extra randomness, now add random (non-zero) multiples of original rows
    # to themselves
    c1_mult = randNonZero()
    c2_mult = randNonZero()
    new_c1 = [new_c1[i] + c1_mult * c1[i] for i in range(len(c1))]
    new_c2 = [new_c2[i] + c2_mult * c2[i] for i in range(len(c2))]

    def coeffToFuncString(coeffs):
        # lots of edge cases for perfect formatting!
        x_sign = '-' if coeffs[0] < 0 else ''
        # No redundant 1s
        x_coeff = str(abs(coeffs[0])) if abs(coeffs[0]) != 1 else ''
        # If x coeff is 0, dont include x
        x_str = f'{x_sign}{x_coeff}x' if coeffs[0] != 0 else ''
        # if x isn't included and y is positive, dont include operator
        op = ' - ' if coeffs[1] < 0 else (' + ' if x_str != '' else '')
        # No redundant 1s
        y_coeff = abs(coeffs[1]) if abs(coeffs[1]) != 1 else ''
        # Don't include if 0, unless x is also 0 (probably never happens)
        y_str = f'{y_coeff}y' if coeffs[1] != 0 else (
            '' if x_str != '' else '0')
        return f'{x_str}{op}{y_str} = {coeffs[2]}'

    problem = f"Given ${coeffToFuncString(new_c1)}$ and ${coeffToFuncString(new_c2)}$, solve for $x$ and $y$."
    solution = f"$x = {x}$, $y = {y}$"
    return problem, solution
    # Add random (non-zero) multiple of equations to each other


def vector_cross(minVal=-20, maxVal=20):
    """Cross product of 2 vectors"""
    a = [random.randint(minVal, maxVal) for _ in range(3)]
    b = [random.randint(minVal, maxVal) for _ in range(3)]
    c = [
        a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

    problem = f"${a} \\times {b} = $"
    solution = f"${c}$"
    return problem, solution


def vector_dot(minVal=-20, maxVal=20):
    """Dot product of 2 vectors"""
    a = [random.randint(minVal, maxVal) for i in range(3)]
    b = [random.randint(minVal, maxVal) for i in range(3)]
    c = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

    problem = f'${a}\\cdot{b}=$'
    solution = f'${c}$'
    return problem, solution

