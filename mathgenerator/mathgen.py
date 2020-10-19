import random
import math
import fractions
from .funcs import *

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

#
def getGenList():
    return(genList)

# Format is:
# <title> = Generator("<Title>", <id>, <generalized problem>, <generalized solution>, <function name>)
# Funcs_start - DO NOT REMOVE!
addition = Generator("Addition", 0, "a+b=", "c", additionFunc)
subtraction = Generator("Subtraction", 1, "a-b=", "c", subtractionFunc)
multiplication = Generator("Multiplication", 2, "a*b=", "c", multiplicationFunc)
division = Generator("Division", 3, "a/b=", "c", divisionFunc)
binaryComplement1s = Generator("Binary Complement 1s", 4, "1010=", "0101", binaryComplement1sFunc)
moduloDivision = Generator("Modulo Division", 5, "a%b=", "c", moduloFunc)
squareRoot = Generator("Square Root", 6, "sqrt(a)=", "b", squareRootFunc)
powerRuleDifferentiation = Generator("Power Rule Differentiation", 7, "nx^m=", "(n*m)x^(m-1)", powerRuleDifferentiationFunc)
square = Generator("Square", 8, "a^2", "b", squareFunc)
lcm = Generator("LCM (Least Common Multiple)", 9,"LCM of a and b = ", "c", lcmFunc)
gcd = Generator("GCD (Greatest Common Denominator)", 10, "GCD of a and b = ", "c", gcdFunc)
basicAlgebra = Generator("Basic Algebra", 11, "ax + b = c", "d", basicAlgebraFunc)
log = Generator("Logarithm", 12, "log2(8)", "3", logFunc)
intDivision = Generator("Easy Division", 13, "a/b=", "c", divisionToIntFunc)
decimalToBinary = Generator("Decimal to Binary", 14,"Binary of a=", "b", DecimalToBinaryFunc)
binaryToDecimal = Generator("Binary to Decimal", 15,"Decimal of a=", "b", BinaryToDecimalFunc)
fractionDivision = Generator("Fraction Division", 16, "(a/b)/(c/d)=", "x/y", divideFractionsFunc)
intMatrix22Multiplication = Generator("Integer Multiplication with 2x2 Matrix",17, "k * [[a,b],[c,d]]=", "[[k*a,k*b],[k*c,k*d]]", multiplyIntToMatrix22)
areaOfTriangle = Generator("Area of Triangle", 18, "Area of Triangle with side lengths a, b, c = ", "area", areaOfTriangleFunc)
doesTriangleExist = Generator("Triangle exists check", 19,"Does triangle with sides a, b and c exist?", "Yes/No", isTriangleValidFunc)
midPointOfTwoPoint = Generator("Midpoint of the two point", 20,"((X1,Y1),(X2,Y2))=", "((X1+X2)/2,(Y1+Y2)/2)", MidPointOfTwoPointFunc)
factoring = Generator("Factoring Quadratic", 21, "x^2+(x1+x2)+x1*x2", "(x-x1)(x-x2)", factoringFunc)
thirdAngleOfTriangle = Generator("Third Angle of Triangle", 22, "Third Angle of the triangle = ", "angle3", thirdAngleOfTriangleFunc)
systemOfEquations = Generator("Solve a System of Equations in R^2", 23, "2x + 5y = 13, -3x - 3y = -6", "x = -1, y = 3", systemOfEquationsFunc)
distance2Point = Generator("Distance between 2 points", 24, "Find the distance between (x1,y1) and (x2,y2)", "sqrt(distanceSquared)", distanceTwoPointsFunc)
pythagoreanTheorem = Generator("Pythagorean Theorem", 25, "The hypotenuse of a right triangle given the other two lengths a and b = ", "hypotenuse", pythagoreanTheoremFunc)
linearEquations = Generator("Linear Equations", 26, "2x+5y=20 & 3x+6y=12", "x=-20 & y=12", linearEquationsFunc)# This has multiple variables whereas #23 has only x and y
primeFactors = Generator("Prime Factorisation", 27, "Prime Factors of a =", "[b, c, d, ...]", primeFactorsFunc)
fractionMultiplication = Generator("Fraction Multiplication", 28, "(a/b)*(c/d)=", "x/y", multiplyFractionsFunc)
angleRegularPolygon = Generator("Angle of a Regular Polygon", 29,"Find the angle of a regular polygon with 6 sides", "120", regularPolygonAngleFunc)
combinations = Generator("Combinations of Objects", 30, "Combinations available for picking 4 objects at a time from 6 distinct objects =", " 15", combinationsFunc)
factorial = Generator("Factorial", 31, "a! = ", "b", factorialFunc)
surfaceAreaCubeGen = Generator("Surface Area of Cube", 32, "Surface area of cube with side a units is", "b units^2", surfaceAreaCube)
surfaceAreaCuboidGen = Generator("Surface Area of Cuboid", 33, "Surface area of cuboid with sides = a units, b units, c units is", "d units^2", surfaceAreaCuboid)
surfaceAreaCylinderGen = Generator("Surface Area of Cylinder", 34, "Surface area of cylinder with height = a units and radius = b units is", "c units^2", surfaceAreaCylinder)
volumeCubeGen = Generator("Volum of Cube", 35, "Volume of cube with side a units is", "b units^3", volumeCube)
volumeCuboidGen = Generator("Volume of Cuboid", 36, "Volume of cuboid with sides = a units, b units, c units is", "d units^3", volumeCuboid)
volumeCylinderGen = Generator( "Volume of cylinder", 37, "Volume of cylinder with height = a units and radius = b units is", "c units^3", volumeCylinder)
surfaceAreaConeGen = Generator( "Surface Area of cone", 38, "Surface area of cone with height = a units and radius = b units is", "c units^2", surfaceAreaCone)
volumeConeGen = Generator( "Volume of cone", 39, "Volume of cone with height = a units and radius = b units is", "c units^3", volumeCone)
commonFactors = Generator("Common Factors", 40, "Common Factors of {a} and {b} = ", "[c, d, ...]", commonFactorsFunc)
intersectionOfTwoLines = Generator("Intersection of Two Lines", 41,"Find the point of intersection of the two lines: y = m1*x + b1 and y = m2*x + b2", "(x, y)", intersectionOfTwoLinesFunc)
permutations = Generator("Permutations", 42, "Total permutations of 4 objects at a time from 10 objects is", "5040", permutationFunc)
vectorCross = Generator("Cross Product of 2 Vectors",43, "a X b = ", "c", vectorCrossFunc)
compareFractions = Generator("Compare Fractions", 44, "Which symbol represents the comparison between a/b and c/d?", ">/</=", compareFractionsFunc)
simpleInterest = Generator("Simple Interest", 45, "Simple interest for a principle amount of a dollars, b% rate of interest and for a time period of c years is = ", "d dollars", simpleInterestFunc)
matrixMultiplication = Generator("Multiplication of two matrices",46, "Multiply two matrices A and B", "C", matrixMultiplicationFunc)
CubeRoot = Generator("Cube Root", 47, "Cuberoot of a upto 2 decimal places is", "b", cubeRootFunc)
powerRuleIntegration = Generator("Power Rule Integration", 48, "nx^m=", "(n/m)x^(m+1)", powerRuleIntegrationFunc)
fourthAngleOfQuadrilateral = Generator("Fourth Angle of Quadrilateral", 49,"Fourth angle of Quadrilateral with angles a,b,c =", "angle4", fourthAngleOfQuadriFunc)
quadraticEquationSolve = Generator("Quadratic Equation", 50, "Find the zeros {x1,x2} of the quadratic equation ax^2+bx+c=0", "x1,x2", quadraticEquation)
hcf = Generator("HCF (Highest Common Factor)", 51,"HCF of a and b = ", "c", hcfFunc)
diceSumProbability = Generator("Probability of a certain sum appearing on faces of dice",52, "If n dices are rolled then probabilty of getting sum of x is =", "z", DiceSumProbFunc)
exponentiation = Generator("Exponentiation", 53, "a^b = ", "c", exponentiationFunc)
confidenceInterval = Generator("Confidence interval For sample S",54, "With X% confidence", "is (A,B)", confidenceIntervalFunc)
surdsComparison = Generator("Comparing surds", 55, "Fill in the blanks a^(1/b) _ c^(1/d)", "</>/=", surdsComparisonFunc)
fibonacciSeries = Generator("Fibonacci Series", 56, "fibonacci series of first a numbers","prints the fibonacci series starting from 0 to a", fibonacciSeriesFunc)
basicTrigonometry = Generator("Trigonometric Values", 57, "What is sin(X)?", "ans", basicTrigonometryFunc)
sumOfAnglesOfPolygon = Generator("Sum of Angles of Polygon", 58,"Sum of angles of polygon with n sides = ", "sum", sumOfAnglesOfPolygonFunc)
dataSummary = Generator("Mean,Standard Deviation,Variance",59, "a,b,c", "Mean:a+b+c/3,Std,Var", dataSummaryFunc)
surfaceAreaSphereGen = Generator("Surface Area of Sphere", 60, "Surface area of sphere with radius = a units is", "d units^2", surfaceAreaSphere)
volumeSphere = Generator("Volume of Sphere", 61, "Volume of sphere with radius r m = ", "(4*pi/3)*r*r*r", volumeSphereFunc)
nthFibonacciNumberGen = Generator("nth Fibonacci number", 62, "What is the nth Fibonacci number", "Fn", nthFibonacciNumberFunc)
profitLossPercent = Generator("Profit or Loss Percent", 63, "Profit/ Loss percent when CP = cp and SP = sp is: ", "percent", profitLossPercentFunc)
binaryToHex = Generator("Binary to Hexidecimal", 64, "Hexidecimal of a=", "b", binaryToHexFunc)
complexNumMultiply = Generator("Multiplication of 2 complex numbers", 65, "(x + j) (y + j) = ", "xy + xj + yj -1", multiplyComplexNumbersFunc)
geometricprogression=Generator("Geometric Progression", 66, "Initial value,Common Ratio,nth Term,Sum till nth term =", "a,r,ar^n-1,sum(ar^n-1", geomProgrFunc)
geometricMean=Generator("Geometric Mean of N Numbers",67,"Geometric mean of n numbers A1 , A2 , ... , An = ","(A1*A2*...An)^(1/n) = ans",geometricMeanFunc)
harmonicMean=Generator("Harmonic Mean of N Numbers",68,"Harmonic mean of n numbers A1 , A2 , ... , An = "," n/((1/A1) + (1/A2) + ... + (1/An)) = ans",harmonicMeanFunc)
eucldianNorm=Generator("Euclidian norm or L2 norm of a vector", 69, "Euclidian Norm of a vector V:[v1, v2, ......., vn]", "sqrt(v1^2 + v2^2 ........ +vn^2)", euclidianNormFunc)
angleBtwVectors=Generator("Angle between 2 vectors", 70, "Angle Between 2 vectors V1=[v11, v12, ..., v1n] and V2=[v21, v22, ....., v2n]", "V1.V2 / (euclidNorm(V1)*euclidNorm(V2))", angleBtwVectorsFunc)
absoluteDifference=Generator("Absolute difference between two numbers", 71, "Absolute difference betweeen two numbers a and b =", "|a-b|", absoluteDifferenceFunc)
vectorDot = Generator("Dot Product of 2 Vectors", 72, "a . b = ", "c", vectorDotFunc)
binary2sComplement = Generator("Binary 2's Complement", 73, "2's complement of 11010110 =", "101010", binary2sComplementFunc)
invertmatrix = Generator("Inverse of a Matrix", 74, "Inverse of a matrix A is", "A^(-1)", matrixInversion)
compoundInterest = Generator("Compound Interest", 75, "Compound interest for a principle amount of p dollars, r% rate of interest and for a time period of t years with n times compounded annually is = ", "A dollars", compoundInterestFunc)
