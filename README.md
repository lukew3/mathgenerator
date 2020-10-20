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
| 0 | Addition | 39+14= | 53 | addition |
| 1 | Subtraction | 28-20= | 8 | subtractionFunc |
| 2 | Multiplication | 23*2= | 46 | multiplicationFunc |
| 3 | Division | 34/27= | 1.2592592592592593 | divisionFunc |
| 4 | Binary Complement 1s | 01101= | 10010 | binaryComplement1sFunc |
| 5 | Modulo Division | 27%67= | 27 | moduloFunc |
| 6 | Square Root | sqrt(81)= | 9 | squareRootFunc |
| 7 | Power Rule Differentiation | 7x^2 + 1x^4 + 4x^8 + 5x^10 | 14x^1 + 4x^3 + 32x^7 + 50x^9 | powerRuleDifferentiationFunc |
| 8 | Square | 2^2= | 4 | squareFunc |
| 9 | LCM (Least Common Multiple) | LCM of 7 and 10 = | 70 | lcmFunc |
| 10 | GCD (Greatest Common Denominator) | GCD of 15 and 3 =  | 3 | gcdFunc |
| 11 | Basic Algebra | 9x + 8 = 9 | 1/9 | basicAlgebraFunc |
| 12 | Logarithm | log2(32) | 5 | logFunc |
| 13 | Easy Division | 176/11 =  | 16 | divisionToIntFunc |
| 14 | Decimal to Binary | Binary of 49= | 110001 | DecimalToBinaryFunc |
| 15 | Binary to Decimal | 01100 | 12 | BinaryToDecimalFunc |
| 16 | Fraction Division | (9/5)/(10/2) | 9/25 | divideFractionsFunc |
| 17 | Integer Multiplication with 2x2 Matrix | 8 * [[8, 9], [0, 3]] =  | [[64,72],[0,24]] | multiplyIntToMatrix22 |
| 18 | Area of Triangle | Area of triangle with side lengths: 19 2 15 =  | (1.7998558638262156e-15+29.393876913398138j) | areaOfTriangleFunc |
| 19 | Triangle exists check | Does triangle with sides 9, 12 and 5 exist? | Yes | isTriangleValidFunc |
| 20 | Midpoint of the two point | (-3,-3),(-7,-4)= | (-5.0,-3.5) | MidPointOfTwoPointFunc |
| 21 | Factoring Quadratic | x^2+4x-12 | (x+6)(x-2) | factoringFunc |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 4 and 27 =  | 149 | thirdAngleOfTriangleFunc |
| 23 | Solve a System of Equations in R^2 | -6x - 10y = 22, 4x - 3y = 53 | x = 8, y = -7 | systemOfEquationsFunc |
| 24 | Distance between 2 points | Find the distance between (6, 2) and (-2, -2) | sqrt(80) | distanceTwoPointsFunc |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 10 and 13 =  | 16.40 | pythagoreanTheoremFunc |
| 26 | Linear Equations | 8x + -8y = -40
20x + -16y = -108 | x = -7, y = -2 | linearEquationsFunc |
| 27 | Prime Factorisation | Find prime factors of 29 | [29] | primeFactorsFunc |
| 28 | Fraction Multiplication | (4/7)*(3/9) | 4/21 | multiplyFractionsFunc |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 3 sides | 60.0 | regularPolygonAngleFunc |
| 30 | Combinations of Objects | Number of combinations from 20 objects picked 5 at a time  | 15504 | combinationsFunc |
| 31 | Factorial | 3! =  | 6 | factorialFunc |
| 32 | Surface Area of Cube | Surface area of cube with side = 3m is | 54 m^2 | surfaceAreaCube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 4m, 15m, 5m is | 310 m^2 | surfaceAreaCuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 14m and radius = 11m is | 1727 m^2 | surfaceAreaCylinder |
| 35 | Volum of Cube | Volume of cube with side = 6m is | 216 m^3 | volumeCube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 9m, 6m, 15m is | 810 m^3 | volumeCuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 21m and radius = 4m is | 1055 m^3 | volumeCylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 7m and radius = 7m is | 371 m^2 | surfaceAreaCone |
| 39 | Volume of cone | Volume of cone with height = 46m and radius = 15m is | 10838 m^3 | volumeCone |
| 40 | Common Factors | Common Factors of 12 and 76 =  | [1, 2, 4] | commonFactorsFunc |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 6x + 8 and y = 3/2x + 4 | (-8/9, 8/3) | intersectionOfTwoLinesFunc |
| 42 | Permutations | Number of Permutations from 15 objects picked 5 at a time =   | 360360 | permutationFunc |
| 43 | Cross Product of 2 Vectors | [-13, -2, 0] X [-4, 14, -4] =  | [8, -52, -190] | vectorCrossFunc |
| 44 | Compare Fractions | Which symbol represents the comparison between 3/8 and 3/9? | > | compareFractionsFunc |
| 45 | Simple Interest | Simple interest for a principle amount of 6266 dollars, 8% rate of interest and for a time period of 3 years is =  | 1503.84 | simpleInterestFunc |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>3</td><td>0</td></tr><tr><td>-1</td><td>-6</td></tr></table>and<table><tr><td>4</td><td>-7</td><td>5</td><td>-9</td></tr><tr><td>0</td><td>8</td><td>-10</td><td>-2</td></tr></table> | <table><tr><td>12</td><td>-21</td><td>15</td><td>-27</td></tr><tr><td>-4</td><td>-41</td><td>55</td><td>21</td></tr></table> | matrixMultiplicationFunc |
| 47 | Cube Root | cuberoot of 362 upto 2 decimal places is: | 7.13 | cubeRootFunc |
| 48 | Power Rule Integration | 2x^6 + 1x^5 + 7x^9 + 1x^10 | (2/6)x^7 + (1/5)x^6 + (7/9)x^10 + (1/10)x^11 + c | powerRuleIntegrationFunc |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 60 , 18, 7 = | 275 | fourthAngleOfQuadriFunc |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 40x^2+121x+89=0 | [-1.26, -1.76] | quadraticEquation |
| 51 | HCF (Highest Common Factor) | HCF of 4 and 12 =  | 4 | hcfFunc |
| 52 | Probability of a certain sum appearing on faces of dice | If 3 dice are rolled at the same time, the probability of getting a sum of 13 = | 21/216 | DiceSumProbFunc |
| 53 | Exponentiation | 11^8 = | 214358881 | exponentiationFunc |
| 54 | Confidence interval For sample S | The confidence interval for sample [239, 265, 215, 283, 231, 296, 270, 260, 289, 271, 245, 251, 206, 255, 257, 247, 292, 232, 276, 297, 263, 254, 279, 253, 211, 236, 274, 209, 275, 278, 212, 214, 226, 230, 256, 249, 293] with 95% confidence is | (262.3172302973649, 245.19628321614857) | confidenceIntervalFunc |
| 55 | Comparing surds | Fill in the blanks 86^(1/4) _ 39^(1/1) | < | surdsComparisonFunc |
| 56 | Fibonacci Series | The Fibonacci Series of the first 10 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] | fibonacciSeriesFunc |
| 57 | Trigonometric Values | What is sin(90)? | 1 | basicTrigonometryFunc |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 5 sides =  | 540 | sumOfAnglesOfPolygonFunc |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[19, 23, 36, 18, 44, 47, 18, 40, 27, 25, 14, 16, 6, 29, 50] | The Mean is 27.466666666666665 , Standard Deviation is 163.0488888888889, Variance is 12.769059827915637 | dataSummaryFunc |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 5m is | 314.1592653589793 m^2 | surfaceAreaSphere |
| 61 | Volume of Sphere | Volume of sphere with radius 63 m =  | 1047394.4243362226 m^3 | volumeSphereFunc |
| 62 | nth Fibonacci number | What is the 60th Fibonacci number? | 1548008755920 | nthFibonacciNumberFunc |
| 63 | Profit or Loss Percent | Profit percent when CP = 121 and SP = 615 is:  | 408.26446280991735 | profitLossPercentFunc |
| 64 | Binary to Hexidecimal | 10110 | 0x16 | binaryToHexFunc |
| 65 | Multiplication of 2 complex numbers | (20-1j) * (-7+14j) =  | (-126+287j) | multiplyComplexNumbersFunc |
| 66 | Geometric Progression | For the given GP [2, 24, 288, 3456, 41472, 497664] ,Find the value of a,common ratio,9th term value, sum upto 10th term | The value of a is 2, common ratio is 12 , 9th term is 859963392 , sum upto 10th term is 11257702586.0 | geomProgrFunc |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 18 , 24 , 99 , 12 =  | (18*24*99*12)^(1/4) = 26.765480655440626 | geometricMeanFunc |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 41 and 82 =  |  2/((1/41) + (1/82)) = 54.66666666666666 | harmonicMeanFunc |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[690.1926568125737, 148.904898302192, 222.19798825467595, 667.3276829127157, 366.9178192723557, 875.6869024243441, 336.14075266140685, 949.1256775112896, 626.0180041672427, 290.7427227038134, 207.55193301803965, 64.93900706542944, 736.3114771837603, 785.1756497858677] is: | 2142.639328828992 | euclidianNormFunc |
| 70 | Angle between 2 vectors | angle between the vectors [293.12905111302047, 909.0452944804068, 423.60965609823086, 870.8703924858319, 958.9076883380749, 837.4625321599826] and [938.5559146533071, 63.15299226225102, 418.14038421596024, 865.5267136591071, 513.9066820998474, 680.6577264839382] is: | NaN | angleBtwVectorsFunc |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 76 and -20 =  | 96 | absoluteDifferenceFunc |
| 72 | Dot Product of 2 Vectors | [19, 10, -5] . [0, -18, 15] =  | -255 | vectorDotFunc |
| 73 | Binary 2's Complement | 2's complement of 110 = | 10 | binary2sComplement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[61, 68, 75], [31, 77, 66], [33, 59, 58]]) is: | Matrix([[11/141, 37/564, -33/188], [95/1833, 1063/7332, -567/2444], [-178/1833, -1355/7332, 863/2444]]) | matrixInversion |
| 75 | Area of a Sector | Given radius, 20 and angle, 235. Find the area of the sector. | Area of sector = 820.30475 | sectorAreaFunc |
| 76 | Mean and Median | Given the series of numbers [7, 89, 72, 14, 97, 48, 35, 12, 11, 27]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 41.2 and Arithmetic median of this series is 31.0 | meanMedianFunc |
| 77 | Determinant to 2x2 Matrix | Det([[26, 78], [39, 24]]) =  |  -2418 | determinantToMatrix22 |
| 78 | Compound Interest | Compound Interest for a principle amount of 6842 dollars, 8% rate of interest and for a time period of 5 compounded monthly is =  | 6842.0 | compoundInterestFunc |
| 79 | Decimal to Hexadecimal | Binary of 860= | 0x35c | deciToHexaFunc |
| 80 | Percentage of a number | What is 75% of 28? | Required percentage = 21.00% | percentageFunc |
| 81 | Celsius To Fahrenheit | Convert 30 degrees Celsius to degrees Fahrenheit = | 86.0 | celsiustofahrenheit |
| 82 | AP Term Calculation | Find the term number 47 of the AP series: -56, 37, 130 ...  | 4222 | arithmeticProgressionTermFunc |
| 83 | AP Sum Calculation | Find the sum of first 79 terms of the AP series: 34, 24, 14 ...  | -28124.0 | arithmeticProgressionSumFunc |
| 84 | Converts decimal to octal | The decimal number 2245 in Octal is:  | 0o4305 | decimalToOctalFunc |
| 85 | Converts decimal to Roman Numerals | The number 1658 in Roman Numerals is:  | MDCLVIII | decimalToRomanNumeralsFunc |
| 86 | Degrees to Radians | Angle 12 in radians is =  | 0.21 | degreeToRadFunc |
| 87 | Radians to Degrees | Angle 3 in degrees is =  | 171.89 | radianToDegFunc |
