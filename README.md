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
| 0 | Addition | 42+2= | 44 | addition |
| 1 | Subtraction | 32-26= | 6 | subtraction |
| 2 | Multiplication | 77*1= | 77 | multiplication |
| 3 | Division | 66/9= | 7.333333333333333 | division |
| 4 | Binary Complement 1s | 1010000 | 0101111 | binaryComplement1s |
| 5 | Modulo Division | 61%35= | 26 | moduloDivision |
| 6 | Square Root | sqrt(1)= | 1 | squareRoot |
| 7 | Power Rule Differentiation | 5x^5 | 25x^4 | powerRuleDifferentiation |
| 8 | Square | 20^2= | 400 | square |
| 9 | LCM (Least Common Multiple) | LCM of 19 and 5 =  | 95 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 10 and 11 =  | 1 | gcd |
| 11 | Basic Algebra | 3x + 7 = 8 | 1/3 | basicAlgebra |
| 12 | Logarithm | log2(128) | 7 | log |
| 13 | Easy Division | 306/18 =  | 17 | intDivision |
| 14 | Decimal to Binary | Binary of 28= | 11100 | decimalToBinary |
| 15 | Binary to Decimal | 10001101 | 141 | binaryToDecimal |
| 16 | Fraction Division | (4/1)/(6/3) | 2 | fractionDivision |
| 17 | Integer Multiplication with 2x2 Matrix | 5 * [[10, 3], [0, 1]] =  | [[50,15],[0,5]] | intMatrix22Multiplication |
| 18 | Area of Triangle | Area of triangle with side lengths: 13 2 14 =  | 11.659223816361019 | areaOfTriangle |
| 19 | Triangle exists check | Does triangle with sides 3, 4 and 25 exist? | No | doesTriangleExist |
| 20 | Midpoint of the two point | (4,-11),(17,-5)= | (10.5,-8.0) | midPointOfTwoPoint |
| 21 | Factoring Quadratic | x^2-12x+35 | (x-7)(x-5) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 20 and 62 =  | 98 | thirdAngleOfTriangle |
| 23 | Solve a System of Equations in R^2 | 5x - 7y = -84, 4x + 5y = 7 | x = -7, y = 7 | systemOfEquations |
| 24 | Distance between 2 points | Find the distance between (5, -18) and (1, 19) | sqrt(1385) | distance2Point |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 15 and 5 =  | 15.81 | pythagoreanTheorem |
| 26 | Linear Equations | -6x + -17y = -220
-13x + -19y = -120 | x = -20, y = 20 | linearEquations |
| 27 | Prime Factorisation | Find prime factors of 62 | [2, 31] | primeFactors |
| 28 | Fraction Multiplication | (8/4)*(1/2) | 1 | fractionMultiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 19 sides | 161.05 | angleRegularPolygon |
| 30 | Combinations of Objects | Number of combinations from 12 objects picked 1 at a time  | 12 | combinations |
| 31 | Factorial | 0! =  | 1 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 8m is | 384 m^2 | surfaceAreaCubeGen |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 18m, 17m, 1m is | 682 m^2 | surfaceAreaCuboidGen |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 31m and radius = 1m is | 201 m^2 | surfaceAreaCylinderGen |
| 35 | Volum of Cube | Volume of cube with side = 9m is | 729 m^3 | volumeCubeGen |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 20m, 1m, 10m is | 200 m^3 | volumeCuboidGen |
| 37 | Volume of cylinder | Volume of cylinder with height = 7m and radius = 7m is | 1077 m^3 | volumeCylinderGen |
| 38 | Surface Area of cone | Surface area of cone with height = 47m and radius = 13m is | 2522 m^2 | surfaceAreaConeGen |
| 39 | Volume of cone | Volume of cone with height = 4m and radius = 4m is | 67 m^3 | volumeConeGen |
| 40 | Common Factors | Common Factors of 20 and 90 =  | [1, 2, 5, 10] | commonFactors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -3/6x + 1 and y = 0/2x + 6 | (-10, 6) | intersectionOfTwoLines |
| 42 | Permutations | Number of Permutations from 11 objects picked 2 at a time =   | 110 | permutations |
| 43 | Cross Product of 2 Vectors | [-19, -3, 2] X [-15, -12, 7] =  | [3, 103, 183] | vectorCross |
| 44 | Compare Fractions | Which symbol represents the comparison between 8/6 and 3/1? | < | compareFractions |
| 45 | Simple Interest | Simple interest for a principle amount of 9862 dollars, 4% rate of interest and for a time period of 1 years is =  | 394.48 | simpleInterest |
| 46 | Multiplication of two matrices | Multiply 
   -50      36       7     -26      -2      63  
    88     -37      60     -19      61     -56  
    48      -5      69     -87     -64     -92  
   -84     -50     -79     -19      86     -13  
     0      28      12     -14      73     -49  
    94     -90       2      26     -38      19  
     2     -11      79     -77      98     -77  
   -87      70      72     -32      64     -99  

 and 

    34      32      -6     -32      46     -23      78     -81     -18  
   -17      24      49     -62     -50      77      38     -98     -64  
   -23     -78      43       5     -83      -5       4     -92     -16  
    46     -47     -92      52     -25     -37      44      51      -7  
    20      26      70      37      96     -73      49      84      42  
   -72     -15     -80     -24      58     -47     -41      45     -69   |  -8245   -1057    -423   -3535    -569    2034   -6329    1219   -5765  
  6619     567   10737    2391    4001   -6291   10147   -7387    6383  
  1472    -161   13318   -5565  -12574   10381     638  -23699    2621  
  1593    5598    3465    7899   13170   -6487   -4857   24642   10618  
  3592    3027   12206    1473    2120    -412    6082    -635    4561  
  3748   -1803  -11460    2072    5462   -8183    2423      11     947  
  2400     960   22950    2483     952   -1974    4625   -5512    9372  
  1132   -2067   22392    1884  -12276    8196    1949   -7148    5677   | matrixMultiplication |
| 47 | Cube Root | cuberoot of 771 upto 2 decimal places is: | 9.17 | CubeRoot |
| 48 | Power Rule Integration | 1x^3 + 8x^8 + 10x^10 | (1/3)x^4 + (8/8)x^9 + (10/10)x^11 + c | powerRuleIntegration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 52 , 84, 154 = | 70 | fourthAngleOfQuadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 51x^2+152x+80=0 | [-0.68, -2.3] | quadraticEquationSolve |
| 51 | HCF (Highest Common Factor) | HCF of 11 and 7 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 2 dice are rolled at the same time, the probability of getting a sum of 11 = | 2/36 | diceSumProbability |
| 53 | Exponentiation | 9^9 = | 387420489 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [291, 254, 274, 207, 253, 289, 268, 280, 225, 240, 278, 270, 247, 252, 211, 212, 295, 241, 290, 206, 222, 263, 264, 228, 229, 256, 209, 292] with 99% confidence is | (265.560249263099, 237.72546502261523) | confidenceInterval |
| 55 | Comparing surds | Fill in the blanks 16^(1/7) _ 67^(1/6) | < | surdsComparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 11 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55] | fibonacciSeries |
| 57 | Trigonometric Values | What is cos(60)? | 1/2 | basicTrigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 5 sides =  | 540 | sumOfAnglesOfPolygon |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[38, 29, 43, 25, 7, 10, 13, 14, 43, 44, 30, 42, 48, 48, 42] | The Mean is 31.733333333333334 , Standard Deviation is 199.26222222222222, Variance is 14.116027140177303 | dataSummary |
| 59 | Surface Area of Sphere | Surface area of Sphere with radius = 13m is | 2123.7166338267 m^2 | surfaceAreaSphereGen |
| 60 | Volume of Sphere | Volume of sphere with radius 84 m =  | 2482712.7095377133 m^3 | volumeSphere |
| 61 | Compound Interest | Compound interest for a principle amount of 5618 dollars, 7% rate of interest and for a time period of 5 year is = | 7879.54 | compoundInterestFunc |
