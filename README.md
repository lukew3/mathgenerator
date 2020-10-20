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
| 0 | Addition | 39+28= | 67 | addition |
| 1 | Subtraction | 46-1= | 45 | subtraction |
| 2 | Multiplication | 70*1= | 70 | multiplication |
| 3 | Division | 79/83= | 0.9518072289156626 | division |
| 4 | Binary Complement 1s | 00= | 11 | binary_complement_1s |
| 5 | Modulo Division | 7%99= | 7 | modulo_division |
| 6 | Square Root | sqrt(36)= | 6 | square_root |
| 7 | Power Rule Differentiation | 1x^3 + 6x^9 + 4x^9 + 2x^3 + 7x^8 | 3x^2 + 54x^8 + 36x^8 + 6x^2 + 56x^7 | power_rule_differentiation |
| 8 | Square | 15^2= | 225 | square |
| 9 | LCM (Least Common Multiple) | LCM of 16 and 10 = | 80 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 14 and 13 =  | 1 | gcd |
| 11 | Basic Algebra | 7x + 2 = 6 | 4/7 | basic_algebra |
| 12 | Logarithm | log2(16) | 4 | log |
| 13 | Easy Division | 345/15 =  | 23 | int_division |
| 14 | Decimal to Binary | Binary of 4= | 100 | decimal_to_binary |
| 15 | Binary to Decimal | 0 | 0 | binary_to_decimal |
| 16 | Fraction Division | (3/10)/(3/5) | 1/2 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 5 * [[8, 0], [7, 3]] =  | [[40,0],[35,15]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 15 15 6 =  | 44.090815370097204 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 15, 42 and 1 exist? | No | valid_triangle |
| 20 | Midpoint of the two point | (-10,19),(-11,-11)= | (-10.5,4.0) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2-4x-12 | (x-6)(x+2) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 71 and 59 =  | 50 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -5x - 7y = -66, -x + 5y = 6 | x = 9, y = 3 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-8, -11) and (5, -4) | sqrt(218) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 17 and 19 =  | 25.50 | pythagorean_theorem |
| 26 | Linear Equations | 17x + -8y = -154
-15x + 13y = 23 | x = -18, y = -19 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 106 | [2, 53] | prime_factors |
| 28 | Fraction Multiplication | (3/9)*(8/4) | 2/3 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 20 sides | 162.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 14 objects picked 6 at a time  | 3003 | combinations |
| 31 | Factorial | 3! =  | 6 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 16m is | 1536 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 14m, 4m, 4m is | 256 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 15m and radius = 4m is | 477 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 3m is | 27 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 6m, 1m, 4m is | 24 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 3m and radius = 11m is | 1140 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 22m and radius = 14m is | 1762 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 10m and radius = 14m is | 2052 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 69 and 45 =  | [1, 3] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 10x - 4 and y = 6/6x + 10 | (14/9, 104/9) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 18 objects picked 3 at a time =   | 4896 | permutation |
| 43 | Cross Product of 2 Vectors | [1, 3, 19] X [-1, 5, 4] =  | [-83, -23, 8] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 1/10 and 9/6? | < | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 3365 dollars, 8% rate of interest and for a time period of 2 years is =  | 538.4 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>1</td><td>2</td><td>-6</td></tr><tr><td>-10</td><td>-7</td><td>-4</td></tr></table>and<table><tr><td>10</td><td>-7</td><td>0</td></tr><tr><td>-8</td><td>-6</td><td>-8</td></tr><tr><td>4</td><td>4</td><td>-5</td></tr></table> | <table><tr><td>-30</td><td>-43</td><td>14</td></tr><tr><td>-60</td><td>96</td><td>76</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 353 upto 2 decimal places is: | 7.07 | cube_root |
| 48 | Power Rule Integration | 7x^4 + 10x^3 | (7/4)x^5 + (10/3)x^4 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 52 , 119, 98 = | 91 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 71x^2+167x+59=0 | [-0.43, -1.92] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 2 and 8 =  | 2 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 2 dice are rolled at the same time, the probability of getting a sum of 2 = | 1/36 | dice_sum_probability |
| 53 | Exponentiation | 6^10 = | 60466176 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [241, 229, 246, 299, 220, 249, 289, 214, 280, 275, 276, 278, 202, 203, 256, 235, 294, 263, 233, 223, 206, 295, 216, 242] with 80% confidence is | (256.54200290575125, 240.45799709424878) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 8^(1/6) _ 38^(1/4) | < | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 13 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144] | fibonacci_series |
| 57 | Trigonometric Values | What is cos(0)? | 1 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 12 sides =  | 1800 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[40, 14, 47, 30, 6, 32, 25, 32, 42, 34, 34, 37, 22, 30, 31] | The Mean is 30.4 , Standard Deviation is 102.77333333333331, Variance is 10.137718349477526 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 1m is | 12.566370614359172 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 98 m =  | 3942455.8304233127 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 26th Fibonacci number? | 121393 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 171 and SP = 313 is:  | 83.04093567251462 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 1011101 | 0x5d | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (11+3j) * (2+18j) =  | (-32+204j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [8, 56, 392, 2744, 19208, 134456] ,Find the value of a,common ratio,7th term value, sum upto 8th term | The value of a is 8, common ratio is 7 , 7th term is 941192 , sum upto 8th term is 7686400.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 3 numbers 47 , 92 and 3 =  | (47*92*3)^(1/3) = 23.49645336547587 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 3 numbers 94 , 92 and 59 =  |  3/((1/94) + (1/92) + (1/59)) = 78.00917337682192 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[304.9779176267893, 837.4224202657908] is: | 891.228276146907 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [673.5350704033146, 195.45799005765386, 92.93464829626352, 116.63589535434215, 594.8238225788838, 345.12804915831896, 421.4756162395643, 718.6449275827789, 134.11947817433213, 573.4174565052257, 96.96537158190588, 188.69415889717357] and [520.2618389520298, 141.25763773504042, 998.0680511901267, 88.96111274282836, 131.27448267605467, 196.35332202572542, 63.657368381112356, 58.100728119799825, 818.3595663049074, 910.4545383236834, 173.11410173656193, 517.355465521104] is: | NaN | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 95 and 92 =  | 3 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [-4, 20, 2] . [8, -14, -14] =  | -340 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 111101001 = | 10111 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[65, 7, 75], [69, 31, 73], [67, 15, 8]]) is: | Matrix([[847/102832, -1069/102832, 907/51416], [-4339/102832, 4505/102832, -215/51416], [521/51416, 253/51416, -383/25708]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 20 and angle, 72. Find the area of the sector. | Area of sector = 251.32741 | sector_area |
| 76 | Mean and Median | Given the series of numbers [59, 80, 5, 46, 57, 30, 13, 3, 54, 48]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 39.5 and Arithmetic median of this series is 47.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[17, 94], [26, 42]]) =  |  -1730 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound Interest for a principle amount of 1069 dollars, 8% rate of interest and for a time period of 3 compounded monthly is =  | 1069.0 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 175= | 0xaf | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 30% of 26? | Required percentage = 7.80% | percentage |
| 81 | Celsius To Fahrenheit | Convert 51 degrees Celsius to degrees Fahrenheit = | 123.8 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 13 of the AP series: -56, -129, -202 ...  | -932 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 93 terms of the AP series: -27, -72, -117 ...  | -195021.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 1871 in Octal is:  | 0o3517 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 3868 in Roman Numerals is:  | MMMDCCCLXVIII | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 99 in radians is =  | 1.73 | degree_to_rad |
| 87 | Radians to Degrees | Angle 2 in degrees is =  | 114.59 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(exp(x)+4*x^(-3))/dx | exp(x) - 12/x^4 | differentiation |
