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
| 0 | Addition | 32+29= | 61 | addition |
| 1 | Subtraction | 45-12= | 33 | subtraction |
| 2 | Multiplication | 25*3= | 75 | multiplication |
| 3 | Division | 32/95= | 0.3368421052631579 | division |
| 4 | Binary Complement 1s | 11= | 00 | binary_complement_1s |
| 5 | Modulo Division | 22%45= | 22 | modulo_division |
| 6 | Square Root | sqrt(144)= | 12 | square_root |
| 7 | Power Rule Differentiation | 3x^1 | 3x^0 | power_rule_differentiation |
| 8 | Square | 2^2= | 4 | square |
| 9 | LCM (Least Common Multiple) | LCM of 5 and 18 = | 90 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 16 and 16 =  | 16 | gcd |
| 11 | Basic Algebra | 8x + 2 = 5 | 3/8 | basic_algebra |
| 12 | Logarithm | log2(128) | 7 | log |
| 13 | Easy Division | 525/25 =  | 21 | int_division |
| 14 | Decimal to Binary | Binary of 39= | 100111 | decimal_to_binary |
| 15 | Binary to Decimal | 01110 | 14 | binary_to_decimal |
| 16 | Fraction Division | (9/4)/(8/4) | 9/8 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 7 * [[3, 3], [9, 2]] =  | [[21,21],[63,14]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 18 7 5 =  | (3.67394039744206e-15+60j) | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 31, 49 and 15 exist? | No | valid_triangle |
| 20 | Midpoint of the two point | (7,-13),(-11,-20)= | (-2.0,-16.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+15x+56 | (x+7)(x+8) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 68 and 72 =  | 40 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -x - 8y = 57, -7x - 7y = 56 | x = -1, y = -7 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-18, -4) and (20, -1) | sqrt(1453) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 14 and 16 =  | 21.26 | pythagorean_theorem |
| 26 | Linear Equations | -8x + 9y = -159, 4x + -7y = 97 | x = 12, y = -7 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 22 | [2, 11] | prime_factors |
| 28 | Fraction Multiplication | (5/9)*(3/8) | 5/24 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 20 sides | 162.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 20 objects picked 0 at a time  | 1 | combinations |
| 31 | Factorial | 4! =  | 24 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 13m is | 1014 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 4m, 3m, 10m is | 164 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 30m and radius = 3m is | 622 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 3m is | 27 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 18m, 4m, 20m is | 1440 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 8m and radius = 2m is | 100 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 9m and radius = 18m is | 2155 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 8m and radius = 12m is | 1206 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 94 and 86 =  | [1, 2] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 0/2x - 2 and y = 10/3x - 4 | (3/5, -2) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 11 objects picked 4 at a time =   | 7920 | permutation |
| 43 | Cross Product of 2 Vectors | [-19, -10, -19] X [-8, -15, 19] =  | [-475, 513, 205] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 8/5 and 4/5? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 1700 dollars, 9% rate of interest and for a time period of 2 years is =  | 306.0 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>7</td><td>-8</td></tr><tr><td>-2</td><td>-2</td></tr><tr><td>5</td><td>-9</td></tr><tr><td>7</td><td>-8</td></tr></table>and<table><tr><td>-10</td><td>-2</td><td>2</td></tr><tr><td>3</td><td>-4</td><td>8</td></tr></table> | <table><tr><td>-94</td><td>18</td><td>-50</td></tr><tr><td>14</td><td>12</td><td>-20</td></tr><tr><td>-77</td><td>26</td><td>-62</td></tr><tr><td>-94</td><td>18</td><td>-50</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 273 upto 2 decimal places is: | 6.49 | cube_root |
| 48 | Power Rule Integration | 3x^5 + 10x^6 + 2x^7 + 2x^9 | (3/5)x^6 + (10/6)x^7 + (2/7)x^8 + (2/9)x^10 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 29 , 193, 28 = | 110 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 51x^2+196x+10=0 | [-0.05, -3.79] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 1 and 13 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 2 dice are rolled at the same time, the probability of getting a sum of 7 = | 6/36 | dice_sum_probability |
| 53 | Exponentiation | 14^5 = | 537824 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [286, 254, 294, 290, 235, 252, 297, 262, 238, 281, 248, 275, 282, 293, 232, 233, 288, 236, 250, 242, 241, 261] with 90% confidence is | (270.2008805103011, 254.34457403515344) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 59^(1/5) _ 34^(1/7) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 14 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233] | fibonacci_series |
| 57 | Trigonometric Values | What is sin(60)? | √3/2 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 6 sides =  | 720 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[46, 12, 41, 13, 40, 14, 21, 24, 5, 43, 34, 19, 9, 18, 39] | The Mean is 25.2 , Standard Deviation is 180.96000000000004, Variance is 13.452137376640191 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 11m is | 1520.5308443374597 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 54 m =  | 659583.6608064842 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 21th Fibonacci number? | 10946 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Loss percent when CP = 294 and SP = 163 is:  | 44.5578231292517 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 010111 | 0x17 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (-15+4j) * (3-8j) =  | (-13+132j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [8, 80, 800, 8000, 80000, 800000] ,Find the value of a,common ratio,11th term value, sum upto 8th term | The value of a is 8, common ratio is 10 , 11th term is 80000000000 , sum upto 8th term is 88888888.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 3 numbers 89 , 18 and 50 =  | (89*18*50)^(1/3) = 43.10663994756918 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 3 numbers 13 , 30 and 40 =  |  3/((1/13) + (1/30) + (1/40)) = 22.18009478672986 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[190.83139432733142, 156.23278912186944] is: | 246.62786837199073 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [424.56, 424.72, 189.19, 78.27, 930.38, 707.61, 196.98, 629.23, 637.74, 251.83, 563.31, 309.15, 811.91, 214.04, 20.86, 802.15, 948.67] and [645.19, 932.88, 213.39, 818.73, 24.01, 671.44, 845.54, 599.61, 791.14, 497.84, 67.99, 29.82, 499.55, 391.4, 546.58, 881.0, 953.93] is: | 0.7 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -93 and 0 =  | 93 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [12, -15, -11] . [11, -18, -17] =  | 589 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 1111 = | 1 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[2, 17, 3], [31, 0, 5], [37, 67, 73]]) is: | Matrix([[67/5953, 208/5953, -17/5953], [2078/29765, -7/5953, -83/29765], [-2077/29765, -99/5953, 527/29765]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 42 and angle, 224. Find the area of the sector. | Area of sector = 3448.21210 | sector_area |
| 76 | Mean and Median | Given the series of numbers [1, 14, 41, 75, 22, 95, 21, 80, 24, 19]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 39.2 and Arithmetic median of this series is 23.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[53, 75], [30, 7]]) =  |  -1879 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 8512 dollars, 10% rate of interest and for a time period of 8 year is =  | 18246.23 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 172= | 0xac | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 73% of 19? | Required percentage = 13.87% | percentage |
| 81 | Celsius To Fahrenheit | Convert 81 degrees Celsius to degrees Fahrenheit = | 177.8 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 53 of the AP series: 75, -14, -103 ...  | -4553 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 5 terms of the AP series: -77, -14, 49 ...  | 245.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 1 in Octal is:  | 0o1 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 2667 in Roman Numerals is:  | MMDCLXVII | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 217 in radians is =  | 3.79 | degree_to_rad |
| 87 | Radians to Degrees | Angle 1 in degrees is =  | 57.3 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(exp(x)+7*x^3)/dx | 21*x^2 + exp(x) | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 61x^2 + 82x + 10 is =  | 71.3333 | definite_integral |
| 90 | isprime | 86 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 4 is =  | 18310 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 24.04exp(i-0.79) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={9, 10, 3, 4} ,b={1, 3, 9}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 3, 4, 9, 10},Intersection is {9, 3}, a-b is {10, 4},b-a is {1}, Symmetric difference is {1, 4, 10} | set_operation |
| 94 | Base Conversion | Convert 30246 from base 9 to base 10. | 19887 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 5 and height, 87? | CSA of cylinder = 2733.19 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 11 sided polygon with lengths of [28, 13, 90, 99, 27, 61, 7, 7, 68, 80, 28]cm is:  | 508 | perimeter_of_polygons |
| 97 | Power of Powers | The 17^4^2 = 17^(4*2) = 17^8 | 6975757441 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 50^10 and 50^7 = 50^(10-7) = 50^3 | 125000 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 7^1 and 40^1 = (7/40)^1 = 0.175^1 | 0.175 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation 3x^2 + 9x + 1 = 0 | simplified solution : ((-0.116, -2.884)), generalized solution : ((-9 + sqrt(69))/2*3, (-9 - sqrt(69))/2*3) | complex_quadratic |
| 101 | Leap Year or Not | Year 2078  | is not a leap year | is_leap_year |
| 102 | Minute to Hour conversion | Convert 562 minutes to Hours & Minutes | 9 hours and 22 minutes | minutes_to_hours |
| 103 | Decimal to Binary Coded Decimal | BCD of Decimal Number 5293 is =  | 141013 | decimal_to_bcd |
| 104 | Circumference | Circumference of circle with radius 60 | 376.99111843077515 | circumference |
| 105 | Combine Like terms | 4x^4 + 6x^4 + 9x^1 + 3x^1 + 5x^4 + 10x^3 | 12x^1 + 10x^3 + 15x^4  | combine_like_terms |
| 105 | Conditional Probability | Someone tested positive for a nasty disease which only 1.34% of population have. Test sensitivity (true positive) is equal to SN= 98.05% whereas test specificity (true negative) SP= 92.32%. What is the probability that this guy really has that disease? | 14.78% | conditional_probability |
