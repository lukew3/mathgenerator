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
| 0 | Addition | 31+18= | 49 | addition |
| 1 | Subtraction | 6-2= | 4 | subtraction |
| 2 | Multiplication | 5*17= | 85 | multiplication |
| 3 | Division | 38/33= | 1.1515151515151516 | division |
| 4 | Binary Complement 1s | 0000010101= | 1111101010 | binary_complement_1s |
| 5 | Modulo Division | 55%0= | 0 | modulo_division |
| 6 | Square Root | sqrt(4)= | 2 | square_root |
| 7 | Power Rule Differentiation | 6x^9 | 54x^8 | power_rule_differentiation |
| 8 | Square | 12^2= | 144 | square |
| 9 | LCM (Least Common Multiple) | LCM of 11 and 11 = | 11 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 15 and 14 =  | 1 | gcd |
| 11 | Basic Algebra | 5x + 6 = 6 | 0 | basic_algebra |
| 12 | Logarithm | log2(256) | 8 | log |
| 13 | Easy Division | 315/15 =  | 21 | int_division |
| 14 | Decimal to Binary | Binary of 93= | 1011101 | decimal_to_binary |
| 15 | Binary to Decimal | 111 | 7 | binary_to_decimal |
| 16 | Fraction Division | (10/5)/(6/9) | 3 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 6 * [[10, 9], [10, 1]] =  | [[60,54],[60,6]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 18 4 19 =  | 35.6151302117513 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 24, 16 and 17 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (10,-8),(1,-1)= | (5.5,-4.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+5x+4 | (x+4)(x+1) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 65 and 24 =  | 91 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -4x - 2y = -42, 3x + 6y = 45 | x = 9, y = 3 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-2, -19) and (-10, 8) | sqrt(793) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 10 and 5 =  | 11.18 | pythagorean_theorem |
| 26 | Linear Equations | 12x + -15y = -288, 17x + -4y = -270 | x = -14, y = 8 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 162 | [2, 3, 3, 3, 3] | prime_factors |
| 28 | Fraction Multiplication | (8/5)*(6/3) | 16/5 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 19 sides | 161.05 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 15 objects picked 9 at a time  | 5005 | combinations |
| 31 | Factorial | 1! =  | 1 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 16m is | 1536 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 9m, 13m, 11m is | 718 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 34m and radius = 12m is | 3468 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 10m is | 1000 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 19m, 12m, 5m is | 1140 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 50m and radius = 7m is | 7696 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 14m and radius = 18m is | 2307 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 34m and radius = 5m is | 890 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 32 and 73 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 8/5x - 1 and y = 2/4x - 3 | (-20/11, -43/11) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 19 objects picked 9 at a time =   | 33522128640 | permutation |
| 43 | Cross Product of 2 Vectors | [-5, -11, -7] X [-11, -9, 17] =  | [-250, 162, -76] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 9/3 and 1/8? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 9909 dollars, 9% rate of interest and for a time period of 3 years is =  | 2675.43 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>-4</td><td>0</td></tr><tr><td>1</td><td>-9</td></tr><tr><td>8</td><td>3</td></tr></table>and<table><tr><td>-2</td><td>4</td><td>-5</td><td>-8</td></tr><tr><td>-4</td><td>9</td><td>8</td><td>1</td></tr></table> | <table><tr><td>8</td><td>-16</td><td>20</td><td>32</td></tr><tr><td>34</td><td>-77</td><td>-77</td><td>-17</td></tr><tr><td>-28</td><td>59</td><td>-16</td><td>-61</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 681 upto 2 decimal places is: | 8.8 | cube_root |
| 48 | Power Rule Integration | 8x^9 + 2x^3 | (8/9)x^10 + (2/3)x^4 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 155 , 8, 53 = | 144 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 29x^2+151x+87=0 | [-0.66, -4.55] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 2 and 7 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 3 dice are rolled at the same time, the probability of getting a sum of 18 = | 1/216 | dice_sum_probability |
| 53 | Exponentiation | 6^1 = | 6 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [276, 270, 278, 269, 201, 297, 206, 249, 202, 256, 231, 257, 294, 218, 245, 287, 212, 240, 290, 224, 237, 283, 216, 272, 281, 210, 207, 253, 258, 239, 233, 252, 259, 291] with 95% confidence is | (259.6528701903449, 239.93536510377274) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 56^(1/8) _ 24^(1/4) | < | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 17 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987] | fibonacci_series |
| 57 | Trigonometric Values | What is tan(90)? | ∞ | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 9 sides =  | 1260 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[39, 7, 46, 21, 41, 29, 27, 44, 47, 25, 42, 46, 36, 14, 20] | The Mean is 32.266666666666666 , Standard Deviation is 153.5288888888889, Variance is 12.390677499188206 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 20m is | 5026.548245743669 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 14 m =  | 11494.040321933857 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 97th Fibonacci number? | 83621143489848688640 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Loss percent when CP = 534 and SP = 142 is:  | 73.40823970037454 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 100101000 | 0x128 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (-12+12j) * (-13-18j) =  | (372+60j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [3, 33, 363, 3993, 43923, 483153] ,Find the value of a,common ratio,6th term value, sum upto 10th term | The value of a is 3, common ratio is 11 , 6th term is 483153 , sum upto 10th term is 7781227380.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 2 numbers 71 and 22 =  | (71*22)^(1/2) = 39.52214569073901 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 67 and 68 =  |  2/((1/67) + (1/68)) = 67.49629629629631 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[989.7678494916759, 897.0852535908015, 478.723813700917, 262.3640311459466, 3.9396467807750746, 807.7450450578759, 631.0200102495029, 231.8997162556714, 7.832244619406126, 986.8740956956434, 764.8397716335004, 156.12003232583328, 859.4725406552614, 658.9347671527104, 146.78083360953374, 799.2621622325604, 930.4734264992945, 779.3457539450127] is: | 2841.934815032343 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [54.78, 647.84, 558.26, 220.69, 895.33, 874.45, 614.25] and [245.71, 329.9, 763.1, 443.48, 56.7, 28.8, 820.93] is: | 0.89 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -52 and -30 =  | 22 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [-18, 20, 1] . [-14, 6, 7] =  | 379 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 1110011011 = | 1100101 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[29, 41, 11], [47, 59, 43], [31, 79, 83]]) is: | Matrix([[-125/3422, 1267/20532, -557/20532], [107/1711, -1033/20532, 365/20532], [-157/3422, 85/3422, 9/1711]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 6 and angle, 133. Find the area of the sector. | Area of sector = 41.78318 | sector_area |
| 76 | Mean and Median | Given the series of numbers [51, 66, 3, 85, 46, 45, 31, 93, 95, 7]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 52.2 and Arithmetic median of this series is 48.5 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[70, 9], [23, 30]]) =  |  1893 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 5669 dollars, 7% rate of interest and for a time period of 5 year is =  | 7951.07 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 906= | 0x38a | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 41% of 37? | Required percentage = 15.17% | percentage |
| 81 | Celsius To Fahrenheit | Convert -21 degrees Celsius to degrees Fahrenheit = | -5.800000000000004 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 44 of the AP series: -12, 23, 58 ...  | 1493 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 14 terms of the AP series: 15, -18, -51 ...  | -2793.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 1517 in Octal is:  | 0o2755 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 3971 in Roman Numerals is:  | MMMCMLXXI | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 292 in radians is =  | 5.1 | degree_to_rad |
| 87 | Radians to Degrees | Angle 3 in degrees is =  | 171.89 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(exp(x)+3*x^2)/dx | 6*x + exp(x) | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 35x^2 + 35x + 12 is =  | 41.1667 | definite_integral |
| 90 | isprime | 98 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 6 is =  | 25496 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 22.2exp(i2.52) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={8, 9, 2, 7} ,b={1, 4}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 2, 4, 7, 8, 9},Intersection is set(), a-b is {8, 9, 2, 7},b-a is {1, 4}, Symmetric difference is {1, 2, 4, 7, 8, 9} | set_operation |
| 94 | Base Conversion | Convert 38238 from base 10 to base 2. | 1001010101011110 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 30 and height, 20? | CSA of cylinder = 3769.91 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 9 sided polygon with lengths of [90, 21, 55, 45, 23, 95, 62, 15, 111]cm is:  | 517 | perimeter_of_polygons |
| 97 | Power of Powers | The 28^9^5 = 28^(9*5) = 28^45 | 132468131465955881734001738124033446011491012025292784170872864768 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 17^2 and 17^2 = 17^(2-2) = 17^0 | 1 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 33^8 and 33^8 = (33/33)^8 = 1.0^8 | 1.0 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation 3x^2 + 7x + 4 = 0 | simplified solution : ((-1.0, -1.333)), generalized solution : ((-7 + 1)/2*3, (-7 - 1)/2*3) | complex_quadratic |
| 101 | Leap Year or Not | Year 1950  | is not a leap year | is_leap_year |
| 102 | Minute to Hour conversion | Convert 659 minutes to Hours & Minutes | 10 hours and 59 minutes | minutes_to_hours |
| 103 | Decimal to Binary Coded Decimal | BCD of Decimal Number 5285 is =  | 14105 | decimal_to_bcd |
| 104 | Circumference | Circumference of circle with radius 31 | 194.85714285714286 | circumference |
| 105 | Combine Like terms | 3x^8 + 10x^8 + 9x^3 + 4x^5 + 7x^7 + 3x^8 + 1x^2 + 9x^1 + 5x^2 + 3x^9 | 9x^1 + 6x^2 + 9x^3 + 4x^5 + 7x^7 + 16x^8 + 3x^9  | combine_like_terms |
| 105 | Conditional Probability | Someone tested positive for a nasty disease which only 0.55% of population have. Test sensitivity (true positive) is equal to SN= 96.72% whereas test specificity (true negative) SP= 93.78%. What is the probability that this guy really has that disease? | 7.92% | conditional_probability |
