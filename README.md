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
| 11 | [Basic Algebra](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/basic_algebra.py) | $2x + 9 = 10$ | $1/2$ | basic_algebra | `maxVariable=10`  |
| 12 | [Logarithm](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/log.py) | $log_{2}(4)=$ | $2$ | log | `maxBase=3` `maxVal=8`  |
| 17 | [Integer Multiplication with 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_int_to_22_matrix.py) | 3 * [[8, 9], [8, 1]] =  | [[24,27],[24,3]] | multiply_int_to_22_matrix | `maxMatrixVal=10` `maxRes=100`  |
| 20 | [Midpoint of the two point](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/midpoint_of_two_points.py) | The midpoint of $(18,-15)$ and $(-3,-16) = $ | $(7.5,-15.5)$ | midpoint_of_two_points | `maxValue=20`  |
| 21 | [Factoring Quadratic](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/factoring.py) | $x^2-2x-8$ | $(x+2)(x-4)$ | factoring | `range_x1=10` `range_x2=10`  |
| 23 | [Solve a System of Equations in R^2](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/system_of_equations.py) | 10x + 4y = -64, -8x +  = 32 | x = -4, y = -6 | system_of_equations | `range_x=10` `range_y=10` `coeff_mult_range=10`  |
| 24 | [Distance between 2 points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/distance_two_points.py) | Find the distance between $(-20, -1)$ and $(17, 1)$ | $\sqrt{1373}$ | distance_two_points | `maxValXY=20` `minValXY=-20`  |
| 26 | [Linear Equations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/linear_equations.py) | Given the equations $-15x + 3y = 183$ and $-1x + -11y = 57$, solve for x and y | $x = -13$, $y = -4$ | linear_equations | `n=2` `varRange=20` `coeffRange=20`  |
| 41 | [Intersection of Two Lines](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/intersection_of_two_lines.py) | Find the point of intersection of the two lines: $y = 6/2x - 5$ and $y = -8/5x$ | $(25/23, -40/23)$ | intersection_of_two_lines | `minM=-10` `maxM=10` `minB=-10` `maxB=10` `minDenominator=1` `maxDenominator=6`  |
| 43 | [Cross Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_cross.py) | [11, -6, -15] X [14, -10, 17] =  | [-252, -397, -26] | vector_cross | `minVal=-20` `maxVal=20`  |
| 45 | [Simple Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/simple_interest.py) | Simple interest for a principle amount of $9156$ dollars, $9\%$ rate of interest and for a time period of $4$ years is $=$  | $3296.16$ | simple_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 46 | [Multiplication of two matrices](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/matrix_multiplication.py) | Multiply<table><tr><td>-4</td><td>2</td><td>-8</td></tr><tr><td>2</td><td>-5</td><td>3</td></tr></table>and<table><tr><td>3</td><td>6</td></tr><tr><td>-7</td><td>10</td></tr><tr><td>2</td><td>-4</td></tr></table> | <table><tr><td>-42</td><td>28</td></tr><tr><td>47</td><td>-50</td></tr></table> | matrix_multiplication | `maxVal=100` `max_dim=10`  |
| 50 | [Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/quadratic_equation.py) | What are the zeros of the quadratic equation $95x^2+191x+52=0$ | ${-0.32, -1.69}$ | quadratic_equation | `maxVal=100`  |
| 65 | [Multiplication of 2 complex numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_complex_numbers.py) | $(1+9j) * 5j = $ | $(-45+5j)$ | multiply_complex_numbers | `minRealImaginaryNum=-20` `maxRealImaginaryNum=20`  |
| 72 | [Dot Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_dot.py) | $[13, -17, 9]\cdot[-14, 3, 5]=$ | $-188$ | vector_dot | `minVal=-20` `maxVal=20`  |
| 74 | [Inverse of a Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/invert_matrix.py) | Matrix([[45, 19, 79], [1, 20, 31], [71, 96, 95]]) | Matrix([[538/56501, -5779/113002, 991/113002], [-1053/56501, 667/56501, 658/56501], [662/56501, 2971/113002, -881/113002]]) | invert_matrix | `SquareMatrixDimension=3` `MaxMatrixElement=99` `OnlyIntegerElementsInInvertedMatrix=False`  |
| 77 | [Determinant to 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/int_matrix_22_determinant.py) | $\det \begin{bmatrix} a & b \\ c & d \end{bmatrix} = $ | $-838$ | int_matrix_22_determinant | `maxMatrixVal=100`  |
| 78 | [Compound Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/compound_interest.py) | Compound interest for a principle amount of $2564$ dollars, $6\%$ rate of interest and for a time period of $1$ years is $=$ | $2717.84$ | compound_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 100 | [complex Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/complex_quadratic.py) | Find the roots of given Quadratic Equation 5x^2 + 9x + 3 = 0 | simplified solution : ((-0.442, -1.358)), generalized solution : ((-9 + sqrt(21))/2*5, (-9 - sqrt(21))/2*5) | complex_quadratic | `prob_type=0` `max_range=10`  |
| 105 | [Combine Like terms](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/combine_like_terms.py) | $4x^{4} + 8x^{18} + 4x^{3} + 5x^{7} + 4x^{16} + 5x^{15}$ | $4x^{3} + 4x^{4} + 5x^{7} + 5x^{15} + 4x^{16} + 8x^{18}$ | combine_like_terms | `maxCoef=10` `maxExp=20` `maxTerms=10`  |
| 111 | [Expanding Factored Binomial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/expanding.py) | $(-2x-9)(3x-2)$ | $-6x^2-23x+18$ | expanding | `range_x1=10` `range_x2=10` `range_a=10` `range_b=10`  |
## basic_math
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 0 | [Addition](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/addition.py) | $0+13=$ | $13$ | addition | `maxSum=99` `maxAddend=50`  |
| 1 | [Subtraction](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/subtraction.py) | $92-1=$ | $91$ | subtraction | `maxMinuend=99` `maxDiff=99`  |
| 2 | [Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/multiplication.py) | $12\cdot3$ | $36$ | multiplication | `maxMulti=12`  |
| 3 | [Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/division.py) | $49\div7=$ | $7$ | division | `maxA=25` `maxB=25`  |
| 6 | [Square Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square_root.py) | $\sqrt{144}=$ | $12$ | square_root | `minNo=1` `maxNo=12`  |
| 8 | [Square](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square.py) | $13^2=$ | $169$ | square | `maxSquareNum=20`  |
| 13 | [Fraction to Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/fraction_to_decimal.py) | $21\div12=$ | $1.75$ | fraction_to_decimal | `maxRes=99` `maxDivid=99`  |
| 16 | [Fraction Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/divide_fractions.py) | $\frac{8}{7}\div\frac{4}{2}=$ | $\frac{4}{7}$ | divide_fractions | `maxVal=10`  |
| 28 | [Fraction Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/fraction_multiplication.py) | $\frac{10}{5}\cdot\frac{6}{9}=$ | $\frac{4}{3}$ | fraction_multiplication | `maxVal=10`  |
| 31 | [Factorial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/factorial.py) | $2! =$ | $2$ | factorial | `maxInput=6`  |
| 44 | [Compare Fractions](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/compare_fractions.py) | Which symbol represents the comparison between $\frac{7}{6}$ and $\frac{9}{10}$? | > | compare_fractions | `maxVal=10`  |
| 47 | [Cube Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/cube_root.py) | What is the cube root of: $\sqrt[3]{848}=$ to 2 decimal places? | $9.47$ | cube_root | `minNo=1` `maxNo=1000`  |
| 53 | [Exponentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/exponentiation.py) | $6^2 =$ | $36$ | exponentiation | `maxBase=20` `maxExpo=10`  |
| 71 | [Absolute difference between two numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/absolute_difference.py) | $|0-18|=$ | $18$ | absolute_difference | `maxA=100` `maxB=100`  |
| 80 | [Percentage of a number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage.py) | What is $70\%$ of $9$? | $6.30$ | percentage | `maxValue=99` `maxpercentage=99`  |
| 90 | [isprime](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/is_prime.py) | Is $42$ prime? | No | is_prime | `max_num=100`  |
| 97 | [Power of Powers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/power_of_powers.py) | Simplify $45^{9^{10}}$ | $45^{90}$ | power_of_powers | `maxBase=50` `maxPower=10`  |
| 118 | [Percentage difference](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage_difference.py) | What is the percentage difference between $37$ and $91$? | $84.38\%$ | percentage_difference | `maxValue=200` `minValue=0`  |
| 119 | [Percentage error](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage_error.py) | Find the percentage error when observed value equals $-22$ and exact value equals $-16$. | $37.5\%$ | percentage_error | `maxValue=100` `minValue=-100`  |
| 120 | [Greatest Common Divisor of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/greatest_common_divisor.py) | $GCD(422140979,291349478)=$ | $1$ | greatest_common_divisor | `numbersCount=2` `maximalNumberLimit=10**9`  |
| 124 | [Is Composite](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/is_composite.py) | Is $79$ composite? | No | is_composite | `maxNum=250`  |
## calculus
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 7 | [Power Rule Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_differentiation.py) | $10x^{4} + 9x^{3} + 10x^{6} + 6x^{1} + 7x^{2}$ | $40x^{3} + 27x^{2} + 60x^{5} + 6x^{0} + 14x^{1}$ | power_rule_differentiation | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 48 | [Power Rule Integration](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_integration.py) | $8x^{7} + 4x^{7} + 5x^{6} + 10x^{6} + 5x^{4}$ | $\frac{8}{7}x^{8} + \frac{4}{7}x^{8} + \frac{5}{6}x^{7} + \frac{10}{6}x^{7} + \frac{5}{4}x^{5} + C$ | power_rule_integration | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 88 | [Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/differentiation.py) | differentiate w.r.t x : d(cos(x)+7*x^4)/dx | 28*x^3 - sin(x) | differentiation | `diff_lvl=2`  |
| 89 | [Definite Integral of Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/definite_integral.py) | The definite integral within limits $0$ to $1$ of the equation $92x^2 + 60x + 41 = $ | $101.6667$ | definite_integral | `max_coeff=100`  |
| 110 | [Stationary Points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/stationary_points.py) | f(x)=x^3 + 7*x^2 + 3*x + 1 | (-7/3 - 2*sqrt(10)/3,(-7/3 - 2*sqrt(10)/3)**3 - 2*sqrt(10) - 6 + 7*(-7/3 - 2*sqrt(10)/3)**2),(-7/3 + 2*sqrt(10)/3,-6 + (-7/3 + 2*sqrt(10)/3)**3 + 7*(-7/3 + 2*sqrt(10)/3)**2 + 2*sqrt(10)) | stationary_points | `maxExp=3` `maxCoef=10`  |
## computer_science
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 4 | [Binary Complement 1s](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_complement_1s.py) | $1 = $ | $0$ | binary_complement_1s | `maxDigits=10`  |
| 5 | [Modulo Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/modulo_division.py) | $84\%29=$ | $26$ | modulo_division | `maxRes=99` `maxModulo=99`  |
| 14 | [Decimal to Binary](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_binary.py) | Binary of $51 = $ | $110011$ | decimal_to_binary | `max_dec=99`  |
| 15 | [Binary to Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_decimal.py) | $001100$ | $12$ | binary_to_decimal | `max_dig=10`  |
| 56 | [Fibonacci Series](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/fibonacci_series.py) | The Fibonacci Series of the first ${n}$ numbers is ? | $0, 1, 1, 2, 3, 5, 8, 13, 21$ | fibonacci_series | `minNo=1`  |
| 62 | [nth Fibonacci number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/nth_fibonacci_number.py) | What is the 70th Fibonacci number? | $190392490709135$ | nth_fibonacci_number | `maxN=100`  |
| 64 | [Binary to Hexidecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_hex.py) | $1101$ | $0xd$ | binary_to_hex | `max_dig=10`  |
| 73 | [Binary 2's Complement](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_2s_complement.py) | 2's complement of $10000110 = $ | $1111010$ | binary_2s_complement | `maxDigits=10`  |
| 79 | [Decimal to Hexadecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_hexadeci.py) | Binary of $497 = $ | $0x1f1$ | decimal_to_hexadeci | `max_dec=1000`  |
| 84 | [Converts decimal to octal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_octal.py) | The decimal number ${x}$ in Octal is:  | $0o7744$ | decimal_to_octal | `maxDecimal=4096`  |
| 91 | [Binary Coded Decimal to Integer](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/bcd_to_decimal.py) | Integer of Binary Coded Decimal $7$ is $=$  | $29953$ | bcd_to_decimal | `maxNumber=10000`  |
| 103 | [Decimal to Binary Coded Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_bcd.py) | BCD of Decimal Number $4111 = $ | $10015$ | decimal_to_bcd | `maxNumber=10000`  |
## geometry
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 18 | [Area of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_triangle.py) | Area of triangle with side lengths: $5, 6 10 = $ | $11.4$ | area_of_triangle | `maxA=20` `maxB=20`  |
| 19 | [Triangle exists check](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/valid_triangle.py) | Does triangle with sides $30, 10$ and $23$ exist? | $Yes$ | valid_triangle | `maxSideLength=50`  |
| 22 | [Third Angle of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/third_angle_of_triangle.py) | Third angle of triangle with angles $47$ and $3 = $ | $130$ | third_angle_of_triangle | `maxAngle=89`  |
| 25 | [Pythagorean Theorem](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/pythagorean_theorem.py) | What is the hypotenuse of a right triangle given the other two sides have lengths $15$ and $12$? | $19.21$ | pythagorean_theorem | `maxLength=20`  |
| 29 | [Angle of a Regular Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_regular_polygon.py) | Find the angle of a regular polygon with $14$ sides | $154.29$ | angle_regular_polygon | `minVal=3` `maxVal=20`  |
| 32 | [Surface Area of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cube.py) | Surface area of cube with side $= 16m$ is | $1536 m^2$ | surface_area_cube | `maxSide=20` `unit='m'`  |
| 33 | [Surface Area of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cuboid.py) | Surface area of cuboid with sides of lengths: $1m, 5m, 13m$ is | $166 m^2$ | surface_area_cuboid | `maxSide=20` `unit='m'`  |
| 34 | [Surface Area of Cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cylinder.py) | Surface area of cylinder with height $= 33m$ and radius $= 18m$ is | $5767 m^2$ | surface_area_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 35 | [Volume of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cube.py) | Volume of cube with a side length of $10m$ is | $1000 m^3$ | volume_cube | `maxSide=20` `unit='m'`  |
| 36 | [Volume of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cuboid.py) | Volume of cuboid with sides = $20m, 15m, 11m$ is | $3300 m^3$ | volume_cuboid | `maxSide=20` `unit='m'`  |
| 37 | [Volume of cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cylinder.py) | Volume of cylinder with height $= 31m$ and radius $= 18m$ is | $31554 m^3$ | volume_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 38 | [Surface Area of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cone.py) | Surface area of cone with height $= 46m$ and radius $= 13m$ is | $2483 m^2$ | surface_area_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 39 | [Volume of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cone.py) | Volume of cone with height $= 16m$ and radius $= 3m$ is | $150 m^3$ | volume_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 49 | [Fourth Angle of Quadrilateral](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/fourth_angle_of_quadrilateral.py) | Fourth angle of quadrilateral with angles $19 , 167, 140 =$ | $34$ | fourth_angle_of_quadrilateral | `maxAngle=180`  |
| 57 | [Trigonometric Values](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/basic_trigonometry.py) | $\tan(90) = $ | $\infty$ | basic_trigonometry | `angles=[0, 30, 45, 60, 90]` `functions=['sin', 'cos', 'tan']`  |
| 58 | [Sum of Angles of Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sum_of_polygon_angles.py) | What is the sum of interior angles of a polygon with $3$ sides? | $180$ | sum_of_polygon_angles | `maxSides=12`  |
| 60 | [Surface Area of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_sphere.py) | Surface area of Sphere with radius $= 3m$ is | $113.09733552923255 m^2$ | surface_area_sphere | `maxSide=20` `unit='m'`  |
| 61 | [Volume of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_sphere.py) | Volume of sphere with radius $17 m = $ | $20579.526276115535 m^3$ | volume_sphere | `maxRadius=100`  |
| 70 | [Angle between 2 vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_btw_vectors.py) | angle between the vectors [669.96, 589.4, 160.83, 579.16, 39.56, 495.57, 114.69, 326.61, 408.39, 205.67, 31.79, 674.05] and [346.4, 732.95, 566.25, 285.64, 660.72, 962.89, 772.29, 454.39, 38.48, 396.46, 584.97, 800.88] is: | 0.72 radians | angle_btw_vectors | `maxEltAmt=20`  |
| 75 | [Area of a Sector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sector_area.py) | What is the area of a sector with radius $29$ and angle $326$ degrees? | $2392.55$ | sector_area | `maxRadius=49` `maxAngle=359`  |
| 86 | [Degrees to Radians](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/degree_to_rad.py) | Angle $172$ degrees in radians is:  | $3.0$ | degree_to_rad | `max_deg=360`  |
| 87 | [Radians to Degrees](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/radian_to_deg.py) | Angle $5.17$ radians in degrees is:  | $296.22$ | radian_to_deg | `max_rad=6.28`  |
| 95 | [Curved surface area of a cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/curved_surface_area_cylinder.py) | What is the curved surface area of a cylinder of radius, $13$ and height, $31$? | $2532.12$ | curved_surface_area_cylinder | `maxRadius=49` `maxHeight=99`  |
| 96 | [Perimeter of Polygons](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/perimeter_of_polygons.py) | The perimeter of a $12$ sided polygon with lengths of $89, 67, 36, 94, 51, 48, 95, 19, 75, 20, 73, 119$cm is:  | $786$ | perimeter_of_polygons | `maxSides=12` `maxLength=120`  |
| 104 | [Circumference](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/circumference.py) | Circumference of circle with radius $50 = $ | $314.16$ | circumference | `maxRadius=100`  |
| 108 | [Arc length of Angle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/arc_length.py) | Given radius, $10$ and angle, $148$. Find the arc length of the angle. | Arc length of the angle $= 25.83087$ | arc_length | `maxRadius=49` `maxAngle=359`  |
| 112 | [Area of Circle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_circle.py) | Area of circle with radius $48$ | $7238.23$ | area_of_circle | `maxRadius=100`  |
| 113 | [Volume of frustum](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_frustum.py) | Volume of frustum with height $= 12m$ and $r1 = 5m$ is and $r2 = 5m$ is  | $615.0 m^3$ | volume_frustum | `maxR1=20` `maxR2=20` `maxHeight=50` `unit='m'`  |
| 114 | [Equation of line from two points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/equation_of_line_from_two_points.py) | What is the equation of the line between points $(-9,19)$ and $(1,-9)$ in slope-intercept form? | $5y = -14x -31$ | equation_of_line_from_two_points | `maxCoordinate=20` `minCoordinate=-20`  |
| 115 | [Area of Circle given center and a point on circle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_circle_given_center_and_point.py) | Area of circle with center $(7,5)$ and passing through $(2.0, 5.0)$ is | $78.54$ | area_of_circle_given_center_and_point | `maxCoordinate = 10` `maxRadius=10`  |
| 117 | [Volume of Hemisphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_hemisphere.py) | Volume of hemisphere with radius $1 m =$  | $2.094 m^3$ | volume_hemisphere | `maxRadius=100`  |
| 122 | [Volume of pyramid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_pyramid.py) | Volume of pyramid with base length $= 11 m$, base width $= 16 m$ and height $= 31 m$ is | $1818.6666666666667 m^3$ | volume_pyramid | `maxLength=20` `maxWidth=20` `maxHeight=50` `unit='m'`  |
| 123 | [Surface area of pyramid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_pyramid.py) | Surface area of pyramid with base length $= 16m$, base width $= 12m$, and height $= 10m$ is | $384 m^2$ | surface_area_pyramid | `unit='m'`  |
## misc
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 9 | [LCM (Least Common Multiple)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/lcm.py) | LCM of $10$ and $13 =$ | $130$ | lcm | `maxVal=20`  |
| 10 | [GCD (Greatest Common Denominator)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/gcd.py) | GCD of $11$ and $6 = $ | $1$ | gcd | `maxVal=20`  |
| 27 | [Prime Factorisation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/prime_factors.py) | Find prime factors of $71$ | $71$ | prime_factors | `minVal=1` `maxVal=200`  |
| 40 | [Common Factors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/common_factors.py) | Common Factors of $10$ and $37 = $ | $[1]$ | common_factors | `maxVal=100`  |
| 51 | [HCF (Highest Common Factor)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/hcf.py) | HCF of $2$ and $18 = $ | $2$ | hcf | `maxVal=20`  |
| 55 | [Comparing surds](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/surds_comparison.py) | Fill in the blanks $89^{\frac{1}{8}}$ _ $62^{\frac{1}{2}}$ | $<$ | surds_comparison | `maxValue=100` `maxRoot=10`  |
| 63 | [Profit or Loss Percent](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/profit_loss_percent.py) | Loss percent when $CP = 780$ and $SP = 77$ is:  | $90.13$ | profit_loss_percent | `maxCP=1000` `maxSP=1000`  |
| 66 | [Geometric Progression](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_progression.py) | For the given GP $[3, 9, 27, 81, 243, 729]$. Find the value of a common ratio, 11th term value, sum upto 6th term | The value of a is $3$, common ratio is $3$ , 11th term is $177147$, sum upto 6th term is $1092.0$ | geometric_progression | `number_values=6` `min_value=2` `max_value=12` `n_term=7` `sum_term=5`  |
| 67 | [Geometric Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_mean.py) | Geometric mean of $4$ numbers $[4, 30, 100, 42] = $ | $26.64$ | geometric_mean | `maxValue=100` `maxCount=4`  |
| 68 | [Harmonic Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/harmonic_mean.py) | Harmonic mean of $2$ numbers $16, 46 = $ | $546.0645161290323$ | harmonic_mean | `maxValue=100` `maxNum=4`  |
| 69 | [Euclidian norm or L2 norm of a vector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/euclidian_norm.py) | Euclidian norm or L2 norm of the vector $[90.63830628307679, 261.8513977001137, 687.911903727283, 872.6676424054388, 933.2820280849627, 445.2308649004979, 316.62614598153857, 938.3387676791752, 364.08630537934397, 516.4831673258176, 607.6823783310027, 384.8531994243025, 311.530953869087, 548.9965014198016, 814.9996881666945, 633.7036759508098, 818.0811504862265]$ is: | $2532.14$ | euclidian_norm | `maxEltAmt=20`  |
| 81 | [Celsius To Fahrenheit](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/celsius_to_fahrenheit.py) | Convert $11$ degrees Celsius to degrees Fahrenheit | $51.8$ | celsius_to_fahrenheit | `maxTemp=100`  |
| 82 | [AP Term Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_term.py) | Find term number $90$ of the AP series: $42, -17, -76 ... $ | $-5209$ | arithmetic_progression_term | `maxd=100` `maxa=100` `maxn=100`  |
| 83 | [AP Sum Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_sum.py) | Find the sum of first $14$ terms of the AP series: $80, 115, 150 ... $ | $4305.0$ | arithmetic_progression_sum | `maxd=100` `maxa=100` `maxn=100`  |
| 85 | [Converts decimal to Roman Numerals](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/decimal_to_roman_numerals.py) | The number $0$ in Roman Numerals is:  | $MMDCCCXL$ | decimal_to_roman_numerals | `maxDecimal=4000`  |
| 92 | [Complex To Polar Form](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/complex_to_polar.py) | $19.21(-12.0\theta + i15.0\theta)$ | $2.25$ | complex_to_polar | `minRealImaginaryNum=-20, maxRealImaginaryNum=20`  |
| 93 | [Union,Intersection,Difference of Two Sets](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/set_operation.py) | Given the two sets $a={8, 3, 6}$, $b={9, 3, 7}. Find the Union, intersection, a-b, b-a, and symmetric difference | Union is ${3, 6, 7, 8, 9}$. Intersection is ${3}$, a-b is ${8, 6}$, b-a is ${9, 7}$. Symmetric difference is ${6, 7, 8, 9}$. | set_operation | `minval=3` `maxval=7` `n_a=4` `n_b=5`  |
| 94 | [Base Conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/base_conversion.py) | Convert $127534$ from base $8$ to base $13$. | $17583$ | base_conversion | `maxNum=60000` `maxBase=16`  |
| 98 | [Quotient of Powers with Same Base](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_base.py) | The Quotient of $3^{7}$ and $3^{2} = $3^{7-2} = 3^{5}$ | $243$ | quotient_of_power_same_base | `maxBase=50` `maxPower=10`  |
| 99 | [Quotient of Powers with Same Power](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_power.py) | The Quotient of $49^{8}$ and $16^{8} = (49/16)^8 = 3.0625^{8}$ | $7737.644615024561$ | quotient_of_power_same_power | `maxBase=50` `maxPower=10`  |
| 101 | [Leap Year or Not](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/is_leap_year.py) | Is 2038 a leap year? | 2038 is not a leap year | is_leap_year | `minNumber=1900` `maxNumber=2099`  |
| 102 | [Minute to Hour conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/minutes_to_hours.py) | Convert $139$ minutes to hours & minutes | $2$ hours and $19$ minutes | minutes_to_hours | `maxMinutes=999`  |
| 106 | [signum function](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/signum_function.py) | signum of 673 is = | $1$ | signum_function | `min=-999` `max=999`  |
| 109 | [Binomial distribution](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/binomial_distribution.py) | A manufacturer of metal pistons finds that, on average, $37.91\%$ of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of $11$ pistons will contain no more than $2$ rejected pistons? | $14.92$ | binomial_distribution | ``  |
| 116 | [Factors of a number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/factors.py) | Factors of $502 = $ | $[1, 2, 251, 502]$ | factors | `maxVal=1000`  |
| 121 | [Product of scientific notations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/product_of_scientific_notations.py) | Product of scientific notations $9.52x10^-3 and 4.34x10^93 = $ | 4.13x10^91 | product_of_scientific_notations | `minExpVal=-100` `maxExpVal=100`  |
## statistics
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 30 | [Combinations of Objects](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/combinations.py) | Find the number of combinations from $12$ objects picked $8$ at a time. | $495$ | combinations | `maxlength=20`  |
| 42 | [Permutations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/permutation.py) | Number of Permutations from $20$ objects picked $8$ at a time is:  | $5079110400$ | permutation | `maxlength=20`  |
| 52 | [Probability of a certain sum appearing on faces of dice](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/dice_sum_probability.py) | If $2$ dice are rolled at the same time, the probability of getting a sum of $8 =$ | \frac{5}{36} | dice_sum_probability | `maxDice=3`  |
| 54 | [Confidence interval For sample S](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/confidence_interval.py) | The confidence interval for sample $[294, 235, 254, 298, 234, 201, 208, 274, 250, 244, 265, 284, 264, 293, 251, 241, 202, 252, 261, 240, 247, 230, 295, 269, 232, 292, 206, 256, 228, 267, 263, 225, 246, 268, 288, 297, 207, 200]$ with $95\%$ confidence is | $(260.8632286016648, 242.3472977141247)$ | confidence_interval | ``  |
| 59 | [Mean,Standard Deviation,Variance](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/data_summary.py) | Find the mean,standard deviation and variance for the data $26, 13, 9, 50, 26, 29, 32, 45, 7, 31, 45, 5, 21, 5, 30$ | The Mean is $24.933333333333334$, Standard Deviation is $206.19555555555556$, Variance is $14.359510978983774$ | data_summary | `number_values=15` `minval=5` `maxval=50`  |
| 76 | [Mean and Median](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/mean_median.py) | Given the series of numbers $[7, 10, 12, 33, 47, 61, 63, 64, 73, 76]$. Find the arithmatic mean and mdian of the series | Arithmetic mean of the series is $44.6$ and Arithmetic median of this series is $54.0$ | mean_median | `maxlen=10`  |
| 107 | [Conditional Probability](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/conditional_probability.py) | Someone tested positive for a nasty disease which only $0.21\%$ of the population have. Test sensitivity (true positive) is equal to $SN=90.02\%$ whereas test specificity (true negative) $SP=99.56\%$. What is the probability that this guy really has that disease? | $30.1\%$ | conditional_probability | ``  |
