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
| 0 | Addition | 27+1= | 28 | addition |
| 1 | Subtraction | 32-27= | 5 | subtraction |
| 2 | Multiplication | 15*3= | 45 | multiplication |
| 3 | Division | 22/52= | 0.4230769230769231 | division |
| 4 | Binary Complement 1s | 000= | 111 | binary_complement_1s |
| 5 | Modulo Division | 36%44= | 36 | modulo_division |
| 6 | Square Root | sqrt(9)= | 3 | square_root |
| 7 | Power Rule Differentiation | 4x^4 + 4x^8 + 3x^2 + 4x^1 | 16x^3 + 32x^7 + 6x^1 + 4x^0 | power_rule_differentiation |
| 8 | Square | 10^2= | 100 | square |
| 9 | LCM (Least Common Multiple) | LCM of 5 and 7 = | 35 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 9 and 2 =  | 1 | gcd |
| 11 | Basic Algebra | 2x + 1 = 10 | 9/2 | basic_algebra |
| 12 | Logarithm | log2(2) | 1 | log |
| 13 | Easy Division | 154/7 =  | 22 | int_division |
| 14 | Decimal to Binary | Binary of 81= | 1010001 | decimal_to_binary |
| 15 | Binary to Decimal | 10010 | 18 | binary_to_decimal |
| 16 | Fraction Division | (2/10)/(6/10) | 1/3 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 4 * [[8, 2], [10, 5]] =  | [[32,8],[40,20]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 15 17 7 =  | 52.36590016413353 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 14, 12 and 40 exist? | No | valid_triangle |
| 20 | Midpoint of the two point | (20,-15),(3,-16)= | (11.5,-15.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2-16x+63 | (x-7)(x-9) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 39 and 55 =  | 86 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | 3x + 2y = -16, 3x + 2y = -16 | x = -6, y = 1 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (17, 17) and (16, 0) | sqrt(290) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 3 and 6 =  | 6.71 | pythagorean_theorem |
| 26 | Linear Equations | -9x + -4y = 44, -20x + -9y = 97 | x = -8, y = 7 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 199 | [199] | prime_factors |
| 28 | Fraction Multiplication | (6/4)*(1/5) | 3/10 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 20 sides | 162.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 19 objects picked 5 at a time  | 11628 | combinations |
| 31 | Factorial | 5! =  | 120 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 11m is | 726 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 14m, 15m, 11m is | 1058 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 30m and radius = 1m is | 194 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 8m is | 512 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 10m, 9m, 9m is | 810 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 20m and radius = 4m is | 1005 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 10m and radius = 4m is | 185 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 34m and radius = 1m is | 35 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 57 and 77 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -10/6x - 4 and y = -4/2x + 10 | (42, -74) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 20 objects picked 9 at a time =   | 60949324800 | permutation |
| 43 | Cross Product of 2 Vectors | [4, -19, -17] X [-15, -1, -7] =  | [116, 283, -289] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 2/7 and 5/2? | < | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 3557 dollars, 3% rate of interest and for a time period of 5 years is =  | 533.55 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>4</td><td>7</td><td>0</td><td>0</td></tr><tr><td>3</td><td>5</td><td>-3</td><td>5</td></tr><tr><td>-9</td><td>-8</td><td>-9</td><td>4</td></tr><tr><td>10</td><td>-4</td><td>5</td><td>-7</td></tr></table>and<table><tr><td>10</td><td>5</td><td>1</td></tr><tr><td>-4</td><td>-1</td><td>-3</td></tr><tr><td>3</td><td>3</td><td>4</td></tr><tr><td>-10</td><td>9</td><td>8</td></tr></table> | <table><tr><td>12</td><td>13</td><td>-17</td></tr><tr><td>-49</td><td>46</td><td>16</td></tr><tr><td>-125</td><td>-28</td><td>11</td></tr><tr><td>201</td><td>6</td><td>-14</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 493 upto 2 decimal places is: | 7.9 | cube_root |
| 48 | Power Rule Integration | 4x^1 + 3x^8 + 10x^2 + 2x^2 + 10x^2 | (4/1)x^2 + (3/8)x^9 + (10/2)x^3 + (2/2)x^3 + (10/2)x^3 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 50 , 99, 150 = | 61 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 48x^2+108x+4=0 | [-0.04, -2.21] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 10 and 9 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 1 dice are rolled at the same time, the probability of getting a sum of 5 = | 1/6 | dice_sum_probability |
| 53 | Exponentiation | 8^3 = | 512 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [280, 285, 226, 201, 281, 267, 200, 219, 239, 208, 235, 291, 262, 223, 248, 292, 269, 263, 206, 256, 252, 222, 221, 237] with 80% confidence is | (252.67446369260804, 237.57553630739196) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 35^(1/8) _ 23^(1/1) | < | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 4 numbers is ? | [0, 1, 1, 2] | fibonacci_series |
| 57 | Trigonometric Values | What is sin(0)? | 0 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 3 sides =  | 180 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[48, 43, 34, 18, 44, 36, 13, 40, 35, 35, 38, 11, 10, 11, 24] | The Mean is 29.333333333333332 , Standard Deviation is 169.28888888888886, Variance is 13.011106366827107 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 8m is | 804.247719318987 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 83 m =  | 2395095.784824196 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 35th Fibonacci number? | 9227465 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 27 and SP = 823 is:  | 2948.1481481481483 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 11000111 | 0xc7 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (1-18j) * (-8+0j) =  | (-8+144j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [9, 99, 1089, 11979, 131769, 1449459] ,Find the value of a,common ratio,10th term value, sum upto 7th term | The value of a is 9, common ratio is 11 , 10th term is 21221529219 , sum upto 7th term is 17538453.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 3 numbers 31 , 76 and 15 =  | (31*76*15)^(1/3) = 32.816242203578014 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 4 numbers 92 , 58 , 23 , 83 =  |  4/((1/92) + (1/58) + (1/23) + (1/83)) = 47.825495383618595 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[36.38067725666217, 442.61220631149655, 502.3274860206511, 192.63540485685093, 984.9063401399998, 160.78033823501792, 236.70055274694923, 723.3837994746971, 54.940314755713146, 712.042190068723] is: | 1603.712888554928 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [651.44, 836.06, 559.59, 874.73, 707.25, 374.4, 229.28, 274.43, 158.51, 86.58, 600.24, 829.38, 64.41, 726.78, 215.5, 518.68, 659.02, 711.32, 726.21] and [231.22, 461.9, 619.6, 776.56, 266.04, 392.15, 830.34, 47.13, 373.1, 113.63, 30.84, 917.3, 532.78, 187.05, 172.89, 836.61, 882.82, 128.56, 285.96] is: | 0.67 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -25 and -49 =  | 24 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [7, 5, -15] . [8, -8, 16] =  | -224 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 10011101 = | 1100011 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[13, 16, 78], [21, 84, 31], [85, 6, 43]]) is: | Matrix([[-1713/237421, 110/237421, 3028/237421], [-866/237421, 6071/474842, -1235/474842], [3507/237421, -641/237421, -378/237421]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 22 and angle, 287. Find the area of the sector. | Area of sector = 1212.20098 | sector_area |
| 76 | Mean and Median | Given the series of numbers [33, 62, 91, 64, 77, 75, 82, 19, 26, 50]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 57.9 and Arithmetic median of this series is 63.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[34, 100], [81, 93]]) =  |  -4938 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 1090 dollars, 5% rate of interest and for a time period of 5 year is =  | 1391.15 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 153= | 0x99 | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 68% of 77? | Required percentage = 52.36% | percentage |
| 81 | Celsius To Fahrenheit | Convert 21 degrees Celsius to degrees Fahrenheit = | 69.80000000000001 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 68 of the AP series: -11, -79, -147 ...  | -4567 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 17 terms of the AP series: -91, -183, -275 ...  | -14059.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 2197 in Octal is:  | 0o4225 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 3620 in Roman Numerals is:  | MMMDCXX | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 355 in radians is =  | 6.2 | degree_to_rad |
| 87 | Radians to Degrees | Angle 3 in degrees is =  | 171.89 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(cot(x)+9*x^4)/dx | 36*x^3 - cot(x)^2 - 1 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 24x^2 + 41x + 61 is =  | 89.5 | definite_integral |
| 90 | isprime | 84 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 4 is =  | 18064 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 18.97exp(i-1.25) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={1, 5, 6, 7} ,b={8, 3, 6, 7}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 3, 5, 6, 7, 8},Intersection is {6, 7}, a-b is {1, 5},b-a is {8, 3}, Symmetric difference is {1, 3, 5, 8} | set_operation |
| 94 | Base Conversion | Convert 1101101111100 from base 2 to base 10. | 7036 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 39 and height, 61? | CSA of cylinder = 14947.7 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 10 sided polygon with lengths of [110, 4, 55, 93, 68, 82, 30, 35, 45, 72]cm is:  | 594 | perimeter_of_polygons |
| 97 | Power of Powers | The 15^2^4 = 15^(2*4) = 15^8 | 2562890625 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 2^3 and 2^5 = 2^(3-5) = 2^-2 | 0.25 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 30^1 and 31^1 = (30/31)^1 = 0.967741935483871^1 | 0.967741935483871 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation 2x^2 + 9x + 3 = 0 | simplified solution : ((-0.363, -4.137)), generalized solution : ((-9 + sqrt(57))/2*2, (-9 - sqrt(57))/2*2) | complex_quadratic |
| 101 | Leap Year or Not | Year 1924  | is a leap year | is_leap_year |
| 102 | Minute to Hour conversion | Convert 292 minutes to Hours & Minutes | 4 hours and 52 minutes | minutes_to_hours |
| 103 | Decimal to Binary Coded Decimal | BCD of Decimal Number 2596 is =  | 1024 | decimal_to_bcd |
| 104 | Circumference | Circumference of circle with radius 17 | 106.81415022205297 | circumference |
| 105 | Combine Like terms | 9x^2 | 9x^2  | combine_like_terms |
| 106 | signum function | signum of -885 is = | -1 | signum_function |
| 107 | Conditional Probability | Someone tested positive for a nasty disease which only 1.53% of population have. Test sensitivity (true positive) is equal to SN= 93.62% whereas test specificity (true negative) SP= 93.01%. What is the probability that this guy really has that disease? | 17.23% | conditional_probability |
| 108 | Arc length of Angle | Given radius, 22 and angle, 345. Find the arc length of the angle. | Arc length of the angle = 132.47049 | arc_length |
| 109 | Binomial distribution | A manufacturer of metal pistons finds that, on average, 31.04% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 20 pistons will contain no more than 6 rejected pistons? | 56.79 | binomial_distribution |
| 110 | Stationary Points | f(x)=5*x^2 + 4 | (0,4) | stationary_points |
