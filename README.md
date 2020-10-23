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
| 0 | Addition | 20+38= | 58 | addition |
| 1 | Subtraction | 2-0= | 2 | subtraction |
| 2 | Multiplication | 31*1= | 31 | multiplication |
| 3 | Division | 53/7= | 7.571428571428571 | division |
| 4 | Binary Complement 1s | 111= | 000 | binary_complement_1s |
| 5 | Modulo Division | 90%6= | 0 | modulo_division |
| 6 | Square Root | sqrt(16)= | 4 | square_root |
| 7 | Power Rule Differentiation | 7x^5 + 8x^10 + 4x^1 + 4x^5 + 7x^3 | 35x^4 + 80x^9 + 4x^0 + 20x^4 + 21x^2 | power_rule_differentiation |
| 8 | Square | 9^2= | 81 | square |
| 9 | LCM (Least Common Multiple) | LCM of 20 and 5 = | 20 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 11 and 2 =  | 1 | gcd |
| 11 | Basic Algebra | 10x + 4 = 8 | 2/5 | basic_algebra |
| 12 | Logarithm | log3(2187) | 7 | log |
| 13 | Easy Division | 247/19 =  | 13 | int_division |
| 14 | Decimal to Binary | Binary of 13= | 1101 | decimal_to_binary |
| 15 | Binary to Decimal | 001 | 1 | binary_to_decimal |
| 16 | Fraction Division | (6/9)/(4/2) | 1/3 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 11 * [[5, 2], [0, 8]] =  | [[55,22],[0,88]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 10 2 11 =  | 9.051933495115836 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 35, 7 and 11 exist? | No | valid_triangle |
| 20 | Midpoint of the two point | (12,-4),(-4,9)= | (4.0,2.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2-3x-28 | (x-7)(x+4) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 50 and 19 =  | 111 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -6x - 4y = -2, x + 10y = 47 | x = -3, y = 5 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (16, 20) and (-9, 14) | sqrt(661) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 7 and 3 =  | 7.62 | pythagorean_theorem |
| 26 | Linear Equations | 14x + -10y = -26, 15x + -11y = -29 | x = 1, y = 4 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 29 | [29] | prime_factors |
| 28 | Fraction Multiplication | (3/7)*(10/3) | 10/7 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 18 sides | 160.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 12 objects picked 5 at a time  | 792 | combinations |
| 31 | Factorial | 2! =  | 2 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 9m is | 486 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 19m, 9m, 6m is | 678 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 39m and radius = 6m is | 1696 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 14m is | 2744 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 4m, 19m, 20m is | 1520 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 27m and radius = 4m is | 1357 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 47m and radius = 15m is | 3031 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 46m and radius = 1m is | 48 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 5 and 89 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -10x - 3 and y = -10/5x - 4 | (1/8, -17/4) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 17 objects picked 6 at a time =   | 8910720 | permutation |
| 43 | Cross Product of 2 Vectors | [14, -7, -18] X [3, -16, 12] =  | [-372, -222, -203] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 6/7 and 2/1? | < | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 1752 dollars, 10% rate of interest and for a time period of 5 years is =  | 876.0 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>-2</td><td>7</td><td>-10</td></tr><tr><td>0</td><td>-4</td><td>-9</td></tr><tr><td>2</td><td>10</td><td>10</td></tr></table>and<table><tr><td>6</td><td>-6</td></tr><tr><td>-5</td><td>3</td></tr><tr><td>6</td><td>10</td></tr></table> | <table><tr><td>-107</td><td>-67</td></tr><tr><td>-34</td><td>-102</td></tr><tr><td>22</td><td>118</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 212 upto 2 decimal places is: | 5.96 | cube_root |
| 48 | Power Rule Integration | 4x^4 | (4/4)x^5 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 81 , 131, 8 = | 140 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 66x^2+177x+45=0 | [-0.28, -2.4] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 8 and 10 =  | 2 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 2 dice are rolled at the same time, the probability of getting a sum of 7 = | 6/36 | dice_sum_probability |
| 53 | Exponentiation | 16^3 = | 4096 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [240, 211, 206, 296, 223, 220, 264, 251, 245, 248, 207, 215, 277, 274, 297, 243, 278, 292, 256, 233, 266, 236, 270, 227, 209, 258, 298] with 99% confidence is | (263.9293815733304, 235.32987768592884) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 63^(1/2) _ 37^(1/4) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 12 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] | fibonacci_series |
| 57 | Trigonometric Values | What is sin(0)? | 0 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 7 sides =  | 900 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[30, 21, 26, 36, 34, 7, 46, 21, 15, 29, 9, 33, 16, 28, 43] | The Mean is 26.266666666666666 , Standard Deviation is 123.39555555555556, Variance is 11.108355213781902 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 6m is | 452.3893421169302 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 10 m =  | 4188.790204786391 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 41th Fibonacci number? | 165580141 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 411 and SP = 499 is:  | 21.41119221411192 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 00010 | 0x2 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (-2-6j) * (-10+2j) =  | (32+56j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [7, 77, 847, 9317, 102487, 1127357] ,Find the value of a,common ratio,8th term value, sum upto 7th term | The value of a is 7, common ratio is 11 , 8th term is 136410197 , sum upto 7th term is 13641019.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 76 , 98 , 2 , 58 =  | (76*98*2*58)^(1/4) = 30.487682589384825 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 3 numbers 77 , 98 and 69 =  |  3/((1/77) + (1/98) + (1/69)) = 79.60970388869067 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[229.4364953887822, 570.6032154600009, 199.52328312454694, 658.3975413255898, 605.9566521345233, 616.6627240713517, 572.9546490919761, 508.8683987353998, 666.172347641998, 865.2735159823208, 594.8620516188639, 418.8436115273115, 69.46437421671337, 385.84806581739593] is: | 2015.3622923166513 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [954.08, 488.66, 694.46, 127.67, 912.65, 462.11, 713.4, 179.41, 728.87, 811.04, 760.22, 688.68, 444.93, 237.29, 485.89, 565.71, 520.56, 44.1, 684.62, 665.12] and [736.88, 60.8, 240.61, 677.58, 887.06, 73.3, 470.5, 884.06, 453.97, 168.97, 921.73, 538.36, 967.82, 236.94, 51.62, 402.46, 57.88, 166.91, 676.47, 708.47] is: | 0.63 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -87 and 69 =  | 156 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [14, -1, 7] . [-12, 15, -9] =  | -246 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 11010 = | 110 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[17, 31, 76], [3, 65, 91], [42, 2, 28]]) is: | Matrix([[-273/10550, 179/15825, 2119/63300], [-623/10550, 679/15825, 1319/63300], [227/5275, -317/15825, -253/15825]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 4 and angle, 2. Find the area of the sector. | Area of sector = 0.27925 | sector_area |
| 76 | Mean and Median | Given the series of numbers [87, 97, 75, 27, 91, 31, 15, 40, 73, 74]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 61.0 and Arithmetic median of this series is 73.5 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[83, 41], [15, 13]]) =  |  464 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 2702 dollars, 7% rate of interest and for a time period of 2 year is =  | 3093.52 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 386= | 0x182 | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 64% of 8? | Required percentage = 5.12% | percentage |
| 81 | Celsius To Fahrenheit | Convert 50 degrees Celsius to degrees Fahrenheit = | 122.0 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 89 of the AP series: -35, -98, -161 ...  | -5579 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 63 terms of the AP series: 7, 100, 193 ...  | 182070.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 265 in Octal is:  | 0o411 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 1439 in Roman Numerals is:  | MCDXXXIX | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 68 in radians is =  | 1.19 | degree_to_rad |
| 87 | Radians to Degrees | Angle 3 in degrees is =  | 171.89 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(ln(x)+2*x^3)/dx | 6*x^2 + 1/x | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 74x^2 + 55x + 86 is =  | 138.1667 | definite_integral |
| 90 | isprime | 32 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 1 is =  | 5461 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 27.59exp(i-2.38) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={1, 2, 3, 5, 6, 8} ,b={1, 10, 2, 9}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 2, 3, 5, 6, 8, 9, 10},Intersection is {1, 2}, a-b is {8, 3, 5, 6},b-a is {9, 10}, Symmetric difference is {3, 5, 6, 8, 9, 10} | set_operation |
| 94 | Base Conversion | Convert 131222 from base 6 to base 2. | 10111010111110 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 27 and height, 94? | CSA of cylinder = 15946.72 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 9 sided polygon with lengths of [48, 30, 110, 95, 10, 33, 87, 70, 78]cm is:  | 561 | perimeter_of_polygons |
| 97 | Power of Powers | The 24^1^3 = 24^(1*3) = 24^3 | 13824 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 41^2 and 41^3 = 41^(2-3) = 41^-1 | 0.024390243902439025 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 30^5 and 35^5 = (30/35)^5 = 0.8571428571428571^5 | 0.46266436603796024 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation 5x^2 + 8x + 2 = 0 | simplified solution : ((-0.31, -1.29)), generalized solution : ((-8 + sqrt(24))/2*5, (-8 - sqrt(24))/2*5) | complex_quadratic |
