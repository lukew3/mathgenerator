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
| 0 | Addition | 14+24= | 38 | addition |
| 1 | Subtraction | 71-17= | 54 | subtraction |
| 2 | Multiplication | 71*1= | 71 | multiplication |
| 3 | Division | 98/53= | 1.849056603773585 | division |
| 4 | Binary Complement 1s | 000001000= | 111110111 | binary_complement_1s |
| 5 | Modulo Division | 19%62= | 19 | modulo_division |
| 6 | Square Root | sqrt(25)= | 5 | square_root |
| 7 | Power Rule Differentiation | 6x^9 + 5x^2 + 1x^7 + 5x^7 | 54x^8 + 10x^1 + 7x^6 + 35x^6 | power_rule_differentiation |
| 8 | Square | 10^2= | 100 | square |
| 9 | LCM (Least Common Multiple) | LCM of 2 and 12 = | 12 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 2 and 14 =  | 2 | gcd |
| 11 | Basic Algebra | 2x + 9 = 9 | 0 | basic_algebra |
| 12 | Logarithm | log3(3) | 1 | log |
| 13 | Easy Division | 204/17 =  | 12 | int_division |
| 14 | Decimal to Binary | Binary of 61= | 111101 | decimal_to_binary |
| 15 | Binary to Decimal | 10101 | 21 | binary_to_decimal |
| 16 | Fraction Division | (8/2)/(5/3) | 12/5 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 3 * [[10, 1], [1, 1]] =  | [[30,3],[3,3]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 4 10 16 =  | (1.7587650643960612e-15+28.722813232690143j) | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 8, 29 and 19 exist? | No | valid_triangle |
| 20 | Midpoint of the two point | (-16,7),(11,-1)= | (-2.5,3.0) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+18x+80 | (x+10)(x+8) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 75 and 36 =  | 69 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | 6x + y = 25, 6x - 7y = -31 | x = 3, y = 7 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-18, 12) and (5, 9) | sqrt(538) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 9 and 15 =  | 17.49 | pythagorean_theorem |
| 26 | Linear Equations | -8x + 2y = 12, 1x + 11y = -24 | x = -2, y = -2 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 103 | [103] | prime_factors |
| 28 | Fraction Multiplication | (5/9)*(3/5) | 1/3 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 17 sides | 158.82 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 13 objects picked 7 at a time  | 1716 | combinations |
| 31 | Factorial | 4! =  | 24 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 9m is | 486 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 2m, 16m, 11m is | 460 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 5m and radius = 14m is | 1671 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 17m is | 4913 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 18m, 5m, 19m is | 1710 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 40m and radius = 4m is | 2010 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 28m and radius = 17m is | 2657 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 45m and radius = 8m is | 3015 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 83 and 21 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 0/5x + 1 and y = 5/5x - 5 | (6, 1) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 10 objects picked 8 at a time =   | 1814400 | permutation |
| 43 | Cross Product of 2 Vectors | [-14, -20, 15] X [12, -11, 11] =  | [-55, 334, 394] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 7/5 and 5/8? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 9940 dollars, 6% rate of interest and for a time period of 5 years is =  | 2982.0 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>10</td><td>2</td></tr><tr><td>-8</td><td>0</td></tr></table>and<table><tr><td>3</td><td>-4</td><td>1</td><td>5</td></tr><tr><td>-1</td><td>1</td><td>-10</td><td>-1</td></tr></table> | <table><tr><td>28</td><td>-38</td><td>-10</td><td>48</td></tr><tr><td>-24</td><td>32</td><td>-8</td><td>-40</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 25 upto 2 decimal places is: | 2.92 | cube_root |
| 48 | Power Rule Integration | 2x^4 + 9x^10 + 7x^1 + 5x^10 + 3x^7 | (2/4)x^5 + (9/10)x^11 + (7/1)x^2 + (5/10)x^11 + (3/7)x^8 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 61 , 128, 38 = | 133 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 22x^2+199x+24=0 | [-0.12, -8.92] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 1 and 1 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 1 dice are rolled at the same time, the probability of getting a sum of 6 = | 1/6 | dice_sum_probability |
| 53 | Exponentiation | 2^10 = | 1024 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [200, 254, 212, 257, 239, 235, 250, 203, 227, 281, 275, 291, 224, 216, 249, 293, 266, 264, 278, 265] with 80% confidence is | (256.9254800588742, 240.97451994112578) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 59^(1/6) _ 50^(1/8) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 3 numbers is ? | [0, 1, 1] | fibonacci_series |
| 57 | Trigonometric Values | What is tan(45)? | 1 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 12 sides =  | 1800 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[28, 23, 25, 46, 36, 42, 48, 40, 23, 21, 32, 25, 41, 43, 35] | The Mean is 33.86666666666667 , Standard Deviation is 79.18222222222222, Variance is 8.898439313847245 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 19m is | 4536.459791783661 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 51 m =  | 555647.2094551196 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 55th Fibonacci number? | 139583862445 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 777 and SP = 861 is:  | 10.81081081081081 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 001 | 0x1 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (16-6j) * (2+2j) =  | (44+20j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [4, 32, 256, 2048, 16384, 131072] ,Find the value of a,common ratio,6th term value, sum upto 7th term | The value of a is 4, common ratio is 8 , 6th term is 131072 , sum upto 7th term is 1198372.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 45 , 3 , 1 , 97 =  | (45*3*1*97)^(1/4) = 10.69735419328368 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 4 numbers 45 , 38 , 75 , 60 =  |  4/((1/45) + (1/38) + (1/75) + (1/60)) = 50.9307520476545 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[591.4087216014599, 881.9117537447569, 886.791583815644, 686.4762274423125, 908.6374557556007, 623.6706969012301, 457.24550363026395] is: | 1951.6255163618057 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [441.74, 751.22, 829.23] and [983.73, 131.61, 537.34] is: | 0.77 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -72 and 18 =  | 90 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [-19, 18, 12] . [18, -13, -17] =  | -780 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 1001000001 = | 110111111 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[61, 3, 14], [4, 5, 7], [13, 8, 95]]) is: | Matrix([[419/24230, -173/24230, -49/24230], [-289/24230, 5613/24230, -371/24230], [-33/24230, -449/24230, 293/24230]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 39 and angle, 161. Find the area of the sector. | Area of sector = 2136.98986 | sector_area |
| 76 | Mean and Median | Given the series of numbers [52, 72, 62, 2, 15, 95, 33, 55, 66, 32]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 48.4 and Arithmetic median of this series is 53.5 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[16, 57], [90, 67]]) =  |  -4058 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 3519 dollars, 2% rate of interest and for a time period of 4 year is =  | 3809.08 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 593= | 0x251 | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 11% of 83? | Required percentage = 9.13% | percentage |
| 81 | Celsius To Fahrenheit | Convert -3 degrees Celsius to degrees Fahrenheit = | 26.6 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 87 of the AP series: -37, 4, 45 ...  | 3489 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 91 terms of the AP series: 62, 29, -4 ...  | -129493.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 432 in Octal is:  | 0o660 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 2876 in Roman Numerals is:  | MMDCCCLXXVI | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 307 in radians is =  | 5.36 | degree_to_rad |
| 87 | Radians to Degrees | Angle 2 in degrees is =  | 114.59 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(sin(x)+2*x^(-4))/dx | cos(x) - 8/x^5 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 24x^2 + 30x + 41 is =  | 64.0 | definite_integral |
| 90 | isprime | 10 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 1 is =  | 4436 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 18.0exp(i1.57) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={9, 2, 3} ,b={1, 2, 5, 7, 8, 9}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 2, 3, 5, 7, 8, 9},Intersection is {9, 2}, a-b is {3},b-a is {8, 1, 5, 7}, Symmetric difference is {1, 3, 5, 7, 8} | set_operation |
| 94 | Base Conversion | Convert 23750 from base 10 to base 16. | 5CC6 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 36 and height, 11? | CSA of cylinder = 2488.14 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 12 sided polygon with lengths of [18, 104, 35, 2, 48, 4, 80, 48, 114, 28, 30, 18]cm is:  | 529 | perimeter_of_polygons |
| 97 | Power of Powers | The 21^7^10 = 21^(7*10) = 21^70 | 359211830356099179055407266181227770855602632046883281967355597156308256906315688053426887401 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 20^7 and 20^8 = 20^(7-8) = 20^-1 | 0.05 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 8^5 and 29^5 = (8/29)^5 = 0.27586206896551724^5 | 0.0015975701800030801 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation x^2 + 7x + 9 = 0 | simplified solution : ((-1.697, -5.303)), generalized solution : ((-7 + sqrt(13))/2*1, (-7 - sqrt(13))/2*1) | complex_quadratic |
| 101 | Leap Year or Not | Year 1916  | is a leap year | is_leap_year |
| 102 | Minute to Hour conversion | Convert 913 minutes to Hours & Minutes | 15 hours and 13 minutes | minutes_to_hours |
| 103 | Decimal to Binary Coded Decimal | BCD of Decimal Number 3865 is =  | 1519 | decimal_to_bcd |
| 104 | Circumference | Circumference of circle with radius 41 | 257.610597594363 | circumference |
| 105 | Combine Like terms | 5x^1 + 5x^1 | 10x^1  | combine_like_terms |
| 106 | signum function | signum of -580 is = | -1 | signum_function |
| 107 | Conditional Probability | Someone tested positive for a nasty disease which only 1.53% of population have. Test sensitivity (true positive) is equal to SN= 90.63% whereas test specificity (true negative) SP= 95.99%. What is the probability that this guy really has that disease? | 25.99% | conditional_probability |
| 108 | Arc length of Angle | Given radius, 4 and angle, 18. Find the arc length of the angle. | Arc length of the angle = 1.25664 | arc_length |
