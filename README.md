# mathgenerator

A math problem generator, created for the purpose of giving self-studying students and teaching organizations the means to easily get access to random math problems to suit their needs.

To try out generators, go to <https://lukew3.com/mathgenerator>

If you have an idea for a generator, please add it as an issue and tag it with the "New Generator" label.

## Table of Contents
* [Installation](#installation)
* [Basic Usage](#basic-usage)
  * [Creating a worksheet](#creating-a-worksheet)
* [Documentation](#documentation)
* [List of Generators](#list-of-generators)
  * [algebra](#algebra)
  * [basic_math](#basic_math)
  * [calculus](#calculus)
  * [computer_science](#computer_science)
  * [geometry](#geometry)
  * [misc](#misc)
  * [statistics](#statistics)

## Installation

The project can be install via pip

```bash
pip install mathgenerator
```

## Basic Usage
Here is an example of how you would generate an addition problem:

```python
from mathgenerator import mathgen

#generate an addition problem
problem, solution = mathgen.addition()

#another way to generate an addition problem using genById()
problem, solution = mathgen.genById(0)
```
### Creating a worksheet
If you wish to create a worksheet, you can use the [worksheetgen](https://github.com/lukew3/worksheetgen) package. Install this with `pip install worksheetgen`. Here is an example of how a worksheet would be generated.
```
from mathgenerator import mathgen
from worksheetgen.wg import Worksheet

worksheet = Worksheet("Worksheet title")
worksheet.add_instruction("Instructions")
# Writes 10 problems generated with id 1, [0] at the end specifies to take problem, and not solution.
for _ in range(10):
	worksheet.add_problem(mathgen.genById(1)[0])
worksheet.write_pdf()
```
This creates the pdf `ws.pdf` in your current directory

## Documentation
* `getGenList()` returns a list of all generators in the repository in the format `[id, title, self, funcname, subjectname]`

* `genById(id)` generates a problem, solution set with generator id `id` in the format `[problem, solution]`

## List of Generators
## algebra
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 11 | [Basic Algebra](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/basic_algebra.py) | 9x + 6 = 6 | 0 | basic_algebra | `maxVariable=10`  |
| 12 | [Logarithm](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/log.py) | log2(256) | 8 | log | `maxBase=3` `maxVal=8`  |
| 17 | [Integer Multiplication with 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_int_to_22_matrix.py) | 1 * [[3, 1], [10, 1]] =  | [[3,1],[10,1]] | multiply_int_to_22_matrix | `maxMatrixVal=10` `maxRes=100`  |
| 20 | [Midpoint of the two point](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/midpoint_of_two_points.py) | (-19,-5),(-10,-3)= | (-14.5,-4.0) | midpoint_of_two_points | `maxValue=20`  |
| 21 | [Factoring Quadratic](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/factoring.py) | x^2-18x+81 | (x-9)(x-9) | factoring | `range_x1=10` `range_x2=10`  |
| 23 | [Solve a System of Equations in R^2](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/system_of_equations.py) | -3x + 4y = -12, -x + 10y = 22 | x = 8, y = 3 | system_of_equations | `range_x=10` `range_y=10` `coeff_mult_range=10`  |
| 24 | [Distance between 2 points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/distance_two_points.py) | Find the distance between (3, 7) and (-20, -18) | sqrt(1154) | distance_two_points | `maxValXY=20` `minValXY=-20`  |
| 26 | [Linear Equations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/linear_equations.py) | 6x + -13y = 111, 2x + -4y = 36 | x = 12, y = -3 | linear_equations | `n=2` `varRange=20` `coeffRange=20`  |
| 41 | [Intersection of Two Lines](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/intersection_of_two_lines.py) | Find the point of intersection of the two lines: y = -8/4x - 7 and y = -7/3x + 4 | (33, -73) | intersection_of_two_lines | `minM=-10` `maxM=10` `minB=-10` `maxB=10` `minDenominator=1` `maxDenominator=6`  |
| 43 | [Cross Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_cross.py) | [1, 7, -1] X [-5, 8, 19] =  | [141, -14, 43] | vector_cross | `minVal=-20` `maxVal=20`  |
| 45 | [Simple Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/simple_interest.py) | Simple interest for a principle amount of 5581 dollars, 1% rate of interest and for a time period of 8 years is =  | 446.48 | simple_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 46 | [Multiplication of two matrices](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/matrix_multiplication.py) | Multiply<table><tr><td>3</td><td>-7</td><td>-9</td><td>-9</td></tr><tr><td>-2</td><td>5</td><td>-4</td><td>10</td></tr></table>and<table><tr><td>9</td><td>-2</td><td>10</td><td>-8</td></tr><tr><td>-3</td><td>10</td><td>-9</td><td>1</td></tr><tr><td>5</td><td>3</td><td>0</td><td>3</td></tr><tr><td>0</td><td>3</td><td>-10</td><td>0</td></tr></table> | <table><tr><td>3</td><td>-130</td><td>183</td><td>-58</td></tr><tr><td>-53</td><td>72</td><td>-165</td><td>9</td></tr></table> | matrix_multiplication | `maxVal=100` `max_dim=10`  |
| 50 | [Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/quadratic_equation.py) | Zeros of the Quadratic Equation 98x^2+108x+23=0 | [-0.29, -0.81] | quadratic_equation | `maxVal=100`  |
| 65 | [Multiplication of 2 complex numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_complex_numbers.py) | (8+10j) * (-7+4j) =  | (-96-38j) | multiply_complex_numbers | `minRealImaginaryNum=-20` `maxRealImaginaryNum=20`  |
| 72 | [Dot Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_dot.py) | [-3, -8, 2] . [15, 7, -6] =  | -113 | vector_dot | `minVal=-20` `maxVal=20`  |
| 74 | [Inverse of a Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/invert_matrix.py) | Inverse of Matrix Matrix([[60, 59, 5], [64, 13, 45], [54, 19, 35]]) is: | Matrix([[20/511, 197/1022, -37/146], [-19/1022, -183/1022, 17/73], [-257/5110, -1023/5110, 107/365]]) | invert_matrix | `SquareMatrixDimension=3` `MaxMatrixElement=99` `OnlyIntegerElementsInInvertedMatrix=False`  |
| 77 | [Determinant to 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/int_matrix_22_determinant.py) | Det([[38, 27], [91, 58]]) =  |  -253 | int_matrix_22_determinant | `maxMatrixVal=100`  |
| 78 | [Compound Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/compound_interest.py) | Compound interest for a principle amount of 5669 dollars, 4% rate of interest and for a time period of 8 year is =  | 7758.42 | compound_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 100 | [complex Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/complex_quadratic.py) | Find the roots of given Quadratic Equation 3x^2 + 9x + 4 = 0 | simplified solution : ((-0.543, -2.457)), generalized solution : ((-9 + sqrt(33))/2*3, (-9 - sqrt(33))/2*3) | complex_quadratic | `prob_type=0` `max_range=10`  |
| 105 | [Combine Like terms](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/combine_like_terms.py) | 7x^1 | 7x^1  | combine_like_terms | `maxCoef=10` `maxExp=20` `maxTerms=10`  |
| 111 | [Expanding Factored Binomial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/expanding.py) | (8x-5)(-3x-3) | -24*x^2-9*x+15 | expanding | `range_x1=10` `range_x2=10` `range_a=10` `range_b=10`  |
## basic_math
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 0 | [Addition](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/addition.py) | 33+15= | 48 | addition | `maxSum=99` `maxAddend=50`  |
| 1 | [Subtraction](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/subtraction.py) | 5-5= | 0 | subtraction | `maxMinuend=99` `maxDiff=99`  |
| 2 | [Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/multiplication.py) | 1*11= | 11 | multiplication | `maxMulti=12`  |
| 3 | [Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/division.py) | 384/16= | 24 | division | `maxA=25` `maxB=25`  |
| 6 | [Square Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square_root.py) | sqrt(49)= | 7 | square_root | `minNo=1` `maxNo=12`  |
| 8 | [Square](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square.py) | 13^2= | 169 | square | `maxSquareNum=20`  |
| 13 | [Complex Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/complex_division.py) | 89/11= | 8.09 | complex_division | `maxRes=99` `maxDivid=99`  |
| 16 | [Fraction Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/divide_fractions.py) | (2/9)/(3/4) | 8/27 | divide_fractions | `maxVal=10`  |
| 28 | [Fraction Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/fraction_multiplication.py) | (3/8)*(10/8) | 15/32 | fraction_multiplication | `maxVal=10`  |
| 31 | [Factorial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/factorial.py) | 2! =  | 2 | factorial | `maxInput=6`  |
| 44 | [Compare Fractions](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/compare_fractions.py) | Which symbol represents the comparison between 9/8 and 10/7? | < | compare_fractions | `maxVal=10`  |
| 47 | [Cube Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/cube_root.py) | What is the cube root of 183 up to 2 decimal places? | 5.68 | cube_root | `minNo=1` `maxNo=1000`  |
| 53 | [Exponentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/exponentiation.py) | 20^6 = | 64000000 | exponentiation | `maxBase=20` `maxExpo=10`  |
| 71 | [Absolute difference between two numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/absolute_difference.py) | |-67--16|= | 51 | absolute_difference | `maxA=100` `maxB=100`  |
| 80 | [Percentage of a number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage.py) | What is 24% of 74? | 17.76 | percentage | `maxValue=99` `maxpercentage=99`  |
| 90 | [isprime](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/is_prime.py) | Is 50 prime? | No | is_prime | `max_num=100`  |
| 97 | [Power of Powers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/power_of_powers.py) | Simplify 48^7^6= | 48^42 | power_of_powers | `maxBase=50` `maxPower=10`  |
## calculus
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 7 | [Power Rule Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_differentiation.py) | 7x^2 + 7x^3 + 5x^9 + 4x^1 | 14x^1 + 21x^2 + 45x^8 + 4x^0 | power_rule_differentiation | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 48 | [Power Rule Integration](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_integration.py) | 4x^6 + 1x^9 + 8x^1 + 1x^8 | (4/6)x^7 + (1/9)x^10 + (8/1)x^2 + (1/8)x^9 + c | power_rule_integration | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 88 | [Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/differentiation.py) | differentiate w.r.t x : d(sin(x)+8*x^3)/dx | 24*x^2 + cos(x) | differentiation | `diff_lvl=2`  |
| 89 | [Definite Integral of Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/definite_integral.py) | The definite integral within limits 0 to 1 of the equation 62x^2 + 93x + 81 is =  | 148.1667 | definite_integral | `max_coeff=100`  |
| 110 | [Stationary Points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/stationary_points.py) | f(x)=9*x^3 + 3*x^2 + 4 | (-2/9,328/81),(0,4) | stationary_points | `maxExp=3` `maxCoef=10`  |
## computer_science
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 4 | [Binary Complement 1s](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_complement_1s.py) | 01000= | 10111 | binary_complement_1s | `maxDigits=10`  |
| 5 | [Modulo Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/modulo_division.py) | 64%42= | 22 | modulo_division | `maxRes=99` `maxModulo=99`  |
| 14 | [Decimal to Binary](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_binary.py) | Binary of 63= | 111111 | decimal_to_binary | `max_dec=99`  |
| 15 | [Binary to Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_decimal.py) | 101 | 5 | binary_to_decimal | `max_dig=10`  |
| 56 | [Fibonacci Series](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/fibonacci_series.py) | The Fibonacci Series of the first 14 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233] | fibonacci_series | `minNo=1`  |
| 62 | [nth Fibonacci number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/nth_fibonacci_number.py) | What is the 67th Fibonacci number? | 44945570212853 | nth_fibonacci_number | `maxN=100`  |
| 64 | [Binary to Hexidecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_hex.py) | 0111111 | 0x3f | binary_to_hex | `max_dig=10`  |
| 73 | [Binary 2's Complement](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_2s_complement.py) | 2's complement of 10 = | 10 | binary_2s_complement | `maxDigits=10`  |
| 79 | [Decimal to Hexadecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_hexadeci.py) | Binary of 169= | 0xa9 | decimal_to_hexadeci | `max_dec=1000`  |
| 84 | [Converts decimal to octal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_octal.py) | The decimal number 3744 in Octal is:  | 0o7240 | decimal_to_octal | `maxDecimal=4096`  |
| 91 | [Binary Coded Decimal to Integer](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/bcd_to_decimal.py) | Integer of Binary Coded Decimal 1 is =  | 5924 | bcd_to_decimal | `maxNumber=10000`  |
| 103 | [Decimal to Binary Coded Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_bcd.py) | BCD of Decimal Number 3461 is =  | 1385 | decimal_to_bcd | `maxNumber=10000`  |
## geometry
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 18 | [Area of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_triangle.py) | Area of triangle with side lengths: 13 7 16 =  | 44.49719092257398 | area_of_triangle | `maxA=20` `maxB=20` `maxC=20`  |
| 19 | [Triangle exists check](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/valid_triangle.py) | Does triangle with sides 32, 44 and 10 exist? | No | valid_triangle | `maxSideLength=50`  |
| 22 | [Third Angle of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/third_angle_of_triangle.py) | Third angle of triangle with angles 24 and 46 =  | 110 | third_angle_of_triangle | `maxAngle=89`  |
| 25 | [Pythagorean Theorem](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/pythagorean_theorem.py) | The hypotenuse of a right triangle given the other two lengths 13 and 10 =  | 16.40 | pythagorean_theorem | `maxLength=20`  |
| 29 | [Angle of a Regular Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_regular_polygon.py) | Find the angle of a regular polygon with 3 sides | 60.0 | angle_regular_polygon | `minVal=3` `maxVal=20`  |
| 32 | [Surface Area of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cube.py) | Surface area of cube with side = 15m is | 1350 m^2 | surface_area_cube | `maxSide=20` `unit='m'`  |
| 33 | [Surface Area of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cuboid.py) | Surface area of cuboid with sides = 6m, 11m, 3m is | 234 m^2 | surface_area_cuboid | `maxSide=20` `unit='m'`  |
| 34 | [Surface Area of Cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cylinder.py) | Surface area of cylinder with height = 38m and radius = 2m is | 502 m^2 | surface_area_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 35 | [Volum of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cube.py) | Volume of cube with side = 3m is | 27 m^3 | volume_cube | `maxSide=20` `unit='m'`  |
| 36 | [Volume of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cuboid.py) | Volume of cuboid with sides = 6m, 14m, 3m is | 252 m^3 | volume_cuboid | `maxSide=20` `unit='m'`  |
| 37 | [Volume of cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cylinder.py) | Volume of cylinder with height = 12m and radius = 16m is | 9650 m^3 | volume_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 38 | [Surface Area of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cone.py) | Surface area of cone with height = 2m and radius = 5m is | 163 m^2 | surface_area_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 39 | [Volume of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cone.py) | Volume of cone with height = 31m and radius = 8m is | 2077 m^3 | volume_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 49 | [Fourth Angle of Quadrilateral](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/fourth_angle_of_quadrilateral.py) | Fourth angle of quadrilateral with angles 166 , 68, 65 = | 61 | fourth_angle_of_quadrilateral | `maxAngle=180`  |
| 57 | [Trigonometric Values](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/basic_trigonometry.py) | What is sin(0)? | 0 | basic_trigonometry | `angles=[0, 30, 45, 60, 90]` `functions=['sin', 'cos', 'tan']`  |
| 58 | [Sum of Angles of Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sum_of_polygon_angles.py) | Sum of angles of polygon with 10 sides =  | 1440 | sum_of_polygon_angles | `maxSides=12`  |
| 60 | [Surface Area of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_sphere.py) | Surface area of Sphere with radius = 13m is | 2123.7166338267 m^2 | surface_area_sphere | `maxSide=20` `unit='m'`  |
| 61 | [Volume of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_sphere.py) | Volume of sphere with radius 33 m =  | 150532.55358940852 m^3 | volume_sphere | `maxRadius=100`  |
| 70 | [Angle between 2 vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_btw_vectors.py) | angle between the vectors [373.03, 280.56, 51.12, 848.19, 914.96, 636.42, 936.04, 218.18, 727.01, 248.11] and [696.71, 8.09, 219.08, 466.57, 583.92, 152.82, 964.12, 686.21, 400.77, 343.46] is: | 0.56 radians | angle_btw_vectors | `maxEltAmt=20`  |
| 75 | [Area of a Sector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sector_area.py) | Given radius, 45 and angle, 145. Find the area of the sector. | Area of sector = 2562.36151 | sector_area | `maxRadius=49` `maxAngle=359`  |
| 86 | [Degrees to Radians](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/degree_to_rad.py) | Angle 196 in radians is =  | 3.42 | degree_to_rad | `max_deg=360`  |
| 87 | [Radians to Degrees](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/radian_to_deg.py) | Angle 1 in degrees is =  | 57.3 | radian_to_deg | `max_rad=3`  |
| 95 | [Curved surface area of a cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/curved_surface_area_cylinder.py) | What is the curved surface area of a cylinder of radius, 16 and height, 21? | CSA of cylinder = 2111.15 | curved_surface_area_cylinder | `maxRadius=49` `maxHeight=99`  |
| 96 | [Perimeter of Polygons](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/perimeter_of_polygons.py) | The perimeter of a 5 sided polygon with lengths of [13, 84, 9, 97, 119]cm is:  | 322 | perimeter_of_polygons | `maxSides=12` `maxLength=120`  |
| 104 | [Circumference](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/circumference.py) | Circumference of circle with radius 48 | 301.59289474462014 | circumference | `maxRadius=100`  |
| 108 | [Arc length of Angle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/arc_length.py) | Given radius, 16 and angle, 326. Find the arc length of the angle. | Arc length of the angle = 91.03637 | arc_length | `maxRadius=49` `maxAngle=359`  |
| 112 | [Area of Circle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_circle.py) | Area of circle with radius 44 | 6084.571428571428 | area_of_circle | `maxRadius=100`  |
## misc
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 9 | [LCM (Least Common Multiple)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/lcm.py) | LCM of 1 and 15 = | 15 | lcm | `maxVal=20`  |
| 10 | [GCD (Greatest Common Denominator)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/gcd.py) | GCD of 3 and 3 =  | 3 | gcd | `maxVal=20`  |
| 27 | [Prime Factorisation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/prime_factors.py) | Find prime factors of 167 | [167] | prime_factors | `minVal=1` `maxVal=200`  |
| 40 | [Common Factors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/common_factors.py) | Common Factors of 55 and 33 =  | [1, 11] | common_factors | `maxVal=100`  |
| 51 | [HCF (Highest Common Factor)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/hcf.py) | HCF of 16 and 9 =  | 1 | hcf | `maxVal=20`  |
| 55 | [Comparing surds](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/surds_comparison.py) | Fill in the blanks 62^(1/7) _ 74^(1/6) | < | surds_comparison | `maxValue=100` `maxRoot=10`  |
| 63 | [Profit or Loss Percent](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/profit_loss_percent.py) | Loss percent when CP = 704 and SP = 134 is:  | 80.9659090909091 | profit_loss_percent | `maxCP=1000` `maxSP=1000`  |
| 66 | [Geometric Progression](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_progression.py) | For the given GP [8, 40, 200, 1000, 5000, 25000] ,Find the value of a,common ratio,8th term value, sum upto 11th term | The value of a is 8, common ratio is 5 , 8th term is 625000 , sum upto 11th term is 97656248.0 | geometric_progression | `number_values=6` `min_value=2` `max_value=12` `n_term=7` `sum_term=5`  |
| 67 | [Geometric Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_mean.py) | Geometric mean of 4 numbers 66 , 46 , 28 , 54 =  | (66*46*28*54)^(1/4) = 46.2874642463462 | geometric_mean | `maxValue=100` `maxNum=4`  |
| 68 | [Harmonic Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/harmonic_mean.py) | Harmonic mean of 4 numbers 74 , 59 , 47 , 36 =  |  4/((1/74) + (1/59) + (1/47) + (1/36)) = 50.30368360304657 | harmonic_mean | `maxValue=100` `maxNum=4`  |
| 69 | [Euclidian norm or L2 norm of a vector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/euclidian_norm.py) | Euclidian norm or L2 norm of the vector[118.69308620957398, 418.5316709436745, 529.1318417822414, 545.3215860464462, 387.999979078107, 298.1451264197782, 392.3895332994427, 833.7453539560848, 555.724882920332, 472.05768476591004, 214.55377537613495, 760.9785260761229, 448.91380437418314, 73.27333213603282, 791.8291233802007, 918.6577753538513] is: | 2165.5845872381433 | euclidian_norm | `maxEltAmt=20`  |
| 81 | [Celsius To Fahrenheit](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/celsius_to_fahrenheit.py) | Convert -12 degrees Celsius to degrees Fahrenheit = | 10.399999999999999 | celsius_to_fahrenheit | `maxTemp=100`  |
| 82 | [AP Term Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_term.py) | Find the term number 29 of the AP series: -80, -71, -62 ...  | 172 | arithmetic_progression_term | `maxd=100` `maxa=100` `maxn=100`  |
| 83 | [AP Sum Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_sum.py) | Find the sum of first 64 terms of the AP series: -94, -6, 82 ...  | 171392.0 | arithmetic_progression_sum | `maxd=100` `maxa=100` `maxn=100`  |
| 85 | [Converts decimal to Roman Numerals](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/decimal_to_roman_numerals.py) | The number 3026 in Roman Numerals is:  | MMMXXVI | decimal_to_roman_numerals | `maxDecimal=4000`  |
| 92 | [Complex To Polar Form](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/complex_to_polar.py) | rexp(itheta) =  | 26.91exp(i-2.3) | complex_to_polar | `minRealImaginaryNum=-20, maxRealImaginaryNum=20`  |
| 93 | [Union,Intersection,Difference of Two Sets](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/set_operation.py) | Given the two sets a={1, 6, 7, 8, 9} ,b={1, 3, 4, 5, 10}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 3, 4, 5, 6, 7, 8, 9, 10},Intersection is {1}, a-b is {8, 9, 6, 7},b-a is {10, 3, 4, 5}, Symmetric difference is {3, 4, 5, 6, 7, 8, 9, 10} | set_operation | `minval=3` `maxval=7` `n_a=4` `n_b=5`  |
| 94 | [Base Conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/base_conversion.py) | Convert A201 from base 14 to base 10. | 27833 | base_conversion | `maxNum=60000` `maxBase=16`  |
| 98 | [Quotient of Powers with Same Base](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_base.py) | The Quotient of 42^7 and 42^6 = 42^(7-6) = 42^1 | 42 | quotient_of_power_same_base | `maxBase=50` `maxPower=10`  |
| 99 | [Quotient of Powers with Same Power](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_power.py) | The Quotient of 31^10 and 37^10 = (31/37)^10 = 0.8378378378378378^10 | 0.17045105659000342 | quotient_of_power_same_power | `maxBase=50` `maxPower=10`  |
| 101 | [Leap Year or Not](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/is_leap_year.py) | Year 1999  | is not a leap year | is_leap_year | `minNumber=1900` `maxNumber=2099`  |
| 102 | [Minute to Hour conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/minutes_to_hours.py) | Convert 851 minutes to Hours & Minutes | 14 hours and 11 minutes | minutes_to_hours | `maxMinutes=999`  |
| 106 | [signum function](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/signum_function.py) | signum of 525 is = | 1 | signum_function | `min=-999` `max=999`  |
| 109 | [Binomial distribution](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/binomial_distribution.py) | A manufacturer of metal pistons finds that, on average, 40.41% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 11 pistons will contain no more than 4 rejected pistons? | 52.15 | binomial_distribution | ``  |
## statistics
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 30 | [Combinations of Objects](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/combinations.py) | Number of combinations from 15 objects picked 1 at a time  | 15 | combinations | `maxlength=20`  |
| 42 | [Permutations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/permutation.py) | Number of Permutations from 11 objects picked 8 at a time =   | 6652800 | permutation | `maxlength=20`  |
| 52 | [Probability of a certain sum appearing on faces of dice](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/dice_sum_probability.py) | If 1 dice are rolled at the same time, the probability of getting a sum of 5 = | 1/6 | dice_sum_probability | `maxDice=3`  |
| 54 | [Confidence interval For sample S](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/confidence_interval.py) | The confidence interval for sample [214, 235, 201, 238, 244, 219, 266, 234, 298, 258, 255, 254, 243, 220, 223, 215, 209, 225, 296, 252, 267, 248, 262, 226, 205, 211, 265] with 99% confidence is | (252.7166888228517, 227.50553339937053) | confidence_interval | ``  |
| 59 | [Mean,Standard Deviation,Variance](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/data_summary.py) | Find the mean,standard deviation and variance for the data[31, 36, 35, 21, 38, 20, 19, 11, 37, 31, 24, 19, 18, 15, 17] | The Mean is 24.8 , Standard Deviation is 75.22666666666666, Variance is 8.673330771201261 | data_summary | `number_values=15` `minval=5` `maxval=50`  |
| 76 | [Mean and Median](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/mean_median.py) | Given the series of numbers [32, 87, 22, 86, 92, 17, 57, 68, 82, 94]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 63.7 and Arithmetic median of this series is 75.0 | mean_median | `maxlen=10`  |
| 107 | [Conditional Probability](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/conditional_probability.py) | Someone tested positive for a nasty disease which only 1.78% of population have. Test sensitivity (true positive) is equal to SN= 96.47% whereas test specificity (true negative) SP= 92.86%. What is the probability that this guy really has that disease? | 19.67% | conditional_probability | ``  |
