# mathgenerator

A math problem generator, created for the purpose of giving teachers and students the means to easily get access to random math exercises to suit their needs.

To try out generators, go to <https://lukew3.github.io/mathgenerator>

See [CONTRIBUTING.md](https://github.com/lukew3/mathgenerator/blob/main/CONTRIBUTING.md) for information about how to contribute.

## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
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

## Usage
Here is an example of how you would generate an addition problem:

```python
import mathgenerator

#generate an addition problem
problem, solution = mathgenerator.addition()

#another way to generate an addition problem using genById()
problem, solution = mathgenerator.genById(0)
```
<!--
### Creating a worksheet
If you wish to create a worksheet, you can use the [worksheetgen](https://github.com/lukew3/worksheetgen) package. Install this with `pip install worksheetgen`. Here is an example of how a worksheet would be generated.
```
from mathgenerator import mathgen
from worksheetgen.wg import Worksheet

ws = Worksheet("Worksheet title")
with ws.section('Section 1', description='These are instructions')
	# Writes 10 problems generated with id 1, [0] at the end specifies to take problem, and not solution.
	for _ in range(10):
		ws.add_problem(mathgen.genById(1)[0])
ws.write_pdf()
```
This creates the pdf `ws.pdf` in your current directory
-->
Problem/solution pairs are generated with either:
* `mathgenerator.<generator_name>()` - generates a problem, solution set from the given generator name.
* `mathgenerator.genById(id)` - generates a problem, solution set with generator id provided by the `id` parameter

<!--
#### `format` kwarg
* Pass `format=latex` to return problem and solution set as latex. If latex is not available for that generator, the problem will return the string "Latex unavailable"
* Pass `format=raw` to return just the raw data for each generator. An array of each variable necessary to the generator is returned.
* If you don't pass a value to the format kwarg, the generator will return a problem and answer in asciimath format.
-->
You can also use `getGenList()` to return a list of all generators included in the library in the format:
```
[id, title, self, funcname, subjectname]
```


## List of Generators
## algebra
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 11 | [Basic Algebra](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/basic_algebra.py) | $10x + 10 = 10$ | $0$ | basic_algebra | `maxVariable=10`  |
| 12 | [Logarithm](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/log.py) | $log_{2}(2)=$ | $1$ | log | `maxBase=3` `maxVal=8`  |
| 17 | [Integer Multiplication with 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_int_to_22_matrix.py) | 4 * [[9, 10], [10, 2]] =  | [[36,40],[40,8]] | multiply_int_to_22_matrix | `maxMatrixVal=10` `maxRes=100`  |
| 20 | [Midpoint of the two point](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/midpoint_of_two_points.py) | The midpoint of $(-19,-8)$ and $(-13,2) = $ | $(-16.0,-3.0)$ | midpoint_of_two_points | `maxValue=20`  |
| 21 | [Factoring Quadratic](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/factoring.py) | $x^2-11x+18$ | $(x-2)(x-9)$ | factoring | `range_x1=10` `range_x2=10`  |
| 23 | [Solve a System of Equations in R^2](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/system_of_equations.py) | -8x - 7y = -78, -2x - 6y = -62 | x = 1, y = 10 | system_of_equations | `range_x=10` `range_y=10` `coeff_mult_range=10`  |
| 24 | [Distance between 2 points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/distance_two_points.py) | Find the distance between $(-9, 6)$ and $(14, 3)$ | $\sqrt{538}$ | distance_two_points | `maxValXY=20` `minValXY=-20`  |
| 26 | [Linear Equations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/linear_equations.py) | Given the equations $-1x + 19y = 213$ and $-17x + -14y = -86$, solve for x and y | $x = -4$, $y = 11$ | linear_equations | `n=2` `varRange=20` `coeffRange=20`  |
| 41 | [Intersection of Two Lines](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/intersection_of_two_lines.py) | Find the point of intersection of the two lines: $y = -4x - 5$ and $y = 4/3x + 6$ | $(-33/16, 13/4)$ | intersection_of_two_lines | `minM=-10` `maxM=10` `minB=-10` `maxB=10` `minDenominator=1` `maxDenominator=6`  |
| 43 | [Cross Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_cross.py) | [3, -15, -7] X [-5, 13, -14] =  | [301, 77, -36] | vector_cross | `minVal=-20` `maxVal=20`  |
| 45 | [Simple Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/simple_interest.py) | Simple interest for a principle amount of $9025$ dollars, $5\%$ rate of interest and for a time period of $10$ years is $=$  | $4512.5$ | simple_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 46 | [Multiplication of two matrices](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/matrix_multiplication.py) | Multiply<table><tr><td>-2</td><td>-6</td><td>-10</td><td>-9</td></tr><tr><td>6</td><td>-4</td><td>-8</td><td>5</td></tr><tr><td>-5</td><td>-2</td><td>2</td><td>-8</td></tr></table>and<table><tr><td>-9</td><td>4</td><td>8</td><td>-3</td></tr><tr><td>3</td><td>0</td><td>7</td><td>9</td></tr><tr><td>-8</td><td>1</td><td>-1</td><td>-2</td></tr><tr><td>-3</td><td>-8</td><td>-5</td><td>-5</td></tr></table> | <table><tr><td>107</td><td>54</td><td>-3</td><td>17</td></tr><tr><td>-17</td><td>-24</td><td>3</td><td>-63</td></tr><tr><td>47</td><td>46</td><td>-16</td><td>33</td></tr></table> | matrix_multiplication | `maxVal=100` `max_dim=10`  |
| 50 | [Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/quadratic_equation.py) | What are the zeros of the quadratic equation $62x^2+199x+68=0$ | ${-0.39, -2.82}$ | quadratic_equation | `maxVal=100`  |
| 65 | [Multiplication of 2 complex numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_complex_numbers.py) | $(-18+7j) * (8+6j) = $ | $(-186-52j)$ | multiply_complex_numbers | `minRealImaginaryNum=-20` `maxRealImaginaryNum=20`  |
| 72 | [Dot Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_dot.py) | $[4, 10, 0]\cdot[14, -12, 14]=$ | $-64$ | vector_dot | `minVal=-20` `maxVal=20`  |
| 74 | [Inverse of a Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/invert_matrix.py) | Matrix([[43, 4, 42], [31, 1, 7], [35, 71, 77]]) | Matrix([[-5/766, 191/4596, -1/4596], [-51/1532, 263/9192, 143/9192], [361/10724, -971/21448, -27/21448]]) | invert_matrix | `SquareMatrixDimension=3` `MaxMatrixElement=99` `OnlyIntegerElementsInInvertedMatrix=False`  |
| 77 | [Determinant to 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/int_matrix_22_determinant.py) | $\det \begin{bmatrix} a & b \\ c & d \end{bmatrix} = $ | $-3046$ | int_matrix_22_determinant | `maxMatrixVal=100`  |
| 78 | [Compound Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/compound_interest.py) | Compound interest for a principle amount of $8095$ dollars, $8\%$ rate of interest and for a time period of $9$ years is $=$ | $16181.94$ | compound_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 100 | [complex Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/complex_quadratic.py) | Find the roots of given Quadratic Equation x^2 + 4x + 1 = 0 | simplified solution : ((-0.268, -3.732)), generalized solution : ((-4 + sqrt(12))/2*1, (-4 - sqrt(12))/2*1) | complex_quadratic | `prob_type=0` `max_range=10`  |
| 105 | [Combine Like terms](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/combine_like_terms.py) | $10x^{13} + 8x^{1} + 1x^{8} + 1x^{6} + 5x^{5} + 5x^{18}$ | $8x^{1} + 5x^{5} + 1x^{6} + 1x^{8} + 10x^{13} + 5x^{18}$ | combine_like_terms | `maxCoef=10` `maxExp=20` `maxTerms=10`  |
| 111 | [Expanding Factored Binomial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/expanding.py) | $(-8x-2)(2x+7)$ | $-16x^2-60x-14$ | expanding | `range_x1=10` `range_x2=10` `range_a=10` `range_b=10`  |
## basic_math
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 0 | [Addition](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/addition.py) | $7+0=$ | $7$ | addition | `maxSum=99` `maxAddend=50`  |
| 1 | [Subtraction](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/subtraction.py) | $62-22=$ | $40$ | subtraction | `maxMinuend=99` `maxDiff=99`  |
| 2 | [Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/multiplication.py) | $9\cdot1$ | $9$ | multiplication | `maxMulti=12`  |
| 3 | [Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/division.py) | $136\div8=$ | $17$ | division | `maxA=25` `maxB=25`  |
| 6 | [Square Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square_root.py) | $\sqrt{9}=$ | $3$ | square_root | `minNo=1` `maxNo=12`  |
| 8 | [Square](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square.py) | $20^2=$ | $400$ | square | `maxSquareNum=20`  |
| 13 | [Fraction to Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/fraction_to_decimal.py) | $15\div83=$ | $0.18$ | fraction_to_decimal | `maxRes=99` `maxDivid=99`  |
| 16 | [Fraction Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/divide_fractions.py) | $\frac{1}{7}\div\frac{1}{6}=$ | $\frac{6}{7}$ | divide_fractions | `maxVal=10`  |
| 28 | [Fraction Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/fraction_multiplication.py) | $\frac{8}{2}\cdot\frac{8}{4}=$ | $\frac{64}{8}$ | fraction_multiplication | `maxVal=10`  |
| 31 | [Factorial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/factorial.py) | $4! =$ | $24$ | factorial | `maxInput=6`  |
| 44 | [Compare Fractions](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/compare_fractions.py) | Which symbol represents the comparison between $\frac{7}{10}$ and $\frac{1}{8}$? | > | compare_fractions | `maxVal=10`  |
| 47 | [Cube Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/cube_root.py) | What is the cube root of: $\sqrt[3]{897}=$ to 2 decimal places? | $9.64$ | cube_root | `minNo=1` `maxNo=1000`  |
| 53 | [Exponentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/exponentiation.py) | $16^1 =$ | $16$ | exponentiation | `maxBase=20` `maxExpo=10`  |
| 71 | [Absolute difference between two numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/absolute_difference.py) | $|-31-14|=$ | $45$ | absolute_difference | `maxA=100` `maxB=100`  |
| 80 | [Percentage of a number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage.py) | What is $70\%$ of $76$? | $53.20$ | percentage | `maxValue=99` `maxpercentage=99`  |
| 90 | [isprime](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/is_prime.py) | Is $45$ prime? | No | is_prime | `max_num=100`  |
| 97 | [Power of Powers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/power_of_powers.py) | Simplify $49^{7^{10}}$ | $49^{70}$ | power_of_powers | `maxBase=50` `maxPower=10`  |
| 118 | [Percentage difference](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage_difference.py) | What is the percentage difference between $98$ and $83$? | $16.57\%$ | percentage_difference | `maxValue=200` `minValue=0`  |
| 119 | [Percentage error](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage_error.py) | Find the percentage error when observed value equals $-63$ and exact value equals $-26$. | $142.31\%$ | percentage_error | `maxValue=100` `minValue=-100`  |
| 120 | [Greatest Common Divisor of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/greatest_common_divisor.py) | $GCD(440119997,635495661)=$ | $1$ | greatest_common_divisor | `numbersCount=2` `maximalNumberLimit=10**9`  |
| 124 | [Is Composite](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/is_composite.py) | Is $89$ composite? | No | is_composite | `maxNum=250`  |
## calculus
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 7 | [Power Rule Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_differentiation.py) | $9x^{5}$ | $45x^{4}$ | power_rule_differentiation | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 48 | [Power Rule Integration](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_integration.py) | $6x^{2} + 10x^{2} + 7x^{5}$ | $\frac{6}{2}x^{3} + \frac{10}{2}x^{3} + \frac{7}{5}x^{6} + C$ | power_rule_integration | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 88 | [Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/differentiation.py) | differentiate w.r.t x : d(exp(x)+6*x^2)/dx | 12*x + exp(x) | differentiation | `diff_lvl=2`  |
| 89 | [Definite Integral of Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/definite_integral.py) | The definite integral within limits $0$ to $1$ of the equation $22x^2 + 4x + 27 = $ | $36.3333$ | definite_integral | `max_coeff=100`  |
| 110 | [Stationary Points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/stationary_points.py) | f(x)=6*x^3 + 3*x^2 + 2 | (-1/3,19/9),(0,2) | stationary_points | `maxExp=3` `maxCoef=10`  |
## computer_science
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 4 | [Binary Complement 1s](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_complement_1s.py) | $011110 = $ | $100001$ | binary_complement_1s | `maxDigits=10`  |
| 5 | [Modulo Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/modulo_division.py) | $27\%36=$ | $27$ | modulo_division | `maxRes=99` `maxModulo=99`  |
| 14 | [Decimal to Binary](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_binary.py) | Binary of $15 = $ | $1111$ | decimal_to_binary | `max_dec=99`  |
| 15 | [Binary to Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_decimal.py) | $0$ | $0$ | binary_to_decimal | `max_dig=10`  |
| 56 | [Fibonacci Series](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/fibonacci_series.py) | The Fibonacci Series of the first ${n}$ numbers is ? | $0, 1, 1, 2, 3$ | fibonacci_series | `minNo=1`  |
| 62 | [nth Fibonacci number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/nth_fibonacci_number.py) | What is the 75th Fibonacci number? | $2111485077978055$ | nth_fibonacci_number | `maxN=100`  |
| 64 | [Binary to Hexidecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_hex.py) | $1001$ | $0x9$ | binary_to_hex | `max_dig=10`  |
| 73 | [Binary 2's Complement](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_2s_complement.py) | 2's complement of $1011 = $ | $101$ | binary_2s_complement | `maxDigits=10`  |
| 79 | [Decimal to Hexadecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_hexadeci.py) | Binary of $24 = $ | $0x18$ | decimal_to_hexadeci | `max_dec=1000`  |
| 84 | [Converts decimal to octal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_octal.py) | The decimal number ${x}$ in Octal is:  | $0o5637$ | decimal_to_octal | `maxDecimal=4096`  |
| 91 | [Binary Coded Decimal to Integer](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/bcd_to_decimal.py) | Integer of Binary Coded Decimal $9$ is $=$  | $39271$ | bcd_to_decimal | `maxNumber=10000`  |
| 103 | [Decimal to Binary Coded Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_bcd.py) | BCD of Decimal Number $2317 = $ | $9013$ | decimal_to_bcd | `maxNumber=10000`  |
## geometry
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 18 | [Area of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_triangle.py) | Area of triangle with side lengths: $3, 8 7 = $ | $10.39$ | area_of_triangle | `maxA=20` `maxB=20`  |
| 19 | [Triangle exists check](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/valid_triangle.py) | Does triangle with sides $6, 8$ and $39$ exist? | $No$ | valid_triangle | `maxSideLength=50`  |
| 22 | [Third Angle of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/third_angle_of_triangle.py) | Third angle of triangle with angles $89$ and $10 = $ | $81$ | third_angle_of_triangle | `maxAngle=89`  |
| 25 | [Pythagorean Theorem](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/pythagorean_theorem.py) | What is the hypotenuse of a right triangle given the other two sides have lengths $10$ and $15$? | $18.03$ | pythagorean_theorem | `maxLength=20`  |
| 29 | [Angle of a Regular Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_regular_polygon.py) | Find the angle of a regular polygon with $17$ sides | $158.82$ | angle_regular_polygon | `minVal=3` `maxVal=20`  |
| 32 | [Surface Area of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cube.py) | Surface area of cube with side $= 2m$ is | $24 m^2$ | surface_area_cube | `maxSide=20` `unit='m'`  |
| 33 | [Surface Area of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cuboid.py) | Surface area of cuboid with sides of lengths: $10m, 10m, 17m$ is | $880 m^2$ | surface_area_cuboid | `maxSide=20` `unit='m'`  |
| 34 | [Surface Area of Cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cylinder.py) | Surface area of cylinder with height $= 7m$ and radius $= 11m$ is | $1244 m^2$ | surface_area_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 35 | [Volume of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cube.py) | Volume of cube with a side length of $13m$ is | $2197 m^3$ | volume_cube | `maxSide=20` `unit='m'`  |
| 36 | [Volume of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cuboid.py) | Volume of cuboid with sides = $13m, 20m, 2m$ is | $520 m^3$ | volume_cuboid | `maxSide=20` `unit='m'`  |
| 37 | [Volume of cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cylinder.py) | Volume of cylinder with height $= 28m$ and radius $= 1m$ is | $87 m^3$ | volume_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 38 | [Surface Area of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cone.py) | Surface area of cone with height $= 29m$ and radius $= 20m$ is | $3470 m^2$ | surface_area_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 39 | [Volume of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cone.py) | Volume of cone with height $= 32m$ and radius $= 5m$ is | $837 m^3$ | volume_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 49 | [Fourth Angle of Quadrilateral](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/fourth_angle_of_quadrilateral.py) | Fourth angle of quadrilateral with angles $125 , 30, 135 =$ | $70$ | fourth_angle_of_quadrilateral | `maxAngle=180`  |
| 57 | [Trigonometric Values](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/basic_trigonometry.py) | $\cos(30) = $ | $\frac{\sqrt{3}}{2}$ | basic_trigonometry | `angles=[0, 30, 45, 60, 90]` `functions=['sin', 'cos', 'tan']`  |
| 58 | [Sum of Angles of Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sum_of_polygon_angles.py) | What is the sum of interior angles of a polygon with $6$ sides? | $720$ | sum_of_polygon_angles | `maxSides=12`  |
| 60 | [Surface Area of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_sphere.py) | Surface area of Sphere with radius $= 17m$ is | $3631.6811075498013 m^2$ | surface_area_sphere | `maxSide=20` `unit='m'`  |
| 61 | [Volume of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_sphere.py) | Volume of sphere with radius $11 m = $ | $5575.279762570686 m^3$ | volume_sphere | `maxRadius=100`  |
| 70 | [Angle between 2 vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_btw_vectors.py) | angle between the vectors [890.27, 819.42, 567.65] and [59.88, 433.3, 20.6] is: | 0.77 radians | angle_btw_vectors | `maxEltAmt=20`  |
| 75 | [Area of a Sector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sector_area.py) | What is the area of a sector with radius $42$ and angle $347$ degrees? | $5341.65$ | sector_area | `maxRadius=49` `maxAngle=359`  |
| 86 | [Degrees to Radians](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/degree_to_rad.py) | Angle $204$ degrees in radians is:  | $3.56$ | degree_to_rad | `max_deg=360`  |
| 87 | [Radians to Degrees](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/radian_to_deg.py) | Angle $5.08$ radians in degrees is:  | $291.06$ | radian_to_deg | `max_rad=6.28`  |
| 95 | [Curved surface area of a cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/curved_surface_area_cylinder.py) | What is the curved surface area of a cylinder of radius, $16$ and height, $34$? | $3418.05$ | curved_surface_area_cylinder | `maxRadius=49` `maxHeight=99`  |
| 96 | [Perimeter of Polygons](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/perimeter_of_polygons.py) | The perimeter of a $3$ sided polygon with lengths of $81, 2, 31$cm is:  | $114$ | perimeter_of_polygons | `maxSides=12` `maxLength=120`  |
| 104 | [Circumference](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/circumference.py) | Circumference of circle with radius $22 = $ | $138.23$ | circumference | `maxRadius=100`  |
| 108 | [Arc length of Angle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/arc_length.py) | Given radius, $37$ and angle, $273$. Find the arc length of the angle. | Arc length of the angle $= 176.29571$ | arc_length | `maxRadius=49` `maxAngle=359`  |
| 112 | [Area of Circle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_circle.py) | Area of circle with radius $4$ | $50.27$ | area_of_circle | `maxRadius=100`  |
| 113 | [Volume of frustum](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_frustum.py) | Volume of frustum with height $= 17m$ and $r1 = 13m$ is and $r2 = 13m$ is  | $13832.0 m^3$ | volume_frustum | `maxR1=20` `maxR2=20` `maxHeight=50` `unit='m'`  |
| 114 | [Equation of line from two points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/equation_of_line_from_two_points.py) | What is the equation of the line between points $(15,4)$ and $(-1,-14)$ in slope-intercept form? | $8y = 9x -103$ | equation_of_line_from_two_points | `maxCoordinate=20` `minCoordinate=-20`  |
| 115 | [Area of Circle given center and a point on circle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_circle_given_center_and_point.py) | Area of circle with center $(1,8)$ and passing through $(5.86, 15.57)$ is | $254.47$ | area_of_circle_given_center_and_point | `maxCoordinate = 10` `maxRadius=10`  |
| 117 | [Volume of Hemisphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_hemisphere.py) | Volume of hemisphere with radius $93 m =$  | $1684641.361 m^3$ | volume_hemisphere | `maxRadius=100`  |
| 122 | [Volume of pyramid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_pyramid.py) | Volume of pyramid with base length $= 3 m$, base width $= 13 m$ and height $= 12 m$ is | $156.0 m^3$ | volume_pyramid | `maxLength=20` `maxWidth=20` `maxHeight=50` `unit='m'`  |
| 123 | [Surface area of pyramid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_pyramid.py) | Surface area of pyramid with base length $= 30m$, base width $= 48m$, and height $= 25m$ is | $2376 m^2$ | surface_area_pyramid | `unit='m'`  |
## misc
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 9 | [LCM (Least Common Multiple)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/lcm.py) | LCM of 4 and 19 = | 76 | lcm | `maxVal=20`  |
| 10 | [GCD (Greatest Common Denominator)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/gcd.py) | GCD of 14 and 3 =  | 1 | gcd | `maxVal=20`  |
| 27 | [Prime Factorisation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/prime_factors.py) | Find prime factors of 181 | [181] | prime_factors | `minVal=1` `maxVal=200`  |
| 40 | [Common Factors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/common_factors.py) | Common Factors of 22 and 11 =  | [1, 11] | common_factors | `maxVal=100`  |
| 51 | [HCF (Highest Common Factor)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/hcf.py) | HCF of 7 and 17 =  | 1 | hcf | `maxVal=20`  |
| 55 | [Comparing surds](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/surds_comparison.py) | Fill in the blanks 26^(1/1) _ 64^(1/8) | > | surds_comparison | `maxValue=100` `maxRoot=10`  |
| 63 | [Profit or Loss Percent](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/profit_loss_percent.py) | Profit percent when CP = 384 and SP = 476 is:  | 23.958333333333336 | profit_loss_percent | `maxCP=1000` `maxSP=1000`  |
| 66 | [Geometric Progression](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_progression.py) | For the given GP [10, 70, 490, 3430, 24010, 168070] ,Find the value of a,common ratio,6th term value, sum upto 7th term | The value of a is 10, common ratio is 7 , 6th term is 168070 , sum upto 7th term is 1372570.0 | geometric_progression | `number_values=6` `min_value=2` `max_value=12` `n_term=7` `sum_term=5`  |
| 67 | [Geometric Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_mean.py) | Geometric mean of 2 numbers 36 and 83 =  | (36*83)^(1/2) = 54.662601474865795 | geometric_mean | `maxValue=100` `maxNum=4`  |
| 68 | [Harmonic Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/harmonic_mean.py) | Harmonic mean of 4 numbers 20 , 35 , 13 , 80 =  |  4/((1/20) + (1/35) + (1/13) + (1/80)) = 23.810302534750612 | harmonic_mean | `maxValue=100` `maxNum=4`  |
| 69 | [Euclidian norm or L2 norm of a vector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/euclidian_norm.py) | Euclidian norm or L2 norm of the vector[303.6737627888933, 45.21884797407372, 624.685782950709, 335.2190228570935, 911.8440695285421] is: | 1195.126029445784 | euclidian_norm | `maxEltAmt=20`  |
| 81 | [Celsius To Fahrenheit](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/celsius_to_fahrenheit.py) | Convert -46 degrees Celsius to degrees Fahrenheit = | -50.8 | celsius_to_fahrenheit | `maxTemp=100`  |
| 82 | [AP Term Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_term.py) | Find the term number 66 of the AP series: -2, -86, -170 ...  | -5462 | arithmetic_progression_term | `maxd=100` `maxa=100` `maxn=100`  |
| 83 | [AP Sum Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_sum.py) | Find the sum of first 12 terms of the AP series: 78, 68, 58 ...  | 276.0 | arithmetic_progression_sum | `maxd=100` `maxa=100` `maxn=100`  |
| 85 | [Converts decimal to Roman Numerals](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/decimal_to_roman_numerals.py) | The number 0 in Roman Numerals is:  | MMLXVII | decimal_to_roman_numerals | `maxDecimal=4000`  |
| 92 | [Complex To Polar Form](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/complex_to_polar.py) | 16.49(-4.0theta + i-16.0theta) | -1.82 | complex_to_polar | `minRealImaginaryNum=-20, maxRealImaginaryNum=20`  |
| 93 | [Union,Intersection,Difference of Two Sets](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/set_operation.py) | Given the two sets a={3, 4, 6, 8, 9} ,b={8, 5, 6, 7}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {3, 4, 5, 6, 7, 8, 9},Intersection is {8, 6}, a-b is {9, 3, 4},b-a is {5, 7}, Symmetric difference is {3, 4, 5, 7, 9} | set_operation | `minval=3` `maxval=7` `n_a=4` `n_b=5`  |
| 94 | [Base Conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/base_conversion.py) | Convert 11171 from base 10 to base 16. | 2BA3 | base_conversion | `maxNum=60000` `maxBase=16`  |
| 98 | [Quotient of Powers with Same Base](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_base.py) | The Quotient of 30^2 and 30^3 = 30^(2-3) = 30^-1 | 0.03333333333333333 | quotient_of_power_same_base | `maxBase=50` `maxPower=10`  |
| 99 | [Quotient of Powers with Same Power](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_power.py) | The Quotient of 6^5 and 17^5 = (6/17)^5 = 0.35294117647058826^5 | 0.0054766078555798245 | quotient_of_power_same_power | `maxBase=50` `maxPower=10`  |
| 101 | [Leap Year or Not](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/is_leap_year.py) | Year 1934  | is not a leap year | is_leap_year | `minNumber=1900` `maxNumber=2099`  |
| 102 | [Minute to Hour conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/minutes_to_hours.py) | Convert 35 minutes to Hours & Minutes | 0 hours and 35 minutes | minutes_to_hours | `maxMinutes=999`  |
| 106 | [signum function](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/signum_function.py) | signum of 981 is = | 1 | signum_function | `min=-999` `max=999`  |
| 109 | [Binomial distribution](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/binomial_distribution.py) | A manufacturer of metal pistons finds that, on average, 36.25% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain no more than 6 rejected pistons? | 96.82 | binomial_distribution | ``  |
| 116 | [Factors of a number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/factors.py) | Factors of 131 =  | [1, 131] | factors | `maxVal=1000`  |
| 121 | [Product of scientific notations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/product_of_scientific_notations.py) | Product of scientific notations 9.1x10^-22 and 6.47x10^12 =  | 5.89x10^-9 | product_of_scientific_notations | `minExpVal=-100` `maxExpVal=100`  |
## statistics
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 30 | [Combinations of Objects](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/combinations.py) | Number of combinations from 11 objects picked 4 at a time  | 330 | combinations | `maxlength=20`  |
| 42 | [Permutations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/permutation.py) | Number of Permutations from 14 objects picked 2 at a time =   | 182 | permutation | `maxlength=20`  |
| 52 | [Probability of a certain sum appearing on faces of dice](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/dice_sum_probability.py) | If 2 dice are rolled at the same time, the probability of getting a sum of 2 = | 1/36 | dice_sum_probability | `maxDice=3`  |
| 54 | [Confidence interval For sample S](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/confidence_interval.py) | The confidence interval for sample [240, 285, 212, 287, 262, 200, 267, 297, 222, 217, 295, 246, 250, 291, 243, 261, 299, 281, 278, 259, 202, 223, 284, 238, 218] with 95% confidence is | (266.46887802967933, 242.09112197032064) | confidence_interval | ``  |
| 59 | [Mean,Standard Deviation,Variance](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/data_summary.py) | Find the mean,standard deviation and variance for the data[14, 50, 38, 26, 13, 43, 20, 6, 15, 42, 6, 50, 19, 18, 32] | The Mean is 26.133333333333333 , Standard Deviation is 217.31555555555553, Variance is 14.741626625157602 | data_summary | `number_values=15` `minval=5` `maxval=50`  |
| 76 | [Mean and Median](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/mean_median.py) | Given the series of numbers [6, 14, 21, 24, 25, 32, 37, 67, 85, 94]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 40.5 and Arithmetic median of this series is 28.5 | mean_median | `maxlen=10`  |
| 107 | [Conditional Probability](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/conditional_probability.py) | Someone tested positive for a nasty disease which only 1.55% of population have. Test sensitivity (true positive) is equal to SN= 95.64% whereas test specificity (true negative) SP= 99.36%. What is the probability that this guy really has that disease? | 70.17% | conditional_probability | ``  |
