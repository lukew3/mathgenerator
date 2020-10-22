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
| 0 | Addition | 13+0= | 13 | addition |
| 1 | Subtraction | 95-6= | 89 | subtraction |
| 2 | Multiplication | 66*0= | 0 | multiplication |
| 3 | Division | 15/42= | 0.35714285714285715 | division |
| 4 | Binary Complement 1s | 01= | 10 | binary_complement_1s |
| 5 | Modulo Division | 59%11= | 4 | modulo_division |
| 6 | Square Root | sqrt(81)= | 9 | square_root |
| 7 | Power Rule Differentiation | 8x^2 + 3x^3 + 1x^9 | 16x^1 + 9x^2 + 9x^8 | power_rule_differentiation |
| 8 | Square | 3^2= | 9 | square |
| 9 | LCM (Least Common Multiple) | LCM of 8 and 4 = | 8 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 12 and 12 =  | 12 | gcd |
| 11 | Basic Algebra | 8x + 10 = 10 | 0 | basic_algebra |
| 12 | Logarithm | log2(128) | 7 | log |
| 13 | Easy Division | 230/10 =  | 23 | int_division |
| 14 | Decimal to Binary | Binary of 93= | 1011101 | decimal_to_binary |
| 15 | Binary to Decimal | 10001 | 17 | binary_to_decimal |
| 16 | Fraction Division | (4/3)/(4/8) | 8/3 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 11 * [[6, 2], [0, 8]] =  | [[66,22],[0,88]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 10 17 7 =  | 0.0 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 13, 40 and 7 exist? | No | valid_triangle |
| 20 | Midpoint of the two point | (-16,-17),(7,11)= | (-4.5,-3.0) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2-3x-18 | (x-6)(x+3) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 49 and 13 =  | 118 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | 3x + y = 18, 4x + 10y = 102 | x = 3, y = 9 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-15, -13) and (-5, -10) | sqrt(109) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 14 and 13 =  | 19.10 | pythagorean_theorem |
| 26 | Linear Equations | -9x + -17y = 417, -1x + -4y = 78 | x = -18, y = -15 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 196 | [2, 2, 7, 7] | prime_factors |
| 28 | Fraction Multiplication | (8/1)*(9/6) | 12 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 8 sides | 135.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 12 objects picked 2 at a time  | 66 | combinations |
| 31 | Factorial | 4! =  | 24 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 14m is | 1176 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 16m, 4m, 12m is | 608 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 8m and radius = 13m is | 1715 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 14m is | 2744 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 5m, 19m, 11m is | 1045 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 26m and radius = 12m is | 11762 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 13m and radius = 8m is | 584 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 45m and radius = 12m is | 6785 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 53 and 11 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -9/6x + 2 and y = 5/4x - 6 | (32/11, -26/11) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 12 objects picked 5 at a time =   | 95040 | permutation |
| 43 | Cross Product of 2 Vectors | [-19, 13, 14] X [7, 17, -11] =  | [-381, -111, -414] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 7/8 and 3/4? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 4874 dollars, 10% rate of interest and for a time period of 1 years is =  | 487.4 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>7</td><td>4</td><td>-5</td><td>4</td></tr><tr><td>0</td><td>-8</td><td>-1</td><td>-5</td></tr></table>and<table><tr><td>-10</td><td>-6</td></tr><tr><td>-3</td><td>-6</td></tr><tr><td>1</td><td>8</td></tr><tr><td>0</td><td>-1</td></tr></table> | <table><tr><td>-87</td><td>-110</td></tr><tr><td>23</td><td>45</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 190 upto 2 decimal places is: | 5.75 | cube_root |
| 48 | Power Rule Integration | 3x^2 + 7x^7 + 1x^6 + 9x^1 | (3/2)x^3 + (7/7)x^8 + (1/6)x^7 + (9/1)x^2 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 126 , 81, 61 = | 92 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 6x^2+139x+34=0 | [-0.25, -22.92] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 19 and 12 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 2 dice are rolled at the same time, the probability of getting a sum of 5 = | 4/36 | dice_sum_probability |
| 53 | Exponentiation | 15^7 = | 170859375 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [204, 279, 272, 203, 275, 286, 253, 237, 271, 222, 297, 265, 242, 239, 259, 241, 261, 254, 217, 219, 298, 273, 238, 209, 268] with 80% confidence is | (258.3266706388717, 244.23332936112834) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 95^(1/7) _ 67^(1/6) | < | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 18 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597] | fibonacci_series |
| 57 | Trigonometric Values | What is cos(45)? | 1/√2 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 7 sides =  | 900 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[41, 44, 15, 26, 15, 50, 27, 22, 11, 32, 14, 8, 23, 50, 9] | The Mean is 25.8 , Standard Deviation is 199.0933333333333, Variance is 14.110043704160994 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 18m is | 4071.5040790523717 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 88 m =  | 2854543.2384361913 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 5th Fibonacci number? | 5 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 190 and SP = 653 is:  | 243.68421052631578 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 000 | 0x0 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (1+11j) * (14-20j) =  | (234+134j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [2, 14, 98, 686, 4802, 33614] ,Find the value of a,common ratio,11th term value, sum upto 10th term | The value of a is 2, common ratio is 7 , 11th term is 564950498 , sum upto 10th term is 94158416.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 5 , 36 , 46 , 11 =  | (5*36*46*11)^(1/4) = 17.372237396461717 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 4 numbers 2 , 69 , 40 , 85 =  |  4/((1/2) + (1/69) + (1/40) + (1/85)) = 7.256137637734391 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[964.0224705098824, 282.67364534639074, 10.524202601537414, 361.644358207216, 691.8214421455904, 573.8396623606926, 972.293614400242, 140.0274501909099, 590.7302519633489, 797.8763197329738, 726.1188608418418, 597.5706485157848, 241.28898511522024, 694.0267219296932, 32.85273313007875, 187.58082258543695, 452.179970384704, 964.184342568536, 589.6017896365979, 936.6845704453358] is: | 2778.1660192850186 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [682.87, 786.47, 315.92, 912.87, 542.62, 602.89, 747.77, 437.42, 3.35, 225.43, 63.6, 535.22, 871.05, 33.58] and [625.58, 654.32, 738.64, 670.61, 575.02, 237.12, 220.81, 78.57, 298.55, 427.21, 396.95, 159.78, 574.71, 847.07] is: | 0.69 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -14 and 27 =  | 41 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [13, -5, -16] . [-6, 11, -2] =  | -101 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 10 = | 10 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[73, 79, 98], [11, 18, 14], [41, 47, 26]]) is: | Matrix([[95/6388, -319/1597, 329/6388], [-36/1597, 265/1597, -7/1597], [221/12776, 24/1597, -445/12776]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 7 and angle, 271. Find the area of the sector. | Area of sector = 115.88114 | sector_area |
| 76 | Mean and Median | Given the series of numbers [17, 84, 55, 4, 28, 41, 50, 54, 35, 14]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 38.2 and Arithmetic median of this series is 38.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[0, 38], [92, 69]]) =  |  -3496 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 6315 dollars, 4% rate of interest and for a time period of 8 year is =  | 8642.51 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 222= | 0xde | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 16% of 10? | Required percentage = 1.60% | percentage |
| 81 | Celsius To Fahrenheit | Convert -30 degrees Celsius to degrees Fahrenheit = | -22.0 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 23 of the AP series: -14, 86, 186 ...  | 2186 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 70 terms of the AP series: 55, -34, -123 ...  | -211085.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 2801 in Octal is:  | 0o5361 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 1366 in Roman Numerals is:  | MCCCLXVI | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 213 in radians is =  | 3.72 | degree_to_rad |
| 87 | Radians to Degrees | Angle 0 in degrees is =  | 0.0 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(ln(x)+5*x^3)/dx | 15*x^2 + 1/x | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 18x^2 + 37x + 1 is =  | 25.5 | definite_integral |
| 90 | isprime | 53 | True | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 1 is =  | 5202 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 10.3exp(i0.51) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={1, 2, 6, 7, 9, 10} ,b={9, 3, 5, 6}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 2, 3, 5, 6, 7, 9, 10},Intersection is {9, 6}, a-b is {1, 2, 10, 7},b-a is {3, 5}, Symmetric difference is {1, 2, 3, 5, 7, 10} | set_operation |
| 94 | Base Conversion | Convert 137673 from base 8 to base 10. | 49083 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 20 and height, 96? | CSA of cylinder = 12063.72 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 10 sided polygon with lengths of [106, 31, 107, 44, 44, 81, 108, 92, 75, 103]cm is:  | 791 | perimeter_of_polygons |
