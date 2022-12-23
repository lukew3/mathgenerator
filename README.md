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
You may prefer to use `import mathgenerator as mg` and run functions like `mg.addition()` so that you don't have to type as much.
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
[id, title, gen_func, funcname, subjectname, kwargs]
```


## List of Generators
## algebra
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 11 | [Basic Algebra](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/basic_algebra.py) | $4x + 9 = 10$ | $1/4$ | basic_algebra | `maxVariable=10`  |
| 12 | [Logarithm](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/log.py) | $log_{2}(16)=$ | $4$ | log | `maxBase=3` `maxVal=8`  |
| 17 | [Integer Multiplication with 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_int_to_22_matrix.py) | $9 * \begin{bmatrix} 2 & 3 \\ 2 & 6 \end{bmatrix} =$ | $\begin{bmatrix} 18 & 27 \\ 18 & 54 \end{bmatrix}$ | multiply_int_to_22_matrix | `maxMatrixVal=10` `maxRes=100`  |
| 20 | [Midpoint of the two point](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/midpoint_of_two_points.py) | The midpoint of $(20,5)$ and $(2,16) = $ | $(11.0,10.5)$ | midpoint_of_two_points | `maxValue=20`  |
| 21 | [Factoring Quadratic](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/factoring.py) | $x^2-3x-70$ | $(x-10)(x+7)$ | factoring | `range_x1=10` `range_x2=10`  |
| 23 | [Solve a System of Equations in R^2](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/system_of_equations.py) | Given $4x + 6y = -46$ and $-7x - 3y = 58$, solve for $x$ and $y$. | $x = -7$, $y = -3$ | system_of_equations | `range_x=10` `range_y=10` `coeff_mult_range=10`  |
| 24 | [Distance between 2 points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/distance_two_points.py) | Find the distance between $(-20, -1)$ and $(-10, -10)$ | $\sqrt{181}$ | distance_two_points | `maxValXY=20` `minValXY=-20`  |
| 26 | [Linear Equations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/linear_equations.py) | Given the equations $2x + 12y = 164$ and $-2x + 18y = 166$, solve for $x$ and $y$ | $x = 16$, $y = 11$ | linear_equations | `n=2` `varRange=20` `coeffRange=20`  |
| 41 | [Intersection of Two Lines](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/intersection_of_two_lines.py) | Find the point of intersection of the two lines: $y = -8x + 3$ and $y = x + 10$ | $(-7/9, 83/9)$ | intersection_of_two_lines | `minM=-10` `maxM=10` `minB=-10` `maxB=10` `minDenominator=1` `maxDenominator=6`  |
| 43 | [Cross Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_cross.py) | [17, -18, 12] X [19, -12, 14] =  | [-108, -10, 138] | vector_cross | `minVal=-20` `maxVal=20`  |
| 45 | [Simple Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/simple_interest.py) | Simple interest for a principle amount of $9540$ dollars, $5\%$ rate of interest and for a time period of $4$ years is $=$  | $1908.0$ | simple_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 46 | [Multiplication of two matrices](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/matrix_multiplication.py) | Multiply$\begin{bmatrix}-7&-4&-10\\-9&3&6\end{bmatrix}$and$\begin{bmatrix}0&3\\-3&0\\1&3\end{bmatrix}$ | $\begin{bmatrix}2&-51\\-3&-9\end{bmatrix}$ | matrix_multiplication | `maxVal=100` `max_dim=10`  |
| 50 | [Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/quadratic_equation.py) | What are the zeros of the quadratic equation $88x^2+98x+13=0$ | ${-0.15, -0.96}$ | quadratic_equation | `maxVal=100`  |
| 65 | [Multiplication of 2 complex numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_complex_numbers.py) | $(-6-11j) * (-2-16j) = $ | $(-164+118j)$ | multiply_complex_numbers | `minRealImaginaryNum=-20` `maxRealImaginaryNum=20`  |
| 72 | [Dot Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_dot.py) | $[-15, -1, 7]\cdot[8, 2, 3]=$ | $-101$ | vector_dot | `minVal=-20` `maxVal=20`  |
| 74 | [Inverse of a Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/invert_matrix.py) | Inverse of Matrix $\begin{bmatrix} 4 & 1 & 4 \\ 3 & 1 & 3 \\ 7 & 2 & 6 \end{bmatrix}$ is: | \begin{bmatrix} 0 & -2 & 1 \\ -3 & 4 & 0 \\ 1 & 1 & -1 \end{bmatrix} | invert_matrix | `SquareMatrixDimension=3` `MaxMatrixElement=99` `OnlyIntegerElementsInInvertedMatrix=True`  |
| 77 | [Determinant to 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/int_matrix_22_determinant.py) | $\det \begin{bmatrix} 78 & 63 \\ 67 & 85 \end{bmatrix}= $ | $2409$ | int_matrix_22_determinant | `maxMatrixVal=100`  |
| 78 | [Compound Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/compound_interest.py) | Compound interest for a principle amount of $5737$ dollars, $3\%$ rate of interest and for a time period of $8$ years is $=$ | $7267.46$ | compound_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 100 | [complex Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/complex_quadratic.py) | Find the roots of given Quadratic Equation $5x^2 + 7x + 1 = 0$ | $((-0.161, -1.239)) = (\frac{-7 + \sqrt{29}}{2*5}, (\frac{-7 - \sqrt{29}}{2*5})$ | complex_quadratic | `prob_type=0` `max_range=10`  |
| 105 | [Combine Like terms](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/combine_like_terms.py) | $5x^{5} + 5x^{12} + 9x^{17} + 8x^{19} + 5x^{5} + 2x^{12}$ | $10x^{5} + 7x^{12} + 9x^{17} + 8x^{19}$ | combine_like_terms | `maxCoef=10` `maxExp=20` `maxTerms=10`  |
| 111 | [Expanding Factored Binomial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/expanding.py) | $(-3x+1)(8x)$ | $-24x^2+8x$ | expanding | `range_x1=10` `range_x2=10` `range_a=10` `range_b=10`  |
## basic_math
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 0 | [Addition](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/addition.py) | $27+4=$ | $31$ | addition | `maxSum=99` `maxAddend=50`  |
| 1 | [Subtraction](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/subtraction.py) | $42-1=$ | $41$ | subtraction | `maxMinuend=99` `maxDiff=99`  |
| 2 | [Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/multiplication.py) | $1\cdot1$ | $1$ | multiplication | `maxMulti=12`  |
| 3 | [Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/division.py) | $432\div18=$ | $24$ | division | `maxA=25` `maxB=25`  |
| 6 | [Square Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square_root.py) | $\sqrt{121}=$ | $11$ | square_root | `minNo=1` `maxNo=12`  |
| 8 | [Square](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square.py) | $9^2=$ | $81$ | square | `maxSquareNum=20`  |
| 13 | [Fraction to Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/fraction_to_decimal.py) | $93\div89=$ | $1.04$ | fraction_to_decimal | `maxRes=99` `maxDivid=99`  |
| 16 | [Fraction Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/divide_fractions.py) | $\frac{6}{2}\div\frac{6}{2}=$ | $\frac{1}{1}$ | divide_fractions | `maxVal=10`  |
| 28 | [Fraction Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/fraction_multiplication.py) | $\frac{3}{5}\cdot\frac{6}{4}=$ | $\frac{9}{10}$ | fraction_multiplication | `maxVal=10`  |
| 31 | [Factorial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/factorial.py) | $1! =$ | $1$ | factorial | `maxInput=6`  |
| 44 | [Compare Fractions](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/compare_fractions.py) | Which symbol represents the comparison between $\frac{1}{2}$ and $\frac{10}{7}$? | < | compare_fractions | `maxVal=10`  |
| 47 | [Cube Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/cube_root.py) | What is the cube root of: $\sqrt[3]{984}=$ to 2 decimal places? | $9.95$ | cube_root | `minNo=1` `maxNo=1000`  |
| 53 | [Exponentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/exponentiation.py) | $1^5 =$ | $1$ | exponentiation | `maxBase=20` `maxExpo=10`  |
| 71 | [Absolute difference between two numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/absolute_difference.py) | $|25--88|=$ | $113$ | absolute_difference | `maxA=100` `maxB=100`  |
| 80 | [Percentage of a number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage.py) | What is $90\%$ of $85$? | $76.50$ | percentage | `maxValue=99` `maxpercentage=99`  |
| 90 | [isprime](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/is_prime.py) | Is $91$ prime? | No | is_prime | `max_num=100`  |
| 97 | [Power of Powers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/power_of_powers.py) | Simplify $40^{7^{3}}$ | $40^{21}$ | power_of_powers | `maxBase=50` `maxPower=10`  |
| 118 | [Percentage difference](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage_difference.py) | What is the percentage difference between $151$ and $29$? | $135.56\%$ | percentage_difference | `maxValue=200` `minValue=0`  |
| 119 | [Percentage error](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage_error.py) | Find the percentage error when observed value equals $-49$ and exact value equals $-85$. | $42.35\%$ | percentage_error | `maxValue=100` `minValue=-100`  |
| 120 | [Greatest Common Divisor of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/greatest_common_divisor.py) | $GCD(615079868,872888560)=$ | $4$ | greatest_common_divisor | `numbersCount=2` `maximalNumberLimit=10**9`  |
| 124 | [Is Composite](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/is_composite.py) | Is $3$ composite? | No | is_composite | `maxNum=250`  |
## calculus
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 7 | [Power Rule Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_differentiation.py) | $8x^{5} + 4x^{2} + 3x^{6} + 6x^{8} + 9x^{2}$ | $40x^{4} + 8x^{1} + 18x^{5} + 48x^{7} + 18x^{1}$ | power_rule_differentiation | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 48 | [Power Rule Integration](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_integration.py) | $10x^{10} + 5x^{10} + 3x^{8} + 5x^{7} + 1x^{1}$ | $\frac{10}{10}x^{11} + \frac{5}{10}x^{11} + \frac{3}{8}x^{9} + \frac{5}{7}x^{8} + \frac{1}{1}x^{2} + C$ | power_rule_integration | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 88 | [Trigonometric Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/trig_differentiation.py) | $\frac{d}{dx}(\csc)=$ | $-\csc \cdot \cot$ | trig_differentiation |  |
| 89 | [Definite Integral of Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/definite_integral.py) | The definite integral within limits $0$ to $1$ of the equation $45x^2 + 2x + 72 = $ | $88.0$ | definite_integral | `max_coeff=100`  |
| 110 | [Stationary Points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/stationary_points.py) | $f(x)=3*x^3 + 6*x^2 + 10$ | ${- \frac{4}{3}, 0}$ | stationary_points | `maxExp=3` `maxCoef=10`  |
## computer_science
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 4 | [Binary Complement 1s](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_complement_1s.py) | $00001 = $ | $11110$ | binary_complement_1s | `maxDigits=10`  |
| 5 | [Modulo Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/modulo_division.py) | $45 \% 29 = $ | $16$ | modulo_division | `maxRes=99` `maxModulo=99`  |
| 14 | [Decimal to Binary](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_binary.py) | Binary of $93 = $ | $1011101$ | decimal_to_binary | `max_dec=99`  |
| 15 | [Binary to Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_decimal.py) | $0011011$ | $27$ | binary_to_decimal | `max_dig=10`  |
| 56 | [Fibonacci Series](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/fibonacci_series.py) | The Fibonacci Series of the first ${n}$ numbers is ? | $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55$ | fibonacci_series | `minNo=1`  |
| 62 | [nth Fibonacci number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/nth_fibonacci_number.py) | What is the 76th Fibonacci number? | $3416454622906715$ | nth_fibonacci_number | `maxN=100`  |
| 64 | [Binary to Hexidecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_hex.py) | $01$ | $0x1$ | binary_to_hex | `max_dig=10`  |
| 73 | [Binary 2's Complement](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_2s_complement.py) | 2's complement of $11000110 = $ | $111010$ | binary_2s_complement | `maxDigits=10`  |
| 79 | [Decimal to Hexadecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_hexadeci.py) | Binary of $389 = $ | $0x185$ | decimal_to_hexadeci | `max_dec=1000`  |
| 84 | [Converts decimal to octal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_octal.py) | The decimal number ${x}$ in Octal is:  | $0o7622$ | decimal_to_octal | `maxDecimal=4096`  |
| 91 | [Binary Coded Decimal to Integer](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/bcd_to_decimal.py) | Integer of Binary Coded Decimal $6$ is $=$  | $24932$ | bcd_to_decimal | `maxNumber=10000`  |
| 103 | [Decimal to Binary Coded Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_bcd.py) | BCD of Decimal Number $4765 = $ | $12913$ | decimal_to_bcd | `maxNumber=10000`  |
## geometry
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 18 | [Area of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_triangle.py) | Area of triangle with side lengths: $11, 14 5 = $ | $24.49$ | area_of_triangle | `maxA=20` `maxB=20`  |
| 19 | [Triangle exists check](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/valid_triangle.py) | Does triangle with sides $49, 17$ and $37$ exist? | $Yes$ | valid_triangle | `maxSideLength=50`  |
| 22 | [Third Angle of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/third_angle_of_triangle.py) | Third angle of triangle with angles $54$ and $61 = $ | $65$ | third_angle_of_triangle | `maxAngle=89`  |
| 25 | [Pythagorean Theorem](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/pythagorean_theorem.py) | What is the hypotenuse of a right triangle given the other two sides have lengths $2$ and $11$? | $11.18$ | pythagorean_theorem | `maxLength=20`  |
| 29 | [Angle of a Regular Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_regular_polygon.py) | Find the angle of a regular polygon with $18$ sides | $160.0$ | angle_regular_polygon | `minVal=3` `maxVal=20`  |
| 32 | [Surface Area of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cube.py) | Surface area of cube with side $= 9m$ is | $486 m^2$ | surface_area_cube | `maxSide=20` `unit='m'`  |
| 33 | [Surface Area of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cuboid.py) | Surface area of cuboid with sides of lengths: $1m, 11m, 13m$ is | $334 m^2$ | surface_area_cuboid | `maxSide=20` `unit='m'`  |
| 34 | [Surface Area of Cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cylinder.py) | Surface area of cylinder with height $= 18m$ and radius $= 12m$ is | $2261 m^2$ | surface_area_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 35 | [Volume of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cube.py) | Volume of cube with a side length of $20m$ is | $8000 m^3$ | volume_cube | `maxSide=20` `unit='m'`  |
| 36 | [Volume of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cuboid.py) | Volume of cuboid with sides = $11m, 4m, 6m$ is | $264 m^3$ | volume_cuboid | `maxSide=20` `unit='m'`  |
| 37 | [Volume of cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cylinder.py) | Volume of cylinder with height $= 23m$ and radius $= 20m$ is | $28902 m^3$ | volume_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 38 | [Surface Area of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cone.py) | Surface area of cone with height $= 26m$ and radius $= 8m$ is | $884 m^2$ | surface_area_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 39 | [Volume of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cone.py) | Volume of cone with height $= 2m$ and radius $= 8m$ is | $134 m^3$ | volume_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 49 | [Fourth Angle of Quadrilateral](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/fourth_angle_of_quadrilateral.py) | Fourth angle of quadrilateral with angles $5 , 9, 185 =$ | $161$ | fourth_angle_of_quadrilateral | `maxAngle=180`  |
| 57 | [Trigonometric Values](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/basic_trigonometry.py) | $\cos(45) = $ | $\frac{1}{\sqrt{2}}$ | basic_trigonometry | `angles=[0, 30, 45, 60, 90]` `functions=['sin', 'cos', 'tan']`  |
| 58 | [Sum of Angles of Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sum_of_polygon_angles.py) | What is the sum of interior angles of a polygon with $6$ sides? | $720$ | sum_of_polygon_angles | `maxSides=12`  |
| 60 | [Surface Area of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_sphere.py) | Surface area of Sphere with radius $= 19m$ is | $4536.459791783661 m^2$ | surface_area_sphere | `maxSide=20` `unit='m'`  |
| 61 | [Volume of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_sphere.py) | Volume of sphere with radius $90 m = $ | $3053628.0592892785 m^3$ | volume_sphere | `maxRadius=100`  |
| 70 | [Angle between 2 vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_btw_vectors.py) | angle between the vectors $[696.76, 365.76, 881.26, 263.67, 552.55, 85.64, 970.8, 682.62, 225.89, 756.1, 543.54, 348.14, 848.32, 772.79, 745.54, 266.96, 745.62, 253.22]$ and $[716.05, 850.26, 0.93, 84.61, 671.18, 534.83, 752.87, 522.17, 295.21, 294.19, 862.81, 738.02, 253.74, 570.99, 477.05, 952.93, 34.86, 709.03]$ is: | $0.74$ radians | angle_btw_vectors | `maxEltAmt=20`  |
| 75 | [Area of a Sector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sector_area.py) | What is the area of a sector with radius $12$ and angle $289$ degrees? | $363.17$ | sector_area | `maxRadius=49` `maxAngle=359`  |
| 86 | [Degrees to Radians](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/degree_to_rad.py) | Angle $133$ degrees in radians is:  | $2.32$ | degree_to_rad | `max_deg=360`  |
| 87 | [Radians to Degrees](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/radian_to_deg.py) | Angle $4.98$ radians in degrees is:  | $285.33$ | radian_to_deg | `max_rad=6.28`  |
| 95 | [Curved surface area of a cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/curved_surface_area_cylinder.py) | What is the curved surface area of a cylinder of radius, $43$ and height, $1$? | $270.18$ | curved_surface_area_cylinder | `maxRadius=49` `maxHeight=99`  |
| 96 | [Perimeter of Polygons](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/perimeter_of_polygons.py) | The perimeter of a $10$ sided polygon with lengths of $99, 54, 82, 93, 113, 111, 51, 76, 63, 56$cm is:  | $798$ | perimeter_of_polygons | `maxSides=12` `maxLength=120`  |
| 104 | [Circumference](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/circumference.py) | Circumference of circle with radius $54 = $ | $339.29$ | circumference | `maxRadius=100`  |
| 108 | [Arc length of Angle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/arc_length.py) | Given radius, $18$ and angle, $52$. Find the arc length of the angle. | Arc length of the angle $= 16.33628$ | arc_length | `maxRadius=49` `maxAngle=359`  |
| 112 | [Area of Circle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_circle.py) | Area of circle with radius $17=$ | $907.92$ | area_of_circle | `maxRadius=100`  |
| 113 | [Volume of frustum](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_frustum.py) | Volume of frustum with height $= 11m$ and $r1 = 2m$ is and $r2 = 2m$ is  | $4192.0 m^3$ | volume_frustum | `maxR1=20` `maxR2=20` `maxHeight=50` `unit='m'`  |
| 114 | [Equation of line from two points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/equation_of_line_from_two_points.py) | What is the equation of the line between points $(20,3)$ and $(1,-18)$ in slope-intercept form? | $19y = 21x -363$ | equation_of_line_from_two_points | `maxCoordinate=20` `minCoordinate=-20`  |
| 115 | [Area of Circle given center and a point on circle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_circle_given_center_and_point.py) | Area of circle with center $(-1,1)$ and passing through $(1.0, 1.0)$ is | $12.57$ | area_of_circle_given_center_and_point | `maxCoordinate = 10` `maxRadius=10`  |
| 117 | [Volume of Hemisphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_hemisphere.py) | Volume of hemisphere with radius $65 m =$  | $575173.255 m^3$ | volume_hemisphere | `maxRadius=100`  |
| 122 | [Volume of pyramid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_pyramid.py) | Volume of pyramid with base length $= 20 m$, base width $= 5 m$ and height $= 37 m$ is | $1233.3333333333333 m^3$ | volume_pyramid | `maxLength=20` `maxWidth=20` `maxHeight=50` `unit='m'`  |
| 123 | [Surface area of pyramid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_pyramid.py) | Surface area of pyramid with base length $= 40m$, base width $= 32m$, and height $= 12m$ is | $2560 m^2$ | surface_area_pyramid | `unit='m'`  |
| 125 | [Complementary and Supplementary Angle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/complementary_and_supplementary_angle.py) | The supplementary angle of 43 = | 137 | complementary_and_supplementary_angle | `maxSupp=180` `maxComp=90`  |
## misc
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 9 | [LCM (Least Common Multiple)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/lcm.py) | LCM of $8$ and $10 =$ | $40$ | lcm | `maxVal=20`  |
| 10 | [GCD (Greatest Common Denominator)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/gcd.py) | GCD of $11$ and $7 = $ | $1$ | gcd | `maxVal=20`  |
| 27 | [Prime Factorisation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/prime_factors.py) | Find prime factors of $39$ | $3, 13$ | prime_factors | `minVal=1` `maxVal=200`  |
| 40 | [Common Factors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/common_factors.py) | Common Factors of $30$ and $27 = $ | $[1, 3]$ | common_factors | `maxVal=100`  |
| 51 | [HCF (Highest Common Factor)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/hcf.py) | HCF of $8$ and $3 = $ | $1$ | hcf | `maxVal=20`  |
| 55 | [Comparing surds](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/surds_comparison.py) | Fill in the blanks $18^{\frac{1}{7}}$ _ $3^{\frac{1}{6}}$ | $>$ | surds_comparison | `maxValue=100` `maxRoot=10`  |
| 63 | [Profit or Loss Percent](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/profit_loss_percent.py) | Profit percent when $CP = 315$ and $SP = 537$ is:  | $70.48$ | profit_loss_percent | `maxCP=1000` `maxSP=1000`  |
| 66 | [Geometric Progression](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_progression.py) | For the given GP $[8, 88, 968, 10648, 117128, 1288408]$. Find the value of a common ratio, 9th term value, sum upto 10th term | The value of a is $8$, common ratio is $11$ , 9th term is $1714871048$, sum upto 10th term is $20749939680.0$ | geometric_progression | `number_values=6` `min_value=2` `max_value=12` `n_term=7` `sum_term=5`  |
| 67 | [Geometric Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_mean.py) | Geometric mean of $2$ numbers $[68, 68] = $ | $68.0$ | geometric_mean | `maxValue=100` `maxCount=4`  |
| 68 | [Harmonic Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/harmonic_mean.py) | Harmonic mean of $2$ numbers $47, 68 = $ | $1889.808695652174$ | harmonic_mean | `maxValue=100` `maxNum=4`  |
| 69 | [Euclidian norm or L2 norm of a vector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/euclidian_norm.py) | Euclidian norm or L2 norm of the vector $[527.9819372799017, 894.2569120773508, 599.3824594907154, 969.7582840231978, 421.6938570424307, 733.944242522682, 63.10925602902362, 56.32392977028688, 75.98051054467004, 74.22280665062675, 542.3722581680679, 3.9128916318467155, 423.95047422398403, 710.7561789338693, 906.963467655613, 900.2118030663215, 307.4106848415229, 534.298333794332, 443.9576166548943, 598.7593783404543]$ is: | $2580.84$ | euclidian_norm | `maxEltAmt=20`  |
| 81 | [Celsius To Fahrenheit](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/celsius_to_fahrenheit.py) | Convert $-33$ degrees Celsius to degrees Fahrenheit | $-27.4$ | celsius_to_fahrenheit | `maxTemp=100`  |
| 82 | [AP Term Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_term.py) | Find term number $45$ of the AP series: $-65, -156, -247 ... $ | $-4069$ | arithmetic_progression_term | `maxd=100` `maxa=100` `maxn=100`  |
| 83 | [AP Sum Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_sum.py) | Find the sum of first $69$ terms of the AP series: $-10, -67, -124 ... $ | $-134412.0$ | arithmetic_progression_sum | `maxd=100` `maxa=100` `maxn=100`  |
| 85 | [Converts decimal to Roman Numerals](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/decimal_to_roman_numerals.py) | The number $0$ in Roman Numerals is:  | $CV$ | decimal_to_roman_numerals | `maxDecimal=4000`  |
| 92 | [Complex To Polar Form](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/complex_to_polar.py) | $9.06(-1.0\theta + i-9.0\theta)$ | $-1.68$ | complex_to_polar | `minRealImaginaryNum=-20, maxRealImaginaryNum=20`  |
| 93 | [Union,Intersection,Difference of Two Sets](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/set_operation.py) | Given the two sets $a={1, 4, 7, 9, 10}$, $b={2, 10, 3, 4}. Find the Union, intersection, a-b, b-a, and symmetric difference | Union is ${1, 2, 3, 4, 7, 9, 10}$. Intersection is ${10, 4}$, a-b is ${1, 9, 7}$, b-a is ${2, 3}$. Symmetric difference is ${1, 2, 3, 7, 9}$. | set_operation | `minval=3` `maxval=7` `n_a=4` `n_b=5`  |
| 94 | [Base Conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/base_conversion.py) | Convert $59A0$ from base $11$ to base $10$. | $7854$ | base_conversion | `maxNum=60000` `maxBase=16`  |
| 98 | [Quotient of Powers with Same Base](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_base.py) | The Quotient of $7^{8}$ and $7^{2} = $7^{8-2} = 7^{6}$ | $117649$ | quotient_of_power_same_base | `maxBase=50` `maxPower=10`  |
| 99 | [Quotient of Powers with Same Power](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_power.py) | The Quotient of $34^{5}$ and $32^{5} = (34/32)^5 = 1.0625^{5}$ | $1.354081153869629$ | quotient_of_power_same_power | `maxBase=50` `maxPower=10`  |
| 101 | [Leap Year or Not](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/is_leap_year.py) | Is 2093 a leap year? | 2093 is not a leap year | is_leap_year | `minNumber=1900` `maxNumber=2099`  |
| 102 | [Minute to Hour conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/minutes_to_hours.py) | Convert $257$ minutes to hours & minutes | $4$ hours and $17$ minutes | minutes_to_hours | `maxMinutes=999`  |
| 106 | [signum function](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/signum_function.py) | signum of 287 is = | $1$ | signum_function | `min=-999` `max=999`  |
| 109 | [Binomial distribution](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/binomial_distribution.py) | A manufacturer of metal pistons finds that, on average, $36.22\%$ of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of $15$ pistons will contain no more than $6$ rejected pistons? | $72.17$ | binomial_distribution | ``  |
| 116 | [Factors of a number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/factors.py) | Factors of $848 = $ | $[1, 2, 4, 8, 16, 53, 106, 212, 424, 848]$ | factors | `maxVal=1000`  |
| 121 | [Product of scientific notations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/product_of_scientific_notations.py) | Product of scientific notations $7.98 \times 10^{21}$ and $2.31 \times 10^{90} = $ | $1.84 \times 10^{112}$ | product_of_scientific_notations | `minExpVal=-100` `maxExpVal=100`  |
## statistics
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 30 | [Combinations of Objects](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/combinations.py) | Find the number of combinations from $14$ objects picked $2$ at a time. | $91$ | combinations | `maxlength=20`  |
| 42 | [Permutations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/permutation.py) | Number of Permutations from $13$ objects picked $5$ at a time is:  | $154440$ | permutation | `maxlength=20`  |
| 52 | [Probability of a certain sum appearing on faces of dice](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/dice_sum_probability.py) | If $2$ dice are rolled at the same time, the probability of getting a sum of $8 =$ | \frac{5}{36} | dice_sum_probability | `maxDice=3`  |
| 54 | [Confidence interval For sample S](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/confidence_interval.py) | The confidence interval for sample $[296, 269, 223, 270, 279, 203, 225, 208, 212, 275, 259, 287, 258, 290, 243, 293, 246, 229, 295, 288, 292]$ with $80\%$ confidence is | $(267.70195663660877, 250.3932814586293)$ | confidence_interval | ``  |
| 59 | [Mean,Standard Deviation,Variance](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/data_summary.py) | Find the mean,standard deviation and variance for the data $5, 35, 49, 36, 47, 25, 47, 44, 24, 35, 13, 12, 13, 33, 50$ | The Mean is $31.2$, Standard Deviation is $213.0933333333333$, Variance is $14.597716716436626$ | data_summary | `number_values=15` `minval=5` `maxval=50`  |
| 76 | [Mean and Median](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/mean_median.py) | Given the series of numbers $[9, 13, 25, 28, 39, 46, 57, 80, 85, 91]$. Find the arithmatic mean and mdian of the series | Arithmetic mean of the series is $47.3$ and Arithmetic median of this series is $42.5$ | mean_median | `maxlen=10`  |
| 107 | [Conditional Probability](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/conditional_probability.py) | Someone tested positive for a nasty disease which only $0.95\%$ of the population have. Test sensitivity (true positive) is equal to $SN=97.64\%$ whereas test specificity (true negative) $SP=91.94\%$. What is the probability that this guy really has that disease? | $10.41\%$ | conditional_probability | ``  |
