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
| 0 | Addition | 16+3= | 19 | subtraction |
| 1 | Subtraction | 96-17= | 79 | multiplication |
| 2 | Multiplication | 48*1= | 48 | multiplicationFunc) |
| 3 | Division | 83/97= | 0.8556701030927835 | division |
| 4 | Binary Complement 1s | 1110110111= | 0001001000 | binaryComplement1s |
| 5 | Modulo Division | 91%53= | 38 | binaryComplement1sFunc) |
| 6 | Square Root | sqrt(64)= | 8 | moduloDivision |
| 7 | Power Rule Differentiation | 6x^7 | 42x^6 | squareRoot |
| 8 | Square | 5^2= | 25 | powerRuleDifferentiation |
| 9 | LCM (Least Common Multiple) | LCM of 20 and 10 = | 20 | "(n*m)x^(m-1)", |
| 10 | GCD (Greatest Common Denominator) | GCD of 16 and 20 =  | 4 | powerRuleDifferentiationFunc) |
| 11 | Basic Algebra | 9x + 10 = 10 | 0 | square |
| 12 | Logarithm | log3(3) | 1 | lcm |
| 13 | Easy Division | 399/19 =  | 21 | lcmFunc) |
| 14 | Decimal to Binary | Binary of 99= | 1100011 | gcd |
| 15 | Binary to Decimal | 011100 | 28 | "c", gcdFunc) |
| 16 | Fraction Division | (6/8)/(4/7) | 21/16 | basicAlgebra |
| 17 | Integer Multiplication with 2x2 Matrix | 2 * [[3, 3], [6, 3]] =  | [[6,6],[12,6]] | basicAlgebraFunc) |
| 18 | Area of Triangle | Area of triangle with side lengths: 11 11 17 =  | 59.348020186018 | log |
| 19 | Triangle exists check | Does triangle with sides 23, 29 and 34 exist? | Yes | intDivision |
| 20 | Midpoint of the two point | (0,-20),(14,-16)= | (7.0,-18.0) | decimalToBinary |
| 21 | Factoring Quadratic | x^2-5x-36 | (x-9)(x+4) | DecimalToBinaryFunc) |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 32 and 60 =  | 88 | binaryToDecimal |
| 23 | Solve a System of Equations in R^2 | 4x - 6y = 14, -7x - 2y = 88 | x = -10, y = -9 | BinaryToDecimalFunc) |
| 24 | Distance between 2 points | Find the distance between (14, -9) and (12, 13) | sqrt(488) | fractionDivision |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 13 and 1 =  | 13.04 | divideFractionsFunc) |
| 26 | Linear Equations | -12x + 13y = -22
-1x + -7y = -18 | x = 4, y = 2 | intMatrix22Multiplication |
| 27 | Prime Factorisation | Find prime factors of 2 | [2] | 17, "k * [[a,b],[c,d]] |
| 28 | Fraction Multiplication | (8/6)*(4/10) | 8/15 | "[[k*a,k*b],[k*c,k*d]]", |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 11 sides | 147.27 | multiplyIntToMatrix22) |
| 30 | Combinations of Objects | Number of combinations from 15 objects picked 7 at a time  | 6435 | areaOfTriangle |
| 31 | Factorial | 3! =  | 6 | "Area of Triangle with side lengths a, b, c |
| 32 | Surface Area of Cube | Surface area of cube with side = 14m is | 1176 m^2 | "area", areaOfTriangleFunc) |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 17m, 7m, 10m is | 718 m^2 | doesTriangleExist |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 36m and radius = 7m is | 1891 m^2 | "Does triangle with sides a, b and c exist?", |
| 35 | Volum of Cube | Volume of cube with side = 10m is | 1000 m^3 | "Yes/No", isTriangleValidFunc) |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 20m, 17m, 4m is | 1360 m^3 | midPointOfTwoPoint |
| 37 | Volume of cylinder | Volume of cylinder with height = 13m and radius = 1m is | 40 m^3 | "((X1,Y1),(X2,Y2)) |
| 38 | Surface Area of cone | Surface area of cone with height = 17m and radius = 9m is | 798 m^2 | MidPointOfTwoPointFunc) |
| 39 | Volume of cone | Volume of cone with height = 15m and radius = 5m is | 392 m^3 | factoring |
| 40 | Common Factors | Common Factors of 69 and 51 =  | [1, 3] | "(x-x1)(x-x2)", factoringFunc) |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 6/3x + 9 and y = 6x + 2 | (7/4, 25/2) | thirdAngleOfTriangle |
| 42 | Permutations | Number of Permutations from 14 objects picked 1 at a time =   | 14 | "Third Angle of the triangle |
| 43 | Cross Product of 2 Vectors | [19, 17, -9] X [10, -10, -2] =  | [-124, -52, -360] | thirdAngleOfTriangleFunc) |
| 44 | Compare Fractions | Which symbol represents the comparison between 10/6 and 10/8? | > | systemOfEquations |
| 45 | Simple Interest | Simple interest for a principle amount of 7091 dollars, 10% rate of interest and for a time period of 4 years is =  | 2836.4 | "2x + 5y |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>2</td><td>8</td><td>-4</td><td>5</td></tr><tr><td>6</td><td>-5</td><td>-6</td><td>4</td></tr></table>and<table><tr><td>-5</td><td>1</td><td>-3</td><td>2</td></tr><tr><td>5</td><td>8</td><td>5</td><td>-5</td></tr><tr><td>-6</td><td>-8</td><td>-6</td><td>-7</td></tr><tr><td>-1</td><td>-5</td><td>3</td><td>-7</td></tr></table> | <table><tr><td>49</td><td>73</td><td>73</td><td>-43</td></tr><tr><td>-23</td><td>-6</td><td>5</td><td>51</td></tr></table> | systemOfEquationsFunc) |
| 47 | Cube Root | cuberoot of 951 upto 2 decimal places is: | 9.83 | distance2Point |
| 48 | Power Rule Integration | 10x^1 + 10x^6 + 1x^4 + 1x^6 | (10/1)x^2 + (10/6)x^7 + (1/4)x^5 + (1/6)x^7 + c | "Find the distance between (x1,y1) and (x2,y2)", |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 15 , 191, 94 = | 60 | "sqrt(distanceSquared)", distanceTwoPointsFunc) |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 48x^2+119x+57=0 | [-0.65, -1.83] | pythagoreanTheorem |
| 51 | HCF (Highest Common Factor) | HCF of 5 and 18 =  | 1 | "Pythagorean Theorem", 25, |
| 52 | Probability of a certain sum appearing on faces of dice | If 1 dice are rolled at the same time, the probability of getting a sum of 2 = | 1/6 | "The hypotenuse of a right triangle given the other two lengths a and b |
| 53 | Exponentiation | 17^7 = | 410338673 | "hypotenuse", pythagoreanTheoremFunc) |
| 54 | Confidence interval For sample S | The confidence interval for sample [247, 230, 236, 207, 226, 278, 221, 297, 280, 267, 240, 259, 291, 284, 242, 252, 257, 220, 260, 213, 294] with 90% confidence is | (262.13973862175516, 242.71740423538768) | # This has multiple variables whereas #23 has only x and y |
| 55 | Comparing surds | Fill in the blanks 17^(1/2) _ 3^(1/6) | > | linearEquations |
| 56 | Fibonacci Series | The Fibonacci Series of the first 14 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233] | "x |
| 57 | Trigonometric Values | What is sin(90)? | 1 | primeFactors |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 7 sides =  | 900 | "[b, c, d, ...]", primeFactorsFunc) |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[10, 47, 7, 37, 22, 44, 9, 30, 37, 8, 50, 29, 19, 12, 37] | The Mean is 26.533333333333335 , Standard Deviation is 214.38222222222217, Variance is 14.641797096744039 | fractionMultiplication |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 6m is | 452.3893421169302 m^2 | "(a/b)*(c/d) |
| 61 | Volume of Sphere | Volume of sphere with radius 54 m =  | 659583.6608064842 m^3 | multiplyFractionsFunc) |
| 62 | nth Fibonacci number | What is the 5th Fibonacci number? | 5 | angleRegularPolygon |
| 63 | Profit or Loss Percent | Loss percent when CP = 801 and SP = 230 is:  | 71.28589263420724 | "Angle of a Regular Polygon", 29, |
| 64 | Binary to Hexidecimal | 101111 | 0x2f | "Find the angle of a regular polygon with 6 sides", "120", |
| 65 | Multiplication of 2 complex numbers | (1+19j) * (-5+10j) =  | (-195-85j) | regularPolygonAngleFunc) |
| 66 | Geometric Progression | For the given GP [8, 88, 968, 10648, 117128, 1288408] ,Find the value of a,common ratio,11th term value, sum upto 8th term | The value of a is 8, common ratio is 11 , 11th term is 207499396808 , sum upto 8th term is 171487104.0 | combinations |
| 67 | Geometric Mean of N Numbers | Geometric mean of 2 numbers 9 and 18 =  | (9*18)^(1/2) = 12.727922061357855 | "Combinations of Objects", 30, |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 59 and 8 =  |  2/((1/59) + (1/8)) = 14.08955223880597 | "Combinations available for picking 4 objects at a time from 6 distinct objects |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[868.2223524505417, 443.64852085459694, 828.1090462421802] is: | 1279.217986044348 | " 15", combinationsFunc) |
| 70 | Angle between 2 vectors | angle between the vectors [47.34750277983446, 802.0548522330859, 163.10760759590525, 544.7736923139344, 595.2668887448631, 781.8577226989729, 505.92984665962115, 212.21898772758718, 417.09503653850567, 498.8451357914803, 216.11050052884383, 316.85172611004697, 531.4467890864679] and [551.4845648456056, 524.0267675199452, 252.30514761182056, 256.4954536977715, 423.09002486817883, 861.6683390714214, 210.90265341510906, 918.3205871874211, 539.9315722140092, 988.4812675617247, 885.1803007416202, 566.6430154592439, 851.2210274645834] is: | NaN | factorial |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 51 and 3 =  | 48 | surfaceAreaCubeGen |
| 72 | Dot Product of 2 Vectors | [4, 20, 12] . [15, 11, 9] =  | 388 | "Surface area of cube with side a units is", |
| 73 | Binary 2's Complement | 2's complement of 1 = | 1 | "b units^2", surfaceAreaCube) |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[2, 25, 60], [29, 30, 28], [23, 73, 95]]) is: | Matrix([[806/34457, 2005/34457, -1100/34457], [-2111/34457, -1190/34457, 1684/34457], [1427/34457, 429/34457, -665/34457]]) | surfaceAreaCuboidGen |
| 75 | Area of a Sector | Given radius, 28 and angle, 317. Find the area of the sector. | Area of sector = 2168.81594 | "Surface Area of Cuboid", 33, |
| 76 | Mean and Median | Given the series of numbers [67, 33, 40, 90, 81, 12, 91, 80, 5, 66]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 56.5 and Arithmetic median of this series is 66.5 | "Surface area of cuboid with sides |
| 77 | Determinant to 2x2 Matrix | Det([[10, 0], [95, 32]]) =  |  320 | "d units^2", surfaceAreaCuboid) |
| 78 | Compound Interest | Compound Interest for a principle amount of 4156 dollars, 8% rate of interest and for a time period of 7 compounded monthly is =  | 4156.0 | surfaceAreaCylinderGen |
| 79 | Decimal to Hexadecimal | Binary of 143= | 0x8f | "Surface Area of Cylinder", 34, |
| 80 | Percentage of a number | What is 49% of 13? | Required percentage = 6.37% | "Surface area of cylinder with height |
