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
| 0 | Addition | 7+40= | 47 | addition |
| 1 | Subtraction | 52-51= | 1 | subtraction |
| 2 | Multiplication | 3*21= | 63 | multiplication |
| 3 | Division | 46/50= | 0.92 | division |
| 4 | Binary Complement 1s | 1011= | 0100 | binary_complement_1s |
| 5 | Modulo Division | 17%78= | 17 | modulo_division |
| 6 | Square Root | sqrt(36)= | 6 | square_root |
| 7 | Power Rule Differentiation | 8x^8 + 1x^4 | 64x^7 + 4x^3 | power_rule_differentiation |
| 8 | Square | 14^2= | 196 | square |
| 9 | LCM (Least Common Multiple) | LCM of 10 and 17 = | 170 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 8 and 8 =  | 8 | gcd |
| 11 | Basic Algebra | 1x + 2 = 3 | 1 | basic_algebra |
| 12 | Logarithm | log3(9) | 2 | log |
| 13 | Easy Division | 17/1 =  | 17 | int_division |
| 14 | Decimal to Binary | Binary of 23= | 10111 | decimal_to_binary |
| 15 | Binary to Decimal | 100 | 4 | binary_to_decimal |
| 16 | Fraction Division | (10/1)/(2/7) | 35 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 1 * [[8, 4], [9, 3]] =  | [[8,4],[9,3]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 16 5 7 =  | (2.5717582782094417e-15+42j) | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 13, 45 and 45 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (17,11),(7,9)= | (12.0,10.0) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2-1x-6 | (x+2)(x-3) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 20 and 30 =  | 130 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | 9x - 9y = -54, 4x + 9y = -11 | x = -5, y = 1 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (21, 19) and (16, -5) | sqrt(601) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 20 and 19 =  | 27.59 | pythagorean_theorem |
| 26 | Linear Equations | -3x + -4y = -23, 20x + -8y = -540 | x = -19, y = 20 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 77 | [7, 11] | prime_factors |
| 28 | Fraction Multiplication | (10/6)*(1/8) | 5/24 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 15 sides | 156.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 11 objects picked 8 at a time  | 165 | combinations |
| 31 | Factorial | 4! =  | 24 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 8m is | 384 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 4m, 4m, 3m is | 80 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 47m and radius = 3m is | 942 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 10m is | 1000 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 6m, 7m, 11m is | 462 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 41m and radius = 12m is | 18547 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 11m and radius = 9m is | 656 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 50m and radius = 18m is | 16964 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 6 and 51 =  | [1, 3] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 2x + 7 and y = -8/2x - 1 | (-4/3, 13/3) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 18 objects picked 3 at a time =   | 4896 | permutation |
| 43 | Cross Product of 2 Vectors | [-18, 10, 2] X [-13, 16, 16] =  | [128, 262, -158] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 9/5 and 10/7? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 7207 dollars, 3% rate of interest and for a time period of 7 years is =  | 1513.47 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>-1</td><td>-3</td></tr><tr><td>8</td><td>4</td></tr><tr><td>-9</td><td>0</td></tr><tr><td>-5</td><td>-7</td></tr></table>and<table><tr><td>4</td><td>-9</td><td>10</td><td>7</td></tr><tr><td>-8</td><td>5</td><td>-3</td><td>-5</td></tr></table> | <table><tr><td>20</td><td>-6</td><td>-1</td><td>8</td></tr><tr><td>0</td><td>-52</td><td>68</td><td>36</td></tr><tr><td>-36</td><td>81</td><td>-90</td><td>-63</td></tr><tr><td>36</td><td>10</td><td>-29</td><td>0</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 388 upto 2 decimal places is: | 7.29 | cube_root |
| 48 | Power Rule Integration | 7x^5 + 2x^8 | (7/5)x^6 + (2/8)x^9 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 133 , 16, 122 = | 89 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 14x^2+149x+5=0 | [-0.03, -10.61] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 15 and 3 =  | 3 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 3 dice are rolled at the same time, the probability of getting a sum of 7 = | 15/216 | dice_sum_probability |
| 53 | Exponentiation | 13^3 = | 2197 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [205, 274, 277, 258, 211, 242, 213, 228, 253, 294, 276, 210, 247, 229, 206, 204, 290, 231, 208, 264, 243, 267, 215, 282, 216, 233, 251, 203, 292, 278, 226] with 99% confidence is | (256.4847632648058, 229.06362383196844) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 9^(1/9) _ 85^(1/2) | < | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 20 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181] | fibonacci_series |
| 57 | Trigonometric Values | What is sin(45)? | 1/√2 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 9 sides =  | 1260 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[27, 42, 37, 26, 30, 22, 32, 7, 36, 15, 6, 10, 17, 16, 12] | The Mean is 22.333333333333332 , Standard Deviation is 123.95555555555556, Variance is 11.133532932342526 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 13m is | 2123.7166338267 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 4 m =  | 268.082573106329 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 15th Fibonacci number? | 610 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 291 and SP = 468 is:  | 60.824742268041234 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 0010 | 0x2 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (19+1j) * (10+19j) =  | (171+371j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [4, 12, 36, 108, 324, 972] ,Find the value of a,common ratio,7th term value, sum upto 6th term | The value of a is 4, common ratio is 3 , 7th term is 2916 , sum upto 6th term is 1456.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 38 , 66 , 80 , 24 =  | (38*66*80*24)^(1/4) = 46.84434709254888 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 4 numbers 19 , 3 , 94 , 47 =  |  4/((1/19) + (1/3) + (1/94) + (1/47)) = 9.572130415364002 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[88.65597674656611, 513.1160127304324] is: | 520.7186617870201 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [247.81, 715.31, 324.88, 189.51, 331.72, 625.64, 723.42] and [393.64, 599.63, 109.53, 333.49, 979.47, 489.72, 878.62] is: | 0.48 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 30 and 30 =  | 0 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [10, -6, 8] . [12, 4, 18] =  | 240 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 1101100 = | 10100 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[56, 89, 27], [19, 5, 14], [3, 80, 35]]) is: | Matrix([[135/9676, 955/67732, -1111/67732], [89/9676, -1879/67732, 271/67732], [-215/9676, 4213/67732, 1411/67732]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 22 and angle, 249. Find the area of the sector. | Area of sector = 1051.70050 | sector_area |
| 76 | Mean and Median | Given the series of numbers [3, 97, 58, 14, 19, 54, 29, 24, 25, 91]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 41.4 and Arithmetic median of this series is 27.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[19, 45], [76, 73]]) =  |  -2033 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 4831 dollars, 4% rate of interest and for a time period of 9 year is =  | 6876.02 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 180= | 0xb4 | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 11% of 69? | Required percentage = 7.59% | percentage |
| 81 | Celsius To Fahrenheit | Convert 95 degrees Celsius to degrees Fahrenheit = | 203.0 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 40 of the AP series: 79, 113, 147 ...  | 1405 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 81 terms of the AP series: 68, -9, -86 ...  | -243972.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 2985 in Octal is:  | 0o5651 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 1752 in Roman Numerals is:  | MDCCLII | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 206 in radians is =  | 3.6 | degree_to_rad |
| 87 | Radians to Degrees | Angle 0 in degrees is =  | 0.0 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(cot(x)+4*x^(-3))/dx | -cot(x)^2 - 1 - 12/x^4 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 43x^2 + 13x + 29 is =  | 49.8333 | definite_integral |
| 90 | isprime | 86 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 5 is =  | 21620 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 22.47exp(i-2.58) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={9, 3, 1, 6} ,b={2, 4, 5, 9, 10}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 2, 3, 4, 5, 6, 9, 10},Intersection is {9}, a-b is {1, 3, 6},b-a is {2, 10, 4, 5}, Symmetric difference is {1, 2, 3, 4, 5, 6, 10} | set_operation |
| 94 | Base Conversion | Convert 111122000 from base 3 to base 16. | 26D0 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 9 and height, 34? | CSA of cylinder = 1922.65 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 3 sided polygon with lengths of [4, 30, 88]cm is:  | 122 | perimeter_of_polygons |
| 97 | Power of Powers | The 20^3^7 = 20^(3*7) = 20^21 | 2097152000000000000000000000 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 10^7 and 10^3 = 10^(7-3) = 10^4 | 10000 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 30^1 and 40^1 = (30/40)^1 = 0.75^1 | 0.75 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation 2x^2 + 7x + 1 = 0 | simplified solution : ((-0.149, -3.351)), generalized solution : ((-7 + sqrt(41))/2*2, (-7 - sqrt(41))/2*2) | complex_quadratic |
| 101 | Leap Year or Not | Year 1972  | is a leap year | is_leap_year |
| 102 | Minute to Hour conversion | Convert 908 minutes to Hours & Minutes | 15 hours and 8 minutes | minutes_to_hours |
| 103 | Decimal to Binary Coded Decimal | BCD of Decimal Number 3603 is =  | 1413 | decimal_to_bcd |
