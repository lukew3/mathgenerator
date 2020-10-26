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
| 0 | Addition | 10+48= | 58 | addition |
| 1 | Subtraction | 92-21= | 71 | subtraction |
| 2 | Multiplication | 89*0= | 0 | multiplication |
| 3 | Division | 9/11= | 0.8181818181818182 | division |
| 4 | Binary Complement 1s | 11001= | 00110 | binary_complement_1s |
| 5 | Modulo Division | 45%50= | 45 | modulo_division |
| 6 | Square Root | sqrt(25)= | 5 | square_root |
| 7 | Power Rule Differentiation | 3x^8 + 3x^3 + 8x^4 + 8x^8 + 8x^5 | 24x^7 + 9x^2 + 32x^3 + 64x^7 + 40x^4 | power_rule_differentiation |
| 8 | Square | 3^2= | 9 | square |
| 9 | LCM (Least Common Multiple) | LCM of 13 and 16 = | 208 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 1 and 20 =  | 1 | gcd |
| 11 | Basic Algebra | 4x + 2 = 9 | 7/4 | basic_algebra |
| 12 | Logarithm | log2(8) | 3 | log |
| 13 | Easy Division | 10/5 =  | 2 | int_division |
| 14 | Decimal to Binary | Binary of 89= | 1011001 | decimal_to_binary |
| 15 | Binary to Decimal | 00011010 | 26 | binary_to_decimal |
| 16 | Fraction Division | (5/9)/(5/1) | 1/9 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 9 * [[7, 6], [0, 3]] =  | [[63,54],[0,27]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 7 6 9 =  | 20.97617696340303 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 1, 9 and 28 exist? | No | valid_triangle |
| 20 | Midpoint of the two point | (11,-12),(-16,-17)= | (-2.5,-14.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+6x-7 | (x-1)(x+7) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 76 and 64 =  | 40 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -3x - 7y = -56, -8x + 5y = 40 | x = 0, y = 8 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-14, 5) and (9, -4) | sqrt(610) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 9 and 9 =  | 12.73 | pythagorean_theorem |
| 26 | Linear Equations | 15x = -75, 15x + -10y = -35 | x = -5, y = -4 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 101 | [101] | prime_factors |
| 28 | Fraction Multiplication | (6/2)*(10/4) | 15/2 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 12 sides | 150.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 13 objects picked 6 at a time  | 1716 | combinations |
| 31 | Factorial | 6! =  | 720 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 11m is | 726 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 18m, 14m, 3m is | 696 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 28m and radius = 16m is | 4423 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 8m is | 512 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 17m, 11m, 18m is | 3366 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 45m and radius = 7m is | 6927 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 19m and radius = 8m is | 719 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 44m and radius = 11m is | 5575 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 51 and 44 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -7/3x - 5 and y = -1/2x - 8 | (18/11, -97/11) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 14 objects picked 3 at a time =   | 2184 | permutation |
| 43 | Cross Product of 2 Vectors | [-12, 13, 1] X [-19, 11, 14] =  | [171, 149, 115] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 3/8 and 6/9? | < | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 8192 dollars, 2% rate of interest and for a time period of 2 years is =  | 327.68 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>2</td><td>5</td></tr><tr><td>-10</td><td>-5</td></tr><tr><td>9</td><td>9</td></tr></table>and<table><tr><td>4</td><td>-5</td></tr><tr><td>-10</td><td>-3</td></tr></table> | <table><tr><td>-42</td><td>-25</td></tr><tr><td>10</td><td>65</td></tr><tr><td>-54</td><td>-72</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 694 upto 2 decimal places is: | 8.85 | cube_root |
| 48 | Power Rule Integration | 1x^3 + 9x^3 | (1/3)x^4 + (9/3)x^4 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 18 , 32, 236 = | 74 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 75x^2+121x+43=0 | [-0.53, -1.08] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 19 and 10 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 2 dice are rolled at the same time, the probability of getting a sum of 9 = | 4/36 | dice_sum_probability |
| 53 | Exponentiation | 2^10 = | 1024 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [235, 266, 205, 259, 244, 267, 261, 275, 248, 210, 287, 297, 212, 272, 228, 271, 249, 225, 280, 298, 237] with 90% confidence is | (263.3453075787769, 243.89278765931834) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 29^(1/8) _ 89^(1/9) | < | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 6 numbers is ? | [0, 1, 1, 2, 3, 5] | fibonacci_series |
| 57 | Trigonometric Values | What is tan(60)? | √3 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 3 sides =  | 180 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[27, 39, 33, 10, 44, 14, 37, 17, 40, 35, 19, 11, 17, 6, 13] | The Mean is 24.133333333333333 , Standard Deviation is 152.91555555555553, Variance is 12.365902941376968 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 11m is | 1520.5308443374597 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 66 m =  | 1204260.4287152681 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 69th Fibonacci number? | 117669030460994 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 652 and SP = 967 is:  | 48.31288343558282 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 011011000 | 0xd8 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (17+16j) * (-3-3j) =  | (-3-99j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [10, 70, 490, 3430, 24010, 168070] ,Find the value of a,common ratio,9th term value, sum upto 9th term | The value of a is 10, common ratio is 7 , 9th term is 57648010 , sum upto 9th term is 67256010.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 3 numbers 58 , 73 and 52 =  | (58*73*52)^(1/3) = 60.383469885511204 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 91 and 18 =  |  2/((1/91) + (1/18)) = 30.055045871559635 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[974.3536143874146, 686.168356481633, 586.22520680975] is: | 1328.1008893926917 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [700.08, 521.5, 513.19, 926.02, 781.96, 37.1, 485.31, 966.82, 811.5, 183.45, 703.93, 628.34, 756.44, 387.15, 771.41, 169.39, 48.66, 615.09] and [768.58, 809.43, 824.23, 109.11, 557.91, 3.33, 483.09, 188.14, 557.91, 655.56, 760.95, 864.19, 470.75, 149.17, 541.68, 615.69, 53.59, 859.28] is: | 0.6 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 15 and -2 =  | 17 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [17, -6, 10] . [-15, 17, -2] =  | -377 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 1001 = | 111 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[70, 89, 73], [36, 43, 66], [96, 99, 13]]) is: | Matrix([[-1195/12566, 607/6283, 547/12566], [2934/31415, -3049/31415, -996/31415], [-282/31415, 807/31415, -97/31415]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 32 and angle, 157. Find the area of the sector. | Area of sector = 1402.96547 | sector_area |
| 76 | Mean and Median | Given the series of numbers [81, 67, 6, 16, 98, 69, 28, 60, 56, 20]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 50.1 and Arithmetic median of this series is 58.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[88, 11], [75, 32]]) =  |  1991 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 7240 dollars, 10% rate of interest and for a time period of 7 year is =  | 14108.71 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 181= | 0xb5 | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 93% of 67? | Required percentage = 62.31% | percentage |
| 81 | Celsius To Fahrenheit | Convert -9 degrees Celsius to degrees Fahrenheit = | 15.8 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 93 of the AP series: 16, -72, -160 ...  | -8080 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 40 terms of the AP series: 79, 111, 143 ...  | 28120.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 453 in Octal is:  | 0o705 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 492 in Roman Numerals is:  | CDXCII | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 146 in radians is =  | 2.55 | degree_to_rad |
| 87 | Radians to Degrees | Angle 3 in degrees is =  | 171.89 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(ln(x)+6*x^(-2))/dx | 1/x - 12/x^3 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 97x^2 + 21x + 68 is =  | 110.8333 | definite_integral |
| 90 | isprime | 100 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 4 is =  | 18071 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 20.25exp(i-1.22) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={1, 3, 4, 6, 7, 8} ,b={8, 1, 3, 5}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 3, 4, 5, 6, 7, 8},Intersection is {8, 1, 3}, a-b is {4, 6, 7},b-a is {5}, Symmetric difference is {4, 5, 6, 7} | set_operation |
| 94 | Base Conversion | Convert 33792 from base 10 to base 8. | 102000 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 12 and height, 87? | CSA of cylinder = 6559.65 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 11 sided polygon with lengths of [82, 107, 53, 3, 14, 47, 106, 22, 90, 87, 22]cm is:  | 633 | perimeter_of_polygons |
| 97 | Power of Powers | The 37^1^5 = 37^(1*5) = 37^5 | 69343957 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 46^3 and 46^7 = 46^(3-7) = 46^-4 | 2.2334111155977858e-07 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 40^3 and 20^3 = (40/20)^3 = 2.0^3 | 8.0 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation 2x^2 + 6x + 1 = 0 | simplified solution : ((-0.177, -2.823)), generalized solution : ((-6 + sqrt(28))/2*2, (-6 - sqrt(28))/2*2) | complex_quadratic |
| 101 | Leap Year or Not | Year 1929  | is not a leap year | is_leap_year |
| 102 | Minute to Hour conversion | Convert 793 minutes to Hours & Minutes | 13 hours and 13 minutes | minutes_to_hours |
| 103 | Decimal to Binary Coded Decimal | BCD of Decimal Number 9170 is =  | 23132 | decimal_to_bcd |
| 104 | Circumference | Circumference of circle with radius 10 | 62.83185307179586 | circumference |
| 105 | Combine Like terms | 6x^1 + 3x^2 + 6x^2 | 6x^1 + 9x^2  | combine_like_terms |
| 106 | signum function | signum of 281 is = | 1 | signum_function |
| 107 | Conditional Probability | Someone tested positive for a nasty disease which only 1.44% of population have. Test sensitivity (true positive) is equal to SN= 93.49% whereas test specificity (true negative) SP= 94.85%. What is the probability that this guy really has that disease? | 20.96% | conditional_probability |
| 108 | Arc length of Angle | Given radius, 42 and angle, 114. Find the arc length of the angle. | Arc length of the angle = 83.56636 | arc_length |
| 109 | Binomial distribution | A manufacturer of metal pistons finds that, on average, 40.72% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 13 pistons will contain no more than 7 rejected pistons? | 89.26 | binomial_distribution |
