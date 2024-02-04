from ._latexBuilder import bmatrix
import random
import math
import fractions
import sympy

FILENAME = "algebra"

def basic_algebra(max_variable=10):
    r"""Basic Algebra

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $1x + 5 = 5$ | $0$ |
    """
    a = random.randint(1, max_variable)
    b = random.randint(1, max_variable)
    c = random.randint(b, max_variable)

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

    #Have to add this and I don't know why
    try:
        if x*int(a) != int(c)-int(b):
            x = f"{c - b}/{a}"
    except:
        return basic_algebra(max_variable)

    problem = f"Solve for x: ${a}x + {b} = {c}$"
    solution = f"{eval(x)}"
    return problem, solution


def combine_like_terms(max_coef=10, max_exp=20, max_terms=10, max_x=10):
    r"""Combine Like Terms

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $6x^{9} + 3x^{2} + 5x^{19} + 3x^{17}$ | $3x^{2} + 6x^{9} + 3x^{17} + 5x^{19}$ |
    """
    numTerms = random.randint(1, max_terms)

    coefs = [random.randint(1, max_coef) for _ in range(numTerms)]
    exponents = [
        random.randint(1, max(max_exp - 1, 2)) for _ in range(numTerms)
    ]

    problem = " + ".join(
        [f"{coefs[i]}x^{{{exponents[i]}}}" for i in range(numTerms)])
    d = {}
    for i in range(numTerms):
        if exponents[i] in d:
            d[exponents[i]] += coefs[i]
        else:
            d[exponents[i]] = coefs[i]
    solution = " + ".join([f"{d[k]}x^{{{k}}}" for k in sorted(d)])

    x = random.randint(1, max_x)
    problem = problem + " for x = " + str(x)
    solution = sympy.sympify(solution.replace("x", "*" + str(x)).replace('{', '').replace('}', ''), evaluate=True)

    return f'Simplify: ${problem}$', f'{solution}'


def complex_quadratic(prob_type=0, max_range=10):
    r"""Complex Quadratic Equation

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the roots of given Quadratic Equation $x^2 + 8x + 8 = 0$ | $((-1.172, -6.828)) = (\frac{-8 + \sqrt{32}}{2}, (\frac{-8 - \sqrt{32}}{2})$ |
    """
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
            solution = rf'(\frac{{{-b} + {sqrt_d}i}}{{{2*a}}}, \frac{{{-b} - {sqrt_d}i}}{{{2*a}}})'
        else:
            solution = rf'(\frac{{{-b} + \sqrt{{{-d}}}i}}{{{2*a}}}, \frac{{{-b} - \sqrt{{{-d}}}i}}{{{2*a}}})'

        return problem, solution

    else:
        s_root1 = round((-b + (d)**0.5) / (2 * a), 3)
        s_root2 = round((-b - (d)**0.5) / (2 * a), 3)

        sqrt_d = (d)**0.5

        if sqrt_d - int(sqrt_d) == 0:
            sqrt_d = int(sqrt_d)
            g_sol = rf'(\frac{{{-b} + {sqrt_d}}}{{{2*a}}}, \frac{{{-b} - {sqrt_d}}}{{{2*a}}})'
        else:
            g_sol = rf'(\frac{{{-b} + \sqrt{{{d}}}}}{{{2*a}}}, (\frac{{{-b} - \sqrt{{{d}}}}}{{{2*a}}})'

        solution = f'$({s_root1, s_root2}) = {g_sol}$'

        return problem, solution


def compound_interest(max_principle=10000, max_rate=10, max_time=10):
    r"""Compound Interest

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Compound interest for a principle amount of $2679$ dollars, $9$% rate of interest and for a time period of $3$ years is $=$ | $3469.38$ |
    """
    p = random.randint(1000, max_principle)
    r = random.randint(1, max_rate)
    n = random.randint(1, max_time)
    a = round(p * (1 + r / 100)**n, 2)

    problem = f"Compound interest for a principle amount of ${p}$ dollars, ${r}$% rate of interest and for a time period of ${n}$ years is $=$"
    return problem, f'{a}'


def distance_two_points(max_val_xy=20, min_val_xy=-20):
    r"""Distance between 2 points

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the distance between $(-19, -6)$ and $(15, -16)$ | $\sqrt{1256}$ |
    """
    if max_val_xy < min_val_xy:
        max_val_xy, min_val_xy = min_val_xy, max_val_xy

    point1X = random.randint(min_val_xy, max_val_xy + 1)
    point1Y = random.randint(min_val_xy, max_val_xy + 1)
    point2X = random.randint(min_val_xy, max_val_xy + 1)
    point2Y = random.randint(min_val_xy, max_val_xy + 1)

    distanceSq = (point1X - point2X)**2 + (point1Y - point2Y)**2

    solution = str(round(distanceSq**0.5, 2))
    problem = f"Find the distance between $({point1X}, {point1Y})$ and $({point2X}, {point2Y})$"
    return problem, solution


def expanding(range_x1=10, range_x2=10, range_a=10, range_b=10):
    r"""Expanding Factored Binomial

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    |$(x-6)(-3x-3)$ | $x^2+18x+18$ |
    """
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
    r"""Factoring Quadratic
    Given a quadratic equation in the form x^2 + bx + c, factor it into it's roots (x - x1)(x -x2)

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $x^2+2x-24$ | $(x-4)(x+6)$ |
    """
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


def int_matrix_22_determinant(max_matrix_val=100):
    r"""Determinant to 2x2 Matrix

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $\det \begin{bmatrix} 88 & 40 \\\ 9 & 91 \end{bmatrix}= $ | $7648$ |
    """
    a = random.randint(0, max_matrix_val)
    b = random.randint(0, max_matrix_val)
    c = random.randint(0, max_matrix_val)
    d = random.randint(0, max_matrix_val)

    determinant = a * d - b * c
    lst = [[a, b], [c, d]]

    problem = rf"Find the determinant of ${bmatrix(lst)}$"
    solution = f"{determinant}"
    return problem, solution


def intersection_of_two_lines(min_m=-10,
                              max_m=10,
                              min_b=-10,
                              max_b=10,
                              min_denominator=1,
                              max_denominator=6):
    r"""Intersection of two lines

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the point of intersection of the two lines: $y = \frac{-2}{6}x + 3$ and $y = \frac{3}{6}x - 8$ | $(\frac{66}{5}, \frac{-7}{5})$ |
    """
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
            m = rf"\frac{{{m[0]}}}{{{m[1]}}}"
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
            x = rf"\frac{{{x.numerator}}}{{{x.denominator}}}"
        return x

    m1 = (random.randint(min_m, max_m),
          random.randint(min_denominator, max_denominator))
    m2 = (random.randint(min_m, max_m),
          random.randint(min_denominator, max_denominator))

    b1 = random.randint(min_b, max_b)
    b2 = random.randint(min_b, max_b)

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


def invert_matrix(square_matrix_dimension=3,
                  max_matrix_element=99,
                  only_integer_elements_in_inverted_matrixe=True):
    r"""Invert Matrix

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Inverse of Matrix $\begin{bmatrix} 4 & 1 & 4 \\\ 5 & 1 & 5 \\\ 12 & 3 & 13 \end{bmatrix}$ is: | $\begin{bmatrix} 2 & 1 & -1 \\\ 5 & -4 & 0 \\\ -3 & 0 & 1 \end{bmatrix}$ |
    """
    if only_integer_elements_in_inverted_matrixe is True:
        isItOk = False
        Mat = list()
        while (isItOk is False):
            Mat = list()
            for i in range(0, square_matrix_dimension):
                z = list()
                for j in range(0, square_matrix_dimension):
                    z.append(0)
                z[i] = 1
                Mat.append(z)
            MaxAllowedMatrixElement = math.ceil(
                pow(max_matrix_element, 1 / (square_matrix_dimension)))
            randomlist = random.sample(range(0, MaxAllowedMatrixElement + 1),
                                       square_matrix_dimension)

            for i in range(0, square_matrix_dimension):
                if i == square_matrix_dimension - 1:
                    Mat[0] = [
                        j + (k * randomlist[i])
                        for j, k in zip(Mat[0], Mat[i])
                    ]
                else:
                    Mat[i + 1] = [
                        j + (k * randomlist[i])
                        for j, k in zip(Mat[i + 1], Mat[i])
                    ]

            for i in range(1, square_matrix_dimension - 1):
                Mat[i] = [
                    sum(i)
                    for i in zip(Mat[square_matrix_dimension - 1], Mat[i])
                ]

            isItOk = True
            for i in Mat:
                for j in i:
                    if j > max_matrix_element:
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
        randomlist = list(sympy.primerange(0, max_matrix_element + 1))
        plist = random.sample(randomlist, square_matrix_dimension)
        randomlist = random.sample(
            range(0, max_matrix_element + 1),
            square_matrix_dimension * square_matrix_dimension)
        randomlist = list(set(randomlist) - set(plist))
        n_list = random.sample(
            randomlist,
            square_matrix_dimension * (square_matrix_dimension - 1))
        Mat = list()
        for i in range(0, square_matrix_dimension):
            z = list()
            z.append(plist[i])
            for j in range(0, square_matrix_dimension - 1):
                z.append(n_list[(i * square_matrix_dimension) + j - i])
            random.shuffle(z)
            Mat.append(z)
        Mat = sympy.Matrix(Mat)

    problem = 'Inverse of Matrix $' + bmatrix(Mat.tolist()) + '$ is:'
    solution = f'${bmatrix(sympy.Matrix.inv(Mat).tolist())}$'
    return problem, solution


def linear_equations(n=2, var_range=20, coeff_range=20):
    r"""Linear Equations

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Given the equations $10x + -20y = 310$ and $-16x + -17y = 141$, solve for $x$ and $y$ | $x = 5$, $y = -13$ |
    """
    if n > 10:
        print("[!] n cannot be greater than 10")
        return None, None

    vars = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'][:n]
    soln = [random.randint(-var_range, var_range) for i in range(n)]
    problem = list()
    solution = "$, $".join(
        ["{} = {}".format(vars[i], soln[i]) for i in range(n)])

    for _ in range(n):
        coeff = [random.randint(-coeff_range, coeff_range) for i in range(n)]
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

    
    vopts = ['x','y']
    vsolve = random.choice(vopts)
    return f'Given the equations ${problem}$, solve for {vsolve}', f'{soln[vopts.index(vsolve)]}'


def line_equation_from_2_points(max_val=20):
    r"""Equation of Line from Two Points

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the equation of the line passing through the points $(-19,-8)$ and $(-2,0)$. | $y=\frac{8}{17}x+\frac{16}{17}$ |
    """
    x1 = random.randint(-max_val, max_val)
    x2 = random.randint(-max_val, max_val)
    if x1 == x2:
        return line_equation_from_2_points(max_val=max_val)
    y1 = random.randint(-max_val, max_val)
    y2 = random.randint(-max_val, max_val)
    m1 = (y2 - y1) // math.gcd(y2 - y1, x2 - x1)
    m2 = (x2 - x1) // math.gcd(y2 - y1, x2 - x1)
    c1 = (y1 * (x2 - x1) - (y2 - y1) * x1) // math.gcd(y1 * (x2 - x1) - (y2 - y1) * x1, (x2 - x1))
    c2 = (x2 - x1) // math.gcd(y1 * (x2 - x1) - (y2 - y1) * x1, (x2 - x1))
    c = rf"{'+' if c1 >= 0 else '-'}\frac{{{abs(c1)}}}{{{c2}}}" if c1 != 0 else ""
    if c2 < 0:
        c2 = -c2
        c1 = -c1
        c = rf"{'+' if c1 >= 0 else '-'}\frac{{{abs(c1)}}}{{{c2}}}"
    if c2 == 1:
        c = f"{c1:+}"

    problem = f'Find the equation of the line passing through the points $({x1},{y1})$ and $({x2},{y2})$.'

    if m1 == 0:
        return problem, f"$y={c}$"
    if m2 < 0:
        m1 = -m1
        m2 = -m2
    if m2 == 1:
        if m1 == 1:
            return problem, f"$y=x{c}$"
        if m1 == -1:
            return problem, f"$y=-x{c}$"
        return problem, f"y={m1}x{c}"

    return problem, rf"$y=\frac{{{m1}}}{{{m2}}}x{c}$"


def log(max_base=3, max_val=8):
    r"""Logarithm

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $log_{3}(243)=$ | $5$ |
    """
    a = random.randint(1, max_val)
    b = random.randint(2, max_base)
    c = pow(b, a)

    problem = f'$log_{{{b}}}({c})=$'
    solution = f'{a}'
    return problem, solution


def matrix_multiplication(max_val=100, max_dim=10):
    r"""Multiply Two Matrices

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Multiply $\begin{bmatrix} 15 & 72 \\\ 64 & -20 \\\ 18 & 59 \\\ -21 & -55 \\\ 20 & -12 \\\ -75 & -42 \\\ 47 & 89 \\\ -53 & 27 \\\ -56 & 44 \end{bmatrix}$ and $\begin{bmatrix} 49 & -2 & 68 & -28 \\\ 49 & 6 & 83 & 42 \end{bmatrix}$ | $\begin{bmatrix} 4263 & 402 & 6996 & 2604 \\\ 2156 & -248 & 2692 & -2632 \\\ 3773 & 318 & 6121 & 1974 \\\ -3724 & -288 & -5993 & -1722 \\\ 392 & -112 & 364 & -1064 \\\ -5733 & -102 & -8586 & 336 \\\ 6664 & 440 & 10583 & 2422 \\\ -1274 & 268 & -1363 & 2618 \\\ -588 & 376 & -156 & 3416 \end{bmatrix}$ |
    """
    m = random.randint(2, max_dim)
    n = random.randint(2, max_dim)
    k = random.randint(2, max_dim)

    # generate matrices a and b
    a = [[random.randint(-max_val, max_val) for _ in range(n)]
         for _ in range(m)]
    b = [[random.randint(-max_val, max_val) for _ in range(k)]
         for _ in range(n)]

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


def midpoint_of_two_points(max_value=20):
    r"""Midpoint of two points

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | The midpoint of $(-8,10)$ and $(18,0) = $ | $(5.0,5.0)$ |
    """
    x1 = random.randint(-20, max_value)
    y1 = random.randint(-20, max_value)
    x2 = random.randint(-20, max_value)
    y2 = random.randint(-20, max_value)
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2

    problem = f"The midpoint of $({x1},{y1})$ and $({x2},{y2}) = $"
    solution = f"$({xm},{ym})$"
    return problem, solution


def multiply_complex_numbers(min_real_imaginary_num=-20,
                             max_real_imaginary_num=20):
    r"""Multiplication of 2 complex numbers

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $(14+18j) * (14+15j) = $ | $(-74+462j)$ |
    """
    num1 = complex(
        random.randint(min_real_imaginary_num, max_real_imaginary_num),
        random.randint(min_real_imaginary_num, max_real_imaginary_num))
    num2 = complex(
        random.randint(min_real_imaginary_num, max_real_imaginary_num),
        random.randint(min_real_imaginary_num, max_real_imaginary_num))
    product = num1 * num2

    problem = f"${num1} * {num2} = $"
    solution = f'${product}$'
    return problem, solution


def multiply_int_to_22_matrix(max_matrix_val=10, max_res=100):
    r"""Multiply Integer to 2x2 Matrix

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $5 * \begin{bmatrix} 1 & 0 \\\ 2 & 9 \end{bmatrix} =$ | $\begin{bmatrix} 5 & 0 \\\ 10 & 45 \end{bmatrix}$ |
    """
    a = random.randint(0, max_matrix_val)
    b = random.randint(0, max_matrix_val)
    c = random.randint(0, max_matrix_val)
    d = random.randint(0, max_matrix_val)

    constant = random.randint(0, int(max_res / max(a, b, c, d)))

    a1 = a * constant
    b1 = b * constant
    c1 = c * constant
    d1 = d * constant
    lst = [[a, b], [c, d]]
    lst1 = [[a1, b1], [c1, d1]]

    problem = f'${constant} * {bmatrix(lst)} =$'
    solution = f'${bmatrix(lst1)}$'
    return problem, solution


def quadratic_equation(max_val=100):
    r"""Quadratic Equation

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What are the zeros of the quadratic equation $22x^2+137x+25=0$ | ${-0.19, -6.04}$ |
    """
    a = random.randint(1, max_val)
    c = random.randint(1, max_val)
    b = random.randint(
        round(math.sqrt(4 * a * c)) + 1,
        round(math.sqrt(4 * max_val * max_val)))
    D = math.sqrt(b * b - 4 * a * c)
    res = {round((-b + D) / (2 * a), 2), round((-b - D) / (2 * a), 2)}

    problem = f"What are the zeros of the quadratic equation ${a}x^2+{b}x+{c}=0$"
    solution = f'${res}$'
    return problem, solution


def simple_interest(max_principle=10000, max_rate=10, max_time=10):
    r"""Simple Interest

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Simple interest for a principle amount of $7217$ dollars, $3$% rate of interest and for a time period of $10$ years is $=$ | $2165.1$ |
    """
    p = random.randint(1000, max_principle)
    r = random.randint(1, max_rate)
    t = random.randint(1, max_time)
    s = round((p * r * t) / 100, 2)

    problem = f"Simple interest for a principle amount of ${p}$ dollars, ${r}$% rate of interest and for a time period of ${t}$ years is $=$ "
    solution = f'{s}'
    return problem, solution


def system_of_equations(range_x=10, range_y=10, coeff_mult_range=10):
    r"""Solve a System of Equations in R^2

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Given $-x + 5y = -28$ and $9x + 2y = 64$, solve for $x$ and $y$. | $x = 8$, $y = -4$ |
    """
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

    if random.randint(0, 1) == 0:
        problem = f"Given ${coeffToFuncString(new_c1)}$ and ${coeffToFuncString(new_c2)}$, solve for $x$"
        solution = f'{x}'
    else:
        problem = f"Given ${coeffToFuncString(new_c1)}$ and ${coeffToFuncString(new_c2)}$, solve for $y$"
        solution = f'{y}'
    return problem, solution
    # Add random (non-zero) multiple of equations to each other


def vector_cross(min_val=-20, max_val=20):
    r"""Cross product of 2 vectors

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $[-1, -4, 10] \times [-11, 1, -16] = $ | $[54, -126, -45]$ |
    """
    a = [random.randint(min_val, max_val) for _ in range(3)]
    b = [random.randint(min_val, max_val) for _ in range(3)]
    c = [
        a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

    problem = rf"${a} \times {b} = $"
    solution = f"${c}$"
    return problem, solution


def vector_dot(min_val=-20, max_val=20):
    r"""Dot product of 2 vectors

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $[12, -9, -8]\cdot[-9, 8, 1]=$ | $-188$ |
    """
    a = [random.randint(min_val, max_val) for i in range(3)]
    b = [random.randint(min_val, max_val) for i in range(3)]
    c = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

    problem = rf'${a}\cdot{b}=$'
    solution = f'{c}'
    return problem, solution


def orthogonal_projection(min_val=-10, max_val=10):
    r"""Orthogonal Projection

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the orthogonal projection of $[2, 3]$ onto $[4, -7]$ | $[\frac{-4}{5}, \frac{7}{5}]$ |
    """
    v = [random.randint(min_val, max_val) for _ in range(2)]
    u = [random.randint(min_val, max_val) for _ in range(2)]
    dot_t = v[0] * u[0] + v[1] * u[1]
    dot_b = u[0] * u[0] + u[1] * u[1]
    frac = fractions.Fraction(dot_t, dot_b).limit_denominator()
    y = [frac * u[0], frac * u[1]]

    if y[0].denominator != 1:
        y[0] = rf'\frac{{{y[0].numerator}}}{{{y[0].denominator}}}'
    if y[1].denominator != 1:
        y[1] = rf'\frac{{{y[1].numerator}}}{{{y[1].denominator}}}'

    problem = f'Find the orthogonal projection of ${v}$ onto ${u}$'
    solution = f'$[{y[0]}, {y[1]}]$'
    return problem, solution
