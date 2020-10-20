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
<!-- list start -->
| 0 | Addition | 8+11= | 19 | addition |
| 1 | Subtraction | 93-26= | 67 | subtractionFunc |
| 2 | Multiplication | 36*2= | 72 | multiplicationFunc |
| 3 | Division | 66/2= | 33.0 | divisionFunc |
| 4 | Binary Complement 1s | 1111= | 0000 | binaryComplement1sFunc |
| 5 | Modulo Division | 31%19= | 12 | moduloFunc |
| 6 | Square Root | sqrt(144)= | 12 | squareRootFunc |
| 7 | Power Rule Differentiation | 3x^10 + 1x^3 + 1x^8 + 5x^9 + 5x^7 | 30x^9 + 3x^2 + 8x^7 + 45x^8 + 35x^6 | powerRuleDifferentiationFunc |
| 8 | Square | 18^2= | 324 | squareFunc |
| 9 | LCM (Least Common Multiple) | LCM of 20 and 3 = | 60 | lcmFunc |
| 10 | GCD (Greatest Common Denominator) | GCD of 8 and 1 =  | 1 | gcdFunc |
| 11 | Basic Algebra | 6x + 5 = 6 | 1/6 | basicAlgebraFunc |
| 12 | Logarithm | log3(6561) | 8 | logFunc |
| 13 | Easy Division | 216/24 =  | 9 | divisionToIntFunc |
| 14 | Decimal to Binary | Binary of 78= | 1001110 | DecimalToBinaryFunc |
| 15 | Binary to Decimal | 01 | 1 | BinaryToDecimalFunc |
| 16 | Fraction Division | (8/10)/(5/2) | 8/25 | divideFractionsFunc |
| 17 | Integer Multiplication with 2x2 Matrix | 8 * [[1, 0], [3, 7]] =  | [[8,0],[24,56]] | multiplyIntToMatrix22 |
| 18 | Area of Triangle | Area of triangle with side lengths: 17 7 8 =  | (2.0782945349651837e-15+33.94112549695428j) | areaOfTriangleFunc |
| 19 | Triangle exists check | Does triangle with sides 31, 46 and 8 exist? | No | isTriangleValidFunc |
| 20 | Midpoint of the two point | (10,7),(4,-8)= | (7.0,-0.5) | MidPointOfTwoPointFunc |
| 21 | Factoring Quadratic | x^2-11x+10 | (x-10)(x-1) | factoringFunc |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 14 and 35 =  | 131 | thirdAngleOfTriangleFunc |
| 23 | Solve a System of Equations in R^2 | 7x - 10y = -90, -7x - 3y = -27 | x = 0, y = 9 | systemOfEquationsFunc |
| 24 | Distance between 2 points | Find the distance between (-3, 1) and (9, 8) | sqrt(193) | distanceTwoPointsFunc |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 18 and 15 =  | 23.43 | pythagoreanTheoremFunc |
| 26 | Linear Equations | 16x + 12y = -4
-18x + 17y = 279 | x = -7, y = 9 | linearEquationsFunc |
| 27 | Prime Factorisation | Find prime factors of 88 | [2, 2, 2, 11] | primeFactorsFunc |
| 28 | Fraction Multiplication | (9/8)*(4/9) | 1/2 | multiplyFractionsFunc |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 7 sides | 128.57 | regularPolygonAngleFunc |
| 30 | Combinations of Objects | Number of combinations from 19 objects picked 2 at a time  | 171 | combinationsFunc |
| 31 | Factorial | 5! =  | 120 | factorialFunc |
| 32 | Surface Area of Cube | Surface area of cube with side = 12m is | 864 m^2 | surfaceAreaCube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 16m, 4m, 13m is | 648 m^2 | surfaceAreaCuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 28m and radius = 15m is | 4052 m^2 | surfaceAreaCylinder |
| 35 | Volum of Cube | Volume of cube with side = 18m is | 5832 m^3 | volumeCube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 17m, 9m, 6m is | 918 m^3 | volumeCuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 3m and radius = 9m is | 763 m^3 | volumeCylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 25m and radius = 2m is | 170 m^2 | surfaceAreaCone |
| 39 | Volume of cone | Volume of cone with height = 33m and radius = 12m is | 4976 m^3 | volumeCone |
| 40 | Common Factors | Common Factors of 1 and 96 =  | [1] | commonFactorsFunc |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -3/2x + 2 and y = -3/6x + 10 | (-8, 14) | intersectionOfTwoLinesFunc |
| 42 | Permutations | Number of Permutations from 17 objects picked 6 at a time =   | 8910720 | permutationFunc |
| 43 | Cross Product of 2 Vectors | [11, 20, -16] X [12, -3, -7] =  | [-188, -115, -273] | vectorCrossFunc |
| 44 | Compare Fractions | Which symbol represents the comparison between 5/2 and 4/10? | > | compareFractionsFunc |
| 45 | Simple Interest | Simple interest for a principle amount of 1229 dollars, 3% rate of interest and for a time period of 5 years is =  | 184.35 | simpleInterestFunc |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>0</td><td>2</td><td>6</td><td>6</td></tr><tr><td>10</td><td>0</td><td>-8</td><td>-2</td></tr></table>and<table><tr><td>5</td><td>0</td><td>-7</td></tr><tr><td>-9</td><td>5</td><td>-7</td></tr><tr><td>4</td><td>0</td><td>4</td></tr><tr><td>-2</td><td>-2</td><td>5</td></tr></table> | <table><tr><td>-6</td><td>-2</td><td>40</td></tr><tr><td>22</td><td>4</td><td>-112</td></tr></table> | matrixMultiplicationFunc |
| 47 | Cube Root | cuberoot of 766 upto 2 decimal places is: | 9.15 | cubeRootFunc |
| 48 | Power Rule Integration | 10x^3 + 3x^5 + 3x^8 + 10x^9 | (10/3)x^4 + (3/5)x^6 + (3/8)x^9 + (10/9)x^10 + c | powerRuleIntegrationFunc |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 135 , 43, 102 = | 80 | fourthAngleOfQuadriFunc |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 87x^2+181x+85=0 | [-0.72, -1.36] | quadraticEquation |
| 51 | HCF (Highest Common Factor) | HCF of 9 and 1 =  | 1 | hcfFunc |
| 52 | Probability of a certain sum appearing on faces of dice | If 1 dice are rolled at the same time, the probability of getting a sum of 3 = | 1/6 | DiceSumProbFunc |
| 53 | Exponentiation | 6^9 = | 10077696 | exponentiationFunc |
| 54 | Confidence interval For sample S | The confidence interval for sample [288, 200, 228, 240, 210, 221, 273, 287, 280, 226, 242, 212, 224, 208, 285, 213, 262, 259, 235, 265, 216, 207, 291, 206, 201, 254, 241, 298, 204, 266] with 99% confidence is | (256.05711554415353, 226.74288445584648) | confidenceIntervalFunc |
| 55 | Comparing surds | Fill in the blanks 16^(1/3) _ 49^(1/6) | > | surdsComparisonFunc |
| 56 | Fibonacci Series | The Fibonacci Series of the first 1 numbers is ? | [0] | fibonacciSeriesFunc |
| 57 | Trigonometric Values | What is sin(45)? | 1/√2 | basicTrigonometryFunc |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 7 sides =  | 900 | sumOfAnglesOfPolygonFunc |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[46, 21, 12, 47, 40, 43, 35, 41, 27, 33, 35, 22, 44, 37, 50] | The Mean is 35.53333333333333 , Standard Deviation is 110.51555555555557, Variance is 10.512637897100593 | dataSummaryFunc |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 14m is | 2463.0086404143976 m^2 | surfaceAreaSphere |
| 61 | Volume of Sphere | Volume of sphere with radius 34 m =  | 164636.21020892428 m^3 | volumeSphereFunc |
| 62 | nth Fibonacci number | What is the 13th Fibonacci number? | 233 | nthFibonacciNumberFunc |
| 63 | Profit or Loss Percent | Loss percent when CP = 695 and SP = 168 is:  | 75.8273381294964 | profitLossPercentFunc |
| 64 | Binary to Hexidecimal | 11101 | 0x1d | binaryToHexFunc |
| 65 | Multiplication of 2 complex numbers | (14+2j) * (1-1j) =  | (16-12j) | multiplyComplexNumbersFunc |
| 66 | Geometric Progression | For the given GP [6, 18, 54, 162, 486, 1458] ,Find the value of a,common ratio,8th term value, sum upto 10th term | The value of a is 6, common ratio is 3 , 8th term is 13122 , sum upto 10th term is 177144.0 | geomProgrFunc |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 71 , 59 , 78 , 58 =  | (71*59*78*58)^(1/4) = 65.9793813576169 | geometricMeanFunc |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 3 numbers 14 , 21 and 11 =  |  3/((1/14) + (1/21) + (1/11)) = 14.288659793814434 | harmonicMeanFunc |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[576.670891061537, 46.740591846397564, 322.19381082504015, 485.7288856110419, 528.0964956855642, 42.47762856557491, 907.4759846289586, 477.6183789730094, 980.6808665536921, 980.6752304528254, 123.2523700978323, 264.0108328134191] is: | 2003.7837643058115 | euclidianNormFunc |
| 70 | Angle between 2 vectors | angle between the vectors [462.6718367070632, 603.9921262501323, 218.40294983726005, 879.6379929319809, 772.4165625498082, 557.3424325254722, 671.6240138545284, 407.73691049303164, 231.90401683768835, 314.3288898599752, 647.3986479012833, 786.3772925969524, 381.49247418156216, 690.8115782481401, 830.9537709699912, 895.7819796935034] and [782.3858606665599, 90.83958140528226, 932.4297057425011, 854.0128086934983, 420.72213888575317, 703.4720080775643, 492.9666278240823, 922.5591826144878, 88.34926267197196, 537.7174105963974, 30.714037169874196, 817.0897228996445, 501.4033203079129, 296.876089485975, 358.88605328027245, 946.7120465075549] is: | NaN | angleBtwVectorsFunc |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -57 and -4 =  | 53 | absoluteDifferenceFunc |
| 72 | Dot Product of 2 Vectors | [18, 12, 20] . [-6, 7, -9] =  | -204 | vectorDotFunc |
| 73 | Binary 2's Complement | 2's complement of 10100 = | 1100 | binary2sComplement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[44, 73, 53], [86, 2, 6], [23, 41, 69]]) is: | Matrix([[9/20285, 716/60855, -83/60855], [483/20285, -1817/243420, -2147/121710], [-58/4057, 25/48684, 619/24342]]) | matrixInversion |
| 75 | Area of a Sector | Given radius, 2 and angle, 249. Find the area of the sector. | Area of sector = 8.69174 | sectorAreaFunc |
| 76 | Mean and Median | Given the series of numbers [81, 96, 30, 55, 32, 34, 36, 69, 51, 6]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 49.0 and Arithmetic median of this series is 43.5 | meanMedianFunc |
| 77 | Determinant to 2x2 Matrix | Det([[51, 96], [40, 81]]) =  |  291 | determinantToMatrix22 |
| 78 | Compound Interest | Compound Interest for a principle amount of 7470 dollars, 9% rate of interest and for a time period of 7 compounded monthly is =  | 7470.0 | compoundInterestFunc |
| 79 | Decimal to Hexadecimal | Binary of 310= | 0x136 | deciToHexaFunc |
| 80 | Percentage of a number | What is 25% of 68? | Required percentage = 17.00% | percentageFunc |
| 81 | Celsius To Fahrenheit | Convert -24 degrees Celsius to degrees Fahrenheit = | -11.200000000000003 | celsiustofahrenheit |
| 82 | AP Term Calculation | Find the term number 15 of the AP series: -91, -5, 81 ...  | 1113 | arithmeticProgressionTermFunc |
| 83 | AP Sum Calculation | Find the sum of first 61 terms of the AP series: 61, 22, -17 ...  | -67649.0 | arithmeticProgressionSumFunc |
| 84 | Converts decimal to octal | The decimal number 3722 in Octal is:  | 0o7212 | decimalToOctalFunc |
| 85 | Converts decimal to Roman Numerals | The number 3575 in Roman Numerals is:  | MMMDLXXV | decimalToRomanNumeralsFunc |
| 86 | Degrees to Radians | Angle 174 in radians is =  | 3.04 | degreeToRadFunc |
| 87 | Radians to Degrees | Angle 2 in degrees is =  | 114.59 | radianToDegFunc |
