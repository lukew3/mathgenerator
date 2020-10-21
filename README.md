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
| 0 | Addition | 15+31= | 46 | addition |
| 1 | Subtraction | 43-14= | 29 | subtraction |
| 2 | Multiplication | 45*1= | 45 | multiplication |
| 3 | Division | 72/45= | 1.6 | division |
| 4 | Binary Complement 1s | 0011= | 1100 | binary_complement_1s |
| 5 | Modulo Division | 14%68= | 14 | modulo_division |
| 6 | Square Root | sqrt(9)= | 3 | square_root |
| 7 | Power Rule Differentiation | 9x^8 | 72x^7 | power_rule_differentiation |
| 8 | Square | 5^2= | 25 | square |
| 9 | LCM (Least Common Multiple) | LCM of 18 and 10 = | 90 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 5 and 17 =  | 1 | gcd |
| 11 | Basic Algebra | 10x + 9 = 10 | 1/10 | basic_algebra |
| 12 | Logarithm | log2(32) | 5 | log |
| 13 | Easy Division | 80/16 =  | 5 | int_division |
| 14 | Decimal to Binary | Binary of 66= | 1000010 | decimal_to_binary |
| 15 | Binary to Decimal | 011001010 | 202 | binary_to_decimal |
| 16 | Fraction Division | (3/8)/(10/7) | 21/80 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 0 * [[2, 6], [0, 4]] =  | [[0,0],[0,0]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 13 2 10 =  | (7.843059660345589e-16+12.808688457449499j) | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 33, 10 and 7 exist? | No | valid_triangle |
| 20 | Midpoint of the two point | (-1,-7),(13,-13)= | (6.0,-10.0) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+8x+7 | (x+1)(x+7) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 47 and 37 =  | 96 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | 3x - 5y = -74, -3x + 9y = 114 | x = -8, y = 10 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (7, 7) and (3, -3) | sqrt(116) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 20 and 9 =  | 21.93 | pythagorean_theorem |
| 26 | Linear Equations | 5x + -8y = -25, -12x + -1y = -243 | x = 19, y = 15 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 16 | [2, 2, 2, 2] | prime_factors |
| 28 | Fraction Multiplication | (3/1)*(5/3) | 5 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 5 sides | 108.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 19 objects picked 2 at a time  | 171 | combinations |
| 31 | Factorial | 2! =  | 2 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 1m is | 6 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 9m, 16m, 20m is | 1288 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 7m and radius = 16m is | 2312 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 12m is | 1728 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 11m, 19m, 8m is | 1672 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 9m and radius = 15m is | 6361 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 36m and radius = 1m is | 116 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 26m and radius = 15m is | 6126 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 64 and 17 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 10/6x + 3 and y = -1/3x + 10 | (7/2, 53/6) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 14 objects picked 1 at a time =   | 14 | permutation |
| 43 | Cross Product of 2 Vectors | [-16, -17, -11] X [12, -19, 5] =  | [-294, -52, 508] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 7/2 and 1/7? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 7256 dollars, 6% rate of interest and for a time period of 2 years is =  | 870.72 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>-6</td><td>3</td><td>10</td><td>4</td></tr><tr><td>9</td><td>9</td><td>-3</td><td>7</td></tr></table>and<table><tr><td>10</td><td>-9</td><td>5</td></tr><tr><td>2</td><td>-10</td><td>-5</td></tr><tr><td>6</td><td>-3</td><td>-7</td></tr><tr><td>2</td><td>1</td><td>-8</td></tr></table> | <table><tr><td>14</td><td>-2</td><td>-147</td></tr><tr><td>104</td><td>-155</td><td>-35</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 723 upto 2 decimal places is: | 8.98 | cube_root |
| 48 | Power Rule Integration | 1x^5 + 2x^8 + 1x^5 + 10x^7 + 1x^6 | (1/5)x^6 + (2/8)x^9 + (1/5)x^6 + (10/7)x^8 + (1/6)x^7 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 58 , 157, 113 = | 32 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 14x^2+92x+17=0 | [-0.19, -6.38] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 13 and 20 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 1 dice are rolled at the same time, the probability of getting a sum of 5 = | 1/6 | dice_sum_probability |
| 53 | Exponentiation | 5^10 = | 9765625 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [266, 244, 292, 288, 230, 251, 211, 272, 260, 257, 231, 234, 254, 277, 202, 206, 258, 298, 243, 213, 214, 239, 247, 232, 203, 296, 238, 282, 222, 283, 261, 253, 252, 278, 215, 267, 212] with 90% confidence is | (255.6152095323176, 240.65506073795265) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 29^(1/1) _ 37^(1/8) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 10 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] | fibonacci_series |
| 57 | Trigonometric Values | What is sin(45)? | 1/√2 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 5 sides =  | 540 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[22, 32, 15, 45, 40, 34, 40, 29, 33, 43, 34, 19, 43, 17, 42] | The Mean is 32.53333333333333 , Standard Deviation is 95.71555555555555, Variance is 9.783432708183541 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 7m is | 615.7521601035994 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 18 m =  | 24429.024474314232 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 76th Fibonacci number? | 3416454622906716 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 300 and SP = 745 is:  | 148.33333333333334 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 0011110 | 0x1e | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (15+4j) * (13+6j) =  | (171+142j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [7, 42, 252, 1512, 9072, 54432] ,Find the value of a,common ratio,9th term value, sum upto 11th term | The value of a is 7, common ratio is 6 , 9th term is 11757312 , sum upto 11th term is 507915877.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 3 numbers 22 , 15 and 25 =  | (22*15*25)^(1/3) = 20.206200103110948 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 3 numbers 37 , 33 and 53 =  |  3/((1/37) + (1/33) + (1/53)) = 39.371121476373965 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[492.40786515780576, 983.9467887251965, 631.4868422143192, 867.3371448756883, 563.3456646686222, 708.0397121576655] is: | 1783.3521007855009 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [541.0289697890829, 573.3715402714977, 323.21175522813905, 134.3110759527537, 485.181412466299, 734.1757394805238, 632.1836650961008, 874.4930077772807, 392.3682318405426, 198.18533509253734, 259.3024324493266, 692.6808468046293, 983.0594493368139, 246.1431141764312, 169.47055701867663, 179.3769672014288, 653.3731083951614, 608.0069028185225] and [716.8150260194301, 661.3439350537182, 503.6201707807608, 922.7936933135436, 887.4562350809547, 764.2289969841399, 743.9308000789802, 604.6893588822073, 185.60578793368342, 335.83315817451984, 969.7123500771294, 181.4419381940483, 275.5957393468893, 228.41527442819876, 971.7792535281106, 0.79249601650766, 878.4199844485163, 888.9960985572237] is: | NaN | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -9 and -91 =  | 82 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [14, -20, -3] . [-3, -18, 15] =  | 273 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 100 = | 100 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[77, 3, 65], [46, 99, 23], [31, 83, 47]]) is: | Matrix([[196/18259, 2627/127813, -3183/127813], [-207/36518, 802/127813, 1219/255626], [107/36518, -3149/127813, 7485/255626]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 15 and angle, 235. Find the area of the sector. | Area of sector = 461.42142 | sector_area |
| 76 | Mean and Median | Given the series of numbers [41, 17, 55, 6, 9, 93, 97, 59, 45, 54]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 47.6 and Arithmetic median of this series is 49.5 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[55, 32], [27, 54]]) =  |  2106 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 4870 dollars, 3% rate of interest and for a time period of 8 year is =  | 6169.17 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 35= | 0x23 | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 98% of 63? | Required percentage = 61.74% | percentage |
| 81 | Celsius To Fahrenheit | Convert -6 degrees Celsius to degrees Fahrenheit = | 21.2 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 33 of the AP series: 72, 140, 208 ...  | 2248 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 72 terms of the AP series: 41, 110, 179 ...  | 179316.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 406 in Octal is:  | 0o626 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 397 in Roman Numerals is:  | CCCXCVII | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 122 in radians is =  | 2.13 | degree_to_rad |
| 87 | Radians to Degrees | Angle 2 in degrees is =  | 114.59 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(tan(x)+4*x^(-3))/dx | tan(x)^2 + 1 - 12/x^4 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 54x^2 + 77x + 69 is =  | 125.5 | definite_integral |
| 90 | isprime | 95 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 4 is =  | 16643 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 1.41exp(i-2.36) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={9, 5, 6} ,b={8, 1, 6}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 5, 6, 8, 9},Intersection is {6}, a-b is {9, 5},b-a is {8, 1}, Symmetric difference is {1, 5, 8, 9} | set_operation |
| 94 | Base Conversion | Convert 121143 from base 7 to base 8. | 53020 | base_conversion |
