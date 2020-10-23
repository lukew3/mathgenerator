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
| 0 | Addition | 6+34= | 40 | addition |
| 1 | Subtraction | 66-1= | 65 | subtraction |
| 2 | Multiplication | 69*1= | 69 | multiplication |
| 3 | Division | 19/52= | 0.36538461538461536 | division |
| 4 | Binary Complement 1s | 10000= | 01111 | binary_complement_1s |
| 5 | Modulo Division | 79%84= | 79 | modulo_division |
| 6 | Square Root | sqrt(64)= | 8 | square_root |
| 7 | Power Rule Differentiation | 2x^8 + 6x^2 + 10x^7 | 16x^7 + 12x^1 + 70x^6 | power_rule_differentiation |
| 8 | Square | 18^2= | 324 | square |
| 9 | LCM (Least Common Multiple) | LCM of 1 and 14 = | 14 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 5 and 7 =  | 1 | gcd |
| 11 | Basic Algebra | 8x + 1 = 9 | 8 | basic_algebra |
| 12 | Logarithm | log2(32) | 5 | log |
| 13 | Easy Division | 165/11 =  | 15 | int_division |
| 14 | Decimal to Binary | Binary of 95= | 1011111 | decimal_to_binary |
| 15 | Binary to Decimal | 1111001000 | 968 | binary_to_decimal |
| 16 | Fraction Division | (3/8)/(1/3) | 9/8 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 11 * [[9, 6], [9, 9]] =  | [[99,66],[99,99]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 2 3 9 =  | (1.0246130234694952e-15+16.73320053068151j) | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 15, 24 and 22 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (8,-11),(8,-6)= | (8.0,-8.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+7x+10 | (x+5)(x+2) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 53 and 11 =  | 116 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -8x - 2y = 78, -8x + 3y = 63 | x = -9, y = -3 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-9, -20) and (17, -19) | sqrt(677) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 17 and 10 =  | 19.72 | pythagorean_theorem |
| 26 | Linear Equations | 20x + -5y = -240, -8x + -9y = -36 | x = -9, y = 12 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 60 | [2, 2, 3, 5] | prime_factors |
| 28 | Fraction Multiplication | (10/8)*(2/8) | 5/16 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 4 sides | 90.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 10 objects picked 1 at a time  | 10 | combinations |
| 31 | Factorial | 3! =  | 6 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 5m is | 150 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 20m, 2m, 4m is | 256 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 4m and radius = 6m is | 376 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 20m is | 8000 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 10m, 6m, 17m is | 1020 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 50m and radius = 14m is | 30787 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 9m and radius = 5m is | 240 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 26m and radius = 9m is | 2205 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 85 and 23 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -8/2x + 6 and y = -7/5x + 5 | (5/13, 58/13) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 18 objects picked 9 at a time =   | 17643225600 | permutation |
| 43 | Cross Product of 2 Vectors | [-9, -11, -7] X [-6, -14, 4] =  | [-142, 78, 60] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 9/1 and 9/4? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 6270 dollars, 4% rate of interest and for a time period of 8 years is =  | 2006.4 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>8</td><td>-4</td><td>1</td></tr><tr><td>2</td><td>2</td><td>-1</td></tr></table>and<table><tr><td>3</td><td>-5</td><td>-4</td></tr><tr><td>2</td><td>-10</td><td>-7</td></tr><tr><td>8</td><td>-8</td><td>7</td></tr></table> | <table><tr><td>24</td><td>-8</td><td>3</td></tr><tr><td>2</td><td>-22</td><td>-29</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 462 upto 2 decimal places is: | 7.73 | cube_root |
| 48 | Power Rule Integration | 3x^5 | (3/5)x^6 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 173 , 63, 34 = | 90 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 64x^2+175x+26=0 | [-0.16, -2.58] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 15 and 3 =  | 3 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 3 dice are rolled at the same time, the probability of getting a sum of 13 = | 21/216 | dice_sum_probability |
| 53 | Exponentiation | 11^9 = | 2357947691 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [234, 272, 289, 255, 291, 219, 225, 282, 266, 288, 259, 269, 275, 260, 262, 250, 270, 241, 287, 294, 200, 210, 298, 273] with 90% confidence is | (270.221486487058, 252.19518017960863) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 22^(1/2) _ 74^(1/6) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 14 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233] | fibonacci_series |
| 57 | Trigonometric Values | What is sin(90)? | 1 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 12 sides =  | 1800 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[29, 50, 21, 44, 44, 17, 34, 47, 7, 10, 26, 7, 6, 49, 21] | The Mean is 27.466666666666665 , Standard Deviation is 249.5822222222222, Variance is 15.798171483504735 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 8m is | 804.247719318987 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 80 m =  | 2144660.584850632 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 4th Fibonacci number? | 3 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 37 and SP = 447 is:  | 1108.1081081081081 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 01100001 | 0x61 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (17+7j) * (7+14j) =  | (21+287j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [12, 60, 300, 1500, 7500, 37500] ,Find the value of a,common ratio,8th term value, sum upto 6th term | The value of a is 12, common ratio is 5 , 8th term is 937500 , sum upto 6th term is 46872.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 2 numbers 46 and 20 =  | (46*20)^(1/2) = 30.331501776206203 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 35 and 3 =  |  2/((1/35) + (1/3)) = 5.526315789473684 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[653.9717397584312, 689.1069921882294, 19.887404949723187, 17.33889409833278, 762.6266577725075, 189.70375690805275, 673.7332899787874] is: | 1405.2569550674714 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [638.9, 178.91, 936.86, 859.08, 27.18, 730.15, 513.96, 244.4, 698.55] and [546.02, 51.57, 631.8, 932.17, 558.58, 598.42, 537.63, 334.25, 289.47] is: | 0.43 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -98 and 73 =  | 171 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [11, -12, -15] . [1, -1, 3] =  | -22 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 1 = | 1 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[75, 30, 13], [5, 89, 16], [74, 48, 59]]) is: | Matrix([[4483/280397, -1146/280397, -677/280397], [889/280397, 3463/280397, -1135/280397], [-6346/280397, -1380/280397, 6525/280397]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 18 and angle, 137. Find the area of the sector. | Area of sector = 387.35837 | sector_area |
| 76 | Mean and Median | Given the series of numbers [80, 93, 16, 39, 48, 88, 7, 95, 40, 2]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 50.8 and Arithmetic median of this series is 44.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[68, 11], [22, 34]]) =  |  2070 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 6075 dollars, 8% rate of interest and for a time period of 9 year is =  | 12143.95 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 716= | 0x2cc | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 13% of 5? | Required percentage = 0.65% | percentage |
| 81 | Celsius To Fahrenheit | Convert -42 degrees Celsius to degrees Fahrenheit = | -43.60000000000001 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 11 of the AP series: -17, 71, 159 ...  | 863 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 80 terms of the AP series: 2, 86, 170 ...  | 265600.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 3350 in Octal is:  | 0o6426 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 1203 in Roman Numerals is:  | MCCIII | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 313 in radians is =  | 5.46 | degree_to_rad |
| 87 | Radians to Degrees | Angle 1 in degrees is =  | 57.3 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(cos(x)+6*x^(-2))/dx | -sin(x) - 12/x^3 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 24x^2 + 13x + 13 is =  | 27.5 | definite_integral |
| 90 | isprime | 84 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 1 is =  | 5458 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 12.21exp(i0.61) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={10, 3, 4, 7} ,b={2, 5, 6, 7}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {2, 3, 4, 5, 6, 7, 10},Intersection is {7}, a-b is {10, 3, 4},b-a is {2, 5, 6}, Symmetric difference is {2, 3, 4, 5, 6, 10} | set_operation |
| 94 | Base Conversion | Convert 44854 from base 10 to base 2. | 1010111100110110 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 1 and height, 20? | CSA of cylinder = 125.66 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 9 sided polygon with lengths of [35, 114, 106, 106, 66, 53, 18, 96, 27]cm is:  | 621 | perimeter_of_polygons |
| 97 | Power of Powers | The 15^7^6 = 15^(7*6) = 15^42 | 24878997722115027320114677422679960727691650390625 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 47^3 and 47^10 = 47^(3-10) = 47^-7 | 1.973853856267171e-12 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 34^1 and 17^1 = (34/17)^1 = 2.0^1 | 2.0 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation 4x^2 + 8x + 3 = 0 | simplified solution : ((-0.5, -1.5)), generalized solution : ((-8 + 4)/2*4, (-8 - 4)/2*4) | complex_quadratic |
| 101 | Conditional Probability | Someone tested positive for a nasty disease which only 1.61% of population have. Test sensitivity (true positive) is equal to SN= 93.28% whereas test specificity (true negative) SP= 92.26%. What is the probability that this guy really has that disease? | 16.47% | conditionalProbability |
