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

| 0 | Addition | 5+49= | 54 | addition |
| 1 | Subtraction | 63-53= | 10 | subtraction |
| 2 | Multiplication | 21*2= | 42 | multiplication |
| 3 | Division | 87/60= | 1.45 | division |
| 4 | Binary Complement 1s | 11011111= | 00100000 | binaryComplement1s |
| 5 | Modulo Division | 10%10= | 0 | moduloDivision |
| 6 | Square Root | sqrt(16)= | 4 | squareRoot |
| 7 | Power Rule Differentiation | 9x^6 + 8x^6 + 5x^9 + 1x^6 + 10x^1 | 54x^5 + 48x^5 + 45x^8 + 6x^5 + 10x^0 | powerRuleDifferentiation |
| 8 | Square | 6^2= | 36 | square |
| 9 | LCM (Least Common Multiple) | LCM of 9 and 6 = | 18 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 3 and 15 =  | 3 | gcd |
| 11 | Basic Algebra | 2x + 2 = 9 | 7/2 | basicAlgebra |
| 12 | Logarithm | log2(4) | 2 | log |
| 13 | Easy Division | 180/15 =  | 12 | intDivision |
| 14 | Decimal to Binary | Binary of 53= | 110101 | decimalToBinary |
| 15 | Binary to Decimal | 1000110111 | 567 | binaryToDecimal |
| 16 | Fraction Division | (10/4)/(1/10) | 25 | fractionDivision |
| 17 | Integer Multiplication with 2x2 Matrix | 1 * [[0, 4], [6, 2]] =  | [[0,4],[6,2]] | intMatrix22Multiplication |
| 18 | Area of Triangle | Area of triangle with side lengths: 8 3 19 =  | (4.3470649019239876e-15+70.9929573971954j) | areaOfTriangle |
| 19 | Triangle exists check | Does triangle with sides 8, 12 and 39 exist? | No | doesTriangleExist |
| 20 | Midpoint of the two point | (-17,-16),(-6,9)= | (-11.5,-3.5) | midPointOfTwoPoint |
| 21 | Factoring Quadratic | x^2-15x+56 | (x-8)(x-7) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 17 and 81 =  | 82 | thirdAngleOfTriangle |
| 23 | Solve a System of Equations in R^2 | -7x - 5y = 22, 5x - 4y = 7 | x = -1, y = -3 | systemOfEquations |
| 24 | Distance between 2 points | Find the distance between (-4, -13) and (15, 10) | sqrt(890) | distance2Point |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 11 and 2 =  | 11.18 | pythagoreanTheorem |
| 26 | Linear Equations | -9x + 15y = 171
-9x + 9y = 135 | x = -9, y = 6 | linearEquations |
| 27 | Prime Factorisation | Find prime factors of 61 | [61] | primeFactors |
| 28 | Fraction Multiplication | (8/7)*(9/10) | 36/35 | fractionMultiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 20 sides | 162.0 | angleRegularPolygon |
| 30 | Combinations of Objects | Number of combinations from 13 objects picked 8 at a time  | 1287 | combinations |
| 31 | Factorial | 6! =  | 720 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 17m is | 1734 m^2 | surfaceAreaCubeGen |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 3m, 18m, 1m is | 150 m^2 | surfaceAreaCuboidGen |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 20m and radius = 15m is | 3298 m^2 | surfaceAreaCylinderGen |
| 35 | Volum of Cube | Volume of cube with side = 7m is | 343 m^3 | volumeCubeGen |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 16m, 5m, 11m is | 880 m^3 | volumeCuboidGen |
| 37 | Volume of cylinder | Volume of cylinder with height = 28m and radius = 12m is | 12666 m^3 | volumeCylinderGen |
| 38 | Surface Area of cone | Surface area of cone with height = 29m and radius = 1m is | 94 m^2 | surfaceAreaConeGen |
| 39 | Volume of cone | Volume of cone with height = 2m and radius = 15m is | 471 m^3 | volumeConeGen |
| 40 | Common Factors | Common Factors of 52 and 53 =  | [1] | commonFactors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -8/4x + 3 and y = -6x - 4 | (-7/4, 13/2) | intersectionOfTwoLines |
| 42 | Permutations | Number of Permutations from 13 objects picked 1 at a time =   | 13 | permutations |
| 43 | Cross Product of 2 Vectors | [-6, -20, -15] X [-17, 14, 18] =  | [-150, 363, -424] | vectorCross |
| 44 | Compare Fractions | Which symbol represents the comparison between 7/4 and 5/6? | > | compareFractions |
| 45 | Simple Interest | Simple interest for a principle amount of 4813 dollars, 2% rate of interest and for a time period of 4 years is =  | 385.04 | simpleInterest |
| 46 | Multiplication of two matrices | Multiply 
   -11     -69      54      67  
    54     -24      52      35  
     9     -76      82      65  
    37     -40      87     -85  
    42      45      74      75  

 and 

    62     -96     -68      97     -88      71      69  
   -38      48     -31       8      53      18     100  
    57     -41      54      81     -74     -80      47  
   -63     -10      86      -6      77      31     -12   |    797   -5140   11565    2353   -1526   -4266   -5925  
  5019   -8818    2890    9048   -7177     327    3350  
  4025   -8524   11762    6517   -5883   -5274   -3905  
 14128   -8189   -3888   10826  -18359   -7688    3662  
   387   -5656    6195    9978   -1012     197    9976   | matrixMultiplication |
| 47 | Cube Root | cuberoot of 566 upto 2 decimal places is: | 8.27 | CubeRoot |
| 48 | Power Rule Integration | 6x^3 + 6x^4 + 5x^2 + 10x^9 | (6/3)x^4 + (6/4)x^5 + (5/2)x^3 + (10/9)x^10 + c | powerRuleIntegration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 6 , 199, 42 = | 113 | fourthAngleOfQuadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 63x^2+118x+19=0 | [-0.18, -1.7] | quadraticEquationSolve |
| 51 | HCF (Highest Common Factor) | HCF of 20 and 14 =  | 2 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 3 dice are rolled at the same time, the probability of getting a sum of 5 = | 6/216 | diceSumProbability |
| 53 | Exponentiation | 1^3 = | 1 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [289, 284, 269, 211, 272, 298, 290, 220, 206, 224, 230, 222, 227, 209, 262, 255, 282, 253, 274, 265, 258, 248, 277, 279, 223, 221, 219, 286, 259, 297, 234, 201, 232, 203, 294, 252, 207, 278, 202] with 80% confidence is | (255.4031906501125, 242.64809140116955) | confidenceInterval |
| 55 | Comparing surds | Fill in the blanks 50^(1/9) _ 61^(1/7) | < | surdsComparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 1 numbers is ? | [0] | fibonacciSeries |
| 57 | Trigonometric Values | What is sin(30)? | 1/2 | basicTrigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 8 sides =  | 1080 | sumOfAnglesOfPolygon |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[11, 17, 17, 20, 25, 38, 45, 19, 38, 31, 23, 16, 42, 28, 16] | The Mean is 25.733333333333334 , Standard Deviation is 107.66222222222224, Variance is 10.376040777783318 | dataSummary |
| 59 | Surface Area of Sphere | Surface area of Sphere with radius = 13m is | 2123.7166338267 m^2 | surfaceAreaSphereGen |
| 60 | Volume of Sphere | Volume of sphere with radius 100 m =  | 4188790.2047863905 m^3 | volumeSphere |
| 61 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 6 and 66 =  |  2/((1/6) + (1/66)) = 11.0 | harmonicMean |
