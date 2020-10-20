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
| 0 | Addition | 31+3= | 34 | addition |
| 1 | Subtraction | 69-64= | 5 | subtraction |
| 2 | Multiplication | 88*1= | 88 | multiplication |
| 3 | Division | 77/8= | 9.625 | division |
| 4 | Binary Complement 1s | 11100= | 00011 | binary_complement_1s |
| 5 | Modulo Division | 40%27= | 13 | modulo_division |
| 6 | Square Root | sqrt(121)= | 11 | square_root |
| 7 | Power Rule Differentiation | 7x^3 | 21x^2 | power_rule_differentiation |
| 8 | Square | 13^2= | 169 | square |
| 9 | LCM (Least Common Multiple) | LCM of 15 and 9 = | 45 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 4 and 20 =  | 4 | gcd |
| 11 | Basic Algebra | 10x + 8 = 9 | 1/10 | basic_algebra |
| 12 | Logarithm | log3(9) | 2 | log |
| 13 | Easy Division | 54/3 =  | 18 | int_division |
| 14 | Decimal to Binary | Binary of 82= | 1010010 | decimal_to_binary |
| 15 | Binary to Decimal | 11 | 3 | binary_to_decimal |
| 16 | Fraction Division | (7/9)/(9/8) | 56/81 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 5 * [[3, 8], [4, 7]] =  | [[15,40],[20,35]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 4 10 12 =  | 18.734993995195193 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 39, 48 and 2 exist? | No | valid_triangle |
| 20 | Midpoint of the two point | (-17,18),(-10,20)= | (-13.5,19.0) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2-16x+60 | (x-10)(x-6) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 35 and 52 =  | 93 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | 4x + 2y = -22, 5x + 6y = -31 | x = -5, y = -1 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (2, -19) and (7, -4) | sqrt(250) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 13 and 9 =  | 15.81 | pythagorean_theorem |
| 26 | Linear Equations | 18x + -12y = -42, 9x + 7y = 161 | x = 7, y = 14 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 45 | [3, 3, 5] | prime_factors |
| 28 | Fraction Multiplication | (7/5)*(3/1) | 21/5 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 16 sides | 157.5 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 14 objects picked 5 at a time  | 2002 | combinations |
| 31 | Factorial | 0! =  | 1 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 3m is | 54 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 7m, 2m, 4m is | 100 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 12m and radius = 3m is | 282 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 19m is | 6859 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 8m, 9m, 10m is | 720 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 13m and radius = 4m is | 653 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 46m and radius = 1m is | 147 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 35m and radius = 10m is | 3665 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 71 and 25 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -7x + 9 and y = 0/3x - 10 | (19/7, -10) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 20 objects picked 8 at a time =   | 5079110400 | permutation |
| 43 | Cross Product of 2 Vectors | [-4, 4, -3] X [-6, 6, 14] =  | [74, 74, 0] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 6/1 and 6/2? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 2266 dollars, 8% rate of interest and for a time period of 6 years is =  | 1087.68 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>6</td><td>9</td><td>-1</td><td>6</td></tr><tr><td>6</td><td>10</td><td>6</td><td>0</td></tr><tr><td>-8</td><td>-6</td><td>-7</td><td>-9</td></tr></table>and<table><tr><td>9</td><td>10</td><td>8</td></tr><tr><td>-2</td><td>-3</td><td>-4</td></tr><tr><td>-9</td><td>5</td><td>7</td></tr><tr><td>8</td><td>-8</td><td>-1</td></tr></table> | <table><tr><td>93</td><td>-20</td><td>-1</td></tr><tr><td>-20</td><td>60</td><td>50</td></tr><tr><td>-69</td><td>-25</td><td>-80</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 196 upto 2 decimal places is: | 5.81 | cube_root |
| 48 | Power Rule Integration | 6x^4 | (6/4)x^5 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 175 , 22, 60 = | 103 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 64x^2+159x+78=0 | [-0.67, -1.81] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 9 and 17 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 2 dice are rolled at the same time, the probability of getting a sum of 5 = | 4/36 | dice_sum_probability |
| 53 | Exponentiation | 18^1 = | 18 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [277, 237, 229, 258, 291, 278, 274, 242, 267, 287, 288, 293, 208, 273, 255, 259, 263, 269, 265, 210, 281, 276, 256, 238, 271, 297, 202, 252] with 95% confidence is | (269.92602102647436, 251.21683611638275) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 58^(1/2) _ 44^(1/1) | < | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 9 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21] | fibonacci_series |
| 57 | Trigonometric Values | What is cos(90)? | 0 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 11 sides =  | 1620 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[11, 43, 11, 20, 7, 47, 42, 16, 37, 29, 39, 11, 36, 25, 49] | The Mean is 28.2 , Standard Deviation is 200.95999999999998, Variance is 14.17603611733548 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 4m is | 201.06192982974676 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 66 m =  | 1204260.4287152681 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 96th Fibonacci number? | 51680708854858489856 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 591 and SP = 796 is:  | 34.686971235194584 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 101010111 | 0x157 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (6+16j) * (15-11j) =  | (266+174j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [5, 30, 180, 1080, 6480, 38880] ,Find the value of a,common ratio,6th term value, sum upto 8th term | The value of a is 5, common ratio is 6 , 6th term is 38880 , sum upto 8th term is 1679615.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 64 , 71 , 42 , 69 =  | (64*71*42*69)^(1/4) = 60.239890804783805 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 13 and 89 =  |  2/((1/13) + (1/89)) = 22.68627450980392 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[776.6691324098483, 606.5799343351656, 285.46422221982624, 372.01270687089004, 86.18433302762118, 939.355471377651, 202.1465319226168, 932.3553335024733, 275.1276478308532, 160.88380854198425] is: | 1758.5739637031488 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [601.4612452378941, 933.4356902778246, 438.03974725076324, 281.0471724516086] and [402.0844562515671, 707.7656850759612, 547.0834759350798, 897.3106790199977] is: | NaN | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 67 and 24 =  | 43 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [12, -8, 13] . [16, -6, 19] =  | 487 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of  = |  | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[52, 89, 11], [44, 72, 61], [17, 87, 7]]) is: | Matrix([[1601/52077, -334/156231, -4637/156231], [-81/17359, -59/52077, 896/52077], [-868/52077, 3011/156231, 172/156231]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 4 and angle, 16. Find the area of the sector. | Area of sector = 2.23402 | sector_area |
| 76 | Mean and Median | Given the series of numbers [90, 44, 84, 5, 79, 31, 78, 89, 56, 34]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 59.0 and Arithmetic median of this series is 67.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[0, 19], [73, 25]]) =  |  -1387 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound Interest for a principle amount of 7422 dollars, 10% rate of interest and for a time period of 2 compounded monthly is =  | 7422.0 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 946= | 0x3b2 | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 94% of 88? | Required percentage = 82.72% | percentage |
| 81 | Celsius To Fahrenheit | Convert 14 degrees Celsius to degrees Fahrenheit = | 57.2 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 48 of the AP series: 33, 9, -15 ...  | -1095 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 12 terms of the AP series: 26, 67, 108 ...  | 3018.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 2394 in Octal is:  | 0o4532 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 25 in Roman Numerals is:  | XXV | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 9 in radians is =  | 0.16 | degree_to_rad |
| 87 | Radians to Degrees | Angle 2 in degrees is =  | 114.59 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(sec(x)+6*x^4)/dx | 24*x^3 + tan(x)*sec(x) | differentiation |
