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
| 0 | Addition | 46+4= | 50 | addition |
| 1 | Subtraction | 63-13= | 50 | subtraction |
| 2 | Multiplication | 25*0= | 0 | multiplication |
| 3 | Division | 66/99= | 0.6666666666666666 | division |
| 4 | Binary Complement 1s | 011101111= | 100010000 | binary_complement_1s |
| 5 | Modulo Division | 50%72= | 50 | modulo_division |
| 6 | Square Root | sqrt(9)= | 3 | square_root |
| 7 | Power Rule Differentiation | 5x^8 + 8x^1 + 5x^2 + 7x^9 + 9x^6 | 40x^7 + 8x^0 + 10x^1 + 63x^8 + 54x^5 | power_rule_differentiation |
| 8 | Square | 12^2= | 144 | square |
| 9 | LCM (Least Common Multiple) | LCM of 14 and 12 = | 84 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 9 and 20 =  | 1 | gcd |
| 11 | Basic Algebra | 9x + 7 = 10 | 1/3 | basic_algebra |
| 12 | Logarithm | log2(16) | 4 | log |
| 13 | Easy Division | 120/24 =  | 5 | int_division |
| 14 | Decimal to Binary | Binary of 27= | 11011 | decimal_to_binary |
| 15 | Binary to Decimal | 1101100000 | 864 | binary_to_decimal |
| 16 | Fraction Division | (2/10)/(10/8) | 4/25 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 16 * [[1, 1], [5, 0]] =  | [[16,16],[80,0]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 18 11 18 =  | 94.26525075551436 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 10, 26 and 25 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (9,-6),(-9,-18)= | (0.0,-12.0) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+3x+2 | (x+1)(x+2) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 18 and 24 =  | 138 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -8x + 5y = 33, 7x - 3y = -33 | x = -6, y = -3 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-3, -18) and (6, -17) | sqrt(82) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 19 and 3 =  | 19.24 | pythagorean_theorem |
| 26 | Linear Equations | -6x + -19y = 42, -20x + -14y = 140 | x = -7, y = 0 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 193 | [193] | prime_factors |
| 28 | Fraction Multiplication | (5/4)*(7/10) | 7/8 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 11 sides | 147.27 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 17 objects picked 3 at a time  | 680 | combinations |
| 31 | Factorial | 2! =  | 2 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 16m is | 1536 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 1m, 2m, 7m is | 46 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 37m and radius = 11m is | 3317 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 5m is | 125 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 2m, 20m, 8m is | 320 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 25m and radius = 5m is | 1963 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 14m and radius = 4m is | 233 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 33m and radius = 17m is | 9987 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 29 and 41 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -2/2x + 3 and y = -10/2x - 1 | (-1, 4) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 18 objects picked 9 at a time =   | 17643225600 | permutation |
| 43 | Cross Product of 2 Vectors | [-3, 6, -11] X [15, -16, 15] =  | [-86, -120, -42] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 4/8 and 9/7? | < | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 9046 dollars, 1% rate of interest and for a time period of 9 years is =  | 814.14 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>1</td><td>1</td><td>-1</td></tr><tr><td>-1</td><td>9</td><td>4</td></tr><tr><td>-10</td><td>3</td><td>-8</td></tr></table>and<table><tr><td>6</td><td>-4</td><td>6</td></tr><tr><td>0</td><td>7</td><td>5</td></tr><tr><td>2</td><td>7</td><td>-8</td></tr></table> | <table><tr><td>4</td><td>-4</td><td>19</td></tr><tr><td>2</td><td>95</td><td>7</td></tr><tr><td>-76</td><td>5</td><td>19</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 335 upto 2 decimal places is: | 6.95 | cube_root |
| 48 | Power Rule Integration | 1x^5 + 3x^1 | (1/5)x^6 + (3/1)x^2 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 64 , 57, 213 = | 26 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 96x^2+191x+81=0 | [-0.61, -1.38] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 15 and 12 =  | 3 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 1 dice are rolled at the same time, the probability of getting a sum of 2 = | 1/6 | dice_sum_probability |
| 53 | Exponentiation | 11^4 = | 14641 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [236, 288, 281, 252, 250, 254, 263, 228, 248, 245, 214, 221, 247, 235, 220, 286, 292, 242, 268, 215, 243, 283, 282, 212] with 99% confidence is | (263.2888975746178, 237.12776909204885) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 13^(1/4) _ 35^(1/1) | < | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 5 numbers is ? | [0, 1, 1, 2, 3] | fibonacci_series |
| 57 | Trigonometric Values | What is cos(30)? | √3/2 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 9 sides =  | 1260 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[45, 17, 14, 27, 12, 11, 13, 38, 14, 48, 38, 48, 30, 41, 36] | The Mean is 28.8 , Standard Deviation is 186.69333333333333, Variance is 13.663576886501328 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 2m is | 50.26548245743669 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 95 m =  | 3591364.0018287315 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 37th Fibonacci number? | 24157817 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 169 and SP = 360 is:  | 113.01775147928994 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 100010 | 0x22 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (12+17j) * (11-3j) =  | (183+151j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [10, 60, 360, 2160, 12960, 77760] ,Find the value of a,common ratio,11th term value, sum upto 7th term | The value of a is 10, common ratio is 6 , 11th term is 604661760 , sum upto 7th term is 559870.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 16 , 99 , 82 , 40 =  | (16*99*82*40)^(1/4) = 47.742730688054316 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 4 numbers 64 , 21 , 60 , 61 =  |  4/((1/64) + (1/21) + (1/60) + (1/61)) = 41.53507105403146 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[508.56178681813515, 829.8393085389811, 141.9778436425696, 157.79854813315953, 936.4111703191011, 60.03432095552797, 309.1650693726604, 532.5680163890804, 249.7649337521495, 693.033334449361, 726.1934281438319, 824.6613026949497, 40.71867012843633] is: | 2000.941549572921 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [108.86, 442.35, 675.26, 315.79, 885.28, 45.3, 892.33, 447.4] and [987.81, 887.54, 199.52, 477.21, 587.71, 963.72, 615.65, 226.26] is: | 0.87 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -55 and 41 =  | 96 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [19, -17, -13] . [-16, 11, 5] =  | -556 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 100 = | 100 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[65, 2, 89], [51, 73, 27], [48, 19, 39]]) is: | Matrix([[-778/25097, -1613/75291, 6443/75291], [231/25097, 579/25097, -928/25097], [845/25097, 1139/75291, -4643/75291]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 15 and angle, 33. Find the area of the sector. | Area of sector = 64.79535 | sector_area |
| 76 | Mean and Median | Given the series of numbers [68, 8, 77, 86, 93, 66, 6, 65, 41, 26]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 53.6 and Arithmetic median of this series is 65.5 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[32, 3], [36, 4]]) =  |  20 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 7744 dollars, 10% rate of interest and for a time period of 2 year is =  | 9370.24 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 803= | 0x323 | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 24% of 7? | Required percentage = 1.68% | percentage |
| 81 | Celsius To Fahrenheit | Convert 50 degrees Celsius to degrees Fahrenheit = | 122.0 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 38 of the AP series: 37, -6, -49 ...  | -1554 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 50 terms of the AP series: -23, 65, 153 ...  | 106650.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 1900 in Octal is:  | 0o3554 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 2656 in Roman Numerals is:  | MMDCLVI | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 184 in radians is =  | 3.21 | degree_to_rad |
| 87 | Radians to Degrees | Angle 0 in degrees is =  | 0.0 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(tan(x)+9*x^4)/dx | 36*x^3 + tan(x)^2 + 1 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 93x^2 + 7x + 75 is =  | 109.5 | definite_integral |
| 90 | isprime | 96 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 7 is =  | 29973 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 15.65exp(i0.46) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={8, 10, 3, 7} ,b={2, 4, 7, 9, 10}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {2, 3, 4, 7, 8, 9, 10},Intersection is {10, 7}, a-b is {8, 3},b-a is {9, 2, 4}, Symmetric difference is {2, 3, 4, 8, 9} | set_operation |
| 94 | Base Conversion | Convert 3540 from base 10 to base 14. | 140C | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 48 and height, 64? | CSA of cylinder = 19301.95 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 3 sided polygon with lengths of [23, 3, 55]cm is:  | 81 | perimeter_of_polygons |
| 97 | Power of Powers | The 9^5^2 = 9^(5*2) = 9^10 | 3486784401 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 40^3 and 40^5 = 40^(3-5) = 40^-2 | 0.000625 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 49^1 and 19^1 = (49/19)^1 = 2.5789473684210527^1 | 2.5789473684210527 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation 6x^2 + 8x + 1 = 0 | simplified solution : ((-0.14, -1.194)), generalized solution : ((-8 + sqrt(40))/2*6, (-8 - sqrt(40))/2*6) | complex_quadratic |
| 101 | Leap Year or Not | Year 2064  | is a leap year | is_leap_year |
| 102 | Minute to Hour conversion | Convert 442 minutes to Hours & Minutes | 7 hours and 22 minutes | minutes_to_hours |
| 103 | Decimal to Binary Coded Decimal | BCD of Decimal Number 5507 is =  | 1583 | decimal_to_bcd |
| 104 | Circumference | Circumference of circle with radius 94 | 590.6194188748811 | circumference |
| 105 | Combine Like terms | 9x^4 + 3x^6 + 9x^1 + 2x^2 + 1x^5 + 2x^3 + 6x^3 + 4x^1 | 13x^1 + 2x^2 + 8x^3 + 9x^4 + 1x^5 + 3x^6  | combine_like_terms |
| 106 | signum function | signum of 697 is = | 1 | signum_function |
| 107 | Conditional Probability | Someone tested positive for a nasty disease which only 1.51% of population have. Test sensitivity (true positive) is equal to SN= 94.60% whereas test specificity (true negative) SP= 93.00%. What is the probability that this guy really has that disease? | 17.16% | conditional_probability |
