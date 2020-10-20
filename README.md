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
| 0 | Addition | 6+12= | 18 | addition |
| 1 | Subtraction | 17-11= | 6 | subtraction |
| 2 | Multiplication | 99*1= | 99 | multiplication |
| 3 | Division | 23/29= | 0.7931034482758621 | division |
| 4 | Binary Complement 1s | 1000= | 0111 | binary_complement_1s |
| 5 | Modulo Division | 80%49= | 31 | modulo_division |
| 6 | Square Root | sqrt(49)= | 7 | square_root |
| 7 | Power Rule Differentiation | 10x^9 | 90x^8 | power_rule_differentiation |
| 8 | Square | 13^2= | 169 | square |
| 9 | LCM (Least Common Multiple) | LCM of 14 and 12 = | 84 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 5 and 19 =  | 1 | gcd |
| 11 | Basic Algebra | 4x + 1 = 2 | 1/4 | basic_algebra |
| 12 | Logarithm | log2(128) | 7 | log |
| 13 | Easy Division | 264/11 =  | 24 | int_division |
| 14 | Decimal to Binary | Binary of 96= | 1100000 | decimal_to_binary |
| 15 | Binary to Decimal | 1011 | 11 | binary_to_decimal |
| 16 | Fraction Division | (8/6)/(8/1) | 1/6 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 2 * [[9, 9], [6, 5]] =  | [[18,18],[12,10]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 16 9 3 =  | (2.402930536500827e-15+39.242833740697165j) | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 37, 37 and 44 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (-16,19),(-4,10)= | (-10.0,14.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+x-42 | (x+7)(x-6) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 8 and 77 =  | 95 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -3x - 2y = 23, 7x + 8y = -87 | x = -1, y = -10 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (17, 10) and (15, 9) | sqrt(5) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 7 and 13 =  | 14.76 | pythagorean_theorem |
| 26 | Linear Equations | -10x + -17y = 373
17x + -17y = 238 | x = -5, y = -19 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 76 | [2, 2, 19] | prime_factors |
| 28 | Fraction Multiplication | (8/3)*(10/1) | 80/3 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 3 sides | 60.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 17 objects picked 2 at a time  | 136 | combinations |
| 31 | Factorial | 0! =  | 1 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 15m is | 1350 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 20m, 13m, 15m is | 1510 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 18m and radius = 12m is | 2261 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 11m is | 1331 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 14m, 8m, 8m is | 896 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 33m and radius = 9m is | 8397 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 3m and radius = 9m is | 522 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 31m and radius = 1m is | 32 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 5 and 90 =  | [1, 5] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 9/6x - 4 and y = -8/6x + 1 | (30/17, -23/17) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 19 objects picked 1 at a time =   | 19 | permutation |
| 43 | Cross Product of 2 Vectors | [-3, -11, -6] X [2, 18, 11] =  | [-13, 21, -32] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 10/4 and 6/9? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 9924 dollars, 2% rate of interest and for a time period of 2 years is =  | 396.96 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>8</td><td>3</td><td>-7</td></tr><tr><td>-3</td><td>3</td><td>-10</td></tr><tr><td>-9</td><td>4</td><td>4</td></tr></table>and<table><tr><td>8</td><td>8</td><td>-3</td></tr><tr><td>9</td><td>4</td><td>1</td></tr><tr><td>-2</td><td>-7</td><td>-7</td></tr></table> | <table><tr><td>105</td><td>125</td><td>28</td></tr><tr><td>23</td><td>58</td><td>82</td></tr><tr><td>-44</td><td>-84</td><td>3</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 194 upto 2 decimal places is: | 5.79 | cube_root |
| 48 | Power Rule Integration | 8x^1 + 2x^1 + 8x^8 + 3x^3 | (8/1)x^2 + (2/1)x^2 + (8/8)x^9 + (3/3)x^4 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 179 , 29, 29 = | 123 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 77x^2+91x+14=0 | [-0.18, -1.0] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 11 and 1 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 3 dice are rolled at the same time, the probability of getting a sum of 13 = | 21/216 | dice_sum_probability |
| 53 | Exponentiation | 16^8 = | 4294967296 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [208, 221, 294, 275, 252, 253, 236, 216, 290, 296, 227, 251, 266, 277, 263, 268, 260, 248, 214, 298, 284, 293, 213, 264, 206, 238, 211, 203, 276, 279, 285, 220, 222, 299] with 90% confidence is | (261.88480835505726, 244.3504857625898) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 68^(1/3) _ 84^(1/8) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 9 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21] | fibonacci_series |
| 57 | Trigonometric Values | What is sin(90)? | 1 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 8 sides =  | 1080 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[35, 18, 28, 21, 50, 17, 30, 33, 14, 41, 35, 31, 7, 28, 8] | The Mean is 26.4 , Standard Deviation is 137.17333333333335, Variance is 11.7121020031988 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 12m is | 1809.5573684677208 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 61 m =  | 950775.7894726198 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 98th Fibonacci number? | 135301852344707186688 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Loss percent when CP = 948 and SP = 729 is:  | 23.10126582278481 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 10101010 | 0xaa | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (-16+11j) * (7+19j) =  | (-321-227j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [8, 56, 392, 2744, 19208, 134456] ,Find the value of a,common ratio,9th term value, sum upto 8th term | The value of a is 8, common ratio is 7 , 9th term is 46118408 , sum upto 8th term is 7686400.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 24 , 6 , 17 , 34 =  | (24*6*17*34)^(1/4) = 16.985274997011718 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 3 numbers 72 , 17 and 14 =  |  3/((1/72) + (1/17) + (1/14)) = 20.812955465587045 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[959.2746467619136, 621.8392214146113, 922.8483095629905, 386.90198896263786, 998.2816134301269, 924.4767901166847, 526.4451342917619, 540.6365528762716, 921.5612942821017, 507.86794502436186] is: | 2415.8011015687784 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [828.7073706479772, 912.8938227679938, 154.5891010528101, 789.3839240933659, 470.5951408141951, 365.0311186930294, 492.5244778860853, 433.2880676781922, 498.50124161369234] and [209.0406231603238, 64.7709335985529, 413.202808762719, 1.9226444773620122, 215.67348315298196, 668.6663275149825, 99.38710508880888, 74.18515931735026, 384.83132929263707] is: | NaN | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 18 and 88 =  | 70 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [5, 9, -5] . [11, 19, -16] =  | 306 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 10 = | 10 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[37, 41, 67], [47, 57, 55], [73, 23, 22]]) is: | Matrix([[1/7686, -71/9394, 782/42273], [-271/7686, 453/9394, -557/42273], [20/549, -17/671, -13/6039]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 39 and angle, 299. Find the area of the sector. | Area of sector = 3968.69546 | sector_area |
| 76 | Mean and Median | Given the series of numbers [2, 78, 43, 59, 84, 10, 17, 62, 44, 94]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 49.3 and Arithmetic median of this series is 51.5 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[74, 66], [92, 76]]) =  |  -448 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound Interest for a principle amount of 8675 dollars, 10% rate of interest and for a time period of 3 compounded monthly is =  | 8675.0 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 533= | 0x215 | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 46% of 69? | Required percentage = 31.74% | percentage |
| 81 | Celsius To Fahrenheit | Convert -43 degrees Celsius to degrees Fahrenheit = | -45.400000000000006 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 67 of the AP series: 3, 99, 195 ...  | 6339 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 16 terms of the AP series: 60, -36, -132 ...  | -10560.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 3881 in Octal is:  | 0o7451 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 2606 in Roman Numerals is:  | MMDCVI | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 55 in radians is =  | 0.96 | degree_to_rad |
| 87 | Radians to Degrees | Angle 2 in degrees is =  | 114.59 | radian_to_deg |
