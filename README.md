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
| 11 | [Basic Algebra](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/basic_algebra.py) | $5x + 5 = 9$ | $4/5$ | basic_algebra | `maxVariable=10`  |
| 12 | [Logarithm](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/log.py) | $log_{2}(128)=$ | $7$ | log | `maxBase=3` `maxVal=8`  |
| 17 | [Integer Multiplication with 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_int_to_22_matrix.py) | $10 * \begin{bmatrix} 2 & 10 \\ 5 & 1 \end{bmatrix} =$ | $\begin{bmatrix} 20 & 100 \\ 50 & 10 \end{bmatrix}$ | multiply_int_to_22_matrix | `maxMatrixVal=10` `maxRes=100`  |
| 20 | [Midpoint of the two point](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/midpoint_of_two_points.py) | The midpoint of $(-20,-14)$ and $(-6,7) = $ | $(-13.0,-3.5)$ | midpoint_of_two_points | `maxValue=20`  |
| 21 | [Factoring Quadratic](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/factoring.py) | $x^2+18x+80$ | $(x+10)(x+8)$ | factoring | `range_x1=10` `range_x2=10`  |
| 23 | [Solve a System of Equations in R^2](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/system_of_equations.py) | Given $7x + 6y = 26$ and $-8x + 5y = -6$, solve for $x$ and $y$. | $x = 2$, $y = 2$ | system_of_equations | `range_x=10` `range_y=10` `coeff_mult_range=10`  |
| 24 | [Distance between 2 points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/distance_two_points.py) | Find the distance between $(2, 13)$ and $(12, 9)$ | $\sqrt{116}$ | distance_two_points | `maxValXY=20` `minValXY=-20`  |
| 26 | [Linear Equations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/linear_equations.py) | Given the equations $-18x + 3y = -195$ and $-3x + -18y = -384$, solve for $x$ and $y$ | $x = 14$, $y = 19$ | linear_equations | `n=2` `varRange=20` `coeffRange=20`  |
| 41 | [Intersection of Two Lines](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/intersection_of_two_lines.py) | Find the point of intersection of the two lines: $y = -x + 9$ and $y = -10/6x - 10$ | $(-57/2, 75/2)$ | intersection_of_two_lines | `minM=-10` `maxM=10` `minB=-10` `maxB=10` `minDenominator=1` `maxDenominator=6`  |
| 43 | [Cross Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_cross.py) | [-9, 14, 16] X [-14, -7, -5] =  | [42, -269, 259] | vector_cross | `minVal=-20` `maxVal=20`  |
| 45 | [Simple Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/simple_interest.py) | Simple interest for a principle amount of $9259$ dollars, $10\%$ rate of interest and for a time period of $3$ years is $=$  | $2777.7$ | simple_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 46 | [Multiplication of two matrices](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/matrix_multiplication.py) | Multiply<table><tr><td>-1</td><td>-2</td><td>-2</td><td>3</td></tr><tr><td>-1</td><td>-3</td><td>7</td><td>-6</td></tr><tr><td>6</td><td>-10</td><td>-3</td><td>-3</td></tr><tr><td>-4</td><td>-10</td><td>1</td><td>-10</td></tr></table>and<table><tr><td>-2</td><td>3</td><td>-5</td><td>-1</td></tr><tr><td>0</td><td>2</td><td>4</td><td>10</td></tr><tr><td>1</td><td>10</td><td>-9</td><td>0</td></tr><tr><td>-2</td><td>0</td><td>3</td><td>-9</td></tr></table> | <table><tr><td>-6</td><td>-27</td><td>24</td><td>-46</td></tr><tr><td>21</td><td>61</td><td>-88</td><td>25</td></tr><tr><td>-9</td><td>-32</td><td>-52</td><td>-79</td></tr><tr><td>29</td><td>-22</td><td>-59</td><td>-6</td></tr></table> | matrix_multiplication | `maxVal=100` `max_dim=10`  |
| 50 | [Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/quadratic_equation.py) | What are the zeros of the quadratic equation $9x^2+126x+38=0$ | ${-0.31, -13.69}$ | quadratic_equation | `maxVal=100`  |
| 65 | [Multiplication of 2 complex numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_complex_numbers.py) | $(5+9j) * (-14-5j) = $ | $(-25-151j)$ | multiply_complex_numbers | `minRealImaginaryNum=-20` `maxRealImaginaryNum=20`  |
| 72 | [Dot Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_dot.py) | $[13, -5, -19]\cdot[12, 20, 4]=$ | $-20$ | vector_dot | `minVal=-20` `maxVal=20`  |
| 74 | [Inverse of a Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/invert_matrix.py) | Matrix([[75, 21, 61], [88, 37, 79], [3, 52, 44]]) | Matrix([[-248/1003, 1124/5015, -299/5015], [-727/2006, 3117/10030, -557/10030], [893/2006, -3837/10030, 927/10030]]) | invert_matrix | `SquareMatrixDimension=3` `MaxMatrixElement=99` `OnlyIntegerElementsInInvertedMatrix=False`  |
| 77 | [Determinant to 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/int_matrix_22_determinant.py) | $\det \begin{bmatrix} 28 & 45 \\ 37 & 22 \end{bmatrix} = $ | $-1049$ | int_matrix_22_determinant | `maxMatrixVal=100`  |
| 78 | [Compound Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/compound_interest.py) | Compound interest for a principle amount of $7869$ dollars, $4\%$ rate of interest and for a time period of $6$ years is $=$ | $9956.8$ | compound_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 100 | [complex Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/complex_quadratic.py) | Find the roots of given Quadratic Equation $2x^2 + 5x + 1 = 0$ | $((-0.219, -2.281)) = ((-5 + \sqrt17)/2*2, (-5 - \sqrt17)/2*2)$ | complex_quadratic | `prob_type=0` `max_range=10`  |
| 105 | [Combine Like terms](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/combine_like_terms.py) | $2x^{6} + 5x^{12} + 3x^{1} + 5x^{3} + 9x^{8} + 9x^{13} + 1x^{10} + 8x^{19}$ | $3x^{1} + 5x^{3} + 2x^{6} + 9x^{8} + 1x^{10} + 5x^{12} + 9x^{13} + 8x^{19}$ | combine_like_terms | `maxCoef=10` `maxExp=20` `maxTerms=10`  |
| 111 | [Expanding Factored Binomial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/expanding.py) | $(-3x-5)(-8x-3)$ | $24x^2+49x+15$ | expanding | `range_x1=10` `range_x2=10` `range_a=10` `range_b=10`  |
## basic_math
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 0 | [Addition](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/addition.py) | $39+37=$ | $76$ | addition | `maxSum=99` `maxAddend=50`  |
| 1 | [Subtraction](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/subtraction.py) | $65-64=$ | $1$ | subtraction | `maxMinuend=99` `maxDiff=99`  |
| 2 | [Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/multiplication.py) | $6\cdot2$ | $12$ | multiplication | `maxMulti=12`  |
| 3 | [Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/division.py) | $25\div25=$ | $1$ | division | `maxA=25` `maxB=25`  |
| 6 | [Square Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square_root.py) | $\sqrt{25}=$ | $5$ | square_root | `minNo=1` `maxNo=12`  |
| 8 | [Square](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square.py) | $5^2=$ | $25$ | square | `maxSquareNum=20`  |
| 13 | [Fraction to Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/fraction_to_decimal.py) | $60\div11=$ | $5.45$ | fraction_to_decimal | `maxRes=99` `maxDivid=99`  |
| 16 | [Fraction Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/divide_fractions.py) | $\frac{6}{10}\div\frac{2}{9}=$ | $\frac{27}{10}$ | divide_fractions | `maxVal=10`  |
| 28 | [Fraction Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/fraction_multiplication.py) | $\frac{2}{6}\cdot\frac{3}{6}=$ | $\frac{1}{6}$ | fraction_multiplication | `maxVal=10`  |
| 31 | [Factorial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/factorial.py) | $2! =$ | $2$ | factorial | `maxInput=6`  |
| 44 | [Compare Fractions](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/compare_fractions.py) | Which symbol represents the comparison between $\frac{10}{7}$ and $\frac{2}{4}$? | > | compare_fractions | `maxVal=10`  |
| 47 | [Cube Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/cube_root.py) | What is the cube root of: $\sqrt[3]{724}=$ to 2 decimal places? | $8.98$ | cube_root | `minNo=1` `maxNo=1000`  |
| 53 | [Exponentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/exponentiation.py) | $2^6 =$ | $64$ | exponentiation | `maxBase=20` `maxExpo=10`  |
| 71 | [Absolute difference between two numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/absolute_difference.py) | $|-51-59|=$ | $110$ | absolute_difference | `maxA=100` `maxB=100`  |
| 80 | [Percentage of a number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage.py) | What is $86\%$ of $71$? | $61.06$ | percentage | `maxValue=99` `maxpercentage=99`  |
| 90 | [isprime](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/is_prime.py) | Is $27$ prime? | No | is_prime | `max_num=100`  |
| 97 | [Power of Powers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/power_of_powers.py) | Simplify $6^{2^{1}}$ | $6^{2}$ | power_of_powers | `maxBase=50` `maxPower=10`  |
| 118 | [Percentage difference](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage_difference.py) | What is the percentage difference between $111$ and $89$? | $22.0\%$ | percentage_difference | `maxValue=200` `minValue=0`  |
| 119 | [Percentage error](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage_error.py) | Find the percentage error when observed value equals $-69$ and exact value equals $-50$. | $38.0\%$ | percentage_error | `maxValue=100` `minValue=-100`  |
| 120 | [Greatest Common Divisor of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/greatest_common_divisor.py) | $GCD(439148129,463956861)=$ | $1$ | greatest_common_divisor | `numbersCount=2` `maximalNumberLimit=10**9`  |
| 124 | [Is Composite](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/is_composite.py) | Is $175$ composite? | Yes | is_composite | `maxNum=250`  |
## calculus
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 7 | [Power Rule Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_differentiation.py) | $6x^{8} + 1x^{5} + 1x^{4} + 2x^{10} + 7x^{5}$ | $48x^{7} + 5x^{4} + 4x^{3} + 20x^{9} + 35x^{4}$ | power_rule_differentiation | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 48 | [Power Rule Integration](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_integration.py) | $10x^{1} + 6x^{7} + 2x^{1} + 5x^{6}$ | $\frac{10}{1}x^{2} + \frac{6}{7}x^{8} + \frac{2}{1}x^{2} + \frac{5}{6}x^{7} + C$ | power_rule_integration | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 88 | [Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/differentiation.py) | differentiate w.r.t x : d(cos(x)+6*x^(-3))/dx | -sin(x) - 18/x^4 | differentiation | `diff_lvl=2`  |
| 89 | [Definite Integral of Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/definite_integral.py) | The definite integral within limits $0$ to $1$ of the equation $20x^2 + 80x + 41 = $ | $87.6667$ | definite_integral | `max_coeff=100`  |
| 110 | [Stationary Points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/stationary_points.py) | f(x)=3*x^3 + 9*x^2 + x + 5 | (-1 - 2*sqrt(2)/3,3*(-1 - 2*sqrt(2)/3)**3 - 2*sqrt(2)/3 + 4 + 9*(-1 - 2*sqrt(2)/3)**2),(-1 + 2*sqrt(2)/3,3*(-1 + 2*sqrt(2)/3)**3 + 9*(-1 + 2*sqrt(2)/3)**2 + 2*sqrt(2)/3 + 4) | stationary_points | `maxExp=3` `maxCoef=10`  |
## computer_science
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 4 | [Binary Complement 1s](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_complement_1s.py) | $0 = $ | $1$ | binary_complement_1s | `maxDigits=10`  |
| 5 | [Modulo Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/modulo_division.py) | $80\%58=$ | $22$ | modulo_division | `maxRes=99` `maxModulo=99`  |
| 14 | [Decimal to Binary](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_binary.py) | Binary of $43 = $ | $101011$ | decimal_to_binary | `max_dec=99`  |
| 15 | [Binary to Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_decimal.py) | $0001101$ | $13$ | binary_to_decimal | `max_dig=10`  |
| 56 | [Fibonacci Series](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/fibonacci_series.py) | The Fibonacci Series of the first ${n}$ numbers is ? | $0, 1, 1, 2, 3, 5, 8, 13, 21$ | fibonacci_series | `minNo=1`  |
| 62 | [nth Fibonacci number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/nth_fibonacci_number.py) | What is the 26th Fibonacci number? | $121393$ | nth_fibonacci_number | `maxN=100`  |
| 64 | [Binary to Hexidecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_hex.py) | $001010$ | $0xa$ | binary_to_hex | `max_dig=10`  |
| 73 | [Binary 2's Complement](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_2s_complement.py) | 2's complement of $100010000 = $ | $11110000$ | binary_2s_complement | `maxDigits=10`  |
| 79 | [Decimal to Hexadecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_hexadeci.py) | Binary of $440 = $ | $0x1b8$ | decimal_to_hexadeci | `max_dec=1000`  |
| 84 | [Converts decimal to octal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_octal.py) | The decimal number ${x}$ in Octal is:  | $0o6567$ | decimal_to_octal | `maxDecimal=4096`  |
| 91 | [Binary Coded Decimal to Integer](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/bcd_to_decimal.py) | Integer of Binary Coded Decimal $4$ is $=$  | $16657$ | bcd_to_decimal | `maxNumber=10000`  |
| 103 | [Decimal to Binary Coded Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_bcd.py) | BCD of Decimal Number $3347 = $ | $1313$ | decimal_to_bcd | `maxNumber=10000`  |
## geometry
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 18 | [Area of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_triangle.py) | Area of triangle with side lengths: $12, 2 11 = $ | $9.92$ | area_of_triangle | `maxA=20` `maxB=20`  |
| 19 | [Triangle exists check](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/valid_triangle.py) | Does triangle with sides $5, 48$ and $39$ exist? | $No$ | valid_triangle | `maxSideLength=50`  |
| 22 | [Third Angle of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/third_angle_of_triangle.py) | Third angle of triangle with angles $26$ and $43 = $ | $111$ | third_angle_of_triangle | `maxAngle=89`  |
| 25 | [Pythagorean Theorem](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/pythagorean_theorem.py) | What is the hypotenuse of a right triangle given the other two sides have lengths $17$ and $19$? | $25.5$ | pythagorean_theorem | `maxLength=20`  |
| 29 | [Angle of a Regular Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_regular_polygon.py) | Find the angle of a regular polygon with $18$ sides | $160.0$ | angle_regular_polygon | `minVal=3` `maxVal=20`  |
| 32 | [Surface Area of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cube.py) | Surface area of cube with side $= 1m$ is | $6 m^2$ | surface_area_cube | `maxSide=20` `unit='m'`  |
| 33 | [Surface Area of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cuboid.py) | Surface area of cuboid with sides of lengths: $13m, 15m, 3m$ is | $558 m^2$ | surface_area_cuboid | `maxSide=20` `unit='m'`  |
| 34 | [Surface Area of Cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cylinder.py) | Surface area of cylinder with height $= 25m$ and radius $= 15m$ is | $3769 m^2$ | surface_area_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 35 | [Volume of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cube.py) | Volume of cube with a side length of $6m$ is | $216 m^3$ | volume_cube | `maxSide=20` `unit='m'`  |
| 36 | [Volume of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cuboid.py) | Volume of cuboid with sides = $11m, 13m, 11m$ is | $1573 m^3$ | volume_cuboid | `maxSide=20` `unit='m'`  |
| 37 | [Volume of cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cylinder.py) | Volume of cylinder with height $= 27m$ and radius $= 19m$ is | $30621 m^3$ | volume_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 38 | [Surface Area of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cone.py) | Surface area of cone with height $= 5m$ and radius $= 5m$ is | $189 m^2$ | surface_area_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 39 | [Volume of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cone.py) | Volume of cone with height $= 19m$ and radius $= 10m$ is | $1989 m^3$ | volume_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 49 | [Fourth Angle of Quadrilateral](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/fourth_angle_of_quadrilateral.py) | Fourth angle of quadrilateral with angles $14 , 29, 7 =$ | $310$ | fourth_angle_of_quadrilateral | `maxAngle=180`  |
| 57 | [Trigonometric Values](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/basic_trigonometry.py) | $\tan(45) = $ | $1$ | basic_trigonometry | `angles=[0, 30, 45, 60, 90]` `functions=['sin', 'cos', 'tan']`  |
| 58 | [Sum of Angles of Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sum_of_polygon_angles.py) | What is the sum of interior angles of a polygon with $5$ sides? | $540$ | sum_of_polygon_angles | `maxSides=12`  |
| 60 | [Surface Area of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_sphere.py) | Surface area of Sphere with radius $= 11m$ is | $1520.5308443374597 m^2$ | surface_area_sphere | `maxSide=20` `unit='m'`  |
| 61 | [Volume of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_sphere.py) | Volume of sphere with radius $57 m = $ | $775734.624395006 m^3$ | volume_sphere | `maxRadius=100`  |
| 70 | [Angle between 2 vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_btw_vectors.py) | angle between the vectors [643.19, 259.78, 952.37, 380.26] and [420.5, 283.5, 196.12, 606.17] is: | 0.71 radians | angle_btw_vectors | `maxEltAmt=20`  |
| 75 | [Area of a Sector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sector_area.py) | What is the area of a sector with radius $37$ and angle $315$ degrees? | $3763.24$ | sector_area | `maxRadius=49` `maxAngle=359`  |
| 86 | [Degrees to Radians](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/degree_to_rad.py) | Angle $275$ degrees in radians is:  | $4.8$ | degree_to_rad | `max_deg=360`  |
| 87 | [Radians to Degrees](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/radian_to_deg.py) | Angle $1.74$ radians in degrees is:  | $99.69$ | radian_to_deg | `max_rad=6.28`  |
| 95 | [Curved surface area of a cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/curved_surface_area_cylinder.py) | What is the curved surface area of a cylinder of radius, $37$ and height, $28$? | $6509.38$ | curved_surface_area_cylinder | `maxRadius=49` `maxHeight=99`  |
| 96 | [Perimeter of Polygons](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/perimeter_of_polygons.py) | The perimeter of a $8$ sided polygon with lengths of $54, 75, 12, 12, 103, 69, 102, 89$cm is:  | $516$ | perimeter_of_polygons | `maxSides=12` `maxLength=120`  |
| 104 | [Circumference](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/circumference.py) | Circumference of circle with radius $26 = $ | $163.36$ | circumference | `maxRadius=100`  |
| 108 | [Arc length of Angle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/arc_length.py) | Given radius, $27$ and angle, $199$. Find the arc length of the angle. | Arc length of the angle $= 93.77654$ | arc_length | `maxRadius=49` `maxAngle=359`  |
| 112 | [Area of Circle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_circle.py) | Area of circle with radius $94=$ | $27759.11$ | area_of_circle | `maxRadius=100`  |
| 113 | [Volume of frustum](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_frustum.py) | Volume of frustum with height $= 23m$ and $r1 = 6m$ is and $r2 = 6m$ is  | $9345.0 m^3$ | volume_frustum | `maxR1=20` `maxR2=20` `maxHeight=50` `unit='m'`  |
| 114 | [Equation of line from two points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/equation_of_line_from_two_points.py) | What is the equation of the line between points $(-5,-18)$ and $(16,13)$ in slope-intercept form? | $21y = 31x -223$ | equation_of_line_from_two_points | `maxCoordinate=20` `minCoordinate=-20`  |
| 115 | [Area of Circle given center and a point on circle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_circle_given_center_and_point.py) | Area of circle with center $(0,3)$ and passing through $(6.0, 3.0)$ is | $113.1$ | area_of_circle_given_center_and_point | `maxCoordinate = 10` `maxRadius=10`  |
| 117 | [Volume of Hemisphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_hemisphere.py) | Volume of hemisphere with radius $89 m =$  | $1476483.621 m^3$ | volume_hemisphere | `maxRadius=100`  |
| 122 | [Volume of pyramid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_pyramid.py) | Volume of pyramid with base length $= 7 m$, base width $= 20 m$ and height $= 4 m$ is | $186.66666666666666 m^3$ | volume_pyramid | `maxLength=20` `maxWidth=20` `maxHeight=50` `unit='m'`  |
| 123 | [Surface area of pyramid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_pyramid.py) | Surface area of pyramid with base length $= 48m$, base width $= 50m$, and height $= 7m$ is | $4800 m^2$ | surface_area_pyramid | `unit='m'`  |
| 125 | [Complementary and Supplementary Angle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/complementary_and_supplementary_angle.py) | The complementary angle of 83 = | 7 | complementary_and_supplementary_angle | `maxSupp=180` `maxComp=90`  |
## misc
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 9 | [LCM (Least Common Multiple)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/lcm.py) | LCM of $20$ and $9 =$ | $180$ | lcm | `maxVal=20`  |
| 10 | [GCD (Greatest Common Denominator)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/gcd.py) | GCD of $1$ and $2 = $ | $1$ | gcd | `maxVal=20`  |
| 27 | [Prime Factorisation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/prime_factors.py) | Find prime factors of $188$ | $2, 2, 47$ | prime_factors | `minVal=1` `maxVal=200`  |
| 40 | [Common Factors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/common_factors.py) | Common Factors of $50$ and $71 = $ | $[1]$ | common_factors | `maxVal=100`  |
| 51 | [HCF (Highest Common Factor)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/hcf.py) | HCF of $9$ and $19 = $ | $1$ | hcf | `maxVal=20`  |
| 55 | [Comparing surds](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/surds_comparison.py) | Fill in the blanks $82^{\frac{1}{9}}$ _ $60^{\frac{1}{2}}$ | $<$ | surds_comparison | `maxValue=100` `maxRoot=10`  |
| 63 | [Profit or Loss Percent](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/profit_loss_percent.py) | Loss percent when $CP = 573$ and $SP = 490$ is:  | $14.49$ | profit_loss_percent | `maxCP=1000` `maxSP=1000`  |
| 66 | [Geometric Progression](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_progression.py) | For the given GP $[6, 36, 216, 1296, 7776, 46656]$. Find the value of a common ratio, 7th term value, sum upto 10th term | The value of a is $6$, common ratio is $6$ , 7th term is $279936$, sum upto 10th term is $72559410.0$ | geometric_progression | `number_values=6` `min_value=2` `max_value=12` `n_term=7` `sum_term=5`  |
| 67 | [Geometric Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_mean.py) | Geometric mean of $3$ numbers $[70, 72, 21] = $ | $47.3$ | geometric_mean | `maxValue=100` `maxCount=4`  |
| 68 | [Harmonic Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/harmonic_mean.py) | Harmonic mean of $3$ numbers $49, 4, 85 = $ | $301.23378004679853$ | harmonic_mean | `maxValue=100` `maxNum=4`  |
| 69 | [Euclidian norm or L2 norm of a vector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/euclidian_norm.py) | Euclidian norm or L2 norm of the vector $[117.31516249702779, 262.01806085974454, 44.88100548767482, 609.28084889853, 765.1967626542811, 307.84248657065285, 4.047638406152632, 193.0976614019312]$ is: | $1083.17$ | euclidian_norm | `maxEltAmt=20`  |
| 81 | [Celsius To Fahrenheit](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/celsius_to_fahrenheit.py) | Convert $-19$ degrees Celsius to degrees Fahrenheit | $-2.200000000000003$ | celsius_to_fahrenheit | `maxTemp=100`  |
| 82 | [AP Term Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_term.py) | Find term number $49$ of the AP series: $74, 105, 136 ... $ | $1562$ | arithmetic_progression_term | `maxd=100` `maxa=100` `maxn=100`  |
| 83 | [AP Sum Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_sum.py) | Find the sum of first $17$ terms of the AP series: $-34, -64, -94 ... $ | $-4658.0$ | arithmetic_progression_sum | `maxd=100` `maxa=100` `maxn=100`  |
| 85 | [Converts decimal to Roman Numerals](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/decimal_to_roman_numerals.py) | The number $0$ in Roman Numerals is:  | $MMDV$ | decimal_to_roman_numerals | `maxDecimal=4000`  |
| 92 | [Complex To Polar Form](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/complex_to_polar.py) | $21.19(7.0\theta + i20.0\theta)$ | $1.23$ | complex_to_polar | `minRealImaginaryNum=-20, maxRealImaginaryNum=20`  |
| 93 | [Union,Intersection,Difference of Two Sets](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/set_operation.py) | Given the two sets $a={8, 1, 10, 3}$, $b={3, 6, 7, 8, 9}. Find the Union, intersection, a-b, b-a, and symmetric difference | Union is ${1, 3, 6, 7, 8, 9, 10}$. Intersection is ${8, 3}$, a-b is ${1, 10}$, b-a is ${9, 6, 7}$. Symmetric difference is ${1, 6, 7, 9, 10}$. | set_operation | `minval=3` `maxval=7` `n_a=4` `n_b=5`  |
| 94 | [Base Conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/base_conversion.py) | Convert $13230112$ from base $4$ to base $2$. | $111101100010110$ | base_conversion | `maxNum=60000` `maxBase=16`  |
| 98 | [Quotient of Powers with Same Base](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_base.py) | The Quotient of $2^{10}$ and $2^{1} = $2^{10-1} = 2^{9}$ | $512$ | quotient_of_power_same_base | `maxBase=50` `maxPower=10`  |
| 99 | [Quotient of Powers with Same Power](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_power.py) | The Quotient of $10^{8}$ and $17^{8} = (10/17)^8 = 0.5882352941176471^{8}$ | $0.014335360832968509$ | quotient_of_power_same_power | `maxBase=50` `maxPower=10`  |
| 101 | [Leap Year or Not](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/is_leap_year.py) | Is 1992 a leap year? | 1992 is a leap year | is_leap_year | `minNumber=1900` `maxNumber=2099`  |
| 102 | [Minute to Hour conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/minutes_to_hours.py) | Convert $199$ minutes to hours & minutes | $3$ hours and $19$ minutes | minutes_to_hours | `maxMinutes=999`  |
| 106 | [signum function](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/signum_function.py) | signum of 865 is = | $1$ | signum_function | `min=-999` `max=999`  |
| 109 | [Binomial distribution](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/binomial_distribution.py) | A manufacturer of metal pistons finds that, on average, $34.87\%$ of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of $20$ pistons will contain no more than $6$ rejected pistons? | $42.14$ | binomial_distribution | ``  |
| 116 | [Factors of a number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/factors.py) | Factors of $722 = $ | $[1, 2, 19, 38, 361, 722]$ | factors | `maxVal=1000`  |
| 121 | [Product of scientific notations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/product_of_scientific_notations.py) | Product of scientific notations $5.08x10^-97 and 3.36x10^-89 = $ | 1.71x10^-185 | product_of_scientific_notations | `minExpVal=-100` `maxExpVal=100`  |
## statistics
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 30 | [Combinations of Objects](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/combinations.py) | Find the number of combinations from $20$ objects picked $7$ at a time. | $77520$ | combinations | `maxlength=20`  |
| 42 | [Permutations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/permutation.py) | Number of Permutations from $18$ objects picked $8$ at a time is:  | $1764322560$ | permutation | `maxlength=20`  |
| 52 | [Probability of a certain sum appearing on faces of dice](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/dice_sum_probability.py) | If $2$ dice are rolled at the same time, the probability of getting a sum of $11 =$ | \frac{2}{36} | dice_sum_probability | `maxDice=3`  |
| 54 | [Confidence interval For sample S](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/confidence_interval.py) | The confidence interval for sample $[205, 244, 246, 240, 221, 281, 212, 219, 241, 267, 232, 287, 290, 295, 283, 231, 251, 239, 271, 224, 275, 253, 242]$ with $90\%$ confidence is | $(258.84910938137114, 241.06393409688974)$ | confidence_interval | ``  |
| 59 | [Mean,Standard Deviation,Variance](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/data_summary.py) | Find the mean,standard deviation and variance for the data $16, 21, 26, 35, 49, 48, 49, 20, 9, 44, 49, 15, 40, 41, 50$ | The Mean is $34.13333333333333$, Standard Deviation is $203.4488888888889$, Variance is $14.263551061670753$ | data_summary | `number_values=15` `minval=5` `maxval=50`  |
| 76 | [Mean and Median](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/mean_median.py) | Given the series of numbers $[3, 14, 48, 51, 52, 54, 56, 69, 84, 86]$. Find the arithmatic mean and mdian of the series | Arithmetic mean of the series is $51.7$ and Arithmetic median of this series is $53.0$ | mean_median | `maxlen=10`  |
| 107 | [Conditional Probability](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/conditional_probability.py) | Someone tested positive for a nasty disease which only $1.33\%$ of the population have. Test sensitivity (true positive) is equal to $SN=97.96\%$ whereas test specificity (true negative) $SP=99.08\%$. What is the probability that this guy really has that disease? | $58.94\%$ | conditional_probability | ``  |
