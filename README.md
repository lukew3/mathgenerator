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
| 0 | Addition | 37+40= | 77 | addition |
| 1 | Subtraction | 69-59= | 10 | subtraction |
| 2 | Multiplication | 18*0= | 0 | multiplication |
| 3 | Division | 66/25= | 2.64 | division |
| 4 | Binary Complement 1s | 00 | 11 | binaryComplement1s |
| 5 | Modulo Division | 37%68= | 37 | moduloDivision |
| 6 | Square Root | sqrt(4)= | 2 | squareRoot |
| 7 | Power Rule Differentiation | 6x^3 + 7x^5 + 6x^4 | 18x^2 + 35x^4 + 24x^3 | powerRuleDifferentiation |
| 8 | Square | 19^2= | 361 | square |
| 9 | LCM (Least Common Multiple) | LCM of 8 and 4 =  | 8 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 20 and 1 =  | 1 | gcd |
| 11 | Basic Algebra | 9x + 7 = 10 | 1/3 | basicAlgebra |
| 12 | Logarithm | log3(9) | 2 | log |
| 13 | Easy Division | 48/24 =  | 2 | intDivision |
| 14 | Decimal to Binary | Binary of 69= | 1000101 | decimalToBinary |
| 15 | Binary to Decimal | 0010101100 | 172 | binaryToDecimal |
| 16 | Fraction Division | (8/2)/(7/5) | 20/7 | fractionDivision |
| 17 | Integer Multiplication with 2x2 Matrix | 10 * [[0, 3], [10, 5]] =  | [[0,30],[100,50]] | intMatrix22Multiplication |
| 18 | Area of Triangle | Area of triangle with side lengths: 16 1 19 =  | (1.5148044320877339e-15+24.73863375370596j) | areaOfTriangle |
| 19 | Triangle exists check | Does triangle with sides 24, 25 and 24 exist? | Yes | doesTriangleExist |
| 20 | Midpoint of the two point | (-15,2),(12,-5)= | (-1.5,-1.5) | midPointOfTwoPoint |
| 21 | Factoring Quadratic | x^2-2x-3 | (x+1)(x-3) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 65 and 78 =  | 37 | thirdAngleOfTriangle |
| 23 | Solve a System of Equations in R^2 | 2x - 8y = -58, 3x - 4y = -31 | x = -1, y = 7 | systemOfEquations |
| 24 | Distance between 2 points | Find the distance between (21, 15) and (7, -4) | sqrt(557) | distance2Point |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 20 and 20 =  | 28.28 | pythagoreanTheorem |
| 26 | Linear Equations | -19x + -4y = 231
13x + 18y = -387 | x = -9, y = -15 | linearEquations |
| 27 | Prime Factorisation | Find prime factors of 185 | [5, 37] | primeFactors |
| 28 | Fraction Multiplication | (4/10)*(4/9) | 8/45 | fractionMultiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 17 sides | 158.82 | angleRegularPolygon |
| 30 | Combinations of Objects | Number of combinations from 10 objects picked 1 at a time  | 10 | combinations |
| 31 | Factorial | 3! =  | 6 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 16m is | 1536 m^2 | surfaceAreaCubeGen |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 6m, 7m, 17m is | 526 m^2 | surfaceAreaCuboidGen |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 19m and radius = 4m is | 578 m^2 | surfaceAreaCylinderGen |
| 35 | Volum of Cube | Volume of cube with side = 7m is | 343 m^3 | volumeCubeGen |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 1m, 17m, 18m is | 306 m^3 | volumeCuboidGen |
| 37 | Volume of cylinder | Volume of cylinder with height = 16m and radius = 10m is | 5026 m^3 | volumeCylinderGen |
| 38 | Surface Area of cone | Surface area of cone with height = 36m and radius = 3m is | 368 m^2 | surfaceAreaConeGen |
| 39 | Volume of cone | Volume of cone with height = 21m and radius = 6m is | 791 m^3 | volumeConeGen |
| 40 | Common Factors | Common Factors of 31 and 79 =  | [1] | commonFactors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 5x and y = -8/3x - 7 | (-21/23, -105/23) | intersectionOfTwoLines |
| 42 | Permutations | Number of Permutations from 13 objects picked 3 at a time =   | 1716 | permutations |
| 43 | Cross Product of 2 Vectors | [10, 11, -18] X [-2, 13, -2] =  | [212, 56, 152] | vectorCross |
| 44 | Compare Fractions | Which symbol represents the comparison between 4/2 and 4/1? | < | compareFractions |
| 45 | Simple Interest | Simple interest for a principle amount of 5369 dollars, 1% rate of interest and for a time period of 9 years is =  | 483.21 | simpleInterest |
| 46 | Multiplication of two matrices | Multiply 
   -16      87     100      -5     -69      97     -75      19  
    90     -83     -16      81     -30      64      -3     -96  
   -74     -66      48      99      35       6     -14      70  
   -24      67      -4     -95       4      51      31     -17  
    61      46     -72      66     -31      15      61     -31  
    84      63      78     -51     -11     -38     -68     -50  
    82      83      16    -100      17       2       8     -83  
    28      71     -68     -66      37     -84      79      32  

 and 

    50     -78      66      -8     -33     -61     -75     -18     -50  
   -98      10     -66     -53     -24     -36      62     -39     -35  
    86     -52     -49      47      62       0     -12      96      55  
    61      41     -77     -89      46     -44      50       4     -81  
   -12     -88     -88       9      83      62      60     -22      15  
    26      -3      44     -60      83     100     -35      97      26  
   -17     -93      -5      79      55      78      32       0     -45  
   -17     -54     -92     -48     -88      46      82     -22      12   |   3271    8443   -2346  -12616     937   -1490   -3233   16984    8750  
 19906    4214   20268   -4021   12861   -6176  -19662    9385   -8839  
 11719    1099  -19689   -6976    8029    7432   13014    7182    2782  
-12865   -3615    4806    5149    2332   10216    -695    2288    6117  
 -3372     836    5371   -7056     210   -5371    -534   -6721  -17158  
  2773   -1963    5727    3403   -5201  -17234  -11486     971    3323  
 -7635   -8262   13038    9246    1015   -5530  -11796   -1931     926  
-19947  -12723   -4715    8769  -12252     168   10130  -19731   -7079   | matrixMultiplication |
| 47 | Cube Root | cuberoot of 136 upto 2 decimal places is: | 5.14 | CubeRoot |
| 48 | Power Rule Integration | 9x^4 + 8x^6 + 2x^5 + 3x^10 + 2x^9 | (9/4)x^5 + (8/6)x^7 + (2/5)x^6 + (3/10)x^11 + (2/9)x^10 + c | powerRuleIntegration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 69 , 87, 120 = | 84 | fourthAngleOfQuadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 71x^2+188x+17=0 | [-0.09, -2.55] | quadraticEquationSolve |
| 51 | HCF (Highest Common Factor) | HCF of 3 and 16 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 3 dice are rolled at the same time, the probability of getting a sum of 8 = | 21/216 | diceSumProbability |
| 53 | Exponentiation | 9^3 = | 729 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [203, 266, 261, 263, 262, 251, 267, 248, 208, 228, 215, 221, 282, 242, 272, 281, 289, 290, 285, 217, 213, 200, 292, 256, 232, 273, 295, 271, 211, 250, 231, 246, 277, 259, 283, 233] with 90% confidence is | (259.72847423786504, 244.32708131769053) | confidenceInterval |
| 55 | Comparing surds | Fill in the blanks 50^(1/7) _ 86^(1/5) | < | surdsComparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 3 numbers is ? | [0, 1, 1] | fibonacciSeries |
| 57 | Trigonometric Values | What is tan(45)? | 1 | basicTrigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 5 sides =  | 540 | sumOfAnglesOfPolygon |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[10, 25, 12, 26, 15, 13, 41, 25, 50, 13, 20, 22, 42, 36, 22] | The Mean is 24.8 , Standard Deviation is 141.09333333333333, Variance is 11.87827147918978 | dataSummary |
| 59 | Surface Area of Sphere | Surface area of Sphere with radius = 5m is | 314.1592653589793 m^2 | surfaceAreaSphereGen |
| 60 | Volume of Sphere | Volume of sphere with radius 70 m =  | 1436755.0402417318 m^3 | volumeSphere |
| 61 | Geometric Mean of N Numbers | Geometric mean of 2 numbers 9 and 5 =  | (9*5)^(1/2) = 6.708203932499369 | geometricMean |
