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
| 0 | Addition | 29+33= | 62 | addition |
| 1 | Subtraction | 62-7= | 55 | subtraction |
| 2 | Multiplication | 93*1= | 93 | multiplication |
| 3 | Division | 59/47= | 1.2553191489361701 | division |
| 4 | Binary Complement 1s | 001110000 | 110001111 | binaryComplement1s |
| 5 | Modulo Division | 89%34= | 21 | moduloDivision |
| 6 | Square Root | sqrt(16)= | 4 | squareRoot |
| 7 | Power Rule Differentiation | 4x^3 | 12x^2 | powerRuleDifferentiation |
| 8 | Square | 12^2= | 144 | square |
| 9 | LCM (Least Common Multiple) | LCM of 10 and 1 =  | 10 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 12 and 5 =  | 1 | gcd |
| 11 | Basic Algebra | 8x + 7 = 10 | 3/8 | basicAlgebra |
| 12 | Logarithm | log3(729) | 6 | log |
| 13 | Easy Division | 378/21 =  | 18 | intDivision |
| 14 | Decimal to Binary | Binary of 4= | 100 | decimalToBinary |
| 15 | Binary to Decimal | 10011 | 19 | binaryToDecimal |
| 16 | Fraction Division | (1/2)/(4/3) | 3/8 | fractionDivision |
| 17 | Integer Multiplication with 2x2 Matrix | 2 * [[0, 7], [7, 7]] =  | [[0,14],[14,14]] | intMatrix22Multiplication |
| 18 | Area of Triangle | Area of triangle with side lengths: 9 14 15 =  | 61.644140029689765 | areaOfTriangle |
| 19 | Triangle exists check | Does triangle with sides 33, 6 and 43 exist? | No | doesTriangleExist |
| 20 | Midpoint of the two point | (-15,-10),(-5,2)= | (-10.0,-4.0) | midPointOfTwoPoint |
| 21 | Factoring Quadratic | x^2-17x+72 | (x-9)(x-8) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 4 and 31 =  | 145 | thirdAngleOfTriangle |
| 23 | Solve a System of Equations in R^2 | 4x - 8y = 48, 3x - 8y = 40 | x = 8, y = -2 | systemOfEquations |
| 24 | Distance between 2 points | Find the distance between (-9, -20) and (18, -19) | sqrt(730) | distance2Point |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 18 and 13 =  | 22.20 | pythagoreanTheorem |
| 26 | Linear Equations | -11x + -16y = -302
1x + 20y = 250 | x = 10, y = 12 | linearEquations |
| 27 | Prime Factorisation | Find prime factors of 55 | [5, 11] | primeFactors |
| 28 | Fraction Multiplication | (4/9)*(8/10) | 16/45 | fractionMultiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 15 sides | 156.0 | angleRegularPolygon |
| 30 | Combinations of Objects | Number of combinations from 13 objects picked 1 at a time  | 13 | combinations |
| 31 | Factorial | 2! =  | 2 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 13m is | 1014 m^2 | surfaceAreaCubeGen |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 5m, 3m, 7m is | 142 m^2 | surfaceAreaCuboidGen |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 15m and radius = 7m is | 967 m^2 | surfaceAreaCylinderGen |
| 35 | Volum of Cube | Volume of cube with side = 11m is | 1331 m^3 | volumeCubeGen |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 6m, 1m, 10m is | 60 m^3 | volumeCuboidGen |
| 37 | Volume of cylinder | Volume of cylinder with height = 26m and radius = 15m is | 18378 m^3 | volumeCylinderGen |
| 38 | Surface Area of cone | Surface area of cone with height = 46m and radius = 14m is | 2730 m^2 | surfaceAreaConeGen |
| 39 | Volume of cone | Volume of cone with height = 7m and radius = 11m is | 886 m^3 | volumeConeGen |
| 40 | Common Factors | Common Factors of 91 and 51 =  | [1] | commonFactors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 6/4x + 5 and y = -7/2x + 3 | (-2/5, 22/5) | intersectionOfTwoLines |
| 42 | Permutations | Number of Permutations from 13 objects picked 4 at a time =   | 17160 | permutations |
| 43 | Cross Product of 2 Vectors | [-14, 13, 20] X [-5, -18, 19] =  | [607, 166, 317] | vectorCross |
| 44 | Compare Fractions | Which symbol represents the comparison between 8/3 and 6/7? | > | compareFractions |
| 45 | Simple Interest | Simple interest for a principle amount of 6128 dollars, 5% rate of interest and for a time period of 5 years is =  | 1532.0 | simpleInterest |
| 46 | Multiplication of two matrices | Multiply [[-20, -14, -88, -62, 39, 94, 21, 75, 26], [89, -67, -80, -60, 32, -23, -79, 11, -69], [13, -75, -66, 3, 67, -79, -49, 6, 36], [-44, -84, 68, -27, -86, -95, -71, -77, -62], [45, 58, 89, 82, 30, -83, -23, 51, 95], [11, 46, 100, -15, 60, -34, 85, 50, -44], [93, -100, -62, 63, -73, -64, 90, -15, 23], [-8, 91, -22, 53, -42, 25, 32, -26, 31], [-60, 90, 75, -42, 19, 33, -30, 74, 13]] and [[-80, 54, -39, 37, -99], [31, -28, -31, 64, 73], [-21, -34, -28, -21, -76], [-94, 55, 66, 0, 17], [-28, 25, -65, -74, 100], [76, 74, -96, -98, -5], [-90, -70, -66, -71, -35], [65, 49, -100, 72, -23], [-95, -97, -31, -84, -86]] | [[15409, 6508, -21665, -10161, 5326], [9859, 17962, 3267, 12768, 3119], [-8761, 1272, 8611, 738, 3881], [4489, -5790, 29652, 11947, -5940], [-22167, -8208, -1142, 6747, -10714], [-4628, -5167, -15527, 1404, 243], [-29240, -2432, 11103, 615, -22487], [-5498, -5038, 1462, -100, 2495], [18214, -3238, -15548, 3691, 6061]] | matrixMultiplication |
| 47 | Cube Root | cuberoot of 711 upto 2 decimal places is: | 8.93 | CubeRoot |
| 48 | Power Rule Integration | 3x^1 | (3/1)x^2 + c | powerRuleIntegration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 94 , 101, 102 = | 63 | fourthAngleOfQuadrilateral |
