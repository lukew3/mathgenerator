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
| 11 | [Basic Algebra](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/basic_algebra.py) | $6x + 1 = 6$ | $5/6$ | basic_algebra | `maxVariable=10`  |
| 12 | [Logarithm](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/log.py) | $log_{3}(729)=$ | $6$ | log | `maxBase=3` `maxVal=8`  |
| 17 | [Integer Multiplication with 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_int_to_22_matrix.py) | $10 * \begin{bmatrix} 4 & 3 \\ 1 & 6 \end{bmatrix} =$ | $\begin{bmatrix} 40 & 30 \\ 10 & 60 \end{bmatrix}$ | multiply_int_to_22_matrix | `maxMatrixVal=10` `maxRes=100`  |
| 20 | [Midpoint of the two point](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/midpoint_of_two_points.py) | The midpoint of $(15,4)$ and $(3,-12) = $ | $(9.0,-4.0)$ | midpoint_of_two_points | `maxValue=20`  |
| 21 | [Factoring Quadratic](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/factoring.py) | $x^2+11x+18$ | $(x+9)(x+2)$ | factoring | `range_x1=10` `range_x2=10`  |
| 23 | [Solve a System of Equations in R^2](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/system_of_equations.py) | Given $y = -6$ and $7x - 8y = 48$, solve for $x$ and $y$. | $x = 0$, $y = -6$ | system_of_equations | `range_x=10` `range_y=10` `coeff_mult_range=10`  |
| 24 | [Distance between 2 points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/distance_two_points.py) | Find the distance between $(20, 18)$ and $(-13, 14)$ | $\sqrt{1105}$ | distance_two_points | `maxValXY=20` `minValXY=-20`  |
| 26 | [Linear Equations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/linear_equations.py) | Given the equations $2x + -6y = 0$ and $17x + -18y = 0$, solve for $x$ and $y$ | $x = 0$, $y = 0$ | linear_equations | `n=2` `varRange=20` `coeffRange=20`  |
| 41 | [Intersection of Two Lines](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/intersection_of_two_lines.py) | Find the point of intersection of the two lines: $y = -6$ and $y = 5x - 2$ | $(-4/5, -6)$ | intersection_of_two_lines | `minM=-10` `maxM=10` `minB=-10` `maxB=10` `minDenominator=1` `maxDenominator=6`  |
| 43 | [Cross Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_cross.py) | [10, 9, -1] X [7, -18, 3] =  | [9, -37, -243] | vector_cross | `minVal=-20` `maxVal=20`  |
| 45 | [Simple Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/simple_interest.py) | Simple interest for a principle amount of $4467$ dollars, $2\%$ rate of interest and for a time period of $1$ years is $=$  | $89.34$ | simple_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 46 | [Multiplication of two matrices](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/matrix_multiplication.py) | Multiply<table><tr><td>-6</td><td>4</td></tr><tr><td>1</td><td>9</td></tr><tr><td>-8</td><td>9</td></tr><tr><td>-2</td><td>7</td></tr></table>and<table><tr><td>-4</td><td>-9</td><td>10</td><td>5</td></tr><tr><td>3</td><td>-2</td><td>1</td><td>-1</td></tr></table> | <table><tr><td>36</td><td>46</td><td>-56</td><td>-34</td></tr><tr><td>23</td><td>-27</td><td>19</td><td>-4</td></tr><tr><td>59</td><td>54</td><td>-71</td><td>-49</td></tr><tr><td>29</td><td>4</td><td>-13</td><td>-17</td></tr></table> | matrix_multiplication | `maxVal=100` `max_dim=10`  |
| 50 | [Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/quadratic_equation.py) | What are the zeros of the quadratic equation $49x^2+184x+20=0$ | ${-0.11, -3.64}$ | quadratic_equation | `maxVal=100`  |
| 65 | [Multiplication of 2 complex numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/multiply_complex_numbers.py) | $(4-7j) * (19+0j) = $ | $(76-133j)$ | multiply_complex_numbers | `minRealImaginaryNum=-20` `maxRealImaginaryNum=20`  |
| 72 | [Dot Product of 2 Vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/vector_dot.py) | $[-3, 17, -5]\cdot[-13, 16, 11]=$ | $256$ | vector_dot | `minVal=-20` `maxVal=20`  |
| 74 | [Inverse of a Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/invert_matrix.py) | Matrix([[85, 2, 68], [73, 59, 16], [19, 64, 63]]) | Matrix([[2693/461783, 4226/461783, -3980/461783], [-4295/461783, 4063/461783, 3604/461783], [3551/461783, -5402/461783, 4869/461783]]) | invert_matrix | `SquareMatrixDimension=3` `MaxMatrixElement=99` `OnlyIntegerElementsInInvertedMatrix=False`  |
| 77 | [Determinant to 2x2 Matrix](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/int_matrix_22_determinant.py) | $\det \begin{bmatrix} 20 & 39 \\ 41 & 72 \end{bmatrix} = $ | $-159$ | int_matrix_22_determinant | `maxMatrixVal=100`  |
| 78 | [Compound Interest](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/compound_interest.py) | Compound interest for a principle amount of $3680$ dollars, $2\%$ rate of interest and for a time period of $7$ years is $=$ | $4227.16$ | compound_interest | `maxPrinciple=10000` `maxRate=10` `maxTime=10`  |
| 100 | [complex Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/complex_quadratic.py) | Find the roots of given Quadratic Equation $x^2 + 6x + 5 = 0$ | $((-1.0, -5.0)) = ((-6 + 4)/2*1, (-6 - 4)/2*1)$ | complex_quadratic | `prob_type=0` `max_range=10`  |
| 105 | [Combine Like terms](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/combine_like_terms.py) | $10x^{3} + 6x^{5} + 8x^{9} + 9x^{19} + 4x^{9} + 1x^{9} + 7x^{16}$ | $10x^{3} + 6x^{5} + 13x^{9} + 7x^{16} + 9x^{19}$ | combine_like_terms | `maxCoef=10` `maxExp=20` `maxTerms=10`  |
| 111 | [Expanding Factored Binomial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/algebra/expanding.py) | $(-2x+6)(x+5)$ | $-2x^2-4x+30$ | expanding | `range_x1=10` `range_x2=10` `range_a=10` `range_b=10`  |
## basic_math
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 0 | [Addition](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/addition.py) | $12+34=$ | $46$ | addition | `maxSum=99` `maxAddend=50`  |
| 1 | [Subtraction](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/subtraction.py) | $67-34=$ | $33$ | subtraction | `maxMinuend=99` `maxDiff=99`  |
| 2 | [Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/multiplication.py) | $2\cdot3$ | $6$ | multiplication | `maxMulti=12`  |
| 3 | [Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/division.py) | $80\div10=$ | $8$ | division | `maxA=25` `maxB=25`  |
| 6 | [Square Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square_root.py) | $\sqrt{16}=$ | $4$ | square_root | `minNo=1` `maxNo=12`  |
| 8 | [Square](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/square.py) | $10^2=$ | $100$ | square | `maxSquareNum=20`  |
| 13 | [Fraction to Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/fraction_to_decimal.py) | $35\div24=$ | $1.46$ | fraction_to_decimal | `maxRes=99` `maxDivid=99`  |
| 16 | [Fraction Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/divide_fractions.py) | $\frac{8}{4}\div\frac{8}{4}=$ | $\frac{1}{1}$ | divide_fractions | `maxVal=10`  |
| 28 | [Fraction Multiplication](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/fraction_multiplication.py) | $\frac{1}{2}\cdot\frac{6}{8}=$ | $\frac{3}{8}$ | fraction_multiplication | `maxVal=10`  |
| 31 | [Factorial](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/factorial.py) | $3! =$ | $6$ | factorial | `maxInput=6`  |
| 44 | [Compare Fractions](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/compare_fractions.py) | Which symbol represents the comparison between $\frac{7}{1}$ and $\frac{8}{3}$? | > | compare_fractions | `maxVal=10`  |
| 47 | [Cube Root](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/cube_root.py) | What is the cube root of: $\sqrt[3]{687}=$ to 2 decimal places? | $8.82$ | cube_root | `minNo=1` `maxNo=1000`  |
| 53 | [Exponentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/exponentiation.py) | $18^9 =$ | $198359290368$ | exponentiation | `maxBase=20` `maxExpo=10`  |
| 71 | [Absolute difference between two numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/absolute_difference.py) | $|15--35|=$ | $50$ | absolute_difference | `maxA=100` `maxB=100`  |
| 80 | [Percentage of a number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage.py) | What is $82\%$ of $11$? | $9.02$ | percentage | `maxValue=99` `maxpercentage=99`  |
| 90 | [isprime](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/is_prime.py) | Is $26$ prime? | No | is_prime | `max_num=100`  |
| 97 | [Power of Powers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/power_of_powers.py) | Simplify $6^{1^{3}}$ | $6^{3}$ | power_of_powers | `maxBase=50` `maxPower=10`  |
| 118 | [Percentage difference](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage_difference.py) | What is the percentage difference between $65$ and $14$? | $129.11\%$ | percentage_difference | `maxValue=200` `minValue=0`  |
| 119 | [Percentage error](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/percentage_error.py) | Find the percentage error when observed value equals $-35$ and exact value equals $-45$. | $22.22\%$ | percentage_error | `maxValue=100` `minValue=-100`  |
| 120 | [Greatest Common Divisor of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/greatest_common_divisor.py) | $GCD(83094356,401226719)=$ | $1$ | greatest_common_divisor | `numbersCount=2` `maximalNumberLimit=10**9`  |
| 124 | [Is Composite](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/is_composite.py) | Is $144$ composite? | Yes | is_composite | `maxNum=250`  |
## calculus
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 7 | [Power Rule Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_differentiation.py) | $7x^{2} + 9x^{5}$ | $14x^{1} + 45x^{4}$ | power_rule_differentiation | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 48 | [Power Rule Integration](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/power_rule_integration.py) | $1x^{10}$ | $\frac{1}{10}x^{11} + C$ | power_rule_integration | `maxCoef=10` `maxExp=10` `maxTerms=5`  |
| 88 | [Differentiation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/differentiation.py) | differentiate w.r.t x : d(ln(x)+2*x^2)/dx | 4*x + 1/x | differentiation | `diff_lvl=2`  |
| 89 | [Definite Integral of Quadratic Equation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/definite_integral.py) | The definite integral within limits $0$ to $1$ of the equation $66x^2 + 97x + 44 = $ | $114.5$ | definite_integral | `max_coeff=100`  |
| 110 | [Stationary Points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/calculus/stationary_points.py) | f(x)=3*x^3 + 8*x^2 + 4*x + 3 | (-8/9 - 2*sqrt(7)/9,3*(-8/9 - 2*sqrt(7)/9)**3 - 8*sqrt(7)/9 - 5/9 + 8*(-8/9 - 2*sqrt(7)/9)**2),(-8/9 + 2*sqrt(7)/9,-5/9 + 3*(-8/9 + 2*sqrt(7)/9)**3 + 8*(-8/9 + 2*sqrt(7)/9)**2 + 8*sqrt(7)/9) | stationary_points | `maxExp=3` `maxCoef=10`  |
## computer_science
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 4 | [Binary Complement 1s](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_complement_1s.py) | $0000 = $ | $1111$ | binary_complement_1s | `maxDigits=10`  |
| 5 | [Modulo Division](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/modulo_division.py) | $60\%17=$ | $9$ | modulo_division | `maxRes=99` `maxModulo=99`  |
| 14 | [Decimal to Binary](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_binary.py) | Binary of $86 = $ | $1010110$ | decimal_to_binary | `max_dec=99`  |
| 15 | [Binary to Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_decimal.py) | $1000100$ | $68$ | binary_to_decimal | `max_dig=10`  |
| 56 | [Fibonacci Series](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/fibonacci_series.py) | The Fibonacci Series of the first ${n}$ numbers is ? | $0, 1, 1, 2, 3, 5, 8, 13, 21, 34$ | fibonacci_series | `minNo=1`  |
| 62 | [nth Fibonacci number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/nth_fibonacci_number.py) | What is the 22th Fibonacci number? | $17711$ | nth_fibonacci_number | `maxN=100`  |
| 64 | [Binary to Hexidecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_to_hex.py) | $00$ | $0x0$ | binary_to_hex | `max_dig=10`  |
| 73 | [Binary 2's Complement](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/binary_2s_complement.py) | 2's complement of $101110 = $ | $10010$ | binary_2s_complement | `maxDigits=10`  |
| 79 | [Decimal to Hexadecimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_hexadeci.py) | Binary of $576 = $ | $0x240$ | decimal_to_hexadeci | `max_dec=1000`  |
| 84 | [Converts decimal to octal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_octal.py) | The decimal number ${x}$ in Octal is:  | $0o3225$ | decimal_to_octal | `maxDecimal=4096`  |
| 91 | [Binary Coded Decimal to Integer](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/bcd_to_decimal.py) | Integer of Binary Coded Decimal $8$ is $=$  | $33810$ | bcd_to_decimal | `maxNumber=10000`  |
| 103 | [Decimal to Binary Coded Decimal](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/computer_science/decimal_to_bcd.py) | BCD of Decimal Number $3264 = $ | $12120$ | decimal_to_bcd | `maxNumber=10000`  |
## geometry
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 18 | [Area of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_triangle.py) | Area of triangle with side lengths: $14, 7 11 = $ | $37.95$ | area_of_triangle | `maxA=20` `maxB=20`  |
| 19 | [Triangle exists check](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/valid_triangle.py) | Does triangle with sides $29, 30$ and $11$ exist? | $Yes$ | valid_triangle | `maxSideLength=50`  |
| 22 | [Third Angle of Triangle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/third_angle_of_triangle.py) | Third angle of triangle with angles $16$ and $43 = $ | $121$ | third_angle_of_triangle | `maxAngle=89`  |
| 25 | [Pythagorean Theorem](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/pythagorean_theorem.py) | What is the hypotenuse of a right triangle given the other two sides have lengths $12$ and $13$? | $17.69$ | pythagorean_theorem | `maxLength=20`  |
| 29 | [Angle of a Regular Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_regular_polygon.py) | Find the angle of a regular polygon with $5$ sides | $108.0$ | angle_regular_polygon | `minVal=3` `maxVal=20`  |
| 32 | [Surface Area of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cube.py) | Surface area of cube with side $= 6m$ is | $216 m^2$ | surface_area_cube | `maxSide=20` `unit='m'`  |
| 33 | [Surface Area of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cuboid.py) | Surface area of cuboid with sides of lengths: $4m, 20m, 7m$ is | $496 m^2$ | surface_area_cuboid | `maxSide=20` `unit='m'`  |
| 34 | [Surface Area of Cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cylinder.py) | Surface area of cylinder with height $= 34m$ and radius $= 19m$ is | $6327 m^2$ | surface_area_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 35 | [Volume of Cube](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cube.py) | Volume of cube with a side length of $8m$ is | $512 m^3$ | volume_cube | `maxSide=20` `unit='m'`  |
| 36 | [Volume of Cuboid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cuboid.py) | Volume of cuboid with sides = $14m, 4m, 1m$ is | $56 m^3$ | volume_cuboid | `maxSide=20` `unit='m'`  |
| 37 | [Volume of cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cylinder.py) | Volume of cylinder with height $= 41m$ and radius $= 6m$ is | $4636 m^3$ | volume_cylinder | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 38 | [Surface Area of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_cone.py) | Surface area of cone with height $= 12m$ and radius $= 10m$ is | $804 m^2$ | surface_area_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 39 | [Volume of cone](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_cone.py) | Volume of cone with height $= 1m$ and radius $= 10m$ is | $104 m^3$ | volume_cone | `maxRadius=20` `maxHeight=50` `unit='m'`  |
| 49 | [Fourth Angle of Quadrilateral](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/fourth_angle_of_quadrilateral.py) | Fourth angle of quadrilateral with angles $72 , 104, 68 =$ | $116$ | fourth_angle_of_quadrilateral | `maxAngle=180`  |
| 57 | [Trigonometric Values](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/basic_trigonometry.py) | $\cos(0) = $ | $1$ | basic_trigonometry | `angles=[0, 30, 45, 60, 90]` `functions=['sin', 'cos', 'tan']`  |
| 58 | [Sum of Angles of Polygon](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sum_of_polygon_angles.py) | What is the sum of interior angles of a polygon with $9$ sides? | $1260$ | sum_of_polygon_angles | `maxSides=12`  |
| 60 | [Surface Area of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_sphere.py) | Surface area of Sphere with radius $= 8m$ is | $804.247719318987 m^2$ | surface_area_sphere | `maxSide=20` `unit='m'`  |
| 61 | [Volume of Sphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_sphere.py) | Volume of sphere with radius $55 m = $ | $696909.9703213357 m^3$ | volume_sphere | `maxRadius=100`  |
| 70 | [Angle between 2 vectors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/angle_btw_vectors.py) | angle between the vectors [224.37, 875.67, 135.57, 610.18, 921.96, 699.28, 506.1, 638.65, 914.89] and [405.18, 763.73, 473.01, 5.7, 832.49, 269.44, 291.37, 819.14, 964.31] is: | 0.46 radians | angle_btw_vectors | `maxEltAmt=20`  |
| 75 | [Area of a Sector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/sector_area.py) | What is the area of a sector with radius $6$ and angle $216$ degrees? | $67.86$ | sector_area | `maxRadius=49` `maxAngle=359`  |
| 86 | [Degrees to Radians](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/degree_to_rad.py) | Angle $324$ degrees in radians is:  | $5.65$ | degree_to_rad | `max_deg=360`  |
| 87 | [Radians to Degrees](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/radian_to_deg.py) | Angle $1.33$ radians in degrees is:  | $76.2$ | radian_to_deg | `max_rad=6.28`  |
| 95 | [Curved surface area of a cylinder](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/curved_surface_area_cylinder.py) | What is the curved surface area of a cylinder of radius, $35$ and height, $54$? | $11875.22$ | curved_surface_area_cylinder | `maxRadius=49` `maxHeight=99`  |
| 96 | [Perimeter of Polygons](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/perimeter_of_polygons.py) | The perimeter of a $11$ sided polygon with lengths of $27, 48, 8, 24, 98, 72, 59, 81, 36, 28, 15$cm is:  | $496$ | perimeter_of_polygons | `maxSides=12` `maxLength=120`  |
| 104 | [Circumference](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/circumference.py) | Circumference of circle with radius $56 = $ | $351.86$ | circumference | `maxRadius=100`  |
| 108 | [Arc length of Angle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/arc_length.py) | Given radius, $8$ and angle, $81$. Find the arc length of the angle. | Arc length of the angle $= 11.30973$ | arc_length | `maxRadius=49` `maxAngle=359`  |
| 112 | [Area of Circle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_circle.py) | Area of circle with radius $85=$ | $22698.01$ | area_of_circle | `maxRadius=100`  |
| 113 | [Volume of frustum](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_frustum.py) | Volume of frustum with height $= 3m$ and $r1 = 19m$ is and $r2 = 19m$ is  | $1812.0 m^3$ | volume_frustum | `maxR1=20` `maxR2=20` `maxHeight=50` `unit='m'`  |
| 114 | [Equation of line from two points](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/equation_of_line_from_two_points.py) | What is the equation of the line between points $(12,-20)$ and $(-2,-4)$ in slope-intercept form? | $7y = -8x -44$ | equation_of_line_from_two_points | `maxCoordinate=20` `minCoordinate=-20`  |
| 115 | [Area of Circle given center and a point on circle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/area_of_circle_given_center_and_point.py) | Area of circle with center $(4,4)$ and passing through $(11.0, 4.0)$ is | $153.94$ | area_of_circle_given_center_and_point | `maxCoordinate = 10` `maxRadius=10`  |
| 117 | [Volume of Hemisphere](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_hemisphere.py) | Volume of hemisphere with radius $89 m =$  | $1476483.621 m^3$ | volume_hemisphere | `maxRadius=100`  |
| 122 | [Volume of pyramid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/volume_pyramid.py) | Volume of pyramid with base length $= 8 m$, base width $= 11 m$ and height $= 35 m$ is | $1026.6666666666667 m^3$ | volume_pyramid | `maxLength=20` `maxWidth=20` `maxHeight=50` `unit='m'`  |
| 123 | [Surface area of pyramid](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/surface_area_pyramid.py) | Surface area of pyramid with base length $= 50m$, base width $= 52m$, and height $= 24m$ is | $3470 m^2$ | surface_area_pyramid | `unit='m'`  |
| 125 | [Complementary and Supplementary Angle](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/geometry/complementary_and_supplementary_angle.py) | The complementary angle of 68 = | 22 | complementary_and_supplementary_angle | `maxSupp=180` `maxComp=90`  |
## misc
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 9 | [LCM (Least Common Multiple)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/lcm.py) | LCM of $15$ and $19 =$ | $285$ | lcm | `maxVal=20`  |
| 10 | [GCD (Greatest Common Denominator)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/gcd.py) | GCD of $2$ and $2 = $ | $2$ | gcd | `maxVal=20`  |
| 27 | [Prime Factorisation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/prime_factors.py) | Find prime factors of $132$ | $2, 2, 3, 11$ | prime_factors | `minVal=1` `maxVal=200`  |
| 40 | [Common Factors](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/common_factors.py) | Common Factors of $80$ and $4 = $ | $[1, 2, 4]$ | common_factors | `maxVal=100`  |
| 51 | [HCF (Highest Common Factor)](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/hcf.py) | HCF of $7$ and $17 = $ | $1$ | hcf | `maxVal=20`  |
| 55 | [Comparing surds](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/surds_comparison.py) | Fill in the blanks $6^{\frac{1}{4}}$ _ $10^{\frac{1}{5}}$ | $<$ | surds_comparison | `maxValue=100` `maxRoot=10`  |
| 63 | [Profit or Loss Percent](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/profit_loss_percent.py) | Loss percent when $CP = 303$ and $SP = 19$ is:  | $93.73$ | profit_loss_percent | `maxCP=1000` `maxSP=1000`  |
| 66 | [Geometric Progression](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_progression.py) | For the given GP $[5, 20, 80, 320, 1280, 5120]$. Find the value of a common ratio, 7th term value, sum upto 7th term | The value of a is $5$, common ratio is $4$ , 7th term is $20480$, sum upto 7th term is $27305.0$ | geometric_progression | `number_values=6` `min_value=2` `max_value=12` `n_term=7` `sum_term=5`  |
| 67 | [Geometric Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/geometric_mean.py) | Geometric mean of $4$ numbers $[18, 39, 72, 6] = $ | $23.47$ | geometric_mean | `maxValue=100` `maxCount=4`  |
| 68 | [Harmonic Mean of N Numbers](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/harmonic_mean.py) | Harmonic mean of $3$ numbers $15, 34, 26 = $ | $193.2511210762332$ | harmonic_mean | `maxValue=100` `maxNum=4`  |
| 69 | [Euclidian norm or L2 norm of a vector](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/euclidian_norm.py) | Euclidian norm or L2 norm of the vector $[707.3039128984115, 289.7482249838592, 880.2106417010565, 934.7563224402314, 668.6549490324835, 250.29551451076594, 174.2832869932438, 2.7724671577435966, 733.050450436363, 776.0934444874142, 549.7300412830676, 426.8456692933408, 84.68197219390916, 692.7894483818749, 413.1097082090539, 800.9658687264597, 198.37108268887172, 79.24179244496443]$ is: | $2396.24$ | euclidian_norm | `maxEltAmt=20`  |
| 81 | [Celsius To Fahrenheit](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/celsius_to_fahrenheit.py) | Convert $35$ degrees Celsius to degrees Fahrenheit | $95.0$ | celsius_to_fahrenheit | `maxTemp=100`  |
| 82 | [AP Term Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_term.py) | Find term number $34$ of the AP series: $91, 90, 89 ... $ | $58$ | arithmetic_progression_term | `maxd=100` `maxa=100` `maxn=100`  |
| 83 | [AP Sum Calculation](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/arithmetic_progression_sum.py) | Find the sum of first $21$ terms of the AP series: $-48, -27, -6 ... $ | $3402.0$ | arithmetic_progression_sum | `maxd=100` `maxa=100` `maxn=100`  |
| 85 | [Converts decimal to Roman Numerals](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/decimal_to_roman_numerals.py) | The number $0$ in Roman Numerals is:  | $MMDCCCX$ | decimal_to_roman_numerals | `maxDecimal=4000`  |
| 92 | [Complex To Polar Form](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/complex_to_polar.py) | $6.0(0.0\theta + i-6.0\theta)$ | $-1.57$ | complex_to_polar | `minRealImaginaryNum=-20, maxRealImaginaryNum=20`  |
| 93 | [Union,Intersection,Difference of Two Sets](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/set_operation.py) | Given the two sets $a={8, 9, 5, 6}$, $b={8, 2, 10, 5}. Find the Union, intersection, a-b, b-a, and symmetric difference | Union is ${2, 5, 6, 8, 9, 10}$. Intersection is ${8, 5}$, a-b is ${9, 6}$, b-a is ${2, 10}$. Symmetric difference is ${2, 6, 9, 10}$. | set_operation | `minval=3` `maxval=7` `n_a=4` `n_b=5`  |
| 94 | [Base Conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/base_conversion.py) | Convert $54774$ from base $10$ to base $2$. | $1101010111110110$ | base_conversion | `maxNum=60000` `maxBase=16`  |
| 98 | [Quotient of Powers with Same Base](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_base.py) | The Quotient of $10^{9}$ and $10^{6} = $10^{9-6} = 10^{3}$ | $1000$ | quotient_of_power_same_base | `maxBase=50` `maxPower=10`  |
| 99 | [Quotient of Powers with Same Power](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/quotient_of_power_same_power.py) | The Quotient of $37^{8}$ and $42^{8} = (37/42)^8 = 0.8809523809523809^{8}$ | $0.3627600635880677$ | quotient_of_power_same_power | `maxBase=50` `maxPower=10`  |
| 101 | [Leap Year or Not](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/is_leap_year.py) | Is 2088 a leap year? | 2088 is a leap year | is_leap_year | `minNumber=1900` `maxNumber=2099`  |
| 102 | [Minute to Hour conversion](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/minutes_to_hours.py) | Convert $458$ minutes to hours & minutes | $7$ hours and $38$ minutes | minutes_to_hours | `maxMinutes=999`  |
| 106 | [signum function](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/signum_function.py) | signum of 508 is = | $1$ | signum_function | `min=-999` `max=999`  |
| 109 | [Binomial distribution](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/binomial_distribution.py) | A manufacturer of metal pistons finds that, on average, $36.87\%$ of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of $10$ pistons will contain no more than $9$ rejected pistons? | $100.0$ | binomial_distribution | ``  |
| 116 | [Factors of a number](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/factors.py) | Factors of $978 = $ | $[1, 2, 3, 6, 163, 326, 489, 978]$ | factors | `maxVal=1000`  |
| 121 | [Product of scientific notations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/misc/product_of_scientific_notations.py) | Product of scientific notations $3.87x10^-83 and 5.98x10^-19 = $ | 2.31x10^-101 | product_of_scientific_notations | `minExpVal=-100` `maxExpVal=100`  |
## statistics
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
| 30 | [Combinations of Objects](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/combinations.py) | Find the number of combinations from $20$ objects picked $4$ at a time. | $4845$ | combinations | `maxlength=20`  |
| 42 | [Permutations](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/permutation.py) | Number of Permutations from $17$ objects picked $6$ at a time is:  | $8910720$ | permutation | `maxlength=20`  |
| 52 | [Probability of a certain sum appearing on faces of dice](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/dice_sum_probability.py) | If $3$ dice are rolled at the same time, the probability of getting a sum of $8 =$ | \frac{21}{216} | dice_sum_probability | `maxDice=3`  |
| 54 | [Confidence interval For sample S](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/confidence_interval.py) | The confidence interval for sample $[235, 283, 218, 248, 275, 253, 208, 279, 259, 234, 256, 217, 270, 286, 290, 245, 207, 247, 211, 241, 261, 274]$ with $80\%$ confidence is | $(256.8855824298169, 242.8416902974558)$ | confidence_interval | ``  |
| 59 | [Mean,Standard Deviation,Variance](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/data_summary.py) | Find the mean,standard deviation and variance for the data $20, 41, 22, 26, 24, 35, 12, 20, 19, 29, 41, 44, 38, 18, 31$ | The Mean is $28.0$, Standard Deviation is $91.6$, Variance is $9.57078889120432$ | data_summary | `number_values=15` `minval=5` `maxval=50`  |
| 76 | [Mean and Median](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/mean_median.py) | Given the series of numbers $[29, 39, 44, 58, 62, 74, 75, 76, 79, 95]$. Find the arithmatic mean and mdian of the series | Arithmetic mean of the series is $63.1$ and Arithmetic median of this series is $68.0$ | mean_median | `maxlen=10`  |
| 107 | [Conditional Probability](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/statistics/conditional_probability.py) | Someone tested positive for a nasty disease which only $0.85\%$ of the population have. Test sensitivity (true positive) is equal to $SN=91.10\%$ whereas test specificity (true negative) $SP=94.34\%$. What is the probability that this guy really has that disease? | $12.13\%$ | conditional_probability | ``  |
