import random

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

def additionFunc(maxSum = 99, maxAddend = 50):
    a = random.randint(0, maxAddend)
    b = random.randint(0, min((maxSum-a), maxAddend)) #The highest value of b will be no higher than the maxsum minus the first number and no higher than the maxAddend as well
    c = a+b
    problem = str(a) + "+" + str(b) + "="
    solution = str(c)
    return problem, solution

def subtractionFunc(maxMinuend = 99, maxDiff = 99):
    a = random.randint(0, maxMinuend)
    b = random.randint(max(0, (a-maxDiff)), a)
    c = a-b
    problem = str(a) + "-" + str(b) + "="
    solution = str(c)
    return problem, solution

def multiplicationFunc(maxRes = 99, maxMulti = 99):
    a = random.randint(0, maxMulti)
    b = random.randint(0, min(int(maxMulti/a), maxRes))
    c = a*b
    problem = str(a) + "*" + str(b) + "="
    solution = str(c)
    return problem, solution

def divisionFunc(maxRes = 99, maxDivid = 99):
    a = random.randint(0, maxDivid)
    b = random.randint(0, min(maxRes, maxDivid))
    c = a/b
    problem = str(a) + "/" + str(b) + "="
    solution = str(c)
    return problem, solution

def binaryComplement1sFunc(maxDigits = 10):
    question = ''
    answer = ''
    for i in range(random.randint(1,maxDigits)):
        temp = str(random.randint(0, 1))
        question += temp
        answer += "0" if temp == "1" else "1"

    problem = question
    solution = answer
    return problem, solution

def moduloFunc(maxRes = 99, maxModulo= 99):
    a = random.randint(0, maxModulo)
    b = random.randint(0, min(maxRes, maxModulo))
    c = a%b
    problem = str(a) + "%" + str(b) + "="
    solution = str(c)
    return problem, solution

def squareRootFunc(minNo = 1, maxNo = 12):
    b = random.randint(minNo, maxNo)
    a = b*b
    problem = "sqrt(" + str(a) + ")="
    solution = str(b)
    return problem, solution

def powerRuleDifferentiationFunc(maxCoef = 10, maxExp = 10, maxTerms = 5):
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

def squareFunc(maxSquareNum = 20):
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
    problem = f"LCM of {a} and {b} = "
    solution = str(d)
    return problem, solution

def basicAlgebraFunc(maxVariable = 10):
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
    elif a == 1 or a == i :
        x = f"{c - b}"
    problem = f"{a}x + {b} = {c}"
    solution = x
    return problem, solution

def logFunc(maxBase=3, maxVal=8):
    a = random.randint(1, maxVal)
    b = random.randint(2, maxBase)
    c = pow(b,a)
    problem = "log"+str(b)+"("+str(c)+")"
    solution = str(a)
    return problem, solution

def divisionToIntFunc(maxA=25, maxB=25):
    a = random.randint(1,maxA)
    b = random.randint(1,maxB)
    divisor = a*b
    dividend=random.choice([a,b])
    problem = f"{divisor}/{dividend} = "
    solution=int(divisor/dividend)
    return problem,solution

def DecimalToBinaryFunc(max_dec=99):
    a = random.randint(1, max_dec)
    b = bin(a).replace("0b", "")
    problem = "Binary of "+str(a)+"="
    solution = str(b)
    return problem, solution

def BinaryToDecimalFunc(max_dig=10):
	problem=''
	for i in range(random.randint(1,max_dig)):
		temp = str(random.randint(0, 1))
		problem += temp

	solution=int(problem, 2);
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

def multiplyIntToMatrix22(maxMatrixVal = 10, maxRes = 100):
    a = random.randint(0, maxMatrixVal)
    b = random.randint(0, maxMatrixVal)
    c = random.randint(0, maxMatrixVal)
    d = random.randint(0, maxMatrixVal)
    constant = random.randint(0, int(maxRes/max(a,b,c,d)))
    problem = f"{constant} * [[{a}, {b}], [{c}, {d}]] = "
    solution = f"[[{a*constant},{b*constant}],[{c*constant},{d*constant}]]"
    return problem, solution

def areaOfTriangleFunc(maxA=20, maxB=20, maxC=20):
	a = random.randint(1, maxA)
	b = random.randint(1, maxB)
	c = random.randint(1, maxC)
	s = (a+b+c)/2
	area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
	problem = "Area of triangle with side lengths: "+ str(a) +" "+ str(b) +" "+ str(c) + " = " 
	solution = area
	return problem, solution

def isTriangleValidFunc(maxSideLength = 50):
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
	x1=random.randint(-20,maxValue)
	y1=random.randint(-20,maxValue)
	x2=random.randint(-20,maxValue)
	y2=random.randint(-20,maxValue)
	problem=f"({x1},{y1}),({x2},{y2})="
	solution=f"({(x1+x2)/2},{(y1+y2)/2})"
	return problem,solution

def factoringFunc(range_x1 = 10, range_x2 = 10):
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

# || Class Instances

#Format is:
#<title> = Generator("<Title>", <id>, <generalized problem>, <generalized solution>, <function name>)
addition = Generator("Addition", 0, "a+b=", "c", additionFunc)
subtraction = Generator("Subtraction", 1, "a-b=", "c", subtractionFunc)
multiplication = Generator("Multiplication", 2, "a*b=", "c", multiplicationFunc)
division = Generator("Division", 3, "a/b=", "c", divisionFunc)
binaryComplement1s = Generator("Binary Complement 1s", 4, "1010=", "0101", binaryComplement1sFunc)
moduloDivision = Generator("Modulo Division", 5, "a%b=", "c", moduloFunc)
squareRoot = Generator("Square Root", 6, "sqrt(a)=", "b", squareRootFunc)
powerRuleDifferentiation = Generator("Power Rule Differentiation", 7, "nx^m=", "(n*m)x^(m-1)", powerRuleDifferentiationFunc)
square = Generator("Square", 8,"a^2", "b", squareFunc)
lcm = Generator("LCM (Least Common Multiple)", 9, "LCM of a and b = ", "c", lcmFunc)
gcd = Generator("GCD (Greatest Common Denominator)", 10, "GCD of a and b = ", "c", gcdFunc)
basicAlgebra = Generator("Basic Algebra", 11, "ax + b = c", "d", basicAlgebraFunc)
log = Generator("Logarithm", 12, "log2(8)", "3", logFunc)
intDivision = Generator("Easy Division", 13,"a/b=","c",divisionToIntFunc)
decimalToBinary = Generator("Decimal to Binary",14,"Binary of a=","b",DecimalToBinaryFunc)
binaryToDecimal = Generator("Binary to Decimal",15,"Decimal of a=","b",BinaryToDecimalFunc)
fractionDivision = Generator("Fraction Division", 16, "(a/b)/(c/d)=", "x/y", divideFractionsFunc)
intMatrix22Multiplication = Generator("Integer Multiplication with 2x2 Matrix", 17, "k * [[a,b],[c,d]]=", "[[k*a,k*b],[k*c,k*d]]", multiplyIntToMatrix22)
areaOfTriangle = Generator("Area of Triangle", 18, "Area of Triangle with side lengths a, b, c = ", "area", areaOfTriangleFunc)
doesTriangleExist = Generator("Triangle exists check", 19, "Does triangle with sides a, b and c exist?","Yes/No", isTriangleValidFunc)
midPointOfTwoPoint=Generator("Midpoint of the two point", 20,"((X1,Y1),(X2,Y2))=","((X1+X2)/2,(Y1+Y2)/2)",MidPointOfTwoPointFunc)
factoring = Generator("Subtraction", 21, "x^2+(x1+x2)+x1*x2", "(x-x1)(x-x2)", factoringFunc)