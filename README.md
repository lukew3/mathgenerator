# mathgenerator

A math problem generator, created for the purpose of giving self-studying students and teaching organizations the means to easily get access to random math problems to suit their needs.

To try out generators, go to <https://todarith.ml/generate/>

If you have an idea for a generator, please add it as an issue and tag it with the "New Generator" label.

## Usage

The project can be install via pip

```bash
pip install mathgenerator
```

Here is an example of how you would generate an addition problem:

```python
from mathgenerator import mathgen

#generate an addition problem
problem, solution = mathgen.addition()

#another way to generate an addition problem using genById()
problem, solution = mathgen.genById(0)
```

## List of Generators

| Id   | Skill                             | Example problem    | Example Solution      | Function Name            |
|------|-----------------------------------|--------------------|-----------------------|--------------------------|
[//]: # list start
| 0 | Addition | 24+32= | 56 | addition |
| 1 | Subtraction | 14-4= | 10 | subtractionFunc |
| 2 | Multiplication | 28*3= | 84 | multiplicationFunc |
| 3 | Division | 55/39= | 1.4102564102564104 | divisionFunc |
| 4 | Binary Complement 1s | 1010000= | 0101111 | binaryComplement1sFunc |
| 5 | Modulo Division | 74%21= | 11 | moduloFunc |
| 6 | Square Root | sqrt(1)= | 1 | squareRootFunc |
| 7 | Power Rule Differentiation | 6x^5 + 10x^4 + 10x^9 | 30x^4 + 40x^3 + 90x^8 | powerRuleDifferentiationFunc |
| 8 | Square | 17^2= | 289 | squareFunc |
| 9 | LCM (Least Common Multiple) | LCM of 6 and 13 = | 78 | lcmFunc |
| 10 | GCD (Greatest Common Denominator) | GCD of 1 and 3 =  | 1 | gcdFunc |
| 11 | Basic Algebra | 3x + 9 = 9 | 0 | basicAlgebraFunc |
| 12 | Logarithm | log3(2187) | 7 | logFunc |
| 13 | Easy Division | 275/11 =  | 25 | divisionToIntFunc |
| 14 | Decimal to Binary | Binary of 87= | 1010111 | DecimalToBinaryFunc |
| 15 | Binary to Decimal | 01111 | 15 | BinaryToDecimalFunc |
| 16 | Fraction Division | (1/8)/(8/1) | 1/64 | divideFractionsFunc |
| 17 | Integer Multiplication with 2x2 Matrix | 7 * [[7, 6], [1, 4]] =  | [[49,42],[7,28]] | multiplyIntToMatrix22 |
| 18 | Area of Triangle | Area of triangle with side lengths: 8 5 18 =  | (3.3825325984308986e-15+55.24094948496088j) | areaOfTriangleFunc |
| 19 | Triangle exists check | Does triangle with sides 22, 8 and 3 exist? | No | isTriangleValidFunc |
| 20 | Midpoint of the two point | (17,-8),(-14,-2)= | (1.5,-5.0) | MidPointOfTwoPointFunc |
| 21 | Factoring Quadratic | x^2+x-20 | (x+5)(x-4) | factoringFunc |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 36 and 55 =  | 89 | thirdAngleOfTriangleFunc |
| 23 | Solve a System of Equations in R^2 | 2x - 7y = 56, -8x + 2y = 36 | x = -7, y = -10 | systemOfEquationsFunc |
| 24 | Distance between 2 points | Find the distance between (2, 19) and (3, 7) | sqrt(145) | distanceTwoPointsFunc |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 16 and 7 =  | 17.46 | pythagoreanTheoremFunc |
| 26 | Linear Equations | -14x + -15y = 219
8x = -48 | x = -6, y = -9 | linearEquationsFunc |
| 27 | Prime Factorisation | Find prime factors of 73 | [73] | primeFactorsFunc |
| 28 | Fraction Multiplication | (8/10)*(6/5) | 24/25 | multiplyFractionsFunc |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 15 sides | 156.0 | regularPolygonAngleFunc |
| 30 | Combinations of Objects | Number of combinations from 15 objects picked 8 at a time  | 6435 | combinationsFunc |
| 31 | Factorial | 4! =  | 24 | factorialFunc |
| 32 | Surface Area of Cube | Surface area of cube with side = 15m is | 1350 m^2 | surfaceAreaCube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 18m, 11m, 19m is | 1498 m^2 | surfaceAreaCuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 38m and radius = 16m is | 5428 m^2 | surfaceAreaCylinder |
| 35 | Volum of Cube | Volume of cube with side = 5m is | 125 m^3 | volumeCube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 3m, 11m, 3m is | 99 m^3 | volumeCuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 20m and radius = 7m is | 3078 m^3 | volumeCylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 23m and radius = 2m is | 157 m^2 | surfaceAreaCone |
| 39 | Volume of cone | Volume of cone with height = 44m and radius = 5m is | 1151 m^3 | volumeCone |
| 40 | Common Factors | Common Factors of 99 and 93 =  | [1, 3] | commonFactorsFunc |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 10/3x - 8 and y = -10x + 4 | (9/10, -5) | intersectionOfTwoLinesFunc |
| 42 | Permutations | Number of Permutations from 19 objects picked 5 at a time =   | 1395360 | permutationFunc |
| 43 | Cross Product of 2 Vectors | [0, 2, -6] X [4, 13, 15] =  | [108, -24, -8] | vectorCrossFunc |
| 44 | Compare Fractions | Which symbol represents the comparison between 1/7 and 7/10? | < | compareFractionsFunc |
| 45 | Simple Interest | Simple interest for a principle amount of 9501 dollars, 10% rate of interest and for a time period of 10 years is =  | 9501.0 | simpleInterestFunc |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>-10</td><td>6</td></tr><tr><td>2</td><td>-4</td></tr><tr><td>1</td><td>-8</td></tr><tr><td>-7</td><td>4</td></tr></table>and<table><tr><td>-5</td><td>-2</td></tr><tr><td>-3</td><td>-8</td></tr></table> | <table><tr><td>32</td><td>-28</td></tr><tr><td>2</td><td>28</td></tr><tr><td>19</td><td>62</td></tr><tr><td>23</td><td>-18</td></tr></table> | matrixMultiplicationFunc |
| 47 | Cube Root | cuberoot of 100 upto 2 decimal places is: | 4.64 | cubeRootFunc |
| 48 | Power Rule Integration | 9x^9 | (9/9)x^10 + c | powerRuleIntegrationFunc |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 29 , 84, 126 = | 121 | fourthAngleOfQuadriFunc |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 39x^2+176x+64=0 | [-0.4, -4.11] | quadraticEquation |
| 51 | HCF (Highest Common Factor) | HCF of 7 and 9 =  | 1 | hcfFunc |
| 52 | Probability of a certain sum appearing on faces of dice | If 3 dice are rolled at the same time, the probability of getting a sum of 13 = | 21/216 | DiceSumProbFunc |
| 53 | Exponentiation | 6^4 = | 1296 | exponentiationFunc |
| 54 | Confidence interval For sample S | The confidence interval for sample [293, 222, 227, 237, 299, 265, 238, 273, 229, 236, 286, 243, 220, 233, 224, 226, 257, 285, 268, 271, 247, 262] with 90% confidence is | (260.4441418746136, 243.28313085265916) | confidenceIntervalFunc |
| 55 | Comparing surds | Fill in the blanks 66^(1/5) _ 74^(1/6) | > | surdsComparisonFunc |
| 56 | Fibonacci Series | The Fibonacci Series of the first 18 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597] | fibonacciSeriesFunc |
| 57 | Trigonometric Values | What is sin(0)? | 0 | basicTrigonometryFunc |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 4 sides =  | 360 | sumOfAnglesOfPolygonFunc |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[31, 20, 40, 14, 41, 42, 12, 18, 26, 41, 16, 48, 37, 30, 18] | The Mean is 28.933333333333334 , Standard Deviation is 134.86222222222221, Variance is 11.61301951355556 | dataSummaryFunc |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 16m is | 3216.990877275948 m^2 | surfaceAreaSphere |
| 61 | Volume of Sphere | Volume of sphere with radius 10 m =  | 4188.790204786391 m^3 | volumeSphereFunc |
| 62 | nth Fibonacci number | What is the 65th Fibonacci number? | 17167680177565 | nthFibonacciNumberFunc |
| 63 | Profit or Loss Percent | Loss percent when CP = 639 and SP = 20 is:  | 96.87010954616588 | profitLossPercentFunc |
| 64 | Binary to Hexidecimal | 10000010 | 0x82 | binaryToHexFunc |
| 65 | Multiplication of 2 complex numbers | (-16-5j) * (13+4j) =  | (-188-129j) | multiplyComplexNumbersFunc |
| 66 | Geometric Progression | For the given GP [5, 30, 180, 1080, 6480, 38880] ,Find the value of a,common ratio,7th term value, sum upto 11th term | The value of a is 5, common ratio is 6 , 7th term is 233280 , sum upto 11th term is 362797055.0 | geomProgrFunc |
| 67 | Geometric Mean of N Numbers | Geometric mean of 3 numbers 12 , 76 and 88 =  | (12*76*88)^(1/3) = 43.134606135637426 | geometricMeanFunc |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 4 numbers 32 , 82 , 98 , 59 =  |  4/((1/32) + (1/82) + (1/98) + (1/59)) = 56.658543052293126 | harmonicMeanFunc |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[30.49374303007102, 744.9799127067523, 232.71392717506222, 219.07162873155772, 268.6667105157799, 655.700721848602, 630.8781230231998, 525.0331442958861, 603.1960329056955] is: | 1482.467804008134 | euclidianNormFunc |
| 70 | Angle between 2 vectors | angle between the vectors [411.45287273810993, 475.5310005335923, 585.8235737751623, 654.4447552592987, 7.9372591993011055, 944.1669660662357, 82.85267978544842, 855.1153353684535, 401.897628624623, 208.74276524448533, 18.113378046332063, 329.92425644581766, 656.1658677733768] and [340.21944929120787, 595.8624349766976, 458.3226781953552, 460.8316651658132, 237.2935680919427, 562.2537489196774, 705.3352878976389, 21.91461098842251, 950.6814899692208, 879.1343421626799, 177.86771165838067, 867.0564995964864, 762.591298578088] is: | NaN | angleBtwVectorsFunc |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -22 and 85 =  | 107 | absoluteDifferenceFunc |
| 72 | Dot Product of 2 Vectors | [-4, -15, -19] . [-12, -18, -13] =  | 565 | vectorDotFunc |
| 73 | Binary 2's Complement | 2's complement of  = |  | binary2sComplement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[23, 14, 90], [15, 42, 7], [37, 19, 79]]) is: | Matrix([[-3185/53919, -604/53919, 3682/53919], [926/53919, 1513/53919, -1189/53919], [47/1997, -3/1997, -28/1997]]) | matrixInversion |
| 75 | Area of a Sector | Given radius, 32 and angle, 182. Find the area of the sector. | Area of sector = 1626.36761 | sectorAreaFunc |
| 76 | Mean and Median | Given the series of numbers [83, 63, 31, 44, 12, 73, 42, 51, 93, 3]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 49.5 and Arithmetic median of this series is 47.5 | meanMedianFunc |
| 77 | Determinant to 2x2 Matrix | Det([[35, 67], [54, 48]]) =  |  -1938 | determinantToMatrix22 |
| 78 | Compound Interest | Compound Interest for a principle amount of 4487 dollars, 5% rate of interest and for a time period of 9 compounded monthly is =  | 4487.0 | compoundInterestFunc |
| 79 | Decimal to Hexadecimal | Binary of 992= | 0x3e0 | deciToHexaFunc |
| 80 | Percentage of a number | What is 37% of 83? | Required percentage = 30.71% | percentageFunc |
| 81 | Celsius To Fahrenheit | Convert 15 degrees Celsius to degrees Fahrenheit = | 59.0 | celsiustofahrenheit |
| 82 | AP Term Calculation | Find the term number 31 of the AP series: -53, -107, -161 ...  | -1673 | arithmeticProgressionTermFunc |
| 83 | AP Sum Calculation | Find the sum of first 56 terms of the AP series: -14, -24, -34 ...  | -16184.0 | arithmeticProgressionSumFunc |
| 84 | Converts decimal to octal | The decimal number 1430 in Octal is:  | 0o2626 | decimalToOctalFunc |
| 85 | Converts decimal to Roman Numerals | The number 3537 in Roman Numerals is:  | MMMDXXXVII | decimalToRomanNumeralsFunc |
| 86 | Degrees to Radians | Angle 87 in radians is =  | 1.52 | degreeToRadFunc |
| 87 | Radians to Degrees | Angle 3 in degrees is =  | 171.89 | radianToDegFunc |
