import random
import math
import fractions

genList = []


# || Generator class
class Generator:
    def __init__(self, title, id, generalProb, generalSol, func):
        self.title = title
        self.id = id
        self.generalProb = generalProb
        self.generalSol = generalSol
        self.func = func
        genList.append([id, title, self])

    def __str__(self):
        return str(self.id) + " " + self.title + " " + self.generalProb + " " + self.generalSol

    def __call__(self, **kwargs):
        return self.func(**kwargs)


# || Non-generator Functions
def genById(id):
    generator = genList[id][2]
    return(generator())


def getGenList():
    return(genList)

# || Generator Functions


def additionFunc(maxSum=99, maxAddend=50):
    a = random.randint(0, maxAddend)
    b = random.randint(0, min((maxSum - a), maxAddend))  # The highest value of b will be no higher than the maxsum minus the first number and no higher than the maxAddend as well
    c = a + b
    problem = str(a) + "+" + str(b) + "="
    solution = str(c)
    return problem, solution


def subtractionFunc(maxMinuend=99, maxDiff=99):
    a = random.randint(0, maxMinuend)
    b = random.randint(max(0, (a - maxDiff)), a)
    c = a - b
    problem = str(a) + "-" + str(b) + "="
    solution = str(c)
    return problem, solution


def multiplicationFunc(maxRes=99, maxMulti=99):
    a = random.randint(0, maxMulti)
    b = random.randint(0, min(int(maxMulti / a), maxRes))
    c = a * b
    problem = str(a) + "*" + str(b) + "="
    solution = str(c)
    return problem, solution


def divisionFunc(maxRes=99, maxDivid=99):
    a = random.randint(0, maxDivid)
    b = random.randint(0, min(maxRes, maxDivid))
    c = a / b
    problem = str(a) + "/" + str(b) + "="
    solution = str(c)
    return problem, solution


def binaryComplement1sFunc(maxDigits=10):
    question = ''
    answer = ''
    for i in range(random.randint(1, maxDigits)):
        temp = str(random.randint(0, 1))
        question += temp
        answer += "0" if temp == "1" else "1"

    problem = question+"="
    solution = answer
    return problem, solution


def moduloFunc(maxRes=99, maxModulo=99):
    a = random.randint(0, maxModulo)
    b = random.randint(0, min(maxRes, maxModulo))
    c = a % b
    problem = str(a) + "%" + str(b) + "="
    solution = str(c)
    return problem, solution


def squareRootFunc(minNo=1, maxNo=12):
    b = random.randint(minNo, maxNo)
    a = b * b
    problem = "sqrt(" + str(a) + ")="
    solution = str(b)
    return problem, solution


def powerRuleDifferentiationFunc(maxCoef=10, maxExp=10, maxTerms=5):
    numTerms = random.randint(1, maxTerms)
    problem = ""
    solution = ""
    for i in range(numTerms):
        if i > 0:
            problem += " + "
            solution += " + "
        coefficient = random.randint(1, maxCoef)
        exponent = random.randint(1, maxExp)
        problem += str(coefficient) + "x^" + str(exponent)
        solution += str(coefficient * exponent) + "x^" + str(exponent - 1)
    return problem, solution


def squareFunc(maxSquareNum=20):
    a = random.randint(1, maxSquareNum)
    b = a * a
    problem = str(a) + "^2" + "="
    solution = str(b)
    return problem, solution


def gcdFunc(maxVal=20):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    while(y):
        x, y = y, x % y
    problem = f"GCD of {a} and {b} = "
    solution = str(x)
    return problem, solution


def lcmFunc(maxVal=20):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    c = a * b
    while(y):
        x, y = y, x % y
    d = c // x
    problem = f"LCM of {a} and {b} ="
    solution = str(d)
    return problem, solution


def basicAlgebraFunc(maxVariable=10):
    a = random.randint(1, maxVariable)
    b = random.randint(1, maxVariable)
    c = random.randint(b, maxVariable)
    # calculate gcd

    def calculate_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    i = calculate_gcd((c - b), a)
    x = f"{(c - b)//i}/{a//i}"
    if (c - b == 0):
        x = "0"
    elif a == 1 or a == i:
        x = f"{c - b}"
    problem = f"{a}x + {b} = {c}"
    solution = x
    return problem, solution


def logFunc(maxBase=3, maxVal=8):
    a = random.randint(1, maxVal)
    b = random.randint(2, maxBase)
    c = pow(b, a)
    problem = "log" + str(b) + "(" + str(c) + ")"
    solution = str(a)
    return problem, solution


def divisionToIntFunc(maxA=25, maxB=25):
    a = random.randint(1, maxA)
    b = random.randint(1, maxB)
    divisor = a * b
    dividend = random.choice([a, b])
    problem = f"{divisor}/{dividend} = "
    solution = int(divisor / dividend)
    return problem, solution


def DecimalToBinaryFunc(max_dec=99):
    a = random.randint(1, max_dec)
    b = bin(a).replace("0b", "")
    problem = "Binary of " + str(a) + "="
    solution = str(b)
    return problem, solution


def BinaryToDecimalFunc(max_dig=10):
    problem = ''
    for i in range(random.randint(1, max_dig)):
        temp = str(random.randint(0, 1))
        problem += temp

    solution = int(problem, 2)
    return problem, solution


def divideFractionsFunc(maxVal=10):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    while (a == b):
        b = random.randint(1, maxVal)
    c = random.randint(1, maxVal)
    d = random.randint(1, maxVal)
    while (c == d):
        d = random.randint(1, maxVal)

    def calculate_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    tmp_n = a * d
    tmp_d = b * c
    gcd = calculate_gcd(tmp_n, tmp_d)
    x = f"{tmp_n//gcd}/{tmp_d//gcd}"
    if (tmp_d == 1 or tmp_d == gcd):
        x = f"{tmp_n//gcd}"
    # for equal numerator and denominators
    problem = f"({a}/{b})/({c}/{d})"
    solution = x
    return problem, solution


def multiplyIntToMatrix22(maxMatrixVal=10, maxRes=100):
    a = random.randint(0, maxMatrixVal)
    b = random.randint(0, maxMatrixVal)
    c = random.randint(0, maxMatrixVal)
    d = random.randint(0, maxMatrixVal)
    constant = random.randint(0, int(maxRes / max(a, b, c, d)))
    problem = f"{constant} * [[{a}, {b}], [{c}, {d}]] = "
    solution = f"[[{a*constant},{b*constant}],[{c*constant},{d*constant}]]"
    return problem, solution


def areaOfTriangleFunc(maxA=20, maxB=20, maxC=20):
    a = random.randint(1, maxA)
    b = random.randint(1, maxB)
    c = random.randint(1, maxC)
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    problem = "Area of triangle with side lengths: " + str(a) + " " + str(b) + " " + str(c) + " = "
    solution = area
    return problem, solution


def isTriangleValidFunc(maxSideLength=50):
    sideA = random.randint(1, maxSideLength)
    sideB = random.randint(1, maxSideLength)
    sideC = random.randint(1, maxSideLength)
    sideSums = [sideA + sideB, sideB + sideC, sideC + sideA]
    sides = [sideC, sideA, sideB]
    exists = True & (sides[0] < sideSums[0]) & (sides[1] < sideSums[1]) & (sides[2] < sideSums[2])
    problem = f"Does triangle with sides {sideA}, {sideB} and {sideC} exist?"
    if exists:
        solution = "Yes"
        return problem, solution
    solution = "No"
    return problem, solution


def MidPointOfTwoPointFunc(maxValue=20):
    x1 = random.randint(-20, maxValue)
    y1 = random.randint(-20, maxValue)
    x2 = random.randint(-20, maxValue)
    y2 = random.randint(-20, maxValue)
    problem = f"({x1},{y1}),({x2},{y2})="
    solution = f"({(x1+x2)/2},{(y1+y2)/2})"
    return problem, solution


def factoringFunc(range_x1=10, range_x2=10):
    x1 = random.randint(-range_x1, range_x1)
    x2 = random.randint(-range_x2, range_x2)

    def intParser(z):
        if (z == 0):
            return ""
        if (z > 0):
            return "+" + str(z)
        if (z < 0):
            return "-" + str(abs(z))

    b = intParser(x1 + x2)
    c = intParser(x1 * x2)

    if (b == "+1"):
        b = "+"

    if (b == ""):
        problem = f"x^2{c}"
    else:
        problem = f"x^2{b}x{c}"

    x1 = intParser(x1)
    x2 = intParser(x2)
    solution = f"(x{x1})(x{x2})"
    return problem, solution


def thirdAngleOfTriangleFunc(maxAngle=89):
    angle1 = random.randint(1, maxAngle)
    angle2 = random.randint(1, maxAngle)
    angle3 = 180 - (angle1 + angle2)
    problem = f"Third angle of triangle with angles {angle1} and {angle2} = "
    solution = angle3
    return problem, solution


def systemOfEquationsFunc(range_x=10, range_y=10, coeff_mult_range=10):
    # Generate solution point first
    x = random.randint(-range_x, range_x)
    y = random.randint(-range_y, range_y)
    # Start from reduced echelon form (coeffs 1)
    c1 = [1, 0, x]
    c2 = [0, 1, y]

    def randNonZero():
        return random.choice([i for i in range(-coeff_mult_range, coeff_mult_range)
                              if i != 0])
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
        y_str = f'{y_coeff}y' if coeffs[1] != 0 else ('' if x_str != '' else '0')
        return f'{x_str}{op}{y_str} = {coeffs[2]}'

    problem = f"{coeffToFuncString(new_c1)}, {coeffToFuncString(new_c2)}"
    solution = f"x = {x}, y = {y}"
    return problem, solution

    # Add random (non-zero) multiple of equations to each other


def distanceTwoPointsFunc(maxValXY=20, minValXY=-20):
    point1X = random.randint(minValXY, maxValXY + 1)
    point1Y = random.randint(minValXY, maxValXY + 1)
    point2X = random.randint(minValXY, maxValXY + 1)
    point2Y = random.randint(minValXY, maxValXY + 1)
    distanceSq = (point1X - point2X) ** 2 + (point1Y - point2Y) ** 2
    solution = f"sqrt({distanceSq})"
    problem = f"Find the distance between ({point1X}, {point1Y}) and ({point2X}, {point2Y})"
    return problem, solution


def pythagoreanTheoremFunc(maxLength=20):
    a = random.randint(1, maxLength)
    b = random.randint(1, maxLength)
    c = (a**2 + b**2)**0.5
    problem = f"The hypotenuse of a right triangle given the other two lengths {a} and {b} = "
    solution = f"{c:.0f}" if c.is_integer() else f"{c:.2f}"
    return problem, solution


def linearEquationsFunc(n=2, varRange=20, coeffRange=20):
    if n > 10:
        print("[!] n cannot be greater than 10")
        return None, None

    vars = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'][:n]
    soln = [random.randint(-varRange, varRange) for i in range(n)]

    problem = list()
    solution = ", ".join(["{} = {}".format(vars[i], soln[i]) for i in range(n)])
    for _ in range(n):
        coeff = [random.randint(-coeffRange, coeffRange) for i in range(n)]
        res = sum([coeff[i] * soln[i] for i in range(n)])

        prob = ["{}{}".format(coeff[i], vars[i]) if coeff[i] != 0 else "" for i in range(n)]
        while "" in prob:
            prob.remove("")
        prob = " + ".join(prob) + " = " + str(res)
        problem.append(prob)

    problem = "\n".join(problem)
    return problem, solution


def primeFactorsFunc(minVal=1, maxVal=200):
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
    problem = f"Find prime factors of {a}"
    solution = f"{factors}"
    return problem, solution


def multiplyFractionsFunc(maxVal=10):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    c = random.randint(1, maxVal)
    d = random.randint(1, maxVal)
    while (a == b):
        b = random.randint(1, maxVal)
    while (c == d):
        d = random.randint(1, maxVal)

    def calculate_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    tmp_n = a * c
    tmp_d = b * d
    gcd = calculate_gcd(tmp_n, tmp_d)
    x = f"{tmp_n//gcd}/{tmp_d//gcd}"
    if (tmp_d == 1 or tmp_d == gcd):
        x = f"{tmp_n//gcd}"
    problem = f"({a}/{b})*({c}/{d})"
    solution = x
    return problem, solution


def regularPolygonAngleFunc(minVal=3, maxVal=20):
    sideNum = random.randint(minVal, maxVal)
    problem = f"Find the angle of a regular polygon with {sideNum} sides"
    exteriorAngle = round((360 / sideNum), 2)
    solution = 180 - exteriorAngle
    return problem, solution


def combinationsFunc(maxlength=20):

    def factorial(a):
        d = 1
        for i in range(a):
            a = (i + 1) * d
            d = a
        return d
    a = random.randint(10, maxlength)
    b = random.randint(0, 9)

    solution = int(factorial(a) / (factorial(b) * factorial(a - b)))
    problem = "Number of combinations from {} objects picked {} at a time ".format(a, b)

    return problem, solution


def factorialFunc(maxInput=6):
    a = random.randint(0, maxInput)
    n = a
    problem = str(a) + "! = "
    b = 1
    if a == 1:
        solution = str(b)
        return problem, solution
    else:
        while n > 0:
            b *= n
            n = n - 1
        solution = str(b)
        return problem, solution


def surfaceAreaCube(maxSide=20, unit='m'):
    a = random.randint(1, maxSide)
    problem = f"Surface area of cube with side = {a}{unit} is"
    ans = 6 * a * a
    solution = f"{ans} {unit}^2"
    return problem, solution


def volumeCube(maxSide=20, unit='m'):
    a = random.randint(1, maxSide)
    problem = f"Volume of cube with side = {a}{unit} is"
    ans = a * a * a
    solution = f"{ans} {unit}^3"
    return problem, solution


def surfaceAreaCuboid(maxSide=20, unit='m'):
    a = random.randint(1, maxSide)
    b = random.randint(1, maxSide)
    c = random.randint(1, maxSide)

    problem = f"Surface area of cuboid with sides = {a}{unit}, {b}{unit}, {c}{unit} is"
    ans = 2 * (a * b + b * c + c * a)
    solution = f"{ans} {unit}^2"
    return problem, solution


def volumeCuboid(maxSide=20, unit='m'):
    a = random.randint(1, maxSide)
    b = random.randint(1, maxSide)
    c = random.randint(1, maxSide)
    problem = f"Volume of cuboid with sides = {a}{unit}, {b}{unit}, {c}{unit} is"
    ans = a * b * c
    solution = f"{ans} {unit}^3"
    return problem, solution


def surfaceAreaCylinder(maxRadius=20, maxHeight=50, unit='m'):
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    problem = f"Surface area of cylinder with height = {a}{unit} and radius = {b}{unit} is"
    ans = int(2 * math.pi * a * b + 2 * math.pi * b * b)
    solution = f"{ans} {unit}^2"
    return problem, solution


def volumeCylinder(maxRadius=20, maxHeight=50, unit='m'):
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    problem = f"Volume of cylinder with height = {a}{unit} and radius = {b}{unit} is"
    ans = int(math.pi * b * b * a)
    solution = f"{ans} {unit}^3"
    return problem, solution


def surfaceAreaCone(maxRadius=20, maxHeight=50, unit='m'):
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    slopingHeight = math.sqrt(a**2 + b**2)
    problem = f"Surface area of cone with height = {a}{unit} and radius = {b}{unit} is"
    ans = int(math.pi * b * slopingHeight + math.pi * b * b)
    solution = f"{ans} {unit}^2"
    return problem, solution


def volumeCone(maxRadius=20, maxHeight=50, unit='m'):
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    problem = f"Volume of cone with height = {a}{unit} and radius = {b}{unit} is"
    ans = int(math.pi * b * b * a * (1 / 3))
    solution = f"{ans} {unit}^3"
    return problem, solution


def commonFactorsFunc(maxVal=100):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
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
    problem = f"Common Factors of {a} and {b} = "
    solution = arr
    return problem, solution


def intersectionOfTwoLinesFunc(
    minM=-10, maxM=10, minB=-10, maxB=10, minDenominator=1, maxDenominator=6
):
    def generateEquationString(m, b):
        """
        Generates an equation given the slope and intercept.
        It handles cases where m is fractional.
        It also ensures that we don't have weird signs such as y = mx + -b.
        """
        if m[1] == 1:
            m = m[0]
        else:
            m = f"{m[0]}/{m[1]}"
        base = f"y = {m}x"
        if b > 0:
            return f"{base} + {b}"
        elif b < 0:
            return f"{base} - {b * -1}"
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

    m1 = (random.randint(minM, maxM), random.randint(minDenominator, maxDenominator))
    m2 = (random.randint(minM, maxM), random.randint(minDenominator, maxDenominator))
    b1 = random.randint(minB, maxB)
    b2 = random.randint(minB, maxB)
    equation1 = generateEquationString(m1, b1)
    equation2 = generateEquationString(m2, b2)
    problem = "Find the point of intersection of the two lines: "
    problem += f"{equation1} and {equation2}"
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
        solution = f"({fractionToString(intersection_x)}, {fractionToString(intersection_y)})"
    return problem, solution


def permutationFunc(maxlength=20):
    a = random.randint(10, maxlength)
    b = random.randint(0, 9)
    solution = int(math.factorial(a) / (math.factorial(a - b)))
    problem = "Number of Permutations from {} objects picked {} at a time =  ".format(a, b)
    return problem, solution


def vectorCrossFunc(minVal=-20, maxVal=20):
    a = [random.randint(minVal, maxVal) for i in range(3)]
    b = [random.randint(minVal, maxVal) for i in range(3)]
    c = [a[1] * b[2] - a[2] * b[1],
         a[2] * b[0] - a[0] * b[2],
         a[0] * b[1] - a[1] * b[0]]
    return str(a) + " X " + str(b) + " = ", str(c)


def compareFractionsFunc(maxVal=10):
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

    if(first > second):
        solution = ">"
    elif(first < second):
        solution = "<"
    else:
        solution = "="

    problem = f"Which symbol represents the comparison between {a}/{b} and {c}/{d}?"
    return problem, solution


def simpleInterestFunc(maxPrinciple=10000, maxRate=10, maxTime=10):
    a = random.randint(1000, maxPrinciple)
    b = random.randint(1, maxRate)
    c = random.randint(1, maxTime)
    d = (a * b * c) / 100
    problem = "Simple interest for a principle amount of " + str(a) + " dollars, " + str(b) + "% rate of interest and for a time period of " + str(c) + " years is = "
    solution = round(d, 2)
    return problem, solution


def matrixMultiplicationFunc(maxVal=100):
    m = random.randint(2, 10)
    n = random.randint(2, 10)
    k = random.randint(2, 10)
    # generate matrices a and b
    a = []
    for r in range(m):
        a.append([])
        for c in range(n):
            a[r].append(random.randint(-maxVal, maxVal))

    b = []
    for r in range(n):
        b.append([])
        for c in range(k):
            b[r].append(random.randint(-maxVal, maxVal))

    res = []
    a_string = matrixMultiplicationFuncHelper(a)
    b_string = matrixMultiplicationFuncHelper(b)

    for r in range(m):
        res.append([])
        for c in range(k):
            temp = 0
            for t in range(n):
                temp += a[r][t] * b[t][c]
            res[r].append(temp)
    problem = f"Multiply \n{a_string}\n and \n\n{b_string}"  # consider using a, b instead of a_string, b_string if the problem doesn't look right
    solution = matrixMultiplicationFuncHelper(res)
    return problem, solution


def matrixMultiplicationFuncHelper(inp):
    m = len(inp)
    n = len(inp[0])
    string = ""
    for i in range(m):
        for j in range(n):
            string += f"{inp[i][j]: 6d}"
            string += "  "
        string += "\n"
    return string


def cubeRootFunc(minNo=1, maxNo=1000):
    b = random.randint(minNo, maxNo)
    a = b**(1 / 3)
    problem = "cuberoot of " + str(b) + " upto 2 decimal places is:"
    solution = str(round(a, 2))
    return problem, solution


def powerRuleIntegrationFunc(maxCoef=10, maxExp=10, maxTerms=5):
    numTerms = random.randint(1, maxTerms)
    problem = ""
    solution = ""
    for i in range(numTerms):
        if i > 0:
            problem += " + "
            solution += " + "
        coefficient = random.randint(1, maxCoef)
        exponent = random.randint(1, maxExp)
        problem += str(coefficient) + "x^" + str(exponent)
        solution += "(" + str(coefficient) + "/" + str(exponent) + ")x^" + str(exponent + 1)
    solution = solution + " + c"
    return problem, solution


def fourthAngleOfQuadriFunc(maxAngle=180):
    angle1 = random.randint(1, maxAngle)
    angle2 = random.randint(1, 240 - angle1)
    angle3 = random.randint(1, 340 - (angle1 + angle2))
    sum_ = angle1 + angle2 + angle3
    angle4 = 360 - sum_
    problem = f"Fourth angle of quadrilateral with angles {angle1} , {angle2}, {angle3} ="
    solution = angle4
    return problem, solution


def quadraticEquation(maxVal=100):
    a = random.randint(1, maxVal)
    c = random.randint(1, maxVal)
    b = random.randint(round(math.sqrt(4 * a * c)) + 1, round(math.sqrt(4 * maxVal * maxVal)))

    problem = "Zeros of the Quadratic Equation {}x^2+{}x+{}=0".format(a, b, c)

    D = math.sqrt(b * b - 4 * a * c)

    solution = str([round((-b + D) / (2 * a), 2), round((-b - D) / (2 * a), 2)])
    return problem, solution

def hcfFunc(maxVal=20):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    while(y):
        x, y = y, x % y
    problem = f"HCF of {a} and {b} = "
    solution = str(x)
    return problem, solution

def DiceSumProbFunc(maxDice=3):
    a = random.randint(1,maxDice)
    b = random.randint(a,6*a)
    count=0
    for i in [1,2,3,4,5,6]:
        if a==1:
            if i==b:
                count=count+1
        elif a==2:
            for j in [1,2,3,4,5,6]:
                if i+j==b:
                    count=count+1
        elif a==3:
            for j in [1,2,3,4,5,6]:
                for k in [1,2,3,4,5,6]:
                    if i+j+k==b:
                        count=count+1
    problem = "If {} dice are rolled at the same time, the probability of getting a sum of {} =".format(a,b)
    solution="{}/{}".format(count, 6**a)
    return problem, solution

def exponentiationFunc(maxBase = 20,maxExpo = 10):
    base = random.randint(1, maxBase)
    expo = random.randint(1, maxExpo)
    problem = f"{base}^{expo} ="
    solution = str(base ** expo)
    return problem, solution

def confidenceIntervalFunc():
    n=random.randint(20,40)
    j=random.randint(0,3)
    lst=random.sample(range(200,300),n)
    lst_per=[80 ,90, 95, 99]
    lst_t = [1.282, 1.645, 1.960, 2.576]
    mean=0
    sd=0
    for i in lst:
        count= i + mean
        mean=count
    mean = mean/n
    for i in lst:
        x=(i-mean)**2+sd
        sd=x
    sd=sd/n
    standard_error = lst_t[j]*math.sqrt(sd/n)
    problem= 'The confidence interval for sample {} with {}% confidence is'.format([x for x in lst], lst_per[j])
    solution= '({}, {})'.format(mean+standard_error, mean-standard_error)
    return problem, solution

def surdsComparisonFunc(maxValue = 100, maxRoot = 10):
    radicand1,radicand2 = tuple(random.sample(range(1,maxValue),2))
    degree1, degree2 = tuple(random.sample(range(1,maxRoot),2))
    problem = f"Fill in the blanks {radicand1}^(1/{degree1}) _ {radicand2}^(1/{degree2})"
    first = math.pow(radicand1, 1/degree1)
    second = math.pow(radicand2, 1/degree2)
    solution = "="
    if first > second:
        solution = ">"
    elif first < second:
        solution = "<"
    return problem, solution

def fibonacciSeriesFunc(minNo=1):
    n = random.randint(minNo,20)
    def createFibList(n):
        l=[]
        for i in range(n):
            if i<2:
                l.append(i)
            else:
                val = l[i-1]+l[i-2]
                l.append(val)
        return l
    fibList=createFibList(n)
    problem = "The Fibonacci Series of the first "+str(n)+" numbers is ?"
    solution = fibList
    return problem,solution

def basicTrigonometryFunc(angles=[0,30,45,60,90],functions=["sin","cos","tan"]): #Handles degrees in quadrant one
    angle=random.choice(angles)
    function=random.choice(functions)

    problem=f"What is {function}({angle})?"
    expression='math.'+function+'(math.radians(angle))'
    result_fraction_map={0.0:"0",0.5:"1/2",0.71:"1/√2",0.87:"√3/2",1.0:"1",0.58:"1/√3",1.73:"√3"}

    solution=result_fraction_map[round(eval(expression),2)] if round(eval(expression),2)<=99999 else "∞"  #for handling the ∞ condition

    return problem,solution

def sumOfAnglesOfPolygonFunc(maxSides = 12):
    side = random.randint(3, maxSides)
    sum = (side - 2) * 180
    problem = f"Sum of angles of polygon with {side} sides = "
    solution = sum
    return problem, solution

def dataSummaryFunc(number_values=15,minval=5,maxval=50):
    random_list=[]
    for i in range(number_values):
        n=random.randint(minval,maxval)
        random_list.append(n)
    a=sum(random_list)
    mean=a/number_values
    var=0
    for i in range(number_values):
        var+=(random_list[i]-mean)**2
    print(random_list)
    print(mean)
    print(var/number_values)
    print((var/number_values)**0.5)
    problem="Find the mean,standard deviation and variance for the data"+str(random_list)
    solution="The Mean is {} , Standard Deviation is {}, Variance is {}".format(mean,var/number_values,(var/number_values)**0.5)
    return problem,solution

def surfaceAreaSphere(maxSide = 20, unit = 'm'):
    r = random.randint(1, maxSide)

    problem = f"Surface area of Sphere with radius = {r}{unit} is"
    ans = 4 * math.pi * r * r
    solution = f"{ans} {unit}^2"
    return problem, solution
def volumeSphereFunc(maxRadius = 100):
    r=random.randint(1,maxRadius)
    problem=f"Volume of sphere with radius {r} m = "
    ans=(4*math.pi/3)*r*r*r
    solution = f"{ans} m^3"
    return problem,solution
# || Class Instances

# Format is:
# <title> = Generator("<Title>", <id>, <generalized problem>, <generalized solution>, <function name>)
addition = Generator("Addition", 0, "a+b=", "c", additionFunc)
subtraction = Generator("Subtraction", 1, "a-b=", "c", subtractionFunc)
multiplication = Generator("Multiplication", 2, "a*b=", "c", multiplicationFunc)
division = Generator("Division", 3, "a/b=", "c", divisionFunc)
binaryComplement1s = Generator("Binary Complement 1s", 4, "1010=", "0101", binaryComplement1sFunc)
moduloDivision = Generator("Modulo Division", 5, "a%b=", "c", moduloFunc)
squareRoot = Generator("Square Root", 6, "sqrt(a)=", "b", squareRootFunc)
powerRuleDifferentiation = Generator("Power Rule Differentiation", 7, "nx^m=", "(n*m)x^(m-1)", powerRuleDifferentiationFunc)
square = Generator("Square", 8, "a^2", "b", squareFunc)
lcm = Generator("LCM (Least Common Multiple)", 9, "LCM of a and b = ", "c", lcmFunc)
gcd = Generator("GCD (Greatest Common Denominator)", 10, "GCD of a and b = ", "c", gcdFunc)
basicAlgebra = Generator("Basic Algebra", 11, "ax + b = c", "d", basicAlgebraFunc)
log = Generator("Logarithm", 12, "log2(8)", "3", logFunc)
intDivision = Generator("Easy Division", 13, "a/b=", "c", divisionToIntFunc)
decimalToBinary = Generator("Decimal to Binary", 14, "Binary of a=", "b", DecimalToBinaryFunc)
binaryToDecimal = Generator("Binary to Decimal", 15, "Decimal of a=", "b", BinaryToDecimalFunc)
fractionDivision = Generator("Fraction Division", 16, "(a/b)/(c/d)=", "x/y", divideFractionsFunc)
intMatrix22Multiplication = Generator("Integer Multiplication with 2x2 Matrix", 17, "k * [[a,b],[c,d]]=", "[[k*a,k*b],[k*c,k*d]]", multiplyIntToMatrix22)
areaOfTriangle = Generator("Area of Triangle", 18, "Area of Triangle with side lengths a, b, c = ", "area", areaOfTriangleFunc)
doesTriangleExist = Generator("Triangle exists check", 19, "Does triangle with sides a, b and c exist?", "Yes/No", isTriangleValidFunc)
midPointOfTwoPoint = Generator("Midpoint of the two point", 20, "((X1,Y1),(X2,Y2))=", "((X1+X2)/2,(Y1+Y2)/2)", MidPointOfTwoPointFunc)
factoring = Generator("Factoring Quadratic", 21, "x^2+(x1+x2)+x1*x2", "(x-x1)(x-x2)", factoringFunc)
thirdAngleOfTriangle = Generator("Third Angle of Triangle", 22, "Third Angle of the triangle = ", "angle3", thirdAngleOfTriangleFunc)
systemOfEquations = Generator("Solve a System of Equations in R^2", 23, "2x + 5y = 13, -3x - 3y = -6", "x = -1, y = 3",systemOfEquationsFunc)
distance2Point = Generator("Distance between 2 points", 24, "Find the distance between (x1,y1) and (x2,y2)", "sqrt(distanceSquared)", distanceTwoPointsFunc)
pythagoreanTheorem = Generator("Pythagorean Theorem", 25, "The hypotenuse of a right triangle given the other two lengths a and b = ", "hypotenuse", pythagoreanTheoremFunc)
linearEquations = Generator("Linear Equations", 26, "2x+5y=20 & 3x+6y=12", "x=-20 & y=12", linearEquationsFunc)  # This has multiple variables whereas #23 has only x and y
primeFactors = Generator("Prime Factorisation", 27, "Prime Factors of a =", "[b, c, d, ...]", primeFactorsFunc)
fractionMultiplication = Generator("Fraction Multiplication", 28, "(a/b)*(c/d)=", "x/y", multiplyFractionsFunc)
angleRegularPolygon = Generator("Angle of a Regular Polygon", 29, "Find the angle of a regular polygon with 6 sides", "120", regularPolygonAngleFunc)
combinations = Generator("Combinations of Objects", 30, "Combinations available for picking 4 objects at a time from 6 distinct objects =", " 15", combinationsFunc)
factorial = Generator("Factorial", 31, "a! = ", "b", factorialFunc)
surfaceAreaCubeGen = Generator("Surface Area of Cube", 32, "Surface area of cube with side a units is", "b units^2", surfaceAreaCube)
surfaceAreaCuboidGen = Generator("Surface Area of Cuboid", 33, "Surface area of cuboid with sides = a units, b units, c units is", "d units^2", surfaceAreaCuboid)
surfaceAreaCylinderGen = Generator("Surface Area of Cylinder", 34, "Surface area of cylinder with height = a units and radius = b units is", "c units^2", surfaceAreaCylinder)
volumeCubeGen = Generator("Volum of Cube", 35, "Volume of cube with side a units is", "b units^3", volumeCube)
volumeCuboidGen = Generator("Volume of Cuboid", 36, "Volume of cuboid with sides = a units, b units, c units is", "d units^3", volumeCuboid)
volumeCylinderGen = Generator("Volume of cylinder", 37, "Volume of cylinder with height = a units and radius = b units is", "c units^3", volumeCylinder)
surfaceAreaConeGen = Generator("Surface Area of cone", 38, "Surface area of cone with height = a units and radius = b units is", "c units^2", surfaceAreaCone)
volumeConeGen = Generator("Volume of cone", 39, "Volume of cone with height = a units and radius = b units is", "c units^3", volumeCone)
commonFactors = Generator("Common Factors", 40, "Common Factors of {a} and {b} = ", "[c, d, ...]", commonFactorsFunc)
intersectionOfTwoLines = Generator("Intersection of Two Lines", 41, "Find the point of intersection of the two lines: y = m1*x + b1 and y = m2*x + b2", "(x, y)", intersectionOfTwoLinesFunc)
permutations = Generator("Permutations", 42, "Total permutations of 4 objects at a time from 10 objects is", "5040", permutationFunc)
vectorCross = Generator("Cross Product of 2 Vectors", 43, "a X b = ", "c", vectorCrossFunc)
compareFractions = Generator("Compare Fractions", 44, "Which symbol represents the comparison between a/b and c/d?", ">/</=", compareFractionsFunc)
simpleInterest = Generator("Simple Interest", 45, "Simple interest for a principle amount of a dollars, b% rate of interest and for a time period of c years is = ", "d dollars", simpleInterestFunc)
matrixMultiplication = Generator("Multiplication of two matrices", 46, "Multiply two matrices A and B", "C", matrixMultiplicationFunc)
CubeRoot = Generator("Cube Root", 47, "Cuberoot of a upto 2 decimal places is", "b", cubeRootFunc)
powerRuleIntegration = Generator("Power Rule Integration", 48, "nx^m=", "(n/m)x^(m+1)", powerRuleIntegrationFunc)
fourthAngleOfQuadrilateral = Generator("Fourth Angle of Quadrilateral", 49, "Fourth angle of Quadrilateral with angles a,b,c =", "angle4", fourthAngleOfQuadriFunc)
quadraticEquationSolve = Generator("Quadratic Equation", 50, "Find the zeros {x1,x2} of the quadratic equation ax^2+bx+c=0", "x1,x2", quadraticEquation)
hcf = Generator("HCF (Highest Common Factor)", 51, "HCF of a and b = ", "c", hcfFunc)
diceSumProbability=Generator("Probability of a certain sum appearing on faces of dice", 52,"If n dices are rolled then probabilty of getting sum of x is =","z", DiceSumProbFunc)
exponentiation = Generator("Exponentiation", 53,"a^b = ","c",exponentiationFunc)
confidenceInterval = Generator("Confidence interval For sample S", 54, "With X% confidence", "is (A,B)", confidenceIntervalFunc)
surdsComparison = Generator("Comparing surds", 55, "Fill in the blanks a^(1/b) _ c^(1/d)", "</>/=", surdsComparisonFunc)
fibonacciSeries = Generator("Fibonacci Series",56,"fibonacci series of first a numbers","prints the fibonacci series starting from 0 to a",fibonacciSeriesFunc)
basicTrigonometry=Generator("Trigonometric Values",57,"What is sin(X)?","ans",basicTrigonometryFunc)
sumOfAnglesOfPolygon = Generator("Sum of Angles of Polygon", 58, "Sum of angles of polygon with n sides = ", "sum", sumOfAnglesOfPolygonFunc)
dataSummary = Generator("Mean,Standard Deviation,Variance", 59, "a,b,c", "Mean:a+b+c/3,Std,Var", dataSummaryFunc)
surfaceAreaSphereGen = Generator("Surface Area of Sphere", 59, "Surface area of sphere with radius = a units is","d units^2", surfaceAreaSphere)
volumeSphere=Generator("Volume of Sphere",60,"Volume of sphere with radius r m = ","(4*pi/3)*r*r*r",volumeSphereFunc)
