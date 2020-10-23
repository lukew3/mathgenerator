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
| 0 | Addition | 16+2= | 18 | addition |
| 1 | Subtraction | 9-6= | 3 | subtraction |
| 2 | Multiplication | 3*0= | 0 | multiplication |
| 3 | Division | 80/88= | 0.9090909090909091 | division |
| 4 | Binary Complement 1s | 0000100= | 1111011 | binary_complement_1s |
| 5 | Modulo Division | 99%94= | 5 | modulo_division |
| 6 | Square Root | sqrt(16)= | 4 | square_root |
| 7 | Power Rule Differentiation | 7x^8 + 4x^10 + 9x^9 + 4x^10 | 56x^7 + 40x^9 + 81x^8 + 40x^9 | power_rule_differentiation |
| 8 | Square | 17^2= | 289 | square |
| 9 | LCM (Least Common Multiple) | LCM of 1 and 8 = | 8 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 11 and 7 =  | 1 | gcd |
| 11 | Basic Algebra | 8x + 4 = 4 | 0 | basic_algebra |
| 12 | Logarithm | log3(729) | 6 | log |
| 13 | Easy Division | 575/25 =  | 23 | int_division |
| 14 | Decimal to Binary | Binary of 55= | 110111 | decimal_to_binary |
| 15 | Binary to Decimal | 01101001 | 105 | binary_to_decimal |
| 16 | Fraction Division | (1/2)/(7/10) | 5/7 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 7 * [[4, 2], [5, 0]] =  | [[28,14],[35,0]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 15 12 8 =  | 47.811478747263195 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 23, 29 and 35 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (8,-2),(-11,-1)= | (-1.5,-1.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+6x+5 | (x+5)(x+1) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 39 and 12 =  | 129 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | 9x + 7y = 14, -6x - 2y = -28 | x = 7, y = -7 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (3, -6) and (3, -5) | sqrt(1) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 7 and 8 =  | 10.63 | pythagorean_theorem |
| 26 | Linear Equations | -5x + -5y = 90, -7x + 4y = 137 | x = -19, y = 1 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 10 | [2, 5] | prime_factors |
| 28 | Fraction Multiplication | (2/9)*(8/10) | 8/45 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 14 sides | 154.29 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 18 objects picked 6 at a time  | 18564 | combinations |
| 31 | Factorial | 3! =  | 6 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 18m is | 1944 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 12m, 13m, 1m is | 362 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 17m and radius = 17m is | 3631 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 16m is | 4096 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 7m, 13m, 14m is | 1274 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 2m and radius = 1m is | 6 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 4m and radius = 6m is | 249 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 39m and radius = 15m is | 9189 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 30 and 61 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 6/6x + 7 and y = 4x + 9 | (-2/3, 19/3) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 15 objects picked 9 at a time =   | 1816214400 | permutation |
| 43 | Cross Product of 2 Vectors | [-10, 6, 12] X [-6, 4, 1] =  | [-42, -62, -4] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 10/1 and 4/6? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 9743 dollars, 1% rate of interest and for a time period of 5 years is =  | 487.15 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>-4</td><td>-8</td></tr><tr><td>-4</td><td>-10</td></tr></table>and<table><tr><td>-5</td><td>9</td></tr><tr><td>7</td><td>-6</td></tr></table> | <table><tr><td>-36</td><td>12</td></tr><tr><td>-50</td><td>24</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 439 upto 2 decimal places is: | 7.6 | cube_root |
| 48 | Power Rule Integration | 2x^1 + 7x^4 + 10x^9 + 6x^10 | (2/1)x^2 + (7/4)x^5 + (10/9)x^10 + (6/10)x^11 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 148 , 57, 12 = | 143 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 72x^2+137x+32=0 | [-0.27, -1.63] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 17 and 1 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 2 dice are rolled at the same time, the probability of getting a sum of 2 = | 1/36 | dice_sum_probability |
| 53 | Exponentiation | 18^1 = | 18 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [268, 237, 275, 264, 256, 215, 225, 294, 286, 283, 239, 219, 287, 262, 241, 223, 273, 279, 206, 274, 228, 236, 252, 285, 212, 229, 254, 295, 244, 232, 211, 213, 210, 227, 255, 280] with 95% confidence is | (258.07181132546515, 240.20596645231262) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 95^(1/2) _ 45^(1/5) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 2 numbers is ? | [0, 1] | fibonacci_series |
| 57 | Trigonometric Values | What is cos(90)? | 0 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 4 sides =  | 360 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[30, 16, 18, 10, 10, 21, 8, 27, 37, 8, 12, 25, 20, 9, 24] | The Mean is 18.333333333333332 , Standard Deviation is 75.42222222222222, Variance is 8.684596837057102 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 8m is | 804.247719318987 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 42 m =  | 310339.08869221417 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 92th Fibonacci number? | 7540113804746369024 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 923 and SP = 973 is:  | 5.417118093174431 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 011010110 | 0xd6 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (7+3j) * (9-10j) =  | (93-43j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [9, 36, 144, 576, 2304, 9216] ,Find the value of a,common ratio,8th term value, sum upto 7th term | The value of a is 9, common ratio is 4 , 8th term is 147456 , sum upto 7th term is 49149.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 3 numbers 96 , 22 and 75 =  | (96*22*75)^(1/3) = 54.1067845799048 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 14 and 99 =  |  2/((1/14) + (1/99)) = 24.530973451327437 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[13.74350761660692, 579.8164944254971, 343.9004348023842, 447.91085049813904, 242.73436069826982, 677.824056340719, 908.0309446289546, 143.65153181819267, 268.05852693335817, 63.42979841101859] is: | 1447.2967158340782 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [554.45, 891.65, 845.2, 235.2, 741.43, 734.84, 92.76, 941.97, 885.6, 436.2, 476.49, 836.42, 743.03, 728.97, 963.3, 802.39] and [980.7, 745.14, 384.18, 452.88, 815.24, 725.39, 887.21, 828.72, 786.58, 990.6, 496.01, 439.13, 947.39, 737.59, 293.98, 880.62] is: | 0.5 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 88 and -73 =  | 161 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [-14, -2, 13] . [0, -18, -2] =  | 10 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of  = |  | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[53, 17, 67], [59, 72, 87], [2, 51, 61]]) is: | Matrix([[-9/26269, 476/26269, -669/26269], [-685/26269, 3099/131345, -658/131345], [573/26269, -2669/131345, 2813/131345]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 44 and angle, 279. Find the area of the sector. | Area of sector = 4713.64562 | sector_area |
| 76 | Mean and Median | Given the series of numbers [67, 20, 53, 42, 74, 89, 54, 4, 37, 49]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 48.9 and Arithmetic median of this series is 51.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[44, 92], [88, 57]]) =  |  -5588 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 3765 dollars, 5% rate of interest and for a time period of 1 year is =  | 3953.25 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 324= | 0x144 | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 45% of 71? | Required percentage = 31.95% | percentage |
| 81 | Celsius To Fahrenheit | Convert 0 degrees Celsius to degrees Fahrenheit = | 32.0 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 6 of the AP series: 29, -38, -105 ...  | -306 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 50 terms of the AP series: -90, -141, -192 ...  | -66975.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 84 in Octal is:  | 0o124 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 1646 in Roman Numerals is:  | MDCXLVI | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 294 in radians is =  | 5.13 | degree_to_rad |
| 87 | Radians to Degrees | Angle 0 in degrees is =  | 0.0 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(exp(x)+2*x^(-4))/dx | exp(x) - 8/x^5 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 100x^2 + 44x + 23 is =  | 78.3333 | definite_integral |
| 90 | isprime | 99 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 7 is =  | 29969 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 22.67exp(i2.42) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={8, 1, 4, 7} ,b={1, 2, 4, 7}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 2, 4, 7, 8},Intersection is {1, 4, 7}, a-b is {8},b-a is {2}, Symmetric difference is {2, 8} | set_operation |
| 94 | Base Conversion | Convert 344333 from base 6 to base 4. | 13031001 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 1 and height, 69? | CSA of cylinder = 433.54 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 8 sided polygon with lengths of [88, 89, 103, 89, 98, 88, 114, 70]cm is:  | 739 | perimeter_of_polygons |
| 97 | Power of Powers | The 44^6^10 = 44^(6*10) = 44^60 | 404725519480944371837890113388236472786198610068547182641046982530192155481830472108593384496562176 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 26^7 and 26^10 = 26^(7-10) = 26^-3 | 5.689576695493855e-05 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 3^10 and 5^10 = (3/5)^10 = 0.6^10 | 0.006046617599999997 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation x^2 + 8x + 1 = 0 | simplified solution : ((-0.127, -7.873)), generalized solution : ((-8 + sqrt(60))/2*1, (-8 - sqrt(60))/2*1) | complex_quadratic |
| 101 | Leap Year or Not | Year 1932  | is a leap year | is_leap_year |
| 102 | Minute to Hour conversion | Convert 751 minutes to Hours & Minutes | 12 hours and 31 minutes | minutes_to_hours |
