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
| 0 | Addition | 0+0= | 0 | addition |
| 1 | Subtraction | 46-14= | 32 | subtraction |
| 2 | Multiplication | 6*12= | 72 | multiplication |
| 3 | Division | 39/11= | 3.5454545454545454 | division |
| 4 | Binary Complement 1s | 0000= | 1111 | binaryComplement1s |
| 5 | Modulo Division | 98%34= | 30 | moduloDivision |
| 6 | Square Root | sqrt(9)= | 3 | squareRoot |
| 7 | Power Rule Differentiation | 5x^5 + 2x^9 + 4x^3 + 3x^3 | 25x^4 + 18x^8 + 12x^2 + 9x^2 | powerRuleDifferentiation |
| 8 | Square | 20^2= | 400 | square |
| 9 | LCM (Least Common Multiple) | LCM of 13 and 13 = | 13 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 16 and 13 =  | 1 | gcd |
| 11 | Basic Algebra | 3x + 2 = 7 | 5/3 | basicAlgebra |
| 12 | Logarithm | log3(243) | 5 | log |
| 13 | Easy Division | 154/14 =  | 11 | intDivision |
| 14 | Decimal to Binary | Binary of 86= | 1010110 | decimalToBinary |
| 15 | Binary to Decimal | 10 | 2 | binaryToDecimal |
| 16 | Fraction Division | (5/1)/(3/2) | 10/3 | fractionDivision |
| 17 | Integer Multiplication with 2x2 Matrix | 4 * [[2, 6], [8, 6]] =  | [[8,24],[32,24]] | intMatrix22Multiplication |
| 18 | Area of Triangle | Area of triangle with side lengths: 9 15 6 =  | 0.0 | areaOfTriangle |
| 19 | Triangle exists check | Does triangle with sides 23, 8 and 32 exist? | No | doesTriangleExist |
| 20 | Midpoint of the two point | (-19,9),(-9,8)= | (-14.0,8.5) | midPointOfTwoPoint |
| 21 | Factoring Quadratic | x^2-1x-42 | (x-7)(x+6) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 41 and 80 =  | 59 | thirdAngleOfTriangle |
| 23 | Solve a System of Equations in R^2 | -6x + 3y = -39, -10x + 5y = -65 | x = 6, y = -1 | systemOfEquations |
| 24 | Distance between 2 points | Find the distance between (20, 0) and (-18, 0) | sqrt(1444) | distance2Point |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 16 and 3 =  | 16.28 | pythagoreanTheorem |
| 26 | Linear Equations | 8x + 11y = 91
-10x + 17y = -83 | x = 10, y = 1 | linearEquations |
| 27 | Prime Factorisation | Find prime factors of 69 | [3, 23] | primeFactors |
| 28 | Fraction Multiplication | (1/2)*(2/1) | 1 | fractionMultiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 11 sides | 147.27 | angleRegularPolygon |
| 30 | Combinations of Objects | Number of combinations from 10 objects picked 1 at a time  | 10 | combinations |
| 31 | Factorial | 0! =  | 1 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 20m is | 2400 m^2 | surfaceAreaCubeGen |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 19m, 6m, 13m is | 878 m^2 | surfaceAreaCuboidGen |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 8m and radius = 9m is | 961 m^2 | surfaceAreaCylinderGen |
| 35 | Volum of Cube | Volume of cube with side = 20m is | 8000 m^3 | volumeCubeGen |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 15m, 7m, 5m is | 525 m^3 | volumeCuboidGen |
| 37 | Volume of cylinder | Volume of cylinder with height = 15m and radius = 15m is | 10602 m^3 | volumeCylinderGen |
| 38 | Surface Area of cone | Surface area of cone with height = 29m and radius = 15m is | 2245 m^2 | surfaceAreaConeGen |
| 39 | Volume of cone | Volume of cone with height = 5m and radius = 7m is | 256 m^3 | volumeConeGen |
| 40 | Common Factors | Common Factors of 84 and 58 =  | [1, 2] | commonFactors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -6/3x and y = 3/5x - 1 | (5/13, -10/13) | intersectionOfTwoLines |
| 42 | Permutations | Number of Permutations from 11 objects picked 9 at a time =   | 19958400 | permutations |
| 43 | Cross Product of 2 Vectors | [-11, -12, -17] X [-12, -20, 13] =  | [-496, 347, 76] | vectorCross |
| 44 | Compare Fractions | Which symbol represents the comparison between 3/5 and 6/9? | < | compareFractions |
| 45 | Simple Interest | Simple interest for a principle amount of 6089 dollars, 3% rate of interest and for a time period of 8 years is =  | 1461.36 | simpleInterest |
| 46 | Multiplication of two matrices | Multiply 
<table><tr><td>    35</td><td>   -82</td><td>   -90</td><td>   -70</td><td>   -68</td></tr> <tr><td>    11</td><td>    15</td><td>   -23</td><td>    94</td><td>   -93</td></tr> <tr><td>   -85</td><td>   -30</td><td>   -79</td><td>     2</td><td>   -71</td></tr> <tr><td>    40</td><td>   -33</td><td>   -24</td><td>    87</td><td>    70</td></tr> <tr><td>    94</td><td>   -86</td><td>   -62</td><td>   -40</td><td>    58</td></tr></table> and 

<table><tr><td>   -91</td><td>    -4</td><td>    -1</td><td>    43</td><td>   -22</td><td>   -73</td><td>   -29</td></tr> <tr><td>    44</td><td>    24</td><td>    90</td><td>   -65</td><td>   100</td><td>    31</td><td>    45</td></tr> <tr><td>    73</td><td>   -64</td><td>    55</td><td>    -9</td><td>   -21</td><td>    51</td><td>     7</td></tr> <tr><td>     5</td><td>    65</td><td>   -31</td><td>    50</td><td>   -62</td><td>   -27</td><td>   -51</td></tr> <tr><td>    55</td><td>   -88</td><td>   -83</td><td>    -5</td><td>   -41</td><td>   -26</td><td>    84]] | [[-17453,   5086,  -4551,   4485,     48,  -6029,  -7477]
 [ -6665,  16082,   4879,   4870,   -274,  -1631, -12411]
 [ -3247,  11054,  -1129,   -539,   3316,   3038,  -5504]
 [ -2559,     79, -12837,   8081, -11940,  -9336,  -1370]
 [-13874,  -6176, -14818,   7900,  -9264, -13118,   -118]] | matrixMultiplication |
| 47 | Cube Root | cuberoot of 432 upto 2 decimal places is: | 7.56 | CubeRoot |
| 48 | Power Rule Integration | 2x^10 | (2/10)x^11 + c | powerRuleIntegration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 29 , 153, 130 = | 48 | fourthAngleOfQuadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 85x^2+188x+3=0 | [-0.02, -2.2] | quadraticEquationSolve |
| 51 | HCF (Highest Common Factor) | HCF of 5 and 7 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 2 dice are rolled at the same time, the probability of getting a sum of 5 = | 4/36 | diceSumProbability |
| 53 | Exponentiation | 13^9 = | 10604499373 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [232, 294, 245, 210, 221, 211, 257, 229, 258, 218, 290, 235, 203, 281, 296, 244, 243, 263, 251, 224, 276, 299, 298, 208, 285, 282, 266, 213, 270, 284, 297, 246, 230, 288, 207, 228, 279, 202, 240, 256] with 80% confidence is | (257.72581618790196, 245.224183812098) | confidenceInterval |
| 55 | Comparing surds | Fill in the blanks 96^(1/7) _ 15^(1/6) | > | surdsComparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 7 numbers is ? | [0, 1, 1, 2, 3, 5, 8] | fibonacciSeries |
| 57 | Trigonometric Values | What is sin(0)? | 0 | basicTrigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 10 sides =  | 1440 | sumOfAnglesOfPolygon |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[15, 24, 20, 12, 49, 43, 21, 27, 11, 44, 19, 25, 40, 40, 7] | The Mean is 26.466666666666665 , Standard Deviation is 169.98222222222222, Variance is 13.03772304592417 | dataSummary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 2m is | 50.26548245743669 m^2 | surfaceAreaSphereGen |
| 61 | Volume of Sphere | Volume of sphere with radius 15 m =  | 14137.166941154068 m^3 | volumeSphere |
| 62 | nth Fibonacci number | What is the 100th Fibonacci number? | 354224848179263111168 | nthFibonacciNumberGen |
| 63 | Profit or Loss Percent | Loss percent when CP = 273 and SP = 196 is:  | 28.205128205128204 | profitLossPercent |
| 64 | Binary to Hexidecimal | 11111101 | 0xfd | binaryToHex |
| 65 | Multiplication of 2 complex numbers | (4-18j) * (-7-7j) =  | (-154+98j) | complexNumMultiply |
| 66 | Geometric Progression | For the given GP [5, 20, 80, 320, 1280, 5120] ,Find the value of a,common ratio,7th term value, sum upto 8th term | The value of a is 5, common ratio is 4 , 7th term is 20480 , sum upto 8th term is 109225.0 | geometricprogression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 2 numbers 73 and 84 =  | (73*84)^(1/2) = 78.30708780180757 | geometricMean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 3 numbers 48 , 90 and 92 =  |  3/((1/48) + (1/90) + (1/92)) = 70.07052186177715 | harmonicMean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[924.2913636750363, 20.503795974707305, 517.3232583455609, 108.40962248839648, 53.90127703299286, 439.08768846258494, 456.9202154814549, 994.1184872614399, 582.1310398602112, 900.2850171703179, 600.8210520400753, 976.4837679476245, 322.81868740893447, 200.87610464653193] is: | 2266.1247066414917 | eucldianNorm |
| 70 | Angle between 2 vectors | angle between the vectors [208.76603907240408, 856.3899288947613, 504.6705923607805, 59.53820731849413, 225.96877896886213, 106.59039269390458, 954.4412959874746, 833.8565561650387] and [137.70718881439137, 398.58328047203594, 697.7790424491039, 94.83157368402372, 84.50274981272999, 643.3388926841467, 27.78410024116851, 405.7876464522183] is: | NaN | angleBtwVectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -11 and 65 =  | 76 | absoluteDifference |
| 72 | Dot Product of 2 Vectors | [-6, -17, -7] . [4, -14, -10] =  | 284 | vectorDot |
| 73 | Binary 2's Complement | 2's complement of 1 = | 1 | binary2sComplement |
