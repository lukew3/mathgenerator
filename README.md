# mathgenerator

A math problem generator, created for the purpose of giving self-studying students and teaching organizations the means to easily get access to random math problems to suit their needs.

To try out generators, go to <https://lukew3.github.io/mathgenerator>

See [CONTRIBUTING.md](https://github.com/lukew3/mathgenerator/blob/main/CONTRIBUTING.md) for information about how to contribute.

## Table of Contents
* [Installation](#installation)
* [Basic Usage](#basic-usage)
  * [More Complicated Usage](#more-complicated-usage)
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

* Pass the kwarg `format=latex` to return problem and solution set as latex. If latex is not available for that generator, the problem will return the string "Latex unavailable"

* Pass the kwarg `format=raw` to return just the raw data for each generator. An array of each variable necessary to the generator is returned.

## List of Generators
## algebra
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 11 | [Basic Algebra](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/basic_algebra.py) | 5x + 10 = 10 | 0 | basic_algebra | `maxVariable=10`  |
| 12 | [Logarithm](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/log.py) | log3(6561) | 8 | log | `maxBase=3` `maxVal=8`  |
| 17 | [Integer Multiplication with 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_int_to_22_matrix.py) | 8 * [[3, 2], [7, 2]] =  | [[24,16],[56,16]] | multiply_int_to_22_matrix | `maxMatrixVal=10` `maxRes=100`  |
| 20 | [Midpoint of the two point](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/midpoint_of_two_points.py) | (20,9),(19,-14)= | (19.5,-2.5) | midpoint_of_two_points | `maxValue=20`  |
| 21 | [Factoring Quadratic](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/factoring.py) | x^2+8x | (x)(x+8) | factoring | `range_x1=10` `range_x2=10`  |
| 23 | [Solve a System of Equations in R^2](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/system_of_equations.py) | -7x + 3y = 27, -7x - 6y = 72 | x = -6, y = -5 | system_of_equations | `range_x=10` `range_y=10` `coeff_mult_range=10`  |
| 24 | [Distance between 2 points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/distance_two_points.py) | Find the distance between (2, -17) and (-3, 3) | sqrt(425) | distance_two_points | `maxValXY=20` `minValXY=-20`  |
| 26 | [Linear Equations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/linear_equations.py) | 8x + -9y = 284, -1x + 8y = -173 | x = 13, y = -20 | linear_equations | `n=2` `varRange=20` `coeffRange=20`  |
| 41 | [Intersection of Two Lines](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/intersection_of_two_lines.py) | Find the point of intersection of the two lines: y = -6/2x - 1 and y = -4/4x + 9 | (-5, 14) | intersection_of_two_lines | `minM=-10` `maxM=10` `minB=-10` `maxB=10` `minDenominator=1` `maxDenominator=6`  |
| 43 | [Cross Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_cross.py) | [14, -13, 12] X [-19, -17, 13] =  | [35, -410, -485] | vector_cross | `minVal=-20` `maxVal=20`  |
| 45 | [Simple Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/simple_interest.py) | Simple interest for a principle amount of 8091 dollars, 10% rate of interest and for a time period of 7 years is =  | 5663.7 | simple_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 46 | [Multiplication of two matrices](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/matrix_multiplication.py) | Multiply<table><tr><td>-1</td><td>7</td><td>-8</td><td>-4</td></tr><tr><td>8</td><td>-9</td><td>-2</td><td>5</td></tr></table>and<table><tr><td>9</td><td>2</td><td>3</td></tr><tr><td>-5</td><td>5</td><td>-10</td></tr><tr><td>5</td><td>4</td><td>-6</td></tr><tr><td>3</td><td>-3</td><td>3</td></tr></table> | <table><tr><td>-96</td><td>13</td><td>-37</td></tr><tr><td>122</td><td>-52</td><td>141</td></tr></table> | matrix_multiplication | `maxVal=100` `max_dim=10`  |
| 50 | [Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/quadratic_equation.py) | Zeros of the Quadratic Equation 7x^2+122x+94=0 | [-0.81, -16.62] | quadratic_equation | `maxVal=100`  |
| 65 | [Multiplication of 2 complex numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_complex_numbers.py) | (-16+20j) * (17+4j) =  | (-352+276j) | multiply_complex_numbers | `minRealImaginaryNum=-20` `maxRealImaginaryNum=20`  |
| 72 | [Dot Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_dot.py) | [4, -3, -16] . [3, 13, 0] =  | -27 | vector_dot | `minVal=-20` `maxVal=20`  |
| 74 | [Inverse of a Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/invert_matrix.py) | Inverse of Matrix Matrix([[41, 99, 20], [79, 6, 68], [18, 53, 66]]) is: | Matrix([[1604/222479, 7/569, -3306/222479], [1995/222479, -3/569, 604/222479], [-4079/444958, 1/1138, 7575/444958]]) | invert_matrix | `SquareMatrixDimension=3` `MaxMatrixElement=99` `OnlyIntegerElementsInInvertedMatrix=False`  |
| 77 | [Determinant to 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/int_matrix_22_determinant.py) | Det([[96, 4], [87, 48]]) =  |  4260 | int_matrix_22_determinant | `maxMatrixVal=100`  |
| 78 | [Compound Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/compound_interest.py) | Compound interest for a principle amount of 2136 dollars, 10% rate of interest and for a time period of 6 year is =  | 3784.05 | compound_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 100 | [complex Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/complex_quadratic.py) | Find the roots of given Quadratic Equation 4x^2 + 4x + 1 = 0 | simplified solution : ((-0.5, -0.5)), generalized solution : ((-4 + 0)/2*4, (-4 - 0)/2*4) | complex_quadratic | `prob_type=0` `max_range=10`  |
| 105 | [Combine Like terms](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/combine_like_terms.py) | 9x^2 + 10x^6 + 6x^1 + 2x^5 + 1x^2 + 4x^5 + 3x^4 | 6x^1 + 10x^2 + 3x^4 + 6x^5 + 10x^6  | combine_like_terms | `maxCoef=10` `maxExp=20` `maxTerms=10`  |
| 111 | [Expanding Factored Binomial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/expanding.py) | (-3x+10)(+6x-2) | -18*x^2+66*x-20 | expanding | `range_x1=10` `range_x2=10` `range_a=10` `range_b=10`  |
## basic_math
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 0 | [Addition](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/addition.py) | 6+27= | 33 | addition | `maxSum=99` `maxAddend=50`  |
| 1 | [Subtraction](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/subtraction.py) | 32-7= | 25 | subtraction | `maxMinuend=99` `maxDiff=99`  |
| 2 | [Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/multiplication.py) | 7*6= | 42 | multiplication | `maxMulti=12`  |
| 3 | [Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/division.py) | 40/4= | 10 | division | `maxA=25` `maxB=25`  |
| 6 | [Square Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square_root.py) | sqrt(64)= | 8 | square_root | `minNo=1` `maxNo=12`  |
| 8 | [Square](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square.py) | 6^2= | 36 | square | `maxSquareNum=20`  |
| 13 | [Complex Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/complex_division.py) | 13/81= | 0.16 | complex_division | `maxRes=99` `maxDivid=99`  |
| 16 | [Fraction Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/divide_fractions.py) | (3/10)/(3/10) | 1 | divide_fractions | `maxVal=10`  |
| 28 | [Fraction Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/fraction_multiplication.py) | (6/2)*(5/4) | 15/4 | fraction_multiplication | `maxVal=10`  |
| 31 | [Factorial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/factorial.py) | 4! =  | 24 | factorial | `maxInput=6`  |
| 44 | [Compare Fractions](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/compare_fractions.py) | Which symbol represents the comparison between 2/10 and 9/6? | < | compare_fractions | `maxVal=10`  |
| 47 | [Cube Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/cube_root.py) | What is the cube root of 356 up to 2 decimal places? | 7.09 | cube_root | `minNo=1` `maxNo=1000`  |
| 53 | [Exponentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/exponentiation.py) | 6^5 = | 7776 | exponentiation | `maxBase=20` `maxExpo=10`  |
| 71 | [Absolute difference between two numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/absolute_difference.py) | |87-65|= | 22 | absolute_difference | `maxA=100` `maxB=100`  |
| 80 | [Percentage of a number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage.py) | What is 9% of 74? | 6.66 | percentage | `maxValue=99` `maxpercentage=99`  |
| 90 | [isprime](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/is_prime.py) | Is 52 prime? | No | is_prime | `max_num=100`  |
| 97 | [Power of Powers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/power_of_powers.py) | Simplify 15^6^10= | 15^60 | power_of_powers | `maxBase=50` `maxPower=10`  |
| 118 | [Percentage difference](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage_difference.py) | What is the percentage difference between 111 and 173? | 43.66% | percentage_difference | `maxValue=200` `minValue=0`  |
| 119 | [Percentage error](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage_error.py) | Find the percentage error when observed value equals -64 and exact value equals -14. | 357.14% | percentage_error | `maxValue=100` `minValue=-100`  |
| 120 | [Greatest Common Divisor of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/greatest_common_divisor.py) | GCD(326471423,856701641)= | 1 | greatest_common_divisor | `numbersCount=2` `maximalNumberLimit=10**9`  |
## calculus
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 7 | [Power Rule Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_differentiation.py) | 7x^7 + 3x^7 + 9x^6 + 6x^1 | 49x^6 + 21x^6 + 54x^5 + 6x^0 | power_rule_differentiation | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 48 | [Power Rule Integration](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_integration.py) | 9x^8 | (9/8)x^9 + c | power_rule_integration | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 88 | [Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/differentiation.py) | differentiate w.r.t x : d(sin(x)+9*x^(-2))/dx | cos(x) - 18/x^3 | differentiation | `diff_lvl=2`  |
| 89 | [Definite Integral of Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/definite_integral.py) | The definite integral within limits 0 to 1 of the equation 68x^2 + 64x + 30 is =  | 84.6667 | definite_integral | `max_coeff=100`  |
| 110 | [Stationary Points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/stationary_points.py) | f(x)=5*x^3 + x^2 + 8 | (-2/15,5404/675),(0,8) | stationary_points | `maxExp=3` `maxCoef=10`  |
## computer_science
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 4 | [Binary Complement 1s](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_complement_1s.py) | 1110= | 0001 | binary_complement_1s | `maxDigits=10`  |
| 5 | [Modulo Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/modulo_division.py) | 4%90= | 4 | modulo_division | `maxRes=99` `maxModulo=99`  |
| 14 | [Decimal to Binary](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_binary.py) | Binary of 76= | 1001100 | decimal_to_binary | `max_dec=99`  |
| 15 | [Binary to Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_decimal.py) | 101 | 5 | binary_to_decimal | `max_dig=10`  |
| 56 | [Fibonacci Series](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/fibonacci_series.py) | The Fibonacci Series of the first 10 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] | fibonacci_series | `minNo=1`  |
| 62 | [nth Fibonacci number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/nth_fibonacci_number.py) | What is the 80th Fibonacci number? | 23416728348467744 | nth_fibonacci_number | `maxN=100`  |
| 64 | [Binary to Hexidecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_hex.py) | 0111011 | 0x3b | binary_to_hex | `max_dig=10`  |
| 73 | [Binary 2's Complement](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_2s_complement.py) | 2's complement of 111001 = | 111 | binary_2s_complement | `maxDigits=10`  |
| 79 | [Decimal to Hexadecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_hexadeci.py) | Binary of 162= | 0xa2 | decimal_to_hexadeci | `max_dec=1000`  |
| 84 | [Converts decimal to octal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_octal.py) | The decimal number 1566 in Octal is:  | 0o3036 | decimal_to_octal | `maxDecimal=4096`  |
| 91 | [Binary Coded Decimal to Integer](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/bcd_to_decimal.py) | Integer of Binary Coded Decimal 8 is =  | 33143 | bcd_to_decimal | `maxNumber=10000`  |
| 103 | [Decimal to Binary Coded Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_bcd.py) | BCD of Decimal Number 6225 is =  | 1851 | decimal_to_bcd | `maxNumber=10000`  |
## geometry
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 18 | [Area of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_triangle.py) | Area of triangle with side lengths: 4 18 17 =  | 33.67 | area_of_triangle | `maxA=20` `maxB=20`  |
| 19 | [Triangle exists check](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/valid_triangle.py) | Does triangle with sides 6, 23 and 24 exist? | Yes | valid_triangle | `maxSideLength=50`  |
| 22 | [Third Angle of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/third_angle_of_triangle.py) | Third angle of triangle with angles 23 and 47 =  | 110 | third_angle_of_triangle | `maxAngle=89`  |
| 25 | [Pythagorean Theorem](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/pythagorean_theorem.py) | The hypotenuse of a right triangle given the other two lengths 6 and 6 =  | 8.49 | pythagorean_theorem | `maxLength=20`  |
| 29 | [Angle of a Regular Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_regular_polygon.py) | Find the angle of a regular polygon with 8 sides | 135.0 | angle_regular_polygon | `minVal=3` `maxVal=20`  |
| 32 | [Surface Area of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cube.py) | Surface area of cube with side = 2m is | 24 m^2 | surface_area_cube | `maxSide=20` `unit='m'`  |
| 33 | [Surface Area of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cuboid.py) | Surface area of cuboid with sides = 19m, 16m, 17m is | 1798 m^2 | surface_area_cuboid | `maxSide=20` `unit='m'`  |
| 34 | [Surface Area of Cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cylinder.py) | Surface area of cylinder with height = 19m and radius = 7m is | 1143 m^2 | surface_area_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 35 | [Volum of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cube.py) | Volume of cube with side = 2m is | 8 m^3 | volume_cube | `maxSide=20` `unit='m'`  |
| 36 | [Volume of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cuboid.py) | Volume of cuboid with sides = 13m, 17m, 9m is | 1989 m^3 | volume_cuboid | `maxSide=20` `unit='m'`  |
| 37 | [Volume of cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cylinder.py) | Volume of cylinder with height = 11m and radius = 2m is | 138 m^3 | volume_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 38 | [Surface Area of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cone.py) | Surface area of cone with height = 31m and radius = 9m is | 1167 m^2 | surface_area_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 39 | [Volume of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cone.py) | Volume of cone with height = 10m and radius = 18m is | 3392 m^3 | volume_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 49 | [Fourth Angle of Quadrilateral](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/fourth_angle_of_quadrilateral.py) | Fourth angle of quadrilateral with angles 51 , 181, 49 = | 79 | fourth_angle_of_quadrilateral | `maxAngle=180`  |
| 57 | [Trigonometric Values](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/basic_trigonometry.py) | What is tan(90)? | ∞ | basic_trigonometry | `angles=[0, 30, 45, 60, 90]` `functions=['sin', 'cos', 'tan']`  |
| 58 | [Sum of Angles of Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sum_of_polygon_angles.py) | Sum of angles of polygon with 12 sides =  | 1800 | sum_of_polygon_angles | `maxSides=12`  |
| 60 | [Surface Area of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_sphere.py) | Surface area of Sphere with radius = 20m is | 5026.548245743669 m^2 | surface_area_sphere | `maxSide=20` `unit='m'`  |
| 61 | [Volume of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_sphere.py) | Volume of sphere with radius 56 m =  | 735618.5806037667 m^3 | volume_sphere | `maxRadius=100`  |
| 70 | [Angle between 2 vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_btw_vectors.py) | angle between the vectors [358.33, 666.13, 650.06, 264.35, 50.1, 338.6, 155.98, 262.18, 470.17, 681.63, 862.29, 561.78, 341.26, 551.94, 484.91, 166.68] and [721.12, 986.28, 667.31, 927.66, 834.74, 48.76, 623.8, 975.84, 466.86, 263.3, 963.54, 653.39, 313.28, 92.3, 218.0, 40.74] is: | 0.67 radians | angle_btw_vectors | `maxEltAmt=20`  |
| 75 | [Area of a Sector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sector_area.py) | Given radius, 39 and angle, 10. Find the area of the sector. | Area of sector = 132.73229 | sector_area | `maxRadius=49` `maxAngle=359`  |
| 86 | [Degrees to Radians](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/degree_to_rad.py) | Angle 227 in radians is =  | 3.96 | degree_to_rad | `max_deg=360`  |
| 87 | [Radians to Degrees](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/radian_to_deg.py) | Angle 0 in degrees is =  | 0.0 | radian_to_deg | `max_rad=3`  |
| 95 | [Curved surface area of a cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/curved_surface_area_cylinder.py) | What is the curved surface area of a cylinder of radius, 10 and height, 21? | CSA of cylinder = 1319.47 | curved_surface_area_cylinder | `maxRadius=49` `maxHeight=99`  |
| 96 | [Perimeter of Polygons](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/perimeter_of_polygons.py) | The perimeter of a 10 sided polygon with lengths of [109, 77, 116, 47, 36, 80, 87, 8, 117, 111]cm is:  | 788 | perimeter_of_polygons | `maxSides=12` `maxLength=120`  |
| 104 | [Circumference](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/circumference.py) | Circumference of circle with radius 8 | 50.26548245743669 | circumference | `maxRadius=100`  |
| 108 | [Arc length of Angle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/arc_length.py) | Given radius, 4 and angle, 323. Find the arc length of the angle. | Arc length of the angle = 22.54965 | arc_length | `maxRadius=49` `maxAngle=359`  |
| 112 | [Area of Circle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_circle.py) | Area of circle with radius 62 | 12081.142857142857 | area_of_circle | `maxRadius=100`  |
| 113 | [Volume of frustum](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_frustum.py) | Volume of frustum with height = 44m and r1 = 19m is and r2 = 19m is  | 29995.0 m^3 | volume_frustum | `maxR1=20` `maxR2=20` `maxHeight=50` `unit='m'`  |
| 114 | [Equation of line from two points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/equation_of_line_from_two_points.py) | What is the equation of the line between points (-12,4) and (8,0) in slope-intercept form? | 5y = -x + 8 | equation_of_line_from_two_points | `maxCoordinate=20` `minCoordinate=-20`  |
| 115 | [Area of Circle given center and a point on circle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_circle_given_center_and_point.py) | Area of circle with center (3,1) and passing through (2.35, 0.24) is | 3.14 | area_of_circle_given_center_and_point | `maxCoordinate = 10` `maxRadius=10`  |
| 117 | [Volume of Hemisphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_hemisphere.py) | Volume of hemisphere with radius 22 m =  | 22301.119 m^3 | volume_hemisphere | `maxRadius=100`  |
## misc
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 9 | [LCM (Least Common Multiple)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/lcm.py) | LCM of 3 and 5 = | 15 | lcm | `maxVal=20`  |
| 10 | [GCD (Greatest Common Denominator)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/gcd.py) | GCD of 3 and 19 =  | 1 | gcd | `maxVal=20`  |
| 27 | [Prime Factorisation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/prime_factors.py) | Find prime factors of 185 | [5, 37] | prime_factors | `minVal=1` `maxVal=200`  |
| 40 | [Common Factors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/common_factors.py) | Common Factors of 19 and 11 =  | [1] | common_factors | `maxVal=100`  |
| 51 | [HCF (Highest Common Factor)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/hcf.py) | HCF of 16 and 13 =  | 1 | hcf | `maxVal=20`  |
| 55 | [Comparing surds](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/surds_comparison.py) | Fill in the blanks 41^(1/3) _ 11^(1/4) | > | surds_comparison | `maxValue=100` `maxRoot=10`  |
| 63 | [Profit or Loss Percent](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/profit_loss_percent.py) | Loss percent when CP = 769 and SP = 460 is:  | 40.18205461638492 | profit_loss_percent | `maxCP=1000` `maxSP=1000`  |
| 66 | [Geometric Progression](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_progression.py) | For the given GP [12, 72, 432, 2592, 15552, 93312] ,Find the value of a,common ratio,10th term value, sum upto 7th term | The value of a is 12, common ratio is 6 , 10th term is 120932352 , sum upto 7th term is 671844.0 | geometric_progression | `number_values=6` `min_value=2` `max_value=12` `n_term=7` `sum_term=5`  |
| 67 | [Geometric Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_mean.py) | Geometric mean of 3 numbers 23 , 42 and 80 =  | (23*42*80)^(1/3) = 42.59471379666575 | geometric_mean | `maxValue=100` `maxNum=4`  |
| 68 | [Harmonic Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/harmonic_mean.py) | Harmonic mean of 2 numbers 19 and 53 =  |  2/((1/19) + (1/53)) = 27.972222222222225 | harmonic_mean | `maxValue=100` `maxNum=4`  |
| 69 | [Euclidian norm or L2 norm of a vector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/euclidian_norm.py) | Euclidian norm or L2 norm of the vector[628.9497984743637, 413.7025276967905, 55.08325175633222, 543.4734094406972, 407.4510705587269, 568.7990971658147, 407.9155106455502, 474.20039089590216, 720.3486866530783, 514.2113795291383, 273.3258978495645, 488.8393919190255, 897.4344293916904, 541.0117215640587] is: | 1985.1961648306578 | euclidian_norm | `maxEltAmt=20`  |
| 81 | [Celsius To Fahrenheit](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/celsius_to_fahrenheit.py) | Convert 89 degrees Celsius to degrees Fahrenheit = | 192.20000000000002 | celsius_to_fahrenheit | `maxTemp=100`  |
| 82 | [AP Term Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_term.py) | Find the term number 81 of the AP series: 24, 104, 184 ...  | 6424 | arithmetic_progression_term | `maxd=100` `maxa=100` `maxn=100`  |
| 83 | [AP Sum Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_sum.py) | Find the sum of first 73 terms of the AP series: -98, -140, -182 ...  | -117530.0 | arithmetic_progression_sum | `maxd=100` `maxa=100` `maxn=100`  |
| 85 | [Converts decimal to Roman Numerals](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/decimal_to_roman_numerals.py) | The number 0 in Roman Numerals is:  | MMMDXXXIX | decimal_to_roman_numerals | `maxDecimal=4000`  |
| 92 | [Complex To Polar Form](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/complex_to_polar.py) | 5.1(-1.0theta + i5.0theta) | 1.77 | complex_to_polar | `minRealImaginaryNum=-20, maxRealImaginaryNum=20`  |
| 93 | [Union,Intersection,Difference of Two Sets](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/set_operation.py) | Given the two sets a={1, 4, 5, 6, 9} ,b={2, 3, 5, 6, 7, 8}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 2, 3, 4, 5, 6, 7, 8, 9},Intersection is {5, 6}, a-b is {1, 4, 9},b-a is {8, 2, 3, 7}, Symmetric difference is {1, 2, 3, 4, 7, 8, 9} | set_operation | `minval=3` `maxval=7` `n_a=4` `n_b=5`  |
| 94 | [Base Conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/base_conversion.py) | Convert 40122 from base 5 to base 15. | B42 | base_conversion | `maxNum=60000` `maxBase=16`  |
| 98 | [Quotient of Powers with Same Base](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_base.py) | The Quotient of 43^10 and 43^1 = 43^(10-1) = 43^9 | 502592611936843 | quotient_of_power_same_base | `maxBase=50` `maxPower=10`  |
| 99 | [Quotient of Powers with Same Power](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_power.py) | The Quotient of 1^7 and 1^7 = (1/1)^7 = 1.0^7 | 1.0 | quotient_of_power_same_power | `maxBase=50` `maxPower=10`  |
| 101 | [Leap Year or Not](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/is_leap_year.py) | Year 1986  | is not a leap year | is_leap_year | `minNumber=1900` `maxNumber=2099`  |
| 102 | [Minute to Hour conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/minutes_to_hours.py) | Convert 446 minutes to Hours & Minutes | 7 hours and 26 minutes | minutes_to_hours | `maxMinutes=999`  |
| 106 | [signum function](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/signum_function.py) | signum of 941 is = | 1 | signum_function | `min=-999` `max=999`  |
| 109 | [Binomial distribution](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/binomial_distribution.py) | A manufacturer of metal pistons finds that, on average, 37.08% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 15 pistons will contain no more than 5 rejected pistons? | 49.63 | binomial_distribution | ``  |
| 116 | [Factors of a number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/Factors.py) | Factors of 661 =  | [1, 661] | Factors | `maxVal=1000`  |
| 121 | [Product of scientific notaions](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/product_of_scientific_notations.py) | Product of scientific notations 7.65x10^-75 and 5.51x10^-50 =  | 4.22x10^-124 | product_of_scientific_notations | `minExpVal=-100` `maxExpVal=100`  |
## statistics
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 30 | [Combinations of Objects](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/combinations.py) | Number of combinations from 15 objects picked 3 at a time  | 455 | combinations | `maxlength=20`  |
| 42 | [Permutations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/permutation.py) | Number of Permutations from 16 objects picked 9 at a time =   | 4151347200 | permutation | `maxlength=20`  |
| 52 | [Probability of a certain sum appearing on faces of dice](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/dice_sum_probability.py) | If 2 dice are rolled at the same time, the probability of getting a sum of 12 = | 1/36 | dice_sum_probability | `maxDice=3`  |
| 54 | [Confidence interval For sample S](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/confidence_interval.py) | The confidence interval for sample [234, 254, 283, 218, 205, 251, 282, 228, 280, 202, 268, 220, 273, 277, 267, 249, 285, 208, 225, 266, 274, 235, 223, 226, 245, 200, 213, 221, 298, 236, 288, 231, 222, 299, 243, 242, 255] with 90% confidence is | (254.32591454896394, 238.97138274833335) | confidence_interval | ``  |
| 59 | [Mean,Standard Deviation,Variance](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/data_summary.py) | Find the mean,standard deviation and variance for the data[23, 20, 35, 38, 24, 41, 6, 7, 26, 37, 49, 12, 15, 31, 12] | The Mean is 25.066666666666666 , Standard Deviation is 162.32888888888888, Variance is 12.740835486297156 | data_summary | `number_values=15` `minval=5` `maxval=50`  |
| 76 | [Mean and Median](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/mean_median.py) | Given the series of numbers [2, 8, 9, 14, 16, 17, 35, 47, 55, 74]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 27.7 and Arithmetic median of this series is 16.5 | mean_median | `maxlen=10`  |
| 107 | [Conditional Probability](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/conditional_probability.py) | Someone tested positive for a nasty disease which only 0.90% of population have. Test sensitivity (true positive) is equal to SN= 98.84% whereas test specificity (true negative) SP= 90.89%. What is the probability that this guy really has that disease? | 8.97% | conditional_probability | ``  |
