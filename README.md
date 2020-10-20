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
| 0 | Addition | 42+42= | 84 | addition |
| 1 | Subtraction | 6-3= | 3 | subtraction |
| 2 | Multiplication | 5*10= | 50 | multiplication |
| 3 | Division | 48/95= | 0.5052631578947369 | division |
| 4 | Binary Complement 1s | 0110000= | 1001111 | binary_complement_1s |
| 5 | Modulo Division | 92%7= | 1 | modulo_division |
| 6 | Square Root | sqrt(1)= | 1 | square_root |
| 7 | Power Rule Differentiation | 3x^8 + 7x^6 + 3x^7 + 1x^3 | 24x^7 + 42x^5 + 21x^6 + 3x^2 | power_rule_differentiation |
| 8 | Square | 19^2= | 361 | square |
| 9 | LCM (Least Common Multiple) | LCM of 14 and 16 = | 112 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 7 and 18 =  | 1 | gcd |
| 11 | Basic Algebra | 10x + 1 = 2 | 1/10 | basic_algebra |
| 12 | Logarithm | log3(6561) | 8 | log |
| 13 | Easy Division | 198/18 =  | 11 | int_division |
| 14 | Decimal to Binary | Binary of 17= | 10001 | decimal_to_binary |
| 15 | Binary to Decimal | 100111010 | 314 | binary_to_decimal |
| 16 | Fraction Division | (9/7)/(4/9) | 81/28 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 15 * [[6, 6], [1, 1]] =  | [[90,90],[15,15]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 18 17 13 =  | 105.29957264870546 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 12, 33 and 30 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (-7,-12),(-1,6)= | (-4.0,-3.0) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2-9x+8 | (x-8)(x-1) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 55 and 17 =  | 108 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | 10x - 6y = 46, 9x + 5y = -21 | x = 1, y = -6 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (14, 8) and (1, -11) | sqrt(530) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 20 and 14 =  | 24.41 | pythagorean_theorem |
| 26 | Linear Equations | -2x + 14y = 154
-10x + -8y = -166 | x = 7, y = 12 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 189 | [3, 3, 3, 7] | prime_factors |
| 28 | Fraction Multiplication | (9/4)*(5/9) | 5/4 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 14 sides | 154.29 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 17 objects picked 9 at a time  | 24310 | combinations |
| 31 | Factorial | 2! =  | 2 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 15m is | 1350 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 6m, 3m, 9m is | 198 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 25m and radius = 17m is | 4486 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 6m is | 216 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 12m, 8m, 20m is | 1920 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 35m and radius = 13m is | 18582 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 45m and radius = 1m is | 144 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 25m and radius = 16m is | 6702 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 52 and 89 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -3/5x + 10 and y = -3/4x - 5 | (-100, 70) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 14 objects picked 8 at a time =   | 121080960 | permutation |
| 43 | Cross Product of 2 Vectors | [-16, -2, -1] X [-16, -7, 19] =  | [-45, 320, 80] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 9/2 and 9/10? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 4736 dollars, 1% rate of interest and for a time period of 7 years is =  | 331.52 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>4</td><td>-2</td><td>-2</td></tr><tr><td>4</td><td>6</td><td>-4</td></tr><tr><td>-1</td><td>1</td><td>-5</td></tr><tr><td>-10</td><td>8</td><td>3</td></tr></table>and<table><tr><td>6</td><td>3</td><td>9</td><td>-4</td></tr><tr><td>-4</td><td>-6</td><td>-3</td><td>0</td></tr><tr><td>-10</td><td>-3</td><td>-7</td><td>-7</td></tr></table> | <table><tr><td>52</td><td>30</td><td>56</td><td>-2</td></tr><tr><td>40</td><td>-12</td><td>46</td><td>12</td></tr><tr><td>40</td><td>6</td><td>23</td><td>39</td></tr><tr><td>-122</td><td>-87</td><td>-135</td><td>19</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 744 upto 2 decimal places is: | 9.06 | cube_root |
| 48 | Power Rule Integration | 9x^1 | (9/1)x^2 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 96 , 118, 81 = | 65 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 88x^2+193x+32=0 | [-0.18, -2.01] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 16 and 3 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 1 dice are rolled at the same time, the probability of getting a sum of 5 = | 1/6 | dice_sum_probability |
| 53 | Exponentiation | 6^5 = | 7776 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [202, 227, 233, 291, 294, 242, 247, 283, 251, 228, 216, 240, 289, 243, 282, 238, 257, 255, 203, 276, 293, 214, 207, 210, 265, 212, 236, 297, 256, 280, 288] with 99% confidence is | (264.1616033070315, 236.1609773381298) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 27^(1/4) _ 87^(1/1) | < | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 5 numbers is ? | [0, 1, 1, 2, 3] | fibonacci_series |
| 57 | Trigonometric Values | What is tan(45)? | 1 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 5 sides =  | 540 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[11, 22, 9, 8, 12, 36, 39, 19, 12, 11, 49, 27, 22, 27, 26] | The Mean is 22.0 , Standard Deviation is 139.73333333333332, Variance is 11.820885471627467 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 20m is | 5026.548245743669 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 69 m =  | 1376055.2813841724 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 33th Fibonacci number? | 3524578 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Loss percent when CP = 883 and SP = 393 is:  | 55.492638731596834 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 00010100 | 0x14 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (-3+0j) * 16j =  | (-0-48j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [4, 20, 100, 500, 2500, 12500] ,Find the value of a,common ratio,6th term value, sum upto 8th term | The value of a is 4, common ratio is 5 , 6th term is 12500 , sum upto 8th term is 390624.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 2 numbers 41 and 54 =  | (41*54)^(1/2) = 47.05316142407437 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 3 numbers 8 , 71 and 68 =  |  3/((1/8) + (1/71) + (1/68)) = 19.507070707070707 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[865.7151963569839, 226.4057036465874, 14.824800248170567, 706.1262882326861, 865.8569268338141, 559.1781356802616, 756.7052133079868, 164.9216239520549, 609.9900978280176, 697.4174107118105, 486.57415492429044, 993.1670184061886, 640.1534234049134, 368.9654609248786] is: | 2364.168521129801 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [275.27222370228554, 360.4704403955723, 828.9475033885524, 339.2072270059939, 233.95550521713915, 887.4530688219838, 390.16238631557763, 351.47764321737054, 103.32257528086953, 867.8009318330934, 525.3164032492849] and [886.3103662444178, 562.6461993125878, 190.16362305272116, 909.6771690252709, 555.7134133875247, 553.903105904929, 828.5687817542065, 208.31947038854025, 388.8973006974784, 424.9452146134446, 460.00088587027324] is: | NaN | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 25 and -64 =  | 89 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [-20, -4, 9] . [4, -19, -3] =  | -31 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 110000 = | 10000 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[43, 31, 88], [96, 41, 11], [68, 89, 13]]) is: | Matrix([[-223/235925, 7429/471850, -3267/471850], [-10/9437, -217/18874, 319/18874], [2878/235925, -1719/471850, -1213/471850]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 45 and angle, 191. Find the area of the sector. | Area of sector = 3375.24861 | sector_area |
| 76 | Mean and Median | Given the series of numbers [44, 90, 6, 3, 25, 67, 76, 86, 51, 69]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 51.7 and Arithmetic median of this series is 59.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[51, 51], [15, 83]]) =  |  3468 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound Interest for a principle amount of 2506 dollars, 5% rate of interest and for a time period of 10 compounded monthly is =  | 2506.0 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 588= | 0x24c | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 21% of 84? | Required percentage = 17.64% | percentage |
| 81 | Celsius To Fahrenheit | Convert 62 degrees Celsius to degrees Fahrenheit = | 143.60000000000002 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 76 of the AP series: 94, 46, -2 ...  | -3506 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 20 terms of the AP series: -69, -146, -223 ...  | -16010.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 1829 in Octal is:  | 0o3445 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 1938 in Roman Numerals is:  | MCMXXXVIII | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 197 in radians is =  | 3.44 | degree_to_rad |
| 87 | Radians to Degrees | Angle 3 in degrees is =  | 171.89 | radian_to_deg |
