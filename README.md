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
| 0 | Addition | 23+50= | 73 | addition |
| 1 | Subtraction | 68-41= | 27 | subtraction |
| 2 | Multiplication | 51*1= | 51 | multiplication |
| 3 | Division | 37/44= | 0.8409090909090909 | division |
| 4 | Binary Complement 1s | 01= | 10 | binaryComplement1s |
| 5 | Modulo Division | 49%54= | 49 | moduloDivision |
| 6 | Square Root | sqrt(16)= | 4 | squareRoot |
| 7 | Power Rule Differentiation | 1x^6 + 8x^4 + 5x^5 | 6x^5 + 32x^3 + 25x^4 | powerRuleDifferentiation |
| 8 | Square | 2^2= | 4 | square |
| 9 | LCM (Least Common Multiple) | LCM of 13 and 1 = | 13 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 14 and 8 =  | 2 | gcd |
| 11 | Basic Algebra | 1x + 6 = 8 | 2 | basicAlgebra |
| 12 | Logarithm | log2(256) | 8 | log |
| 13 | Easy Division | 96/4 =  | 24 | intDivision |
| 14 | Decimal to Binary | Binary of 12= | 1100 | decimalToBinary |
| 15 | Binary to Decimal | 010010100 | 148 | binaryToDecimal |
| 16 | Fraction Division | (5/10)/(5/2) | 1/5 | fractionDivision |
| 17 | Integer Multiplication with 2x2 Matrix | 1 * [[2, 6], [6, 6]] =  | [[2,6],[6,6]] | intMatrix22Multiplication |
| 18 | Area of Triangle | Area of triangle with side lengths: 15 13 20 =  | 97.48846085563153 | areaOfTriangle |
| 19 | Triangle exists check | Does triangle with sides 30, 30 and 47 exist? | Yes | doesTriangleExist |
| 20 | Midpoint of the two point | (-8,11),(2,3)= | (-3.0,7.0) | midPointOfTwoPoint |
| 21 | Factoring Quadratic | x^2-3x-28 | (x+4)(x-7) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 59 and 50 =  | 71 | thirdAngleOfTriangle |
| 23 | Solve a System of Equations in R^2 | 3x + 7y = -61, 6x + 7y = -52 | x = 3, y = -10 | systemOfEquations |
| 24 | Distance between 2 points | Find the distance between (-10, -6) and (-2, 14) | sqrt(464) | distance2Point |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 17 and 13 =  | 21.40 | pythagoreanTheorem |
| 26 | Linear Equations | -2x + 9y = 16
-15x + 3y = -267 | x = 19, y = 6 | linearEquations |
| 27 | Prime Factorisation | Find prime factors of 94 | [2, 47] | primeFactors |
| 28 | Fraction Multiplication | (8/10)*(10/7) | 8/7 | fractionMultiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 19 sides | 161.05 | angleRegularPolygon |
| 30 | Combinations of Objects | Number of combinations from 14 objects picked 8 at a time  | 3003 | combinations |
| 31 | Factorial | 5! =  | 120 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 16m is | 1536 m^2 | surfaceAreaCubeGen |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 9m, 16m, 12m is | 888 m^2 | surfaceAreaCuboidGen |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 41m and radius = 11m is | 3593 m^2 | surfaceAreaCylinderGen |
| 35 | Volum of Cube | Volume of cube with side = 3m is | 27 m^3 | volumeCubeGen |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 2m, 8m, 14m is | 224 m^3 | volumeCuboidGen |
| 37 | Volume of cylinder | Volume of cylinder with height = 43m and radius = 15m is | 30394 m^3 | volumeCylinderGen |
| 38 | Surface Area of cone | Surface area of cone with height = 49m and radius = 2m is | 320 m^2 | surfaceAreaConeGen |
| 39 | Volume of cone | Volume of cone with height = 31m and radius = 17m is | 9381 m^3 | volumeConeGen |
| 40 | Common Factors | Common Factors of 55 and 82 =  | [1] | commonFactors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 0/4x + 1 and y = 3/5x - 9 | (50/3, 1) | intersectionOfTwoLines |
| 42 | Permutations | Number of Permutations from 11 objects picked 0 at a time =   | 1 | permutations |
| 43 | Cross Product of 2 Vectors | [16, -20, -19] X [-16, -13, -11] =  | [-27, 480, -528] | vectorCross |
| 44 | Compare Fractions | Which symbol represents the comparison between 6/7 and 8/5? | < | compareFractions |
| 45 | Simple Interest | Simple interest for a principle amount of 7762 dollars, 2% rate of interest and for a time period of 2 years is =  | 310.48 | simpleInterest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>18</td><td>-56</td><td>97</td><td>-66</td><td>-25</td><td>55</td><td>-99</td><td>86</td></tr><tr><td>2</td><td>-45</td><td>27</td><td>-87</td><td>-30</td><td>-15</td><td>93</td><td>-62</td></tr><tr><td>83</td><td>-25</td><td>55</td><td>-8</td><td>75</td><td>-34</td><td>-71</td><td>-22</td></tr><tr><td>-75</td><td>94</td><td>-6</td><td>84</td><td>-88</td><td>-38</td><td>60</td><td>98</td></tr><tr><td>20</td><td>-48</td><td>74</td><td>-73</td><td>-81</td><td>-25</td><td>60</td><td>-93</td></tr><tr><td>-23</td><td>-89</td><td>-63</td><td>90</td><td>36</td><td>30</td><td>18</td><td>19</td></tr><tr><td>-21</td><td>15</td><td>89</td><td>35</td><td>-60</td><td>-53</td><td>-85</td><td>22</td></tr><tr><td>-70</td><td>-76</td><td>-37</td><td>-98</td><td>-73</td><td>77</td><td>81</td><td>72</td></tr></table>and<table><tr><td>-14</td><td>13</td></tr><tr><td>-78</td><td>96</td></tr><tr><td>-17</td><td>95</td></tr><tr><td>72</td><td>69</td></tr><tr><td>67</td><td>41</td></tr><tr><td>85</td><td>49</td></tr><tr><td>-64</td><td>38</td></tr><tr><td>36</td><td>-44]] | [[ 10147,  -6357]
 [-14710,  -3435]
 [  5164,   3031]
 [ -9570,   5773]
 [-17790,   -529]
 [ 19309,  -5824]
 [ -2162,   2782]
 [  -457, -17793]] | matrixMultiplication |
| 47 | Cube Root | cuberoot of 402 upto 2 decimal places is: | 7.38 | CubeRoot |
| 48 | Power Rule Integration | 9x^1 | (9/1)x^2 + c | powerRuleIntegration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 171 , 62, 4 = | 123 | fourthAngleOfQuadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 79x^2+159x+79=0 | [-0.89, -1.12] | quadraticEquationSolve |
| 51 | HCF (Highest Common Factor) | HCF of 18 and 16 =  | 2 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 3 dice are rolled at the same time, the probability of getting a sum of 10 = | 27/216 | diceSumProbability |
| 53 | Exponentiation | 5^9 = | 1953125 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [259, 228, 251, 245, 222, 216, 209, 288, 229, 249, 278, 226, 256, 263, 248, 211, 210, 270, 260, 269] with 99% confidence is | (257.86513442744837, 230.83486557255162) | confidenceInterval |
| 55 | Comparing surds | Fill in the blanks 70^(1/7) _ 61^(1/6) | < | surdsComparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 16 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610] | fibonacciSeries |
| 57 | Trigonometric Values | What is sin(45)? | 1/√2 | basicTrigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 3 sides =  | 180 | sumOfAnglesOfPolygon |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[48, 46, 29, 28, 17, 48, 24, 23, 5, 9, 27, 33, 46, 7, 36] | The Mean is 28.4 , Standard Deviation is 201.97333333333336, Variance is 14.211732242528823 | dataSummary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 19m is | 4536.459791783661 m^2 | surfaceAreaSphereGen |
| 61 | Volume of Sphere | Volume of sphere with radius 63 m =  | 1047394.4243362226 m^3 | volumeSphere |
| 62 | nth Fibonacci number | What is the 85th Fibonacci number? | 259695496911123328 | nthFibonacciNumberGen |
| 63 | Profit or Loss Percent | Loss percent when CP = 937 and SP = 72 is:  | 92.31590181430096 | profitLossPercent |
| 64 | Binary to Hexidecimal | 1001111 | 0x4f | binaryToHex |
| 65 | Multiplication of 2 complex numbers | (-3+2j) * (-6+7j) =  | (4-33j) | complexNumMultiply |
| 66 | Geometric Progression | For the given GP [6, 24, 96, 384, 1536, 6144] ,Find the value of a,common ratio,9th term value, sum upto 9th term | The value of a is 6, common ratio is 4 , 9th term is 393216 , sum upto 9th term is 524286.0 | geometricprogression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 54 , 80 , 35 , 39 =  | (54*80*35*39)^(1/4) = 49.27811645529654 | geometricMean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 4 numbers 2 , 84 , 93 , 16 =  |  4/((1/2) + (1/84) + (1/93) + (1/16)) = 6.835767022149303 | harmonicMean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[784.3594765936149, 831.2509235672187, 16.078601582030892, 985.0579481288806, 734.7344412338676, 998.0941258783216, 354.94078353536895, 413.5643355103187, 581.4239813447576, 903.949312712381, 806.494025130463] is: | 2432.1700989717465 | eucldianNorm |
| 70 | Angle between 2 vectors | angle between the vectors [689.0197023764115, 694.8793500248185] and [927.4787145023294, 343.6872076155678] is: | NaN | angleBtwVectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -23 and 44 =  | 67 | absoluteDifference |
| 72 | Dot Product of 2 Vectors | [17, 9, 8] . [18, 9, 4] =  | 419 | vectorDot |
| 73 | Binary 2's Complement | 2's complement of 101 = | 11 | binary2sComplement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[13, 88, 85], [65, 37, 52], [89, 45, 2]]) is: | Matrix([[-1133/167543, 3649/335086, 1431/335086], [2249/167543, -7539/335086, 4849/335086], [-184/167543, 7247/335086, -5239/335086]]) | invertmatrix |
| 75 | Area of a Sector | Given radius, 6 and angle, 328. Find the area of the sector. | Area of sector = 103.04424 | sectorArea |
| 76 | Mean and Median | Given the series of numbers [55, 61, 83, 85, 52, 78, 30, 58, 76, 37]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 61.5 and Arithmetic median of this series is 59.5 | meanMedian |
